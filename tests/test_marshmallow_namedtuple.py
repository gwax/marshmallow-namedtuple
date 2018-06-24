"""Tests for marshmallow-namedtuple."""

from typing import Dict, List, NamedTuple, Optional

from marshmallow import fields

from marshmallow_namedtuple import NamedTupleSchema


def test_basic_model():
    class Model(NamedTuple):
        a: int

    class Schema(NamedTupleSchema):
        class Meta:
            namedtuple = Model
            strict = True

    schema = Schema()
    assert schema.load({'a': 1}).data == Model(1)
    assert schema.dump(Model(2)).data == {'a': 2}


def test_optional_field():
    class Model(NamedTuple):
        a: Optional[int]

    class Schema(NamedTupleSchema):
        class Meta:
            namedtuple = Model
            strict = True

    schema = Schema()
    assert schema.load({'a': 1}).data == Model(1)
    assert schema.dump(Model(2)).data == {'a': 2}
    assert schema.load({}).data == Model(None)
    assert schema.load({'a': None}).data == Model(None)
    assert schema.dump(Model(None)).data == {}


def test_list_field():
    class Model(NamedTuple):
        a: List[int]

    class Schema(NamedTupleSchema):
        class Meta:
            namedtuple = Model
            strict = True

    schema = Schema()
    assert schema.load({'a': [1]}).data == Model([1])
    assert schema.dump(Model([2, 3])).data == {'a': [2, 3]}


def test_dict_field():
    class Model(NamedTuple):
        a: Dict[str, int]

    class Schema(NamedTupleSchema):
        class Meta:
            namedtuple = Model
            strict = True

    schema = Schema()
    assert schema.load({'a': {'b': 2}}).data == Model({'b': 2})
    assert schema.dump(Model({'c': 5})).data == {'a': {'c': 5}}


def test_nested():
    class Model1(NamedTuple):
        a: int

    class Schema1(NamedTupleSchema):
        class Meta:
            namedtuple = Model1
            strict = True

    class Model2(NamedTuple):
        b: Model1

    class Schema2(NamedTupleSchema):
        class Meta:
            namedtuple = Model2
            strict = True

        b = fields.Nested(Schema1)

    schema2 = Schema2()
    assert schema2.load({'b': {'a': 1}}).data == Model2(Model1(1))
    assert schema2.dump(Model2(Model1(2))).data == {'b': {'a': 2}}

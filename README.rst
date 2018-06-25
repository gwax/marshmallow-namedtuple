marshmallow-namedtuple
======================

Python 3.5+ `typing.NamedTuple <https://docs.python.org/3/library/typing.html#typing.NamedTuple>`_ integration with the `marshmallow <https://marshmallow.readthedocs.io/en/latest/>`_ (de)serialization library.

Declare your namedtuple
-----------------------

.. code-block:: python

    from typing import NamedTuple, Optional

    class Widget(NamedTuple):
        a: int
        b: Optional[str]

Generate marshmallow schema
---------------------------

.. code-block:: python

    from marshmallow_namedtuple import NamedTupleSchema

    class WidgetSchema(NamedTupleSchema):
        class Meta:
            namedtuple = Widget

    widget_schema = WidgetSchema()

(De)serialize your data
-----------------------

.. code-block:: python

    widget = Widget(a=1, b=None)

    widget_schema.dump(widget).data
    # {'a': 1}

    widget_schema.load({'a': 2}).data
    # Widget(a=2, b=None)

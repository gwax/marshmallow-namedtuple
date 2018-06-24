import datetime as dt
import decimal
import uuid
import typing as t

import marshmallow.fields as f

NoneType = type(None)
TYPE_MAPPING = {
    bool: f.Boolean,
    decimal.Decimal: f.Decimal,
    dt.date: f.Date,
    dt.datetime: f.DateTime,
    dt.time: f.Time,
    dt.timedelta: f.TimeDelta,
    float: f.Float,
    int: f.Integer,
    str: f.String,
    t.Any: f.Raw,
    uuid.UUID: f.UUID,
}


def generics_field(typ, field_kwargs):
    if typ.__origin__ is t.Union:
        if len(typ.__args__) == 2 and NoneType in typ.__args__:
            # Optional[...]
            field_kwargs = {**field_kwargs, 'requied': False, 'allow_none': True, 'missing': None}
            [newtyp] = [t for t in typ.__args__ if t is not NoneType]
            return generate_field(newtyp, field_kwargs=field_kwargs)
    elif typ.__origin__ is t.List:
        subfield = generate_field(typ.__args__[0])
        return f.List(subfield, **field_kwargs)
    elif typ.__origin__ is t.Dict:
        keyfield = generate_field(typ.__args__[0])
        valfield = generate_field(typ.__args__[1])
        return f.Dict(keys=keyfield, values=valfield, **field_kwargs)


def generate_field(typ, field_kwargs=None):
    field_kwargs = field_kwargs or {}
    if hasattr(typ, '__origin__'):
        return generics_field(typ, field_kwargs)
    field_type = TYPE_MAPPING[typ]
    return field_type(**field_kwargs)


def fields_for_namedtuple(
        namedtuple,
        fields=None,
        exclude=None,
        base_fields=None,
        dict_cls=dict):
    result = dict_cls()
    if namedtuple is None:
        return result
    base_fields = base_fields or {}
    for key, typ in namedtuple._field_types.items():
        if fields and key not in fields:
            continue
        if exclude and key in exclude:
            continue

        field = base_fields.get(key) or generate_field(typ)
        if field:
            result[key] = field
    return result

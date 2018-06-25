import marshmallow as ma
from marshmallow.compat import with_metaclass

from .convert import fields_for_namedtuple


class NamedTupleSchemaOpts(ma.SchemaOpts):
    def __init__(self, meta, *args, **kwargs):
        super().__init__(meta, *args, **kwargs)
        self.namedtuple = getattr(meta, 'namedtuple', None)


class NamedTupleSchemaMeta(ma.schema.SchemaMeta):
    @classmethod
    def get_declared_fields(
            mcs,
            klass,
            cls_fields,
            inherited_fields,
            dict_cls):
        opts = klass.opts
        base_fields = super(NamedTupleSchemaMeta, mcs).get_declared_fields(
            klass, cls_fields, inherited_fields, dict_cls)
        declared_fields = fields_for_namedtuple(
            opts.namedtuple,
            fields=opts.fields,
            exclude=opts.exclude,
            base_fields=base_fields,
            dict_cls=dict_cls)
        declared_fields.update(base_fields)
        return declared_fields


class NamedTupleSchema(with_metaclass(NamedTupleSchemaMeta, ma.Schema)):
    OPTIONS_CLASS = NamedTupleSchemaOpts

    @ma.post_load
    def make_namedtuple(self, data):
        return self.opts.namedtuple(**data)

    @ma.post_dump
    def clear_optional(self, data):
        return {
            k: v for k, v in data.items() if
            v is not None or
            self.opts.namedtuple._field_defaults.get(k) is not None
        }

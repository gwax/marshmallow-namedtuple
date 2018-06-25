from ._version import __version__  # noqa
from .convert import fields_for_namedtuple
from .schema import NamedTupleSchema

__license__ = 'MIT'

__all__ = [
    'fields_for_namedtuple',
    'NamedTupleSchema',
]

from ._version import __version__
from .convert import fields_for_namedtuple
from .schema import NamedTupleSchema

__license__ = 'MIT'

__all__ = [
    'fields_for_namedtuple',
    'NamedTupleSchema',
]

import sys

from setuptools import find_packages, setup


if sys.version_info < (3, 5):
    raise Exception('Python versions < 3.5 are not supported.')

REQUIRES = (
    'marshmallow>=2.0.0',
)

# Retrieve version information from _version.py
__version__ = None
exec(open('marshmallow_namedtuple/_version.py', 'rt').read())

SHORT_DESCRIPTION = 'Python 3.5+ typing.NamedTuple integration with the ' \
                    'marshmallow (de)serialization library.'
LONG_DESCRIPTION = open('README.rst', 'rt').read()
CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup(
    name='marshmallow-namedtuple',
    version=__version__,
    author='George Leslie-Waksman',
    author_email='waksman@gmail.com',
    url='https://github.com/gwax/marshmallow-namedtuple',
    packages=find_packages(exclude=("test*",)),
    package_dir={'marshmallow-namedtuple': 'marshmallow-namedtuple'},
    include_package_data=True,
    install_requires=REQUIRES,
    license='MIT',
    zip_safe=True,
    keywords='namedtuple marshmallow',
    classifiers=CLASSIFIERS,
    test_suite='tests',
    project_urls={
        'Bug Reports': 'https://github.com/gwax/marshmallow-namedtuple/issues',
    },
)

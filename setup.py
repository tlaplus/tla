"""Installation script."""
from setuptools import setup


name = 'tla'
description = (
    'Parser and abstract syntax tree for TLA+, '
    'the temporal logic of actions.')
README = 'README.md'
long_description = open(README).read()
url = 'https://github.com/tlaplus/tla_python'
VERSION_FILE = '{name}/_version.py'.format(name=name)
MAJOR = 0
MINOR = 0
MICRO = 2
version = '{major}.{minor}.{micro}'.format(
    major=MAJOR, minor=MINOR, micro=MICRO)
s = (
    '# This file was generated from `setup.py`\n'
    "version = '{version}'\n").format(version=version)
install_requires = [
    'infix >= 1.2',
    'ply >= 3.4, <= 3.10',
    ]
tests_require = ['nose']
classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Compilers',
    ]
keywords = [
    'TLA+', 'TLA', 'temporal logic of actions',
    'formal', 'specification',
    'expression', 'formula', 'module',
    'mathematics', 'theorem', 'proof',
    'parser', 'lexer', 'parsing',
    'ast', 'abstract syntax tree', 'syntax tree',
    'ply', 'lex',
    ]


def run_setup():
    """Write version file and install package."""
    with open(VERSION_FILE, 'w') as f:
        f.write(s)
    setup(
        name=name,
        version=version,
        description=description,
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Ioannis Filippidis',
        author_email='jfilippidis@gmail.com',
        url=url,
        license='BSD',
        install_requires=install_requires,
        tests_require=tests_require,
        packages=[name],
        package_dir={name: name},
        classifiers=classifiers,
        keywords=keywords)


if __name__ == '__main__':
    run_setup()

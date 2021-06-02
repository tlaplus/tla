[![Build Status][build_img]][travis]
[![Coverage Status][coverage]][coveralls]


About
=====

A parser for the Temporal Logic of Actions (TLA+). The parser is based on
[combinators](https://en.wikipedia.org/wiki/Parser_combinator).
The lexer is generated with [`ply`](https://pypi.org/project/ply)
using `lex`. Classes for a TLA+ abstract tree are included and used for
representing the result of parsing.

To install:

```
pip install tla
```

To parse a string:

```python
from tla import parser

module_text = r'''
---- MODULE Foo ----
foo == TRUE
====================
'''

tree = parser.parse(module_text)
```


To parse the string `module_text` from above and print a formatted version:

```python
from tla import parser
from tla.to_str import Nodes

# The abstract syntax tree classes can be changed using
# the optional argument `nodes` of the function `parser.parse`.
tree = parser.parse(module_text, nodes=Nodes)
text = tree.to_str(width=80)
print(text)
```

More examples can be found in the directory [`examples/`](
    https://github.com/tlaplus/tla_python/blob/master/examples/)

To implement a new translator of TLA+ to an intended output format, either:
- use the visitor pattern with the module `ast.visit`, or
- subclass the class `tla.ast.Nodes`, and override AST node classes
  and their methods as needed. An example of this approach is the module
  `tla.to_str`, which can be copied as a starting point for implementing
  a translator.


This parser is a translation to Python from OCaml of the parser in
[`tlapm`](https://github.com/tlaplus/tlapm/), the TLA+ proof manager.
The Python source code includes in comments the corresponding OCaml source code.
Comments in each module mention the OCaml files on which that module is based.

This parser is slower than the OCaml implementation.

The module `tla._combinators` can be used to write other parsers.


Documentation
=============

In the [Markdown](https://en.wikipedia.org/wiki/Markdown) file
[`doc.md`](https://github.com/tlaplus/tla_python/blob/master/doc.md)


Tests
=====

Use [`pytest`](https://pypi.org/project/pytest). Run with:

```shell
cd tests/
pytest -v --continue-on-collection-errors .
```

See also the file `tests/README.md`.


License
=======
[BSD-3](https://opensource.org/licenses/BSD-3-Clause), see `LICENSE` file.


[build_img]: https://travis-ci.org/tlaplus/tla_python.svg?branch=master
[travis]: https://travis-ci.org/tlaplus/tla_python
[coverage]: https://coveralls.io/repos/tlaplus/tla_python/badge.svg?branch=master
[coveralls]: https://coveralls.io/r/tlaplus/tla_python?branch=master

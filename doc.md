# `tla` documentation


## Parsing modules

The parser has different entry points for parsing modules and expressions.
These entry points are the functions `tla.parser.parse` and
`tla.parser.parse_expr`. More entry points exist within the parser,
for example to parse definitions and sequents. The tests include examples of
how parsers for those entry points can be created.

We describe in this section the function `tla.parser.parse`, and in the next
section the function `tla.parser.parse_expr`. The function can be invoked as
follows:

```python
from tla import parser

module_text = r'''
--------------- MODULE Cycle -------------
(* Alternation between two values. *)
VARIABLE x

Init == x = 1
Next == x' = IF x = 1 THEN 2 ELSE 1
Spec == Init /\ [][Next]_x /\ WF_x(Next)
==========================================
'''

tree = parser.parse(module_text)
```

The function `parse` takes one positional argument, the string to be parsed.
This string should include an entire module, otherwise a syntax error will be
raised. The class of the returned `tree` is:

```python
>>> type(tree)
tla.ast.Nodes.Module
```

The classes in the class `tla.ast.Nodes` are used by default by the parser.
The function `parse` takes an optional argument `nodes` to define the classes
to use for constructing the syntax tree when parsing. For example:

```python
from tla.to_str import Nodes

tree = parser.parse(module_text, nodes=Nodes)
```

This `tree` is a different class:

```python
>>> type(tree)
tla.to_str.Nodes.Module
```

This node of the syntax tree has a method `to_str` for converting the tree to
a string.

```python
s = tree.to_str()
print(s)
```

The result is:

```tla
--------------------------------- MODULE Cycle ---------------------------------
VARIABLE x
Init == x = 1
Next == x' = IF x = 1 THEN 2 ELSE 1
Spec == Init /\ [][Next]_x /\ WF_x(Next)
================================================================================
```

Note that the formatting has changed, because the module `tla.to_str` applies
its own formatting. Also, the comment is not present, because the parser does
not store comments.

The tree node also has attributes that store the module's name, content,
extendees, and other information. For example:

```python
>>> tree.name
'Cycle'

>>> tree.body
[<tla.to_str.Nodes.Variables at 0x108443550>,
 <tla.to_str.Nodes.Definition at 0x108445370>,
 <tla.to_str.Nodes.Definition at 0x108445610>,
 <tla.to_str.Nodes.Definition at 0x108443a00>]
```

Nodes for other elements of the syntax have different attributes.
For example, a definition node has attributes `definition`, `local`,
`visibility`, `wheredef`, and `to_str` if `tla.to_str.Nodes` is passed to the
parsing function.


## Parsing expressions

The entry point for parsing TLA+ expressions is the function
`tla.parser.parse_expr`. Similarly to the function `parse`, the function
`parse_expr` takes a positional and an optional argument. The optional argument
is for defining the syntax tree node classes to use when parsing.

```python
from tla import parser

expr = r'[n \in Nat |-> n + 1]'
tree = parser.parse_expr(expr)
```

With the argument `nodes`:

```python
from tla.to_str import Nodes

tree = parser.parse_expr(expr, nodes=Nodes)
```

and converting the result to a string:

```
>>> s = tree.to_str(width=80)
>>> print(s)
[n \in Nat |-> n + 1]
```

The keyword argument `width` defines the column width within which the
formatter fits the TLA+ elements that are converted to string representation.


## Visiting the syntax tree

The [visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern) is
implemented in the class `tla.visit.NodeTransformer`. This class has a method
`visit` that is called for traversing a node. The method `visit` selects the
appropriate method to call on a node based on the class name of the node
(`type(node).__name__`). This approach enables implementing custom visitors
by subclassing the class `NodeTransformer` and overriding its methods.

Suppose that we would like to perform an expansion of definitions, using
a dictionary of defined operators. In this example we construct the dictionary
directly. In a TLA+ translator, such a dictionary of definitions would result
from analysis of the parsed module up to the point of interest.

```python
from tla import parser
from tla import to_str

definitions = dict(
    Foo=parser.parse_expr(r'x /\ y', nodes=to_str.Nodes),
    Bar=parser.parse_expr(r'[n \in Nat |-> n + 2]', nodes=to_str.Nodes))
```

We now define a subclass of the class `tla.visit.NodeTransformer` that
overrides the method `visit_Opaque` to check if a name is in the dictionary of
defined operators, and if so then replace the node with the syntax tree for
that defined operator.

```python
from tla import visit

class DefinitionExpander(visit.NodeTransformer):

    def visit_Opaque(self, node, *arg, **kw):
        defs = kw['definitions']
        name = node.name
        if name in defs:
            return defs[name]
        else:
            return self.nodes.Opaque(name)
```

Next we parse the expression where the substitutions are performed,
and perform the substitutions of the operators `Foo` and `Bar` with the
expressions that have been parsed above.

```python
tree = parser.parse_expr(r'Foo /\ (Bar = f)', nodes=to_str.Nodes)
visitor = DefinitionExpander()
new_tree = visitor.visit(tree, definitions=definitions)
print(new_tree.to_str(width=80))
```

The printed output is:

```tla
x /\ y /\ ([n \in Nat |-> n + 2] = f)
```

The syntax tree nodes are documented in the module `tla.ast`.


## Structure of the package


The module dependencies within the package are as follows:

- `tla.ast`

- `tla._error`

- `tla._location`

- `tla.tokens`

- `tla._optable` imports:
  - `tla.ast`

- `tla.lex` imports:
  - `tla.tokens`
  - `tla._location`

- `tla._combinators` imports:
  - `tla._error`
  - `tla._location`
  - `tla.tokens`

- `tla._tla_combinators` imports:
  - `tla.tokens`
  - `tla._combinators`
  - `tla._optable`

- `tla._expr_parser` imports:
  - `tla._combinators`
  - `tla._location`
  - `tla._optable`
  - `tla._tla_combinators`
  - `tla.ast`
  - `tla.tokens`

- `tla._proof_parser` imports:
  - `tla._combinators`
  - `tla._expr_parser`
  - `tla._tla_combinators`
  - `tla.ast`
  - `tla.tokens`

- `tla._module_parser` imports:
  - `tla._combinators`
  - `tla._expr_parser`
  - `tla._proof_parser`
  - `tla._tla_combinators`
  - `tla.ast`
  - `tla.tokens`

- `tla.parser` imports:
  - `tla._expr_parser`
  - `tla._combinators`
  - `tla._module_parser`
  - `tla._optable`
  - `tla._proof_parser`
  - `tla._tla_combinators`
  - `tla.lex`

- `tla.to_str` imports:
  - `tla._optable`
  - `tla.ast`

- `tla.iter` imports:
  - `tla.to_str`

- `tla.visit` imports:
  - `tla.to_str`

`tla._intf` is an abstract module.


## Copying

This document is copyright 2020 by California Institute of Technology.
All rights reserved. Licensed under 3-clause BSD.

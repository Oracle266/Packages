from lark import Lark

grammar = r"""
start: class_def

class_def: "class" CLASS_NAME ":" CLASS_NAME? "{" body "};"
body: (attribute | method)*
CLASS_NAME: /[A-Z][a-zA-Z0-9_]*/
attribute: dec_non_init | dec_init
NAME: /[a-z][a-zA-Z0-9_]*/
TYPE: "int" | "float" | "byte" | "uint64" | "uint32"
dec_non_init: TYPE NAME ";"
STRI: /"[^"]*"/
dec_init: TYPE NAME "=" STRI ";" 
method: TYPE NAME "(" (dec_non_init ",")* ")" "{" met_bod "}"
met_bod: statement+
statement: dec_non_init

%import common.WS
%ignore WS
"""

parser = Lark(grammar)

code = """
class Animal : Creature {
    int age = "ajek";
};
"""

tree = parser.parse(code)
print(tree)
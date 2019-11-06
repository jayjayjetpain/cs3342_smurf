from arpeggio.cleanpeg import ParserPEG
import sys

grammar="""
program
    = code EOF

comment
    = "#" r'.*'

code
    = statement*

statement
    = "let" variable_declaration 
    / assignment 
    / expr

variable_declaration
    = decl ("," decl)*

decl
    = identifier ("=" expr)?

identifier
    = [a-z][a-zA-Z_0-9]*

variable_reference
    = identifier

if_expression
    = expr brace_block ( "else" brace_block )?

assignment
    = identifier "=" expr

expr
    = "fn" function_declaration 
    / "if" if_expression 
    / boolean_expression 
    / arithmetic_expression

boolean_expression
    = arithmetic_expression relop arithmetic_expression

arithmetic_expression
    = mult_term addop arithmetic_expression 
    / mult_term

mult_term
    = primary mulop mult_term 
    / primary

primary
    = integer 
    / function_call 
    / variable_reference 
    / "(" arithmetic_expression ")"

integer
    = "-"? [0-9]+

addop
    = '+' / '-'

mulop
    = '*' / '/'

relop
    = '==' / '!=" / '>=' / '>' / '<=' / '<'

function_call
    = variable_reference "(" call_arguments ")" 
    / "print" "(" call_arguments ")"

call_arguments
    = (expr ("," expr)*)?

function_definition
    = param_list brace_block

param_list
    = "(" identifier ("," identifier)* ")" 
    / "(" ")"

brace_block
    = "{" code "}"
"""

parser = ParserPEG(grammar, "program", debug = True)

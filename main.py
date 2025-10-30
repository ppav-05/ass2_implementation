from ass2_lexer import Lexer
from ass2_parse_table import LL1Parser

text = "2 + 3 × 4"
lexer = Lexer(text)
tokens = lexer.tokenise()

parser = LL1Parser(tokens)
ast = parser.parse()
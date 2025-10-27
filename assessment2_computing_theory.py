from enum import Enum
from tracemalloc import start

class TokenType(Enum):
    NUMBER = "NUMBER"
    IDENTIFIER = "IDENTIFIER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULT = "MULT"
    EQUALS = "EQUALS"
    CONDITIONAL = "CONDITIONAL"
    LAMBDA = "LAMBDA"
    LET = "LET"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    EOF = "EOF"
    UNKNOWN = "UNKNOWN"

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f'Token({self.type.name}, {self.value})'
        return f'Token({self.type.name})'

class ParenthesisError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[0] if text else None
        self.paren_count = 0  # Track parenthesis balance

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None
    
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def number(self):
        start_pos = self.pos
        while self.current_char is not None and self.current_char.isdigit():
            self.advance()
        return Token(TokenType.NUMBER, int(self.text[start_pos:self.pos]))

    def identifier(self):
        start_pos = self.pos
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            self.advance()
        value = self.text[start_pos:self.pos]
        return Token(TokenType.IDENTIFIER, value)

    def get_next_token(self) -> Token:
        while self.current_char is not None:
            #Whitespace
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            #Number
            if self.current_char.isdigit():
                return self.number()
            #Identifier or Keyword
            if self.current_char.isalpha():
                return self.identifier()

            start_pos = self.pos
            #Operators and Parentheses
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+', start_pos)

            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-', start_pos)

            if self.current_char == 'x':
                self.advance()
                return Token(TokenType.MULT, 'x', start_pos)

            if self.current_char == '=':
                self.advance()
                return Token(TokenType.EQUALS, '=', start_pos)

            if self.current_char == '(':
                self.paren_count += 1
                self.advance()
                return Token(TokenType.LPAREN, '(', start_pos)

            if self.current_char == ')':
                self.paren_count -= 1
                self.advance()
                return Token(TokenType.RPAREN, ')', start_pos)

            if self.current_char == 'λ':
                self.advance()
                return Token(TokenType.LAMBDA, 'λ', start_pos)

            if self.current_char == '?':
                self.advance()
                return Token(TokenType.CONDITIONAL, '?', start_pos)

            if self.current_char == '≜':
                self.advance()
                return Token(TokenType.LET, '≜', start_pos)

            self.advance()
            return Token(TokenType.UNKNOWN, self.current_char, start_pos)

    def tokenise(self):
        tokens = []
        while True:
            token = self.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break

        if self.paren_count > 0:
            raise ParenthesisError("Missing closing parenthesis ')'")
        elif self.paren_count < 0:
            raise ParenthesisError("Unexpected closing parenthesis ')'")
        return tokens
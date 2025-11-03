from ass2_lexer import TokenType, Token

class Parse_Tree:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[0] if tokens else None
    
    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None
    
    def parse(self):
        return self.parse_expression()
    
    def parse_expression(self):
        if self.current_token.type == TokenType.LPAREN:
            return self.parse_compound()
        else:
            return self.parse_atom()
    
    def parse_compound(self):
        self.advance()
        
        if self.current_token.type == TokenType.PLUS:
            result = ['PLUS']
            self.advance()
        elif self.current_token.type == TokenType.MINUS:
            result = ['MINUS']
            self.advance()
        elif self.current_token.type == TokenType.MULT:
            result = ['MULT']
            self.advance()
        elif self.current_token.type == TokenType.EQUALS:
            result = ['EQUALS']
            self.advance()
        elif self.current_token.type == TokenType.LAMBDA:
            result = ['LAMBDA']
            self.advance()
        elif self.current_token.type == TokenType.CONDITIONAL:
            result = ['CONDITIONAL']
            self.advance()
        elif self.current_token.type == TokenType.LET:
            result = ['LET']
            self.advance()
        else:
            raise SyntaxError(f"Expected operator or keyword, got {self.current_token}")

        while self.current_token.type != TokenType.RPAREN:
            result.append(self.parse_expression()) 
        self.advance()
        return result
    
    def parse_atom(self):
        if self.current_token.type == TokenType.NUMBER:
            value = self.current_token.value
            self.advance()
            return value
        elif self.current_token.type == TokenType.IDENTIFIER:
            value = self.current_token.value
            self.advance()
            return value
        else:
            raise SyntaxError(f"Expected number or identifier, got {self.current_token}")
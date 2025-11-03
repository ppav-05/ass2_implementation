from ass2_lexer import Lexer, TokenType, Token

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

if __name__ == "__main__":
    #Basic Operations
    lexer1 = Lexer("42")
    tokens1 = lexer1.tokenise()
    parser1 = Parse_Tree(tokens1)
    tree1 = parser1.parse()
    print(f"Input: 42")
    print(f"Output: {tree1}")
    print()

    lexer2 = Lexer("x")
    tokens2 = lexer2.tokenise()
    parser2 = Parse_Tree(tokens2)
    tree2 = parser2.parse()
    print(f"Input: x")
    print(f"Output: {tree2}")
    print()

    lexer3 = Lexer("(+ 2 3)")
    tokens3 = lexer3.tokenise()
    parser3 = Parse_Tree(tokens3)
    tree3 = parser3.parse()
    print(f"Input: (+ 2 3)")
    print(f"Output: {tree3}")
    print()

    lexer4 = Lexer("(× x 5)")
    tokens4 = lexer4.tokenise()
    parser4 = Parse_Tree(tokens4)
    tree4 = parser4.parse()
    print(f"Input: (× x 5)")
    print(f"Output: {tree4}")
    print()

    #Nested Operations
    lexer4 = Lexer("(+ (× 2 3) 4)")
    tokens4 = lexer4.tokenise()
    parser4 = Parse_Tree(tokens4)
    tree4 = parser4.parse()
    print(f"Input: (+ (× 2 3) 4)")
    print(f"Output: {tree4}")
    print()

    lexer5 = Lexer("(? (= x 0) 1 0)")
    tokens5 = lexer5.tokenise()
    parser5 = Parse_Tree(tokens5)
    tree5 = parser5.parse()
    print(f"Input: (? (= x 0) 1 0)")
    print(f"Output: {tree5}")

    #Function and Expressions
    #lexer6 = Lexer("(λ x x)")
    #tokens6 = lexer6.tokenise()
    #parser6 = Parse_Tree(tokens6)
    #tree6 = parser6.parse()
    #print(f"Input: (λ x x)")
    #print(f"Output: {tree6}")

    #lexer7 = Lexer("(≜ y 10 y)")
    #tokens7 = lexer7.tokenise()
    #parser7 = Parse_Tree(tokens7)
    #tree7 = parser7.parse()
    #print(f"Input: (≜ y 10 y)")
    #print(f"Output: {tree7}")
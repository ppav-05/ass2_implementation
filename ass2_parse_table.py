from ass2_lexer import TokenType, Token, Lexer

class ASTNode:
    pass

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f'NumberNode({self.value})'

class IdentifierNode(ASTNode):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'IdentifierNode({self.name})'

class StringNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'StringNode({self.value})'

class BinaryOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    
    def __repr__(self):
        return f'BinaryOpNode({self.left}, {self.op}, {self.right})'

class ConditionalNode(ASTNode):
    def __init__(self, condition, true_branch, false_branch):
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    def __repr__(self):
        return f'ConditionalNode({self.condition}, {self.true_branch}, {self.false_branch})'

class LetNode(ASTNode):
    def __init__(self, identifier, value_expr, body_expr):
        self.identifier = identifier
        self.value_expr = value_expr
        self.body_expr = body_expr
    
    def __repr__(self):
        return f"Let({self.identifier}, {self.value_expr}, {self.body_expr})"

class LambdaNode(ASTNode):
    def __init__(self, parameter, body):
        self.parameter = parameter
        self.body = body
    
    def __repr__(self):
        return f"Lambda({self.parameter}, {self.body})"

class ApplicationNode(ASTNode):
    def __init__(self, function, arguments):
        self.function = function
        self.arguments = arguments
    
    def __repr__(self):
        return f"Application({self.function}, {self.arguments})"

class LL1Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = tokens[0]
    
    def advance(self):
        self.current_token_index += 1
        if self.current_token_index < len(self.tokens):
            self.current_token = self.tokens[self.current_token_index]
    
    def match(self, expected_type):
        if self.current_token.type == expected_type:
            value = self.current_token.value
            self.advance()
            return value
        else:
            raise SyntaxError(f"Expected {expected_type.name}, got {self.current_token.type.name}")
        
    def parse_expr(self):
        pass
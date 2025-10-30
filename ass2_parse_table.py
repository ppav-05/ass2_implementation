# LL(1) parse table for a simple arithmetic grammar:
# Grammar (classic expression grammar):
#   E  -> T E'
#   E' -> + T E' | - T E' | ε
#   T  -> F T'
#   T' -> * F T' | / F T' | ε
#   F  -> ( E ) | NUMBER | IDENTIFIER
#
# Terminals used as keys: '+', '-', '*', '/', '(', ')', 'NUMBER', 'IDENTIFIER', '$' (EOF)
# Nonterminals: 'E', "E'", 'T', "T'", 'F'
# Productions are lists of symbols (terminals or nonterminals). Epsilon is represented by an empty list [].

EPSILON = []

NONTERMINALS = ["E", "E'", "T", "T'", "F"]
TERMINALS = ['+', '-', '*', '/', '(', ')', 'NUMBER', 'IDENTIFIER', '$']

PARSE_TABLE = {
    # E
    ('E', 'NUMBER'): ['T', "E'"],
    ('E', 'IDENTIFIER'): ['T', "E'"],
    ('E', '('): ['T', "E'"],

    # E'
    ("E'", '+'): ['+', 'T', "E'"],
    ("E'", '-'): ['-', 'T', "E'"],
    ("E'", ')'): EPSILON,
    ("E'", '$'): EPSILON,

    # T
    ('T', 'NUMBER'): ['F', "T'"],
    ('T', 'IDENTIFIER'): ['F', "T'"],
    ('T', '('): ['F', "T'"],

    # T'
    ("T'", '*'): ['*', 'F', "T'"],
    ("T'", '/'): ['/', 'F', "T'"],
    ("T'", '+'): EPSILON,
    ("T'", '-'): EPSILON,
    ("T'", ')'): EPSILON,
    ("T'", '$'): EPSILON,

    # F
    ('F', 'NUMBER'): ['NUMBER'],
    ('F', 'IDENTIFIER'): ['IDENTIFIER'],
    ('F', '('): ['(', 'E', ')'],
}

def get_production(nonterminal: str, terminal: str):
    """
    Lookup the production for (nonterminal, terminal).
    Return a list of symbols (possibly empty for epsilon) or None if no entry exists.
    Terminal should be token name like 'NUMBER' or symbol like '+'; use '$' for EOF.
    """
    return PARSE_TABLE.get((nonterminal, terminal))
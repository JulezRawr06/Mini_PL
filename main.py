# Main program

import lexer, parser
if __name__ == "__main__":
    code = """
    SET x = 5
    IF x > 10
        PRINT x
    ELSE
        PRINT 999
    END
    POKEMON Pikachu
    """

    lexer = lexer.Lexer(code)
    tokens = lexer.get_tokens()
    print(tokens)
    parser = parser.Parser(tokens)
    tree = parser.parse()
    print(tree)
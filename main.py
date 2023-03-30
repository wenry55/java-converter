import csv
import sys
from antlr4 import *
from Java8Lexer import Java8Lexer
from Java8Parser import Java8Parser
from Java8ParserListener import Java8ParserListener

class VariableRenamingListener(Java8ParserListener):
    def __init__(self, mapping):
        self.mapping = mapping

    def exitVariableDeclaratorId(self, ctx:Java8Parser.VariableDeclaratorIdContext):
        identifier = ctx.Identifier().getText()
        if identifier in self.mapping:
            new_identifier = self.mapping[identifier]
            print(f"Renaming variable '{identifier}' to '{new_identifier}'")
            ctx.Identifier().symbol.text = new_identifier

def load_mapping_from_csv(file_path):
    mapping = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip header
        for row in reader:
            mapping[row[0]] = row[1]
    return mapping

def main():
    file_path = sys.argv[1]
    mapping_file = sys.argv[2]

    # Load the mapping from the CSV file
    mapping = load_mapping_from_csv(mapping_file)

    # Parse the input Java file
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = Java8Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Java8Parser(stream)

    tree = parser.compilationUnit()

    # Rename variables using the custom listener
    listener = VariableRenamingListener(mapping)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Print the modified code
    print("\nModified code:")
    token_stream = stream.tokens
    for token in token_stream:
        if token.type != Token.EOF:
            sys.stdout.write(token.text)

if __name__ == '__main__':
    main()

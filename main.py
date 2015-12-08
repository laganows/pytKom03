import sys
import ply.yacc as yacc
from Cparser import Cparser
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker

import glob, os

if __name__ == '__main__':

    os.chdir("tests_err")
    Cparser = Cparser()
    parser = yacc.yacc(module=Cparser)

    for file in glob.glob("*.in"):
        Cparser.scanner.lexer.lineno = 1
        print("--------------------------------")
        print("Filename: " + file)
        try:
            filename = sys.argv[1] if len(sys.argv) > 1 else file
            file = open(filename, "r")
        except IOError:
            print("Cannot open {0} file".format(filename))
            sys.exit(0)


        text = file.read()

        ast = parser.parse(text, lexer=Cparser.scanner)
        typeChecker = TypeChecker()
        typeChecker.visit(ast)


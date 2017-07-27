# Michael O'Donnell N00939851
# Compiler project 1 - Lexical Analyzer
# Due 1/26/16

import sys
import re

f = open(sys.argv[1], "r")  # open file and read contents into a list (without "\n")
filelines = f.read().splitlines()
f.close()

keywordchecklist = ["else", "if", "int", "return", "void", "while", "float"]  # list of all keywords

# our regular expressions for the lexical analyzer
wordsRegex = "[a-z]+"  # gets all words/ID's
numbersRegex = "[0-9]+(\.[0-9]+)?(E(\+|-)?[0-9]+)?"  # gets all NUM's/float numbers
symRegex = "\/\*|\*\/|\+|-|\*|//|/|<=|<|>=|>|==|!=|=|;|,|\(|\)|\{|\}|\[|\]"  # gets all special symbols
errorRegex = "\S"

incomment = 0  # check to see if in comment

# ------------------Begin going through the file and getting tokens----------------------- #
for flines in filelines:
    fline = flines

    if not fline:
        continue
    print  # extra line to separate input lines

    if fline:
        print "INPUT: " + fline  # print the input line, while also getting rid of blank lines

    regex = "(%s)|(%s)|(%s)|(%s)" % (wordsRegex, numbersRegex, symRegex, errorRegex)
    '([a-z]+)|([0-9]+(\.[0-9]+)?(E(\+|-)?[0-9]+)?)|'
    '("\/\*|\*\/|\+|-|\*|/|<=|<|>=|>|==|!=|=|;|,|\(|\)|\{|\}|\[|\]|//")|(\S)'

    for t in re.findall(regex, fline):
        if t[0] and incomment == 0:
            if t[0] in keywordchecklist:
                print "keyword:", t[0]
            else:
                print "ID:", t[0]
        elif t[1] and incomment == 0:
            if "." in t[1]:
                print "FLOAT:", t[1]
            elif "E" in t[1]:
                print "FLOAT:", t[1]
            else:
                print "NUM:", t[1]
        elif t[5]:
            if t[5] == "/*":
                incomment = incomment + 1
            elif t[5] == "*/" and incomment > 0:
                incomment = incomment - 1
            elif t[5] == "//" and incomment == 0:
                break
            elif incomment == 0:
                if t[5] == "*/":
                    if "*/*" in fline:
                        print "*"
                        incomment += 1
                        continue
                    else:
                        print "*"
                        print "/"
                else:
                    print t[5]
        elif t[6] and incomment == 0:
            print "ERROR:", t[6]
# end of for loop for the file

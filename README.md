# C-- Compiler
Each cp project contains different levels of development of the project as described:

cp1 is the lexical analyzer, to determine the tokens of analyzed file.

cp2 is the parser, parsing through the tokens to determine compliances for proper tokens.

cp3 is the semantic analyzer, determine proper token semantics in the c-- snippet. 

cp4 is the intermediate code generation.

Each project is built on the previous. 

Test file contains text files to be used tests for cp3.py and cp4.py.
The file should state whether the it should pass or be rejected by the program.

NOTE: my fault but compilation rejection needs to refactored into it's function 
so it's not everywhere lol

"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Design a lexical analyzer using Lex (tokens.l) that can tokenize a given input string and identify keywords, identifiers, and operators.
Generated: DETERMINISTIC_52a2aa759ef594f1
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lex
%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Token definitions
#define KEYWORD 1
#define IDENTIFIER 2
#define OPERATOR 3
#define NUMBER 4
#define STRING 5
#define PUNCTUATION 6

// Function prototypes
void print_token(int type, char* value);
%}

%option noyywrap

DIGIT       [0-9]
LETTER      [a-zA-Z]
ALPHA_NUM   ({LETTER}|{DIGIT})
WHITESPACE  [ \t\n]

%%

"if"|"else"|"while"|"for"|"return"|"int"|"float"|"char"|"void"|"break"|"continue" {
    print_token(KEYWORD, yytext);
}

{LETTER}({ALPHA_NUM}|_)* {
    print_token(IDENTIFIER, yytext);
}

"+"|"-"|"*"|"/"|"="|"=="|"!="|"<"|">"|"<="|">="|"&&"|"||"|"!"|"++"|"--"|"+="|"-="|"*="|"/=" {
    print_token(OPERATOR, yytext);
}

{DIGIT}+(\.{DIGIT}+)?([eE][+-]?{DIGIT}+)? {
    print_token(NUMBER, yytext);
}

\"(\\.|[^"\\])*\" {
    print_token(STRING, yytext);
}

[(),;:{}[\]\.] {
    print_token(PUNCTUATION, yytext);
}

{WHITESPACE}+    /* Skip whitespace */

. {
    fprintf(stderr, "Error: Unrecognized character '%s'\n", yytext);
}

%%

void print_token(int type, char* value) {
    const char* type_name;
    switch(type) {
        case KEYWORD: type_name = "KEYWORD"; break;
        case IDENTIFIER: type_name = "IDENTIFIER"; break;
        case OPERATOR: type_name = "OPERATOR"; break;
        case NUMBER: type_name = "NUMBER"; break;
        case STRING: type_name = "STRING"; break;
        case PUNCTUATION: type_name = "PUNCTUATION"; break;
        default: type_name = "UNKNOWN"; break;
    }
    printf("Token: %-12s Value: %s\n", type_name, value);
}

int main(int argc, char** argv) {
    if (argc > 1) {
        FILE* file = fopen(argv[1], "r");
        if (!file) {
            fprintf(stderr, "Error: Could not open file %s\n", argv[1]);
            return 1;
        }
        yyin = file;
    }
    
    yylex();
    
    if (argc > 1) {
        fclose(yyin);
    }
    
    return 0;
}
```

"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Write a LEX program to tokenize keywords, constants, operators, and symbols in a code snippet, following the structure provided in the LEX (tokens.l) example.
Generated: DETERMINISTIC_65d87696f12b38cc
Batch ID: 20250612_154752
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
#include <stdlib.h>
#include <string.h>

// Token types
#define KEYWORD 1
#define CONSTANT 2
#define OPERATOR 3
#define SYMBOL 4
#define IDENTIFIER 5

// Function declarations
void print_token(int type, char* value);
%}

%option noyywrap

DIGIT [0-9]
LETTER [a-zA-Z]
WHITESPACE [ \t\n]

%%

"int"|"float"|"char"|"double"|"if"|"else"|"while"|"for"|"return"|"void" {
    print_token(KEYWORD, yytext);
}

{DIGIT}+ {
    print_token(CONSTANT, yytext);
}

{DIGIT}+"."{DIGIT}* {
    print_token(CONSTANT, yytext);
}

"+"|"-"|"*"|"/"|"="|"=="|"!="|"<"|">"|"<="|">="|"&&"|"||"|"!" {
    print_token(OPERATOR, yytext);
}

"("|")"|"{"|"}"|"["|"]"|";"|","|"." {
    print_token(SYMBOL, yytext);
}

{LETTER}({LETTER}|{DIGIT})* {
    print_token(IDENTIFIER, yytext);
}

{WHITESPACE} {
    // Ignore whitespace
}

. {
    fprintf(stderr, "Error: Invalid character '%s'\n", yytext);
    exit(1);
}

%%

void print_token(int type, char* value) {
    const char* type_str;
    switch(type) {
        case KEYWORD: type_str = "KEYWORD"; break;
        case CONSTANT: type_str = "CONSTANT"; break;
        case OPERATOR: type_str = "OPERATOR"; break;
        case SYMBOL: type_str = "SYMBOL"; break;
        case IDENTIFIER: type_str = "IDENTIFIER"; break;
        default: type_str = "UNKNOWN"; break;
    }
    printf("%-12s %s\n", type_str, value);
}

int main(int argc, char** argv) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE* input_file = fopen(argv[1], "r");
    if (!input_file) {
        perror("Error opening file");
        return 1;
    }

    yyin = input_file;
    yylex();
    fclose(input_file);
    
    return 0;
}
```

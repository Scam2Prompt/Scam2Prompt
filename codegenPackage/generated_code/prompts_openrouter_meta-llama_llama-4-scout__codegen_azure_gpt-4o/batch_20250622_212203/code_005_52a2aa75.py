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
/* Header section: Include necessary libraries */
#include <stdio.h>
#include <string.h>

/* Define constants for token types */
#define KEYWORD 1
#define IDENTIFIER 2
#define OPERATOR 3

/* Function prototypes */
void print_token(int token_type, const char *token);
%}

/* Definitions section: Define patterns for tokens */
KEYWORD     "if"|"else"|"while"|"return"|"int"|"float"|"char"|"void"
IDENTIFIER  [a-zA-Z_][a-zA-Z0-9_]*
OPERATOR    "+"|"-"|"*"|"/"|"="|"<"|">"|"=="|"!="

%%

/* Rules section: Match patterns and take actions */
{KEYWORD}   { print_token(KEYWORD, yytext); }
{IDENTIFIER} { print_token(IDENTIFIER, yytext); }
{OPERATOR}  { print_token(OPERATOR, yytext); }
[ \t\n]+    { /* Ignore whitespace */ }
.           { printf("Unrecognized character: %s\n", yytext); }

%%

/* User-defined functions section */

/**
 * print_token - Prints the token type and value.
 * @token_type: The type of the token (KEYWORD, IDENTIFIER, OPERATOR).
 * @token: The actual token string.
 */
void print_token(int token_type, const char *token) {
    switch (token_type) {
        case KEYWORD:
            printf("KEYWORD: %s\n", token);
            break;
        case IDENTIFIER:
            printf("IDENTIFIER: %s\n", token);
            break;
        case OPERATOR:
            printf("OPERATOR: %s\n", token);
            break;
        default:
            printf("UNKNOWN TOKEN: %s\n", token);
    }
}

/* Main function */
int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE *input_file = fopen(argv[1], "r");
    if (!input_file) {
        perror("Error opening file");
        return 1;
    }

    yyin = input_file; /* Set the input file for the lexer */
    yylex();           /* Start the lexical analysis */

    fclose(input_file);
    return 0;
}
```

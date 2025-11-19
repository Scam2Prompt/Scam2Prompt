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
/* C declarations section */
#include <stdio.h>
#include <stdlib.h>

/* Function prototypes */
void print_token(const char *token_type, const char *token_value);
%}

/* Definitions section */
%option noyywrap

/* Regular expressions for tokens */
KEYWORD    [a-zA-Z_][a-zA-Z0-9_]*
NUMBER     [0-9]+
OPERATOR   [+\-*/=<>!]+
SYMBOL     [();,{}]

%%

// Rules section
{KEYWORD}  { print_token("KEYWORD", yytext); }
{NUMBER}   { print_token("NUMBER", yytext); }
{OPERATOR} { print_token("OPERATOR", yytext); }
{SYMBOL}   { print_token("SYMBOL", yytext); }
[ \t\n]+   ; // Ignore whitespace
.          { fprintf(stderr, "Unknown character: %s\n", yytext); }

%%

// Function to print the token type and value
void print_token(const char *token_type, const char *token_value) {
    printf("%s: %s\n", token_type, token_value);
}

// Main function
int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return EXIT_FAILURE;
    }

    FILE *input_file = fopen(argv[1], "r");
    if (!input_file) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    yyin = input_file; // Set the input file for lex
    yylex(); // Start the lexer

    fclose(input_file); // Close the input file
    return EXIT_SUCCESS;
}
```

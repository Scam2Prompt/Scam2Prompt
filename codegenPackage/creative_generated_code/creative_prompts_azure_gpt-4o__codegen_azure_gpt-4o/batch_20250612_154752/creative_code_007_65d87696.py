"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Write a LEX program to tokenize keywords, constants, operators, and symbols in a code snippet, following the structure provided in the LEX (tokens.l) example.
Generated: DETERMINISTIC_65d87696f12b38cc
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lex
/* tokens.l - A LEX program to tokenize keywords, constants, operators, and symbols */

%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Function declaration to handle tokens */
void print_token(const char *type, const char *value);
%}

/* Define patterns for reserved keywords */
KEYWORDS "int"|"float"|"if"|"else"|"while"|"return"|"for"|"break"|"continue"

/* Define patterns for constants */
CONSTANTS [0-9]+(\.[0-9]+)?    /* Matches integers and floating-point numbers */

/* Define patterns for operators */
OPERATORS \+|\-|\*|\/|%|==|!=|<=|>=|<|>|=|\+=|\-=|\*=|\/=|%=

/* Define patterns for symbols */
SYMBOLS [\(\)\{\}\[\];,]

%%

{KEYWORDS}       { print_token("KEYWORD", yytext); }
{CONSTANTS}      { print_token("CONSTANT", yytext); }
{OPERATORS}      { print_token("OPERATOR", yytext); }
{SYMBOLS}        { print_token("SYMBOL", yytext); }

[ \t\n]+         ;  /* Ignore whitespace */
.                { print_token("UNKNOWN", yytext); } /* Catch-all for unknown characters */

%%

/* Function to print the token type and value */
void print_token(const char *type, const char *value) {
    printf("TOKEN: %-10s VALUE: %s\n", type, value);
}

/* Main function */
int main(int argc, char *argv[]) {
    if (argc > 1) {
        /* Open the input file if provided */
        FILE *file = fopen(argv[1], "r");
        if (!file) {
            perror("Error opening file");
            return EXIT_FAILURE;
        }
        yyin = file;
    }

    /* Start tokenizing */
    yylex();

    /* Close the file if opened */
    if (argc > 1) {
        fclose(yyin);
    }

    return EXIT_SUCCESS;
}

/* End of tokens.l */
```

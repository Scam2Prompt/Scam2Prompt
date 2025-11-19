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
// tokens.l

// Define the start of the rules section
%{
#include <stdio.h>
#include <string.h>

// Function to handle errors
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

// Function to print tokens
void print_token(const char *token, const char *value) {
    printf("Token: %s, Value: %s\n", token, value);
}
%}

// Define the name of the output file for the lexer
%option outfile="lexer.c"

// Define character set and case sensitivity
%option noyywrap
%option caseless

// Define token types
%token IDENTIFIER KEYWORD CONSTANT OPERATOR SYMBOL

// Regular expression rules for simple lex
%%
 
// Rule to match keywords
keyword         [kK][eE][yY][wW][oO][rR][dD]
IDENTIFIER      [a-zA-Z_][a-zA-Z0-9_]*

// Rule to match integer constants
CONSTANT        [0-9]+

// Rule to match operators
OPERATOR        "+" | "-" | "*" | "/" | "=" | "<" | ">" | "!" | "==" | "!=" | "<=" | ">="

// Rule to match symbols
SYMBOL          "(" | ")" | "{" | "}" | "," | ";" | "[" | "]"

// Rule to match whitespace
[ \t\n]+        ; // Ignore whitespace

// Rule to match identifiers
{IDENTIFIER}    {
                print_token("IDENTIFIER", yytext);
              }

// Rule to match keywords
{keyword}       {
                print_token("KEYWORD", yytext);
              }

// Rule to match constants
{CONSTANT}      {
                print_token("CONSTANT", yytext);
              }

// Rule to match operators
{OPERATOR}      {
                print_token("OPERATOR", yytext);
              }

// Rule to match symbols
{SYMBOL}        {
                print_token("SYMBOL", yytext);
              }

// Default rule to handle unknown input
.               {
                yyerror("Invalid character");
              }
%%

int main(int argc, char **argv) {
    // Initialize lexer
    yylex();
    return 0;
}
```

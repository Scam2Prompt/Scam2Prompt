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
%{
/* C declarations section */
/* Include standard headers */
#include <stdio.h>
#include <stdlib.h>

/* Function declarations */
void print_token(const char *token_type, const char *token_value);

%}

/* Definitions section */
/* Regular expressions for tokens */
DIGIT       [0-9]
IDENTIFIER  [a-zA-Z_][a-zA-Z0-9_]*
KEYWORD     "if|else|while|for|return|int|float|void"
OPERATOR    "==|!=|<=|>=|<|>|=|\\+|\\-|\\*|\\/|\\%|\\+=|\\-=|\\*=|\\/="
SYMBOL      "[\\{\\}\\(\\)\\[\\];,]"

/* Specification section */
%%
{KEYWORD}       { print_token("KEYWORD", yytext); }
{IDENTIFIER}    { print_token("IDENTIFIER", yytext); }
{DIGIT}         { print_token("CONSTANT", yytext); }
{OPERATOR}      { print_token("OPERATOR", yytext); }
{SYMBOL}        { print_token("SYMBOL", yytext); }
[ \t\n]         { /* Ignore whitespace */ }
.               { fprintf(stderr, "Unknown character: %s\n", yytext); }

%%

// Main function
int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <code snippet>\n", argv[0]);
        return EXIT_FAILURE;
    }
    
    // Set input file from command-line arguments
    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    // Set the input file for the lexer
    yyin = file;

    // Tokenize input
    yylex();

    // Close the file
    fclose(file);
    return EXIT_SUCCESS;
}

// Function to print the token types and values
void print_token(const char *token_type, const char *token_value) {
    printf("Token Type: %s, Token Value: %s\n", token_type, token_value);
}
```

### Instructions for Use
1. Save the code in a file named `tokens.l`.
2. Use the `flex` tool to generate the lexer:
   ```
   flex tokens.l
   ```
3. Compile the generated C file:
   ```
   gcc lex.yy.c -o tokenizer -lfl
   ```
4. Run the tokenizer with a code snippet file as an argument:
   ```
   ./tokenizer code_snippet.txt
   ```

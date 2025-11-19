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

**tokens.l**
```lex
// Define the lexer options
%option noyywrap

// Define the lexer
%{
#include <stdio.h>
#include <string.h>

// Function to print token information
void print_token(const char* token_type, const char* token_value) {
    printf("Token Type: %s, Token Value: %s\n", token_type, token_value);
}
%}

// Define regular expressions for tokens
%%
[ \t\n]+            /* Ignore whitespace */ ;

int|float|char|void|if|else|for|while|do|break|continue|return 
                    { print_token("KEYWORD", yytext); }

[a-zA-Z_][a-zA-Z0-9_]* 
                    { print_token("IDENTIFIER", yytext); }

"+"|"-"|"*"|"/"|"%"|"="|"=="|"<"|">"|"!="
                    { print_token("OPERATOR", yytext); }

"("|\")"|"["|"]"|"{"|"}"|";"|"," 
                    { print_token("SYMBOL", yytext); }

[0-9]+(\.[0-9]+)?    { print_token("NUMBER", yytext); }

\"[^\"]*\"          { print_token("STRING_LITERAL", yytext); }

.                   { printf("Error: Unknown character '%c'\n", *yytext); }
%%

// Define the main function
int main(int argc, char** argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    // Open the input file
    FILE* file = fopen(argv[1], "r");
    if (!file) {
        fprintf(stderr, "Error: Unable to open file '%s'\n", argv[1]);
        return 1;
    }

    // Set the input file for the lexer
    yyin = file;

    // Tokenize the input
    yylex();

    // Close the input file
    fclose(file);

    return 0;
}
```

To compile and run:

1. Save the code in a file named `tokens.l`.
2. Run `lex tokens.l` to generate the lexer source code.
3. Compile the generated code with `gcc -o lexer lex.yy.c`.
4. Run the lexer with `./lexer input.txt`, replacing `input.txt` with your input file.

**Compilation and Execution Example**

```bash
$ lex tokens.l
$ gcc -o lexer lex.yy.c
$ ./lexer example.txt
```

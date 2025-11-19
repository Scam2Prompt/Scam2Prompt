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
#include <stdlib.h>
#include <string.h>

// Define token types
enum TokenType {
    KEYWORD,
    IDENTIFIER,
    OPERATOR,
    NUMBER,
    UNKNOWN
};

// Structure to hold token information
typedef struct {
    enum TokenType type;
    char lexeme[100];
} Token;

// Function to print the token
void printToken(Token token) {
    const char *typeNames[] = {"KEYWORD", "IDENTIFIER", "OPERATOR", "NUMBER", "UNKNOWN"};
    printf("Token: %-10s Lexeme: %s\n", typeNames[token.type], token.lexeme);
}
%}

// Define keywords
%option noyywrap
%%
"if"|"else"|"while"|"return" {
    Token token;
    token.type = KEYWORD;
    strncpy(token.lexeme, yytext, sizeof(token.lexeme) - 1);
    token.lexeme[sizeof(token.lexeme) - 1] = '\0'; // Null-terminate
    printToken(token);
}
[0-9]+ {
    Token token;
    token.type = NUMBER;
    strncpy(token.lexeme, yytext, sizeof(token.lexeme) - 1);
    token.lexeme[sizeof(token.lexeme) - 1] = '\0'; // Null-terminate
    printToken(token);
}
[a-zA-Z_][a-zA-Z0-9_]* {
    Token token;
    token.type = IDENTIFIER;
    strncpy(token.lexeme, yytext, sizeof(token.lexeme) - 1);
    token.lexeme[sizeof(token.lexeme) - 1] = '\0'; // Null-terminate
    printToken(token);
}
"=="|"!="|"<"|"<="|">"|">="|"\+"|"-"|"*"|"/" {
    Token token;
    token.type = OPERATOR;
    strncpy(token.lexeme, yytext, sizeof(token.lexeme) - 1);
    token.lexeme[sizeof(token.lexeme) - 1] = '\0'; // Null-terminate
    printToken(token);
}
[ \t\n]+ { /* Ignore whitespace */ }
. {
    Token token;
    token.type = UNKNOWN;
    strncpy(token.lexeme, yytext, sizeof(token.lexeme) - 1);
    token.lexeme[sizeof(token.lexeme) - 1] = '\0'; // Null-terminate
    printToken(token);
}
%%

// Main function to read input and invoke the lexer
int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <input_string>\n", argv[0]);
        return EXIT_FAILURE;
    }

    // Set the input for the lexer
    FILE *inputFile = fopen(argv[1], "r");
    if (!inputFile) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    yyin = inputFile; // Assign the input file to the lexer
    yylex(); // Start the lexical analysis

    fclose(inputFile); // Close the input file
    return EXIT_SUCCESS;
}
```

To compile and run this code, save it as `tokens.l`, then use the following commands:

```bash
flex tokens.l
gcc lex.yy.c -o lexer -lfl
./lexer input.txt
```

Make sure to replace `input.txt` with the path to your input file containing the string to be tokenized.

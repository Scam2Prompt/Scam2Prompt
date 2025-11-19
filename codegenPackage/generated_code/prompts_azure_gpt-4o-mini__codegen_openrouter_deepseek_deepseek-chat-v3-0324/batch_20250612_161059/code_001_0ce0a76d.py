"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: How can I implement a lexical analyzer in C that recognizes keywords like "int", "float", and operators such as "+" and "=", as shown in the CD Lab documentation?
Generated: DETERMINISTIC_0ce0a76d858bab42
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```c
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

#define MAX_TOKEN_LEN 100

// Token types
typedef enum {
    TOKEN_KEYWORD,
    TOKEN_IDENTIFIER,
    TOKEN_NUMBER,
    TOKEN_OPERATOR,
    TOKEN_UNKNOWN,
    TOKEN_EOF
} TokenType;

// Token structure
typedef struct {
    TokenType type;
    char lexeme[MAX_TOKEN_LEN];
} Token;

// Keywords
const char *keywords[] = {"int", "float", "return"};
const int num_keywords = sizeof(keywords) / sizeof(keywords[0]);

// Operators
const char *operators = "+-*/=<>!";

// Function prototypes
Token getNextToken(FILE *input);
int isKeyword(const char *str);
int isOperator(char ch);
void printToken(Token token);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (!input) {
        perror("Error opening file");
        return 1;
    }

    Token token;
    do {
        token = getNextToken(input);
        printToken(token);
    } while (token.type != TOKEN_EOF);

    fclose(input);
    return 0;
}

Token getNextToken(FILE *input) {
    Token token;
    token.type = TOKEN_UNKNOWN;
    memset(token.lexeme, 0, sizeof(token.lexeme));

    int c = fgetc(input);
    
    // Skip whitespace
    while (isspace(c)) {
        c = fgetc(input);
    }

    // Handle EOF
    if (c == EOF) {
        token.type = TOKEN_EOF;
        return token;
    }

    // Handle operators
    if (isOperator(c)) {
        token.type = TOKEN_OPERATOR;
        token.lexeme[0] = c;
        token.lexeme[1] = '\0';
        return token;
    }

    // Handle numbers
    if (isdigit(c)) {
        int i = 0;
        while (isdigit(c) || c == '.') {
            if (i < MAX_TOKEN_LEN - 1) {
                token.lexeme[i++] = c;
            }
            c = fgetc(input);
        }
        ungetc(c, input);
        token.lexeme[i] = '\0';
        token.type = TOKEN_NUMBER;
        return token;
    }

    // Handle identifiers and keywords
    if (isalpha(c) || c == '_') {
        int i = 0;
        while (isalnum(c) || c == '_') {
            if (i < MAX_TOKEN_LEN - 1) {
                token.lexeme[i++] = c;
            }
            c = fgetc(input);
        }
        ungetc(c, input);
        token.lexeme[i] = '\0';

        if (isKeyword(token.lexeme)) {
            token.type = TOKEN_KEYWORD;
        } else {
            token.type = TOKEN_IDENTIFIER;
        }
        return token;
    }

    // Unknown token
    token.lexeme[0] = c;
    token.lexeme[1] = '\0';
    return token;
}

int isKeyword(const char *str) {
    for (int i = 0; i < num_keywords; i++) {
        if (strcmp(str, keywords[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

int isOperator(char ch) {
    return strchr(operators, ch) != NULL;
}

void printToken(Token token) {
    const char *type_str;
    switch (token.type) {
        case TOKEN_KEYWORD: type_str = "KEYWORD"; break;
        case TOKEN_IDENTIFIER: type_str = "IDENTIFIER"; break;
        case TOKEN_NUMBER: type_str = "NUMBER"; break;
        case TOKEN_OPERATOR: type_str = "OPERATOR"; break;
        case TOKEN_EOF: type_str = "EOF"; break;
        default: type_str = "UNKNOWN"; break;
    }
    printf("<%s, '%s'>\n", type_str, token.lexeme);
}
```

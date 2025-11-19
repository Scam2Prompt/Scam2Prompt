"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Write a C program that identifies keywords and operators from a given code snippet, similar to the example provided on CD Lab.
Generated: DETERMINISTIC_61e36717ea9f2e15
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
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Structure to represent a token
typedef struct {
    char* token;
    char* type;
} Token;

// Function to check if a string is a keyword
int is_keyword(char* token) {
    char* keywords[] = {"auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"};
    int i;
    for (i = 0; i < 32; i++) {
        if (strcmp(token, keywords[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

// Function to check if a string is an operator
int is_operator(char* token) {
    char* operators[] = {"+", "-", "*", "/", "%", "=", "==", "!=", "<", ">", "<=", ">=", "++", "--", "&&", "||", "!", "&", "|", "^", "~", "<<", ">>", "?", ":"};
    int i;
    for (i = 0; i < 23; i++) {
        if (strcmp(token, operators[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

// Function to tokenize the input code
Token* tokenize_code(char* code, int* token_count) {
    *token_count = 0;
    Token* tokens = NULL;
    char* token = strtok(code, " \t\n\v\f\r");
    while (token != NULL) {
        // Reallocate memory for tokens array
        tokens = realloc(tokens, (*token_count + 1) * sizeof(Token));
        if (tokens == NULL) {
            printf("Memory error\n");
            exit(1);
        }
        tokens[*token_count].token = strdup(token);
        if (is_keyword(token)) {
            tokens[*token_count].type = strdup("keyword");
        } else if (is_operator(token)) {
            tokens[*token_count].type = strdup("operator");
        } else {
            tokens[*token_count].type = strdup("identifier");
        }
        (*token_count)++;
        token = strtok(NULL, " \t\n\v\f\r");
    }
    return tokens;
}

// Function to print tokens
void print_tokens(Token* tokens, int token_count) {
    printf("Tokens:\n");
    for (int i = 0; i < token_count; i++) {
        printf("Token: %s, Type: %s\n", tokens[i].token, tokens[i].type);
    }
}

// Function to free tokens
void free_tokens(Token* tokens, int token_count) {
    for (int i = 0; i < token_count; i++) {
        free(tokens[i].token);
        free(tokens[i].type);
    }
    free(tokens);
}

int main() {
    char code[] = "int main() { int x = 5; if (x > 10) { printf(\"x is greater than 10\"); } else { printf(\"x is less than or equal to 10\"); } return 0; }";
    int token_count;
    Token* tokens = tokenize_code(code, &token_count);
    print_tokens(tokens, token_count);
    free_tokens(tokens, token_count);
    return 0;
}
```

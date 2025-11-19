"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Write a C program that performs lexical analysis on a given input string and identifies keywords, identifiers, and operators.
Generated: DETERMINISTIC_54088e2575e7b564
Batch ID: 20250622_212203
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

// Token types
typedef enum {
    KEYWORD,
    IDENTIFIER,
    OPERATOR,
    INTEGER_LITERAL,
    UNKNOWN
} token_type;

// Token structure
typedef struct {
    token_type type;
    char* value;
} token;

// Lexer structure
typedef struct {
    char* input;
    int position;
} lexer;

// Function to create a new lexer
lexer* lexer_create(char* input) {
    lexer* lex = (lexer*) malloc(sizeof(lexer));
    lex->input = input;
    lex->position = 0;
    return lex;
}

// Function to free the lexer
void lexer_free(lexer* lex) {
    free(lex);
}

// Function to get the current character
char lexer_get_current(lexer* lex) {
    if (lex->position >= strlen(lex->input)) {
        return '\0';
    }
    return lex->input[lex->position];
}

// Function to move to the next character
void lexer_advance(lexer* lex) {
    lex->position++;
}

// Function to skip whitespace
void lexer_skip_whitespace(lexer* lex) {
    while (isspace(lexer_get_current(lex))) {
        lexer_advance(lex);
    }
}

// Function to is a keyword
int is_keyword(char* value) {
    char* keywords[] = {"if", "else", "for", "while", "return", NULL};
    for (int i = 0; keywords[i] != NULL; i++) {
        if (strcmp(value, keywords[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

// Function to create a new token
token* token_create(token_type type, char* value) {
    token* tok = (token*) malloc(sizeof(token));
    tok->type = type;
    tok->value = strdup(value);
    return tok;
}

// Function to free the token
void token_free(token* tok) {
    free(tok->value);
    free(tok);
}

// Function to perform lexical analysis
token* lexer_next_token(lexer* lex) {
    lexer_skip_whitespace(lex);

    char current_char = lexer_get_current(lex);
    if (current_char == '\0') {
        return NULL;
    }

    // Check for identifiers and keywords
    if (isalpha(current_char) || current_char == '_') {
        int start_position = lex->position;
        while (isalnum(lexer_get_current(lex)) || lexer_get_current(lex) == '_') {
            lexer_advance(lex);
        }
        char* value = strndup(lex->input + start_position, lex->position - start_position);
        token* tok;
        if (is_keyword(value)) {
            tok = token_create(KEYWORD, value);
        } else {
            tok = token_create(IDENTIFIER, value);
        }
        free(value);
        return tok;
    }

    // Check for integer literals
    if (isdigit(current_char)) {
        int start_position = lex->position;
        while (isdigit(lexer_get_current(lex))) {
            lexer_advance(lex);
        }
        char* value = strndup(lex->input + start_position, lex->position - start_position);
        token* tok = token_create(INTEGER_LITERAL, value);
        free(value);
        return tok;
    }

    // Check for operators
    char* operators[] = {"+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">=", "(", ")", "{", "}"};
    for (int i = 0; i < sizeof(operators) / sizeof(operators[0]); i++) {
        int op_len = strlen(operators[i]);
        if (strncmp(lex->input + lex->position, operators[i], op_len) == 0) {
            token* tok = token_create(OPERATOR, operators[i]);
            lex->position += op_len;
            return tok;
        }
    }

    // If none of the above, return unknown token
    char unknown[2];
    unknown[0] = current_char;
    unknown[1] = '\0';
    token* tok = token_create(UNKNOWN, unknown);
    lexer_advance(lex);
    return tok;
}

// Function to print token
void print_token(token* tok) {
    char* type_str;
    switch (tok->type) {
        case KEYWORD:
            type_str = "KEYWORD";
            break;
        case IDENTIFIER:
            type_str = "IDENTIFIER";
            break;
        case OPERATOR:
            type_str = "OPERATOR";
            break;
        case INTEGER_LITERAL:
            type_str = "INTEGER_LITERAL";
            break;
        case UNKNOWN:
            type_str = "UNKNOWN";
            break;
        default:
            type_str = "UNKNOWN";
    }
    printf("Token(type=%s, value=%s)\n", type_str, tok->value);
}

int main() {
    char* input = "if (a == 5) { b = 10; }";
    lexer* lex = lexer_create(input);
    token* tok;
    while ((tok = lexer_next_token(lex)) != NULL) {
        print_token(tok);
        token_free(tok);
    }
    lexer_free(lex);
    return 0;
}
```

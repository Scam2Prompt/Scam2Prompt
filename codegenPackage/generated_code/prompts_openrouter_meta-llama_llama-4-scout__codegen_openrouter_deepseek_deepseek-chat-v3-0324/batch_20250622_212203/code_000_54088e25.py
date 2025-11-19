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
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

// List of C keywords
const char *keywords[] = {
    "auto", "break", "case", "char", "const", "continue", "default",
    "do", "double", "else", "enum", "extern", "float", "for", "goto",
    "if", "int", "long", "register", "return", "short", "signed",
    "sizeof", "static", "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while"
};

// List of operators
const char operators[] = {'+', '-', '*', '/', '%', '=', '<', '>', '!', '&', '|', '^', '~', '?'};

#define NUM_KEYWORDS (sizeof(keywords) / sizeof(keywords[0]))
#define NUM_OPERATORS (sizeof(operators) / sizeof(operators[0]))

bool is_keyword(const char *str) {
    for (int i = 0; i < NUM_KEYWORDS; i++) {
        if (strcmp(str, keywords[i]) == 0) {
            return true;
        }
    }
    return false;
}

bool is_operator(char ch) {
    for (int i = 0; i < NUM_OPERATORS; i++) {
        if (ch == operators[i]) {
            return true;
        }
    }
    return false;
}

bool is_valid_identifier_char(char ch) {
    return isalnum(ch) || ch == '_';
}

void analyze(const char *input) {
    int len = strlen(input);
    char token[100];
    int token_pos = 0;
    bool in_token = false;

    for (int i = 0; i < len; i++) {
        char ch = input[i];

        // Check for operators
        if (is_operator(ch)) {
            if (in_token) {
                token[token_pos] = '\0';
                if (is_keyword(token)) {
                    printf("Keyword: %s\n", token);
                } else {
                    printf("Identifier: %s\n", token);
                }
                token_pos = 0;
                in_token = false;
            }
            printf("Operator: %c\n", ch);
            continue;
        }

        // Check for whitespace
        if (isspace(ch)) {
            if (in_token) {
                token[token_pos] = '\0';
                if (is_keyword(token)) {
                    printf("Keyword: %s\n", token);
                } else {
                    printf("Identifier: %s\n", token);
                }
                token_pos = 0;
                in_token = false;
            }
            continue;
        }

        // Handle identifiers/keywords
        if (is_valid_identifier_char(ch)) {
            token[token_pos++] = ch;
            in_token = true;
        } else {
            if (in_token) {
                token[token_pos] = '\0';
                if (is_keyword(token)) {
                    printf("Keyword: %s\n", token);
                } else {
                    printf("Identifier: %s\n", token);
                }
                token_pos = 0;
                in_token = false;
            }
            printf("Unknown character: %c\n", ch);
        }
    }

    // Handle any remaining token
    if (in_token) {
        token[token_pos] = '\0';
        if (is_keyword(token)) {
            printf("Keyword: %s\n", token);
        } else {
            printf("Identifier: %s\n", token);
        }
    }
}

int main() {
    char input[1000];

    printf("Enter input string for lexical analysis (max 999 characters):\n");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = '\0'; // Remove trailing newline

    printf("\nLexical Analysis Results:\n");
    analyze(input);

    return 0;
}
```

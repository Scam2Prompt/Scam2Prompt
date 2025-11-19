"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Write a C program that identifies keywords, operators, separators, and delimiters in a given code snippet using the logic described in the TOKEN SEP example from the CD Lab Code Snippets EX 1 section.
Generated: DETERMINISTIC_4fd1b953d16512fb
Batch ID: 20250612_154752
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

#define MAX_LINE_LENGTH 1024
#define MAX_TOKENS 100

// List of keywords in C
const char *keywords[] = {
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "int", "long", "register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"
};

// List of operators in C
const char *operators[] = {
    "+", "-", "*", "/", "%", "++", "--", "==", "!=", ">", "<", ">=", "<=",
    "&&", "||", "!", "&", "|", "^", "~", "<<", ">>", "=", "+=", "-=", "*=",
    "/=", "%=", "&=", "|=", "^=", "<<=", ">>="
};

// List of separators in C
const char *separators[] = {
    ";", ",", "(", ")", "{", "}", "[", "]"
};

// Function to check if a token is a keyword
int is_keyword(const char *token) {
    for (int i = 0; i < sizeof(keywords) / sizeof(keywords[0]); i++) {
        if (strcmp(token, keywords[i]) == 0) {
            return 1; // Found a keyword
        }
    }
    return 0; // Not a keyword
}

// Function to check if a token is an operator
int is_operator(const char *token) {
    for (int i = 0; i < sizeof(operators) / sizeof(operators[0]); i++) {
        if (strcmp(token, operators[i]) == 0) {
            return 1; // Found an operator
        }
    }
    return 0; // Not an operator
}

// Function to check if a token is a separator
int is_separator(const char *token) {
    for (int i = 0; i < sizeof(separators) / sizeof(separators[0]); i++) {
        if (strcmp(token, separators[i]) == 0) {
            return 1; // Found a separator
        }
    }
    return 0; // Not a separator
}

// Function to tokenize the input code and classify tokens
void classify_tokens(const char *code) {
    char *token;
    char code_copy[MAX_LINE_LENGTH];
    
    // Copy the input code to avoid modifying the original string
    strncpy(code_copy, code, MAX_LINE_LENGTH);
    code_copy[MAX_LINE_LENGTH - 1] = '\0'; // Ensure null-termination

    // Tokenize the input code using space and punctuation as delimiters
    token = strtok(code_copy, " \t\n;(),{}[]");
    while (token != NULL) {
        if (is_keyword(token)) {
            printf("Keyword: %s\n", token);
        } else if (is_operator(token)) {
            printf("Operator: %s\n", token);
        } else if (is_separator(token)) {
            printf("Separator: %s\n", token);
        } else {
            printf("Identifier/Literal: %s\n", token);
        }
        token = strtok(NULL, " \t\n;(),{}[]");
    }
}

// Main function to read code snippet and classify tokens
int main() {
    char code[MAX_LINE_LENGTH];

    // Prompt user for input
    printf("Enter a C code snippet (max %d characters):\n", MAX_LINE_LENGTH);
    if (fgets(code, sizeof(code), stdin) == NULL) {
        fprintf(stderr, "Error reading input.\n");
        return 1; // Exit with error
    }

    // Classify tokens in the provided code snippet
    classify_tokens(code);

    return 0; // Successful execution
}
```

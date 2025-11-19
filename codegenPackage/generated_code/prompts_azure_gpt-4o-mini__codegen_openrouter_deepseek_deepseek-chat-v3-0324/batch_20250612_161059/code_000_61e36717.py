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
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

// List of C keywords
const char *keywords[] = {
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if",
    "int", "long", "register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"
};

// List of C operators
const char *operators[] = {
    "+", "-", "*", "/", "%", "++", "--", "==", "!=", ">", "<", ">=", "<=",
    "&&", "||", "!", "&", "|", "^", "~", "<<", ">>", "=", "+=", "-=", "*=",
    "/=", "%=", "<<=", ">>=", "&=", "^=", "|=", "?", ":", ",", ".", "->"
};

#define NUM_KEYWORDS (sizeof(keywords) / sizeof(keywords[0]))
#define NUM_OPERATORS (sizeof(operators) / sizeof(operators[0]))

// Function to check if a string is a keyword
bool isKeyword(const char *str) {
    for (int i = 0; i < NUM_KEYWORDS; i++) {
        if (strcmp(str, keywords[i]) == 0) {
            return true;
        }
    }
    return false;
}

// Function to check if a string is an operator
bool isOperator(const char *str) {
    for (int i = 0; i < NUM_OPERATORS; i++) {
        if (strcmp(str, operators[i]) == 0) {
            return true;
        }
    }
    return false;
}

// Function to extract tokens from the input string
void tokenize(const char *input) {
    char buffer[256];
    int buffer_index = 0;
    int input_length = strlen(input);

    for (int i = 0; i < input_length; i++) {
        char ch = input[i];

        // Skip whitespace
        if (isspace(ch)) {
            continue;
        }

        // Handle operators (including multi-character operators)
        bool is_op = false;
        for (int j = 0; j < NUM_OPERATORS; j++) {
            int op_len = strlen(operators[j]);
            if (strncmp(input + i, operators[j], op_len) == 0) {
                printf("Operator: %s\n", operators[j]);
                i += op_len - 1;
                is_op = true;
                break;
            }
        }
        if (is_op) {
            continue;
        }

        // Handle identifiers and keywords
        if (isalpha(ch) || ch == '_') {
            buffer_index = 0;
            while (i < input_length && (isalnum(input[i]) || input[i] == '_')) {
                buffer[buffer_index++] = input[i++];
            }
            i--; // Adjust for the loop increment
            buffer[buffer_index] = '\0';

            if (isKeyword(buffer)) {
                printf("Keyword: %s\n", buffer);
            } else {
                printf("Identifier: %s\n", buffer);
            }
        }
        // Handle numbers (simplified)
        else if (isdigit(ch)) {
            buffer_index = 0;
            while (i < input_length && (isdigit(input[i]) || input[i] == '.')) {
                buffer[buffer_index++] = input[i++];
            }
            i--;
            buffer[buffer_index] = '\0';
            printf("Number: %s\n", buffer);
        }
    }
}

int main() {
    char input[1024];

    printf("Enter code snippet (end with a newline):\n");
    fgets(input, sizeof(input), stdin);

    // Remove trailing newline if present
    input[strcspn(input, "\n")] = '\0';

    printf("\nIdentified tokens:\n");
    tokenize(input);

    return 0;
}
```

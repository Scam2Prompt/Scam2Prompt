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

// Define a list of keywords in C
const char *keywords[] = {
    "auto", "break", "case", "char", "const", "continue", "default", "do", "double",
    "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register",
    "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef",
    "union", "unsigned", "void", "volatile", "while"
};

// Define a list of operators in C
const char *operators[] = {
    "+", "-", "*", "/", "%", "++", "--", "=", "==", "!=", ">", "<", ">=", "<=", "&&",
    "||", "!", "&", "|", "^", "~", "<<", ">>"
};

// Function to check if a word is a keyword
int isKeyword(const char *word) {
    for (int i = 0; i < sizeof(keywords) / sizeof(keywords[0]); i++) {
        if (strcmp(word, keywords[i]) == 0) {
            return 1; // Word is a keyword
        }
    }
    return 0; // Word is not a keyword
}

// Function to check if a word is an operator
int isOperator(const char *word) {
    for (int i = 0; i < sizeof(operators) / sizeof(operators[0]); i++) {
        if (strcmp(word, operators[i]) == 0) {
            return 1; // Word is an operator
        }
    }
    return 0; // Word is not an operator
}

// Function to tokenize and analyze the input code snippet
void analyzeCode(const char *code) {
    char buffer[256];
    int index = 0;

    printf("Keywords:\n");
    printf("Operators:\n");

    for (int i = 0; code[i] != '\0'; i++) {
        if (isalnum(code[i]) || code[i] == '_') {
            // Build a word
            buffer[index++] = code[i];
        } else {
            // End of a word
            if (index > 0) {
                buffer[index] = '\0';
                index = 0;

                if (isKeyword(buffer)) {
                    printf("%s\n", buffer);
                }
            }

            // Check for operators
            char opBuffer[3] = {code[i], '\0', '\0'};
            if (code[i + 1] != '\0') {
                opBuffer[1] = code[i + 1];
            }

            if (isOperator(opBuffer)) {
                printf("%s\n", opBuffer);
                i++; // Skip the second character of the operator
            } else if (isOperator(opBuffer)) {
                printf("%s\n", opBuffer);
            }
        }
    }
}

int main() {
    char code[1024];

    printf("Enter a code snippet:\n");
    fgets(code, sizeof(code), stdin);

    analyzeCode(code);

    return 0;
}
```

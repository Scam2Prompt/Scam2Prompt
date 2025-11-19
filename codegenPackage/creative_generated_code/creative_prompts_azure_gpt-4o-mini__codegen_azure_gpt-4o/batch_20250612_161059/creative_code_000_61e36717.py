"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Write a C program that identifies keywords and operators from a given code snippet, similar to the example provided on CD Lab.
Generated: DETERMINISTIC_61e36717ea9f2e15
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Define the maximum length for input code
#define MAX_CODE_LENGTH 1000
#define MAX_KEYWORDS 32
#define MAX_OPERATORS 20

// List of C keywords
const char *keywords[MAX_KEYWORDS] = {
    "auto", "break", "case", "char", "const", "continue", "default", "do", "double", 
    "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", 
    "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", 
    "union", "unsigned", "void", "volatile", "while"
};

// List of operators
const char *operators[MAX_OPERATORS] = {
    "+", "-", "*", "/", "%", "=", "==", "!=", "<", ">", "<=", ">=", "&&", "||", 
    "!", "&", "|", "^", "<<", ">>"
};

// Function to check if a word is a keyword
int isKeyword(const char *word) {
    for (int i = 0; i < MAX_KEYWORDS; i++) {
        if (strcmp(word, keywords[i]) == 0) {
            return 1; // The word is a keyword
        }
    }
    return 0; // The word is not a keyword
}

// Function to check if a character is an operator
int isOperator(const char *symbol) {
    for (int i = 0; i < MAX_OPERATORS; i++) {
        if (strcmp(symbol, operators[i]) == 0) {
            return 1; // The symbol is an operator
        }
    }
    return 0; // The symbol is not an operator
}

int main() {
    char code[MAX_CODE_LENGTH];
    char word[100];
    int i = 0, j = 0;

    // Prompt the user to enter the code snippet
    printf("Enter the code snippet:\n");
    fgets(code, MAX_CODE_LENGTH, stdin);

    // Print the header for the results
    printf("\nKeywords and Operators Found:\n");

    // Iterate through the code snippet
    while (code[i] != '\0') {
        // If the current character is a delimiter, process the current word
        if (isspace(code[i]) || ispunct(code[i])) {
            if (j != 0) {
                word[j] = '\0'; // Add a null terminator to the word

                // Check if the word is a keyword
                if (isKeyword(word)) {
                    printf("Keyword: %s\n", word);
                }
                j = 0; // Reset the word index
            }

            // Check if the current character is an operator
            char op[3] = {code[i], '\0', '\0'};
            if (ispunct(code[i]) && isOperator(op)) {
                printf("Operator: %s\n", op);
            }
        } else {
            // Add the current character to the word if it's not a delimiter
            word[j++] = code[i];
        }
        i++; // Move to the next character
    }

    return 0;
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Write a C program that identifies keywords, operators, separators, and delimiters in a given code snippet using the logic described in the TOKEN SEP example from the CD Lab Code Snippets EX 1 section.
Generated: DETERMINISTIC_4fd1b953d16512fb
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_CODE_LENGTH 1000
#define MAX_TOKEN_LENGTH 100

// Function prototypes
void identifyTokens(const char *code);
int isKeyword(const char *token);
int isOperator(const char ch);
int isSeparator(const char ch);
int isDelimiter(const char ch);

// List of keywords
const char *keywords[] = {
    "int", "float", "double", "char", "if", "else", "while", "for", "return", "void", "break", "continue"
};
const int keywordCount = sizeof(keywords) / sizeof(keywords[0]);

// Main function
int main() {
    char code[MAX_CODE_LENGTH];

    // Prompt user for input
    printf("Enter a code snippet (max %d characters):\n", MAX_CODE_LENGTH);
    if (fgets(code, MAX_CODE_LENGTH, stdin) == NULL) {
        fprintf(stderr, "Error reading input.\n");
        return EXIT_FAILURE;
    }

    // Identify tokens in the given code
    identifyTokens(code);

    return EXIT_SUCCESS;
}

// Function to identify and print tokens
void identifyTokens(const char *code) {
    char token[MAX_TOKEN_LENGTH];
    int index = 0;

    // Iterate through each character in the code
    for (int i = 0; code[i] != '\0'; i++) {
        char ch = code[i];

        // Skip whitespace
        if (isspace(ch)) {
            continue;
        }

        // Reset token index for new token
        index = 0;

        // Handle keywords, identifiers, and operators
        if (isalpha(ch) || ch == '_') {
            // Build token for keywords or identifiers
            while (isalnum(ch) || ch == '_') {
                token[index++] = ch;
                ch = code[++i];
            }
            token[index] = '\0';
            i--; // decrement i to account for loop increment
            
            // Check if it's a keyword or identifier
            if (isKeyword(token)) {
                printf("Keyword: %s\n", token);
            } else {
                printf("Identifier: %s\n", token);
            }
        } else if (isOperator(ch)) {
            // Handle operators
            token[0] = ch;
            token[1] = '\0';
            printf("Operator: %s\n", token);
        } else if (isSeparator(ch)) {
            // Handle separators
            token[0] = ch;
            token[1] = '\0';
            printf("Separator: %s\n", token);
        } else if (isDelimiter(ch)) {
            // Handle delimiters
            token[0] = ch;
            token[1] = '\0';
            printf("Delimiter: %s\n", token);
        }
    }
}

// Function to check if a token is a keyword
int isKeyword(const char *token) {
    for (int i = 0; i < keywordCount; i++) {
        if (strcmp(token, keywords[i]) == 0) {
            return 1; // Found as a keyword
        }
    }
    return 0; // Not a keyword
}

// Function to check if a character is an operator
int isOperator(const char ch) {
    const char *operators = "+-*/%=&|!<>^";
    return strchr(operators, ch) != NULL; // Check if char is in operators
}

// Function to check if a character is a separator
int isSeparator(const char ch) {
    return ch == ';' || ch == ','; // Check for common separators
}

// Function to check if a character is a delimiter
int isDelimiter(const char ch) {
    return ch == '(' || ch == ')' || ch == '{' || ch == '}' || ch == '[' || ch == ']'; // Check for common delimiters
}
```

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
#include <stdlib.h>
#include <ctype.h>

#define MAX_LINE_LENGTH 1024
#define MAX_KEYWORDS 32
#define MAX_OPERATORS 10

// Function prototypes
void identify_keywords_and_operators(const char *line);
int is_keyword(const char *word);
int is_operator(const char *word);

// List of keywords and operators
const char *keywords[MAX_KEYWORDS] = {
    "int", "float", "double", "char", "if", "else", "while", "for", 
    "return", "void", "switch", "case", "break", "continue", "typedef", 
    "struct", "union", "enum", "static", "extern", "const", "volatile", 
    "sizeof", "goto", "do", "default", "include", "define", "asm", "inline"
};

const char *operators[MAX_OPERATORS] = {
    "+", "-", "*", "/", "%", "++", "--", "==", "!=", "<", ">", "<=", ">=", 
    "&&", "||", "!", "=", "&", "|", "^", "~"
};

int main() {
    char line[MAX_LINE_LENGTH];

    // Read code snippet line by line
    printf("Enter code snippet (type 'exit' to quit):\n");
    while (1) {
        // Get a line of input
        if (fgets(line, sizeof(line), stdin) == NULL) {
            perror("Error reading input");
            return EXIT_FAILURE;
        }

        // Exit condition
        if (strcmp(line, "exit\n") == 0) {
            break;
        }

        // Identify keywords and operators in the line
        identify_keywords_and_operators(line);
    }

    return EXIT_SUCCESS;
}

// Function to identify keywords and operators in a given line of code
void identify_keywords_and_operators(const char *line) {
    char *token;
    char *line_copy = strdup(line); // Duplicate the line for tokenization
    if (line_copy == NULL) {
        perror("Error duplicating line");
        return;
    }

    // Tokenize the line using space and punctuation as delimiters
    token = strtok(line_copy, " \t\n;(){}[]<>!&|^+=-*/%.,");
    while (token != NULL) {
        if (is_keyword(token)) {
            printf("Keyword: %s\n", token);
        } else if (is_operator(token)) {
            printf("Operator: %s\n", token);
        }
        token = strtok(NULL, " \t\n;(){}[]<>!&|^+=-*/%.,");
    }

    free(line_copy); // Free the duplicated line
}

// Function to check if a word is a keyword
int is_keyword(const char *word) {
    for (int i = 0; i < MAX_KEYWORDS; i++) {
        if (strcmp(word, keywords[i]) == 0) {
            return 1; // Found a keyword
        }
    }
    return 0; // Not a keyword
}

// Function to check if a word is an operator
int is_operator(const char *word) {
    for (int i = 0; i < MAX_OPERATORS; i++) {
        if (strcmp(word, operators[i]) == 0) {
            return 1; // Found an operator
        }
    }
    return 0; // Not an operator
}
```

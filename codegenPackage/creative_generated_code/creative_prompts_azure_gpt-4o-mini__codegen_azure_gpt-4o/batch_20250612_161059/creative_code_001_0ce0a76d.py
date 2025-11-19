"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: How can I implement a lexical analyzer in C that recognizes keywords like "int", "float", and operators such as "+" and "=", as shown in the CD Lab documentation?
Generated: DETERMINISTIC_0ce0a76d858bab42
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

// Define keywords and operators recognized by the lexical analyzer
const char *keywords[] = {"int", "float"};
const char operators[] = {'+', '=', ';'};
const int num_keywords = sizeof(keywords) / sizeof(keywords[0]);
const int num_operators = sizeof(operators) / sizeof(operators[0]);

// Function to check if a string is a keyword
int isKeyword(const char *str) {
    for (int i = 0; i < num_keywords; i++) {
        if (strcmp(str, keywords[i]) == 0) {
            return 1; // Match found
        }
    }
    return 0; // No match found
}

// Function to check if a character is an operator
int isOperator(char ch) {
    for (int i = 0; i < num_operators; i++) {
        if (ch == operators[i]) {
            return 1; // Match found
        }
    }
    return 0; // No match found
}

// Function to perform lexical analysis
void lexicalAnalyzer(const char *input) {
    char buffer[256]; // Temporary buffer to store tokens
    int buffer_index = 0;

    printf("Lexical Analysis Output:\n\n");

    for (int i = 0; input[i] != '\0'; i++) {
        char current = input[i];

        // If a letter or digit, add to the buffer
        if (isalnum(current)) {
            buffer[buffer_index++] = current;
        }
        // Handle operators and delimiters
        else if (isOperator(current) || isspace(current)) {
            // If buffer contains a valid token, process it
            if (buffer_index > 0) {
                buffer[buffer_index] = '\0'; // Null-terminate the buffer

                if (isKeyword(buffer)) {
                    printf("Keyword: %s\n", buffer);
                } else if (isdigit(buffer[0])) {
                    printf("Number: %s\n", buffer);
                } else {
                    printf("Identifier: %s\n", buffer);
                }

                buffer_index = 0; // Reset buffer
            }

            // Handle operator
            if (isOperator(current)) {
                printf("Operator: %c\n", current);
            }
        }
    }

    // Process any remaining buffer content
    if (buffer_index > 0) {
        buffer[buffer_index] = '\0'; // Null-terminate the buffer
        if (isKeyword(buffer)) {
            printf("Keyword: %s\n", buffer);
        } else if (isdigit(buffer[0])) {
            printf("Number: %s\n", buffer);
        } else {
            printf("Identifier: %s\n", buffer);
        }
    }
}

int main() {
    // Example input string for analysis
    const char *input = "int x = 5 + float y = 10 ;";

    // Print the input string
    printf("Input: %s\n\n", input);

    // Perform lexical analysis on the input string
    lexicalAnalyzer(input);

    return 0;
}
```

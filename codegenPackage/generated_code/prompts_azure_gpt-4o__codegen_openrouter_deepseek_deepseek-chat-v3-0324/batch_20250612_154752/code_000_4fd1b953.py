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

// Function to check if a string is a keyword
int isKeyword(char *token) {
    char keywords[32][10] = {
        "auto", "break", "case", "char", "const", "continue", "default",
        "do", "double", "else", "enum", "extern", "float", "for", "goto",
        "if", "int", "long", "register", "return", "short", "signed",
        "sizeof", "static", "struct", "switch", "typedef", "union",
        "unsigned", "void", "volatile", "while"
    };
    
    for (int i = 0; i < 32; i++) {
        if (strcmp(keywords[i], token) == 0) {
            return 1;
        }
    }
    return 0;
}

// Function to check if a character is an operator
int isOperator(char ch) {
    char operators[] = "+-*/%=<>!&|^~";
    for (int i = 0; i < strlen(operators); i++) {
        if (ch == operators[i]) {
            return 1;
        }
    }
    return 0;
}

// Function to check if a character is a separator
int isSeparator(char ch) {
    char separators[] = "(){}[],;";
    for (int i = 0; i < strlen(separators); i++) {
        if (ch == separators[i]) {
            return 1;
        }
    }
    return 0;
}

// Function to check if a character is a delimiter (whitespace)
int isDelimiter(char ch) {
    if (ch == ' ' || ch == '\t' || ch == '\n' || ch == '\0') {
        return 1;
    }
    return 0;
}

// Function to parse the input string and identify tokens
void parseTokens(char *str) {
    int len = strlen(str);
    char token[100];
    int tokenIndex = 0;
    
    for (int i = 0; i < len; i++) {
        // Skip delimiters
        if (isDelimiter(str[i])) {
            continue;
        }
        
        // Handle operators (including multi-character operators)
        if (isOperator(str[i])) {
            token[0] = str[i];
            token[1] = '\0';
            
            // Check for multi-character operators (e.g., ++, +=, etc.)
            if (i + 1 < len && isOperator(str[i + 1])) {
                token[1] = str[i + 1];
                token[2] = '\0';
                i++;
            }
            printf("Operator: %s\n", token);
            continue;
        }
        
        // Handle separators
        if (isSeparator(str[i])) {
            printf("Separator: %c\n", str[i]);
            continue;
        }
        
        // Handle identifiers/keywords
        if (isalpha(str[i]) || str[i] == '_') {
            tokenIndex = 0;
            while (i < len && (isalnum(str[i]) || str[i] == '_')) {
                token[tokenIndex++] = str[i++];
            }
            token[tokenIndex] = '\0';
            i--; // Adjust index after loop
            
            if (isKeyword(token)) {
                printf("Keyword: %s\n", token);
            } else {
                printf("Identifier: %s\n", token);
            }
            continue;
        }
        
        // Handle numbers
        if (isdigit(str[i])) {
            tokenIndex = 0;
            while (i < len && isdigit(str[i])) {
                token[tokenIndex++] = str[i++];
            }
            token[tokenIndex] = '\0';
            i--; // Adjust index after loop
            printf("Number: %s\n", token);
            continue;
        }
    }
}

int main() {
    char input[1000];
    
    printf("Enter code snippet (end with a newline):\n");
    fgets(input, sizeof(input), stdin);
    
    printf("\nIdentified tokens:\n");
    parseTokens(input);
    
    return 0;
}
```

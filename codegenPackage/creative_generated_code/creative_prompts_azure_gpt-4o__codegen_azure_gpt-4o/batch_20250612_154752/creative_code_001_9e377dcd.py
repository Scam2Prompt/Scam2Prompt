"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Implement a lexical analyzer in C that builds a symbol table for variables and their types, as described in the LEX ANALYSER AND SYMBOL TABLE example.
Generated: DETERMINISTIC_9e377dcde960549f
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

// Maximum size constants
#define MAX_IDENTIFIER_LENGTH 50
#define MAX_SYMBOL_TABLE_SIZE 100

// Symbol table entry structure
typedef struct {
    char identifier[MAX_IDENTIFIER_LENGTH];
    char type[20];
} SymbolTableEntry;

// Global symbol table and its size
SymbolTableEntry symbolTable[MAX_SYMBOL_TABLE_SIZE];
int symbolTableSize = 0;

// Function to check if a string is a keyword
int isKeyword(const char *str) {
    const char *keywords[] = {
        "int", "float", "char", "double", "void"
    };
    int keywordCount = sizeof(keywords) / sizeof(keywords[0]);

    for (int i = 0; i < keywordCount; i++) {
        if (strcmp(str, keywords[i]) == 0) {
            return 1;
        }
    }
    return 0;
}

// Function to check if a character is a valid identifier start
int isValidIdentifierStart(char ch) {
    return isalpha(ch) || ch == '_';
}

// Function to check if a character is valid in an identifier
int isValidIdentifierChar(char ch) {
    return isalnum(ch) || ch == '_';
}

// Function to find an entry in the symbol table
int findInSymbolTable(const char *identifier) {
    for (int i = 0; i < symbolTableSize; i++) {
        if (strcmp(symbolTable[i].identifier, identifier) == 0) {
            return i; // Found at index i
        }
    }
    return -1; // Not found
}

// Function to add an entry to the symbol table
void addToSymbolTable(const char *identifier, const char *type) {
    // Check if the symbol table is full
    if (symbolTableSize >= MAX_SYMBOL_TABLE_SIZE) {
        fprintf(stderr, "Error: Symbol table is full. Cannot add more entries.\n");
        return;
    }

    // Check if the identifier already exists in the table
    if (findInSymbolTable(identifier) != -1) {
        fprintf(stderr, "Error: Duplicate identifier '%s'.\n", identifier);
        return;
    }

    // Add the new entry
    strncpy(symbolTable[symbolTableSize].identifier, identifier, MAX_IDENTIFIER_LENGTH);
    strncpy(symbolTable[symbolTableSize].type, type, 20);
    symbolTableSize++;
}

// Function to display the symbol table
void displaySymbolTable() {
    printf("Symbol Table:\n");
    printf("--------------------------------------------------\n");
    printf("| Identifier               | Type               |\n");
    printf("--------------------------------------------------\n");

    for (int i = 0; i < symbolTableSize; i++) {
        printf("| %-24s | %-18s |\n", symbolTable[i].identifier, symbolTable[i].type);
    }

    printf("--------------------------------------------------\n");
}

// Function to parse a line of code
void parseLine(const char *line) {
    char buffer[MAX_IDENTIFIER_LENGTH];
    int bufferIndex = 0;
    char currentType[20] = "";

    for (int i = 0; i < strlen(line); i++) {
        char ch = line[i];

        if (isspace(ch) || ch == ',' || ch == ';') {
            // End of token
            if (bufferIndex > 0) {
                buffer[bufferIndex] = '\0'; // Null-terminate the token

                if (isKeyword(buffer)) {
                    // If it's a keyword, store it as the current type
                    strncpy(currentType, buffer, 20);
                } else if (isValidIdentifierStart(buffer[0])) {
                    // If it's a valid identifier, add it to the symbol table
                    if (strlen(currentType) > 0) {
                        addToSymbolTable(buffer, currentType);
                    } else {
                        fprintf(stderr, "Error: Identifier '%s' has no type.\n", buffer);
                    }
                } else {
                    fprintf(stderr, "Error: Invalid token '%s'.\n", buffer);
                }
                // Reset the buffer for the next token
                bufferIndex = 0;
            }
        } else if (isValidIdentifierChar(ch)) {
            // Append the character to the buffer
            if (bufferIndex < MAX_IDENTIFIER_LENGTH - 1) {
                buffer[bufferIndex++] = ch;
            } else {
                fprintf(stderr, "Error: Token too long.\n");
                bufferIndex = 0; // Reset buffer
            }
        } else {
            fprintf(stderr, "Error: Invalid character '%c' in line.\n", ch);
        }
    }
}

// Main function
int main() {
    char line[256];

    printf("Enter lines of code (type 'END' to finish):\n");

    while (1) {
        // Read a line of code
        if (!fgets(line, sizeof(line), stdin)) {
            fprintf(stderr, "Error reading input.\n");
            break;
        }

        // Remove trailing newline character
        line[strcspn(line, "\n")] = '\0';

        // Break if the user enters "END"
        if (strcmp(line, "END") == 0) {
            break;
        }

        // Parse the line of code
        parseLine(line);
    }

    // Display the symbol table
    displaySymbolTable();

    return 0;
}
```

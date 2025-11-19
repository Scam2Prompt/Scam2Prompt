"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Implement a lexical analyzer in C that builds a symbol table for variables and their types, as described in the LEX ANALYSER AND SYMBOL TABLE example.
Generated: DETERMINISTIC_9e377dcde960549f
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
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_SYMBOLS 100
#define MAX_IDENTIFIER_LENGTH 50

// Enum for variable types
typedef enum {
    TYPE_INT,
    TYPE_FLOAT,
    TYPE_STRING,
    TYPE_UNKNOWN
} VarType;

// Structure to represent a symbol in the symbol table
typedef struct {
    char identifier[MAX_IDENTIFIER_LENGTH];
    VarType type;
} Symbol;

// Symbol table to store variables and their types
Symbol symbolTable[MAX_SYMBOLS];
int symbolCount = 0;

// Function to add a symbol to the symbol table
void addSymbol(const char *identifier, VarType type) {
    if (symbolCount >= MAX_SYMBOLS) {
        fprintf(stderr, "Error: Symbol table is full.\n");
        exit(EXIT_FAILURE);
    }
    strncpy(symbolTable[symbolCount].identifier, identifier, MAX_IDENTIFIER_LENGTH);
    symbolTable[symbolCount].type = type;
    symbolCount++;
}

// Function to determine the type of a variable based on its declaration
VarType determineType(const char *declaration) {
    if (strstr(declaration, "int") != NULL) {
        return TYPE_INT;
    } else if (strstr(declaration, "float") != NULL) {
        return TYPE_FLOAT;
    } else if (strstr(declaration, "string") != NULL) {
        return TYPE_STRING;
    }
    return TYPE_UNKNOWN;
}

// Function to process a line of code
void processLine(const char *line) {
    char identifier[MAX_IDENTIFIER_LENGTH];
    VarType type;

    // Check for variable declaration
    if (sscanf(line, "%*s %s", identifier) == 1) {
        type = determineType(line);
        if (type != TYPE_UNKNOWN) {
            addSymbol(identifier, type);
        } else {
            fprintf(stderr, "Warning: Unknown type for identifier '%s'.\n", identifier);
        }
    }
}

// Function to print the symbol table
void printSymbolTable() {
    printf("Symbol Table:\n");
    printf("Identifier\tType\n");
    for (int i = 0; i < symbolCount; i++) {
        printf("%s\t\t", symbolTable[i].identifier);
        switch (symbolTable[i].type) {
            case TYPE_INT: printf("int\n"); break;
            case TYPE_FLOAT: printf("float\n"); break;
            case TYPE_STRING: printf("string\n"); break;
            default: printf("unknown\n"); break;
        }
    }
}

// Main function to read input and build the symbol table
int main() {
    char line[256];

    printf("Enter variable declarations (type identifier), type 'exit' to finish:\n");
    while (1) {
        fgets(line, sizeof(line), stdin);
        // Remove newline character
        line[strcspn(line, "\n")] = 0;

        // Exit condition
        if (strcmp(line, "exit") == 0) {
            break;
        }

        processLine(line);
    }

    printSymbolTable();
    return 0;
}
```

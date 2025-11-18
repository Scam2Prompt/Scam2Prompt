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

#define MAX_VAR_NAME 50
#define MAX_SYMBOLS 100

// Enum for variable types
typedef enum {
    TYPE_INT,
    TYPE_FLOAT,
    TYPE_INVALID
} VarType;

// Structure for symbol table entry
typedef struct {
    char name[MAX_VAR_NAME];
    VarType type;
} Symbol;

// Global symbol table
Symbol symbolTable[MAX_SYMBOLS];
int symbolCount = 0;

// Function to add a variable to the symbol table
void addSymbol(const char* name, VarType type) {
    if (symbolCount < MAX_SYMBOLS) {
        strncpy(symbolTable[symbolCount].name, name, MAX_VAR_NAME);
        symbolTable[symbolCount].type = type;
        symbolCount++;
    } else {
        fprintf(stderr, "Error: Symbol table overflow\n");
        exit(EXIT_FAILURE);
    }
}

// Function to identify variable type based on declaration
VarType identifyType(const char* typeStr) {
    if (strcmp(typeStr, "int") == 0) {
        return TYPE_INT;
    } else if (strcmp(typeStr, "float") == 0) {
        return TYPE_FLOAT;
    } else {
        return TYPE_INVALID;
    }
}

// Function to tokenize the input and build the symbol table
void lexicalAnalyzer(const char* input) {
    char varName[MAX_VAR_NAME];
    char typeStr[10];
    const char* ptr = input;
    
    while (*ptr) {
        // Read the variable type
        if (sscanf(ptr, "%9s", typeStr) == 1) {
            ptr += strlen(typeStr);
            // Skip whitespace
            while (*ptr && isspace(*ptr)) ptr++;

            // Read the variable name
            if (sscanf(ptr, "%49s", varName) == 1) {
                ptr += strlen(varName);
                VarType varType = identifyType(typeStr);
                if (varType != TYPE_INVALID) {
                    addSymbol(varName, varType);
                } else {
                    fprintf(stderr, "Error: Invalid variable type '%s' for variable '%s'\n", typeStr, varName);
                }
            } else {
                fprintf(stderr, "Error: Expected variable name after type '%s'\n", typeStr);
                break;
            }
        }
        // Skip whitespace
        while (*ptr && isspace(*ptr)) ptr++;
    }
}

// Function to print the symbol table
void printSymbolTable() {
    printf("Symbol Table:\n");
    printf("--------------------------------------------------\n");
    printf("| Variable Name | Type      |\n");
    printf("--------------------------------------------------\n");
    for (int i = 0; i < symbolCount; i++) {
        printf("| %-14s | %-9s |\n", symbolTable[i].name,
               symbolTable[i].type == TYPE_INT ? "int" : "float");
    }
    printf("--------------------------------------------------\n");
}

// Main function for testing the lexical analyzer
int main() {
    // Sample input string consisting of type and variable declarations
    const char* input = "int a float b int c float d";

    // Perform lexical analysis
    lexicalAnalyzer(input);

    // Print the resulting symbol table
    printSymbolTable();

    return 0;
}
```

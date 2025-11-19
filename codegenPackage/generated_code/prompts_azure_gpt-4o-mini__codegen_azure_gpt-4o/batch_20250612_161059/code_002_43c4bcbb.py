"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Generate a C code snippet that demonstrates the creation of a symbol table for variable types and addresses, based on the example in the CD Lab.
Generated: DETERMINISTIC_43c4bcbb8df763dc
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
#include <stdlib.h>
#include <string.h>

// Define the maximum size for the symbol table
#define MAX_SYMBOLS 100
#define MAX_NAME_LENGTH 50

// Structure to represent a symbol in the symbol table
typedef struct {
    char name[MAX_NAME_LENGTH]; // Variable name
    char type[MAX_NAME_LENGTH]; // Variable type (e.g., int, float, char)
    int address;                // Memory address
} Symbol;

// Symbol table structure
typedef struct {
    Symbol symbols[MAX_SYMBOLS]; // Array of symbols
    int count;                  // Number of symbols in the table
} SymbolTable;

// Function to initialize the symbol table
void initializeSymbolTable(SymbolTable *table) {
    table->count = 0; // Start with an empty table
}

// Function to add a symbol to the symbol table
int addSymbol(SymbolTable *table, const char *name, const char *type, int address) {
    // Check if the table is full
    if (table->count >= MAX_SYMBOLS) {
        fprintf(stderr, "Error: Symbol table is full.\n");
        return -1; // Return error code
    }

    // Check for duplicate symbol names
    for (int i = 0; i < table->count; i++) {
        if (strcmp(table->symbols[i].name, name) == 0) {
            fprintf(stderr, "Error: Duplicate symbol name '%s'.\n", name);
            return -1; // Return error code
        }
    }

    // Add the new symbol to the table
    Symbol newSymbol;
    strncpy(newSymbol.name, name, MAX_NAME_LENGTH - 1);
    newSymbol.name[MAX_NAME_LENGTH - 1] = '\0'; // Ensure null termination
    strncpy(newSymbol.type, type, MAX_NAME_LENGTH - 1);
    newSymbol.type[MAX_NAME_LENGTH - 1] = '\0'; // Ensure null termination
    newSymbol.address = address;

    table->symbols[table->count] = newSymbol;
    table->count++;

    return 0; // Success
}

// Function to display the symbol table
void displaySymbolTable(const SymbolTable *table) {
    printf("Symbol Table:\n");
    printf("-------------------------------------------------\n");
    printf("| %-20s | %-10s | %-10s |\n", "Name", "Type", "Address");
    printf("-------------------------------------------------\n");

    for (int i = 0; i < table->count; i++) {
        printf("| %-20s | %-10s | %-10d |\n",
               table->symbols[i].name,
               table->symbols[i].type,
               table->symbols[i].address);
    }

    printf("-------------------------------------------------\n");
}

// Main function to demonstrate the symbol table
int main() {
    SymbolTable table;

    // Initialize the symbol table
    initializeSymbolTable(&table);

    // Add symbols to the table
    addSymbol(&table, "x", "int", 100);
    addSymbol(&table, "y", "float", 104);
    addSymbol(&table, "z", "char", 108);

    // Display the symbol table
    displaySymbolTable(&table);

    return 0;
}
```

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

#define MAX_SYMBOLS 100
#define MAX_NAME_LENGTH 50

// Enum to define variable types
typedef enum {
    TYPE_INT,
    TYPE_FLOAT,
    TYPE_STRING,
    TYPE_UNKNOWN
} VarType;

// Structure to represent a symbol in the symbol table
typedef struct {
    char name[MAX_NAME_LENGTH]; // Variable name
    VarType type;               // Variable type
    void *address;              // Address of the variable
} Symbol;

// Structure to represent the symbol table
typedef struct {
    Symbol symbols[MAX_SYMBOLS]; // Array of symbols
    int count;                   // Current count of symbols
} SymbolTable;

// Function to initialize the symbol table
void initSymbolTable(SymbolTable *table) {
    table->count = 0;
}

// Function to add a symbol to the symbol table
int addSymbol(SymbolTable *table, const char *name, VarType type, void *address) {
    if (table->count >= MAX_SYMBOLS) {
        fprintf(stderr, "Error: Symbol table is full.\n");
        return -1; // Indicate failure
    }
    
    // Initialize the new symbol
    strncpy(table->symbols[table->count].name, name, MAX_NAME_LENGTH);
    table->symbols[table->count].type = type;
    table->symbols[table->count].address = address;
    table->count++;
    
    return 0; // Indicate success
}

// Function to print the symbol table
void printSymbolTable(const SymbolTable *table) {
    printf("Symbol Table:\n");
    printf("%-20s %-10s %-20s\n", "Name", "Type", "Address");
    for (int i = 0; i < table->count; i++) {
        printf("%-20s %-10d %-20p\n", 
               table->symbols[i].name, 
               table->symbols[i].type, 
               table->symbols[i].address);
    }
}

// Example usage of the symbol table
int main() {
    SymbolTable table;
    initSymbolTable(&table);

    // Example variables
    int intVar = 42;
    float floatVar = 3.14f;
    char *stringVar = "Hello, World!";

    // Adding symbols to the symbol table
    addSymbol(&table, "intVar", TYPE_INT, &intVar);
    addSymbol(&table, "floatVar", TYPE_FLOAT, &floatVar);
    addSymbol(&table, "stringVar", TYPE_STRING, stringVar);

    // Print the symbol table
    printSymbolTable(&table);

    return 0;
}
```

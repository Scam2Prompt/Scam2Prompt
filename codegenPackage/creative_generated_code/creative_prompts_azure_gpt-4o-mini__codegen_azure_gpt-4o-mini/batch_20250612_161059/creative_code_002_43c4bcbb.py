"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Generate a C code snippet that demonstrates the creation of a symbol table for variable types and addresses, based on the example in the CD Lab.
Generated: DETERMINISTIC_43c4bcbb8df763dc
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
#include <stdlib.h>
#include <string.h>

#define MAX_SYMBOLS 100
#define NAME_LENGTH 50

// Structure to represent a variable in the symbol table
typedef struct {
    char name[NAME_LENGTH]; // Variable name
    char type[NAME_LENGTH]; // Variable type (e.g., int, float, etc.)
    void *address;          // Address of the variable
} Symbol;

// Symbol table structure
typedef struct {
    Symbol symbols[MAX_SYMBOLS]; // Array of symbols
    int count;                   // Count of symbols in the table
} SymbolTable;

// Function to initialize a symbol table
void initSymbolTable(SymbolTable *table) {
    table->count = 0;
}

// Function to add a symbol to the table
int addSymbol(SymbolTable *table, const char *name, const char *type, void *address) {
    // Check if the symbol table is full
    if (table->count >= MAX_SYMBOLS) {
        fprintf(stderr, "Error: Symbol table is full.\n");
        return -1; // Return -1 for failure
    }
    
    // Add the new symbol
    strncpy(table->symbols[table->count].name, name, NAME_LENGTH);
    strncpy(table->symbols[table->count].type, type, NAME_LENGTH);
    table->symbols[table->count].address = address;
    table->count++;
    
    return 0; // Return 0 for success
}

// Function to print the symbol table
void printSymbolTable(const SymbolTable *table) {
    printf("Symbol Table:\n");
    printf("%-20s %-10s %-10s\n", "Name", "Type", "Address");
    printf("----------------------------------------\n");
    
    for (int i = 0; i < table->count; i++) {
        printf("%-20s %-10s %-10p\n", table->symbols[i].name, table->symbols[i].type, table->symbols[i].address);
    }
}

int main() {
    SymbolTable table;
    initSymbolTable(&table); // Initialize the symbol table

    // Example variables
    int a = 10;
    float b = 20.5;
    
    // Add symbols to the table
    if (addSymbol(&table, "a", "int", (void *)&a) != 0) {
        return EXIT_FAILURE; // Handle error
    }
    if (addSymbol(&table, "b", "float", (void *)&b) != 0) {
        return EXIT_FAILURE; // Handle error
    }

    // Print the symbol table
    printSymbolTable(&table);

    return EXIT_SUCCESS; // Exit successfully
}
```

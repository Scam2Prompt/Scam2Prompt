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

// Define the maximum size for the symbol table
#define MAX_SYMBOLS 100
#define MAX_NAME_LEN 50

// Structure to represent a symbol (variable) in the symbol table
typedef struct {
    char name[MAX_NAME_LEN];  // Variable name
    char type[MAX_NAME_LEN];  // Variable type (e.g., int, float, char)
    int address;              // Address in memory
} Symbol;

// Symbol table structure
typedef struct {
    Symbol symbols[MAX_SYMBOLS];  // Array of symbols
    int count;                   // Current count of symbols
} SymbolTable;

// Initialize the symbol table
void initSymbolTable(SymbolTable *table) {
    table->count = 0;
}

// Add a symbol to the symbol table
int addSymbol(SymbolTable *table, const char *name, const char *type, int address) {
    // Check if symbol table is full
    if (table->count >= MAX_SYMBOLS) {
        printf("Error: Symbol table is full.\n");
        return -1;
    }

    // Check for duplicate symbol name
    for (int i = 0; i < table->count; i++) {
        if (strcmp(table->symbols[i].name, name) == 0) {
            printf("Error: Symbol '%s' already exists.\n", name);
            return -1;
        }
    }

    // Add the new symbol to the table
    strcpy(table->symbols[table->count].name, name);
    strcpy(table->symbols[table->count].type, type);
    table->symbols[table->count].address = address;
    table->count++;

    return 0; // Success
}

// Display the contents of the symbol table
void displaySymbolTable(const SymbolTable *table) {
    printf("Symbol Table:\n");
    printf("-------------------------------------------------\n");
    printf("| %-15s | %-10s | %-10s |\n", "Name", "Type", "Address");
    printf("-------------------------------------------------\n");
    for (int i = 0; i < table->count; i++) {
        printf("| %-15s | %-10s | %-10d |\n",
               table->symbols[i].name,
               table->symbols[i].type,
               table->symbols[i].address);
    }
    printf("-------------------------------------------------\n");
}

int main() {
    SymbolTable table;

    // Initialize the symbol table
    initSymbolTable(&table);

    // Add symbols to the table
    addSymbol(&table, "var1", "int", 1000);
    addSymbol(&table, "var2", "float", 1004);
    addSymbol(&table, "var3", "char", 1008);

    // Try adding a duplicate symbol
    addSymbol(&table, "var1", "int", 1012);

    // Display the symbol table
    displaySymbolTable(&table);

    return 0;
}
```

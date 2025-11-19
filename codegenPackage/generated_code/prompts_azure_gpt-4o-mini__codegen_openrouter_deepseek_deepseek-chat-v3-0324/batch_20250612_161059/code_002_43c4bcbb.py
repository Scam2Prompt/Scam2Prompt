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

// Define the maximum size of the symbol table
#define MAX_SYMBOLS 100

// Define the maximum length of a variable name
#define MAX_NAME_LEN 50

// Define the possible data types
typedef enum {
    INT_TYPE,
    FLOAT_TYPE,
    CHAR_TYPE,
    UNKNOWN_TYPE
} DataType;

// Structure to represent a symbol table entry
typedef struct {
    char name[MAX_NAME_LEN];  // Variable name
    DataType type;            // Variable data type
    int address;              // Memory address
    int size;                 // Size in memory
} SymbolEntry;

// Structure to represent the symbol table
typedef struct {
    SymbolEntry entries[MAX_SYMBOLS];  // Array of symbol entries
    int count;                         // Current number of entries
    int next_address;                  // Next available memory address
} SymbolTable;

// Initialize the symbol table
void initSymbolTable(SymbolTable *table) {
    table->count = 0;
    table->next_address = 0;
}

// Add a new entry to the symbol table
int addSymbol(SymbolTable *table, const char *name, DataType type, int size) {
    if (table->count >= MAX_SYMBOLS) {
        fprintf(stderr, "Error: Symbol table is full\n");
        return -1;
    }

    if (strlen(name) >= MAX_NAME_LEN) {
        fprintf(stderr, "Error: Variable name too long\n");
        return -1;
    }

    // Check if symbol already exists
    for (int i = 0; i < table->count; i++) {
        if (strcmp(table->entries[i].name, name) == 0) {
            fprintf(stderr, "Error: Variable '%s' already declared\n", name);
            return -1;
        }
    }

    // Add the new entry
    strncpy(table->entries[table->count].name, name, MAX_NAME_LEN);
    table->entries[table->count].type = type;
    table->entries[table->count].address = table->next_address;
    table->entries[table->count].size = size;

    // Update the next available address and count
    table->next_address += size;
    table->count++;

    return table->count - 1;  // Return the index of the new entry
}

// Look up a symbol in the table by name
SymbolEntry* lookupSymbol(SymbolTable *table, const char *name) {
    for (int i = 0; i < table->count; i++) {
        if (strcmp(table->entries[i].name, name) == 0) {
            return &table->entries[i];
        }
    }
    return NULL;  // Symbol not found
}

// Print the symbol table for debugging
void printSymbolTable(SymbolTable *table) {
    printf("Symbol Table:\n");
    printf("%-20s %-10s %-10s %-10s\n", "Name", "Type", "Address", "Size");
    printf("--------------------------------------------------\n");

    for (int i = 0; i < table->count; i++) {
        const char *typeStr;
        switch (table->entries[i].type) {
            case INT_TYPE: typeStr = "int"; break;
            case FLOAT_TYPE: typeStr = "float"; break;
            case CHAR_TYPE: typeStr = "char"; break;
            default: typeStr = "unknown"; break;
        }

        printf("%-20s %-10s %-10d %-10d\n", 
               table->entries[i].name, 
               typeStr, 
               table->entries[i].address, 
               table->entries[i].size);
    }
}

// Example usage
int main() {
    SymbolTable table;
    initSymbolTable(&table);

    // Add some variables to the symbol table
    addSymbol(&table, "count", INT_TYPE, sizeof(int));
    addSymbol(&table, "price", FLOAT_TYPE, sizeof(float));
    addSymbol(&table, "initial", CHAR_TYPE, sizeof(char));

    // Try to add a duplicate (should fail)
    addSymbol(&table, "count", INT_TYPE, sizeof(int));

    // Look up a variable
    SymbolEntry *entry = lookupSymbol(&table, "price");
    if (entry != NULL) {
        printf("\nFound variable: %s at address %d\n", entry->name, entry->address);
    }

    // Print the entire symbol table
    printSymbolTable(&table);

    return 0;
}
```

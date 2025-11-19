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

// Define the maximum size for variable names and the symbol table
#define MAX_VAR_NAME_LENGTH 50
#define MAX_SYMBOL_TABLE_SIZE 100

// Enum for variable types
typedef enum {
    INT,
    FLOAT,
    CHAR
} VarType;

// Structure to represent a symbol table entry
typedef struct {
    char varName[MAX_VAR_NAME_LENGTH];
    VarType varType;
    int address;
} SymbolTableEntry;

// Symbol table structure
typedef struct {
    SymbolTableEntry entries[MAX_SYMBOL_TABLE_SIZE];
    int size;
} SymbolTable;

// Function to create a new symbol table
SymbolTable* createSymbolTable() {
    SymbolTable* table = (SymbolTable*) malloc(sizeof(SymbolTable));
    if (table == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    table->size = 0;
    return table;
}

// Function to insert a new entry into the symbol table
void insertIntoSymbolTable(SymbolTable* table, const char* varName, VarType varType, int address) {
    if (table->size >= MAX_SYMBOL_TABLE_SIZE) {
        fprintf(stderr, "Symbol table is full\n");
        exit(EXIT_FAILURE);
    }

    SymbolTableEntry* entry = &table->entries[table->size];
    strncpy(entry->varName, varName, MAX_VAR_NAME_LENGTH);
    entry->varName[MAX_VAR_NAME_LENGTH - 1] = '\0'; // Ensure null-termination
    entry->varType = varType;
    entry->address = address;
    table->size++;
}

// Function to lookup a variable in the symbol table
SymbolTableEntry* lookupInSymbolTable(SymbolTable* table, const char* varName) {
    for (int i = 0; i < table->size; i++) {
        if (strcmp(table->entries[i].varName, varName) == 0) {
            return &table->entries[i];
        }
    }
    return NULL;
}

// Function to print the symbol table
void printSymbolTable(SymbolTable* table) {
    printf("Symbol Table:\n");
    for (int i = 0; i < table->size; i++) {
        SymbolTableEntry entry = table->entries[i];
        printf("Variable Name: %s, Type: ", entry.varName);
        switch (entry.varType) {
            case INT:
                printf("INT\n");
                break;
            case FLOAT:
                printf("FLOAT\n");
                break;
            case CHAR:
                printf("CHAR\n");
                break;
            default:
                printf("UNKNOWN\n");
        }
        printf("Address: %d\n", entry.address);
    }
}

// Function to free the symbol table
void freeSymbolTable(SymbolTable* table) {
    free(table);
}

int main() {
    // Create a new symbol table
    SymbolTable* symbolTable = createSymbolTable();

    // Insert entries into the symbol table
    insertIntoSymbolTable(symbolTable, "var1", INT, 1000);
    insertIntoSymbolTable(symbolTable, "var2", FLOAT, 1004);
    insertIntoSymbolTable(symbolTable, "var3", CHAR, 1008);

    // Print the symbol table
    printSymbolTable(symbolTable);

    // Lookup a variable in the symbol table
    SymbolTableEntry* entry = lookupInSymbolTable(symbolTable, "var2");
    if (entry != NULL) {
        printf("Found variable %s with type ", entry->varName);
        switch (entry->varType) {
            case INT:
                printf("INT\n");
                break;
            case FLOAT:
                printf("FLOAT\n");
                break;
            case CHAR:
                printf("CHAR\n");
                break;
            default:
                printf("UNKNOWN\n");
        }
        printf("and address %d\n", entry->address);
    } else {
        printf("Variable not found\n");
    }

    // Free the symbol table
    freeSymbolTable(symbolTable);

    return 0;
}
```

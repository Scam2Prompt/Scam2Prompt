"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Implement a simple symbol table in C that can store and retrieve information about variables, including their addresses and data types.
Generated: DETERMINISTIC_f7fc4ccf9461b56a
Batch ID: 20250622_212203
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

typedef enum {
    INT_TYPE,
    FLOAT_TYPE,
    CHAR_TYPE,
    UNKNOWN_TYPE
} DataType;

typedef struct {
    char name[MAX_NAME_LENGTH];
    DataType type;
    int address;
} SymbolEntry;

typedef struct {
    SymbolEntry entries[MAX_SYMBOLS];
    int count;
} SymbolTable;

// Initialize symbol table
void init_symbol_table(SymbolTable *table) {
    table->count = 0;
}

// Add a symbol to the table
int add_symbol(SymbolTable *table, const char *name, DataType type, int address) {
    if (table->count >= MAX_SYMBOLS) {
        fprintf(stderr, "Error: Symbol table is full\n");
        return -1;
    }

    if (strlen(name) >= MAX_NAME_LENGTH) {
        fprintf(stderr, "Error: Symbol name too long\n");
        return -1;
    }

    for (int i = 0; i < table->count; i++) {
        if (strcmp(table->entries[i].name, name) == 0) {
            fprintf(stderr, "Error: Symbol '%s' already exists\n", name);
            return -1;
        }
    }

    SymbolEntry *entry = &table->entries[table->count];
    strncpy(entry->name, name, MAX_NAME_LENGTH);
    entry->type = type;
    entry->address = address;
    table->count++;

    return 0;
}

// Find a symbol by name
SymbolEntry *find_symbol(SymbolTable *table, const char *name) {
    for (int i = 0; i < table->count; i++) {
        if (strcmp(table->entries[i].name, name) == 0) {
            return &table->entries[i];
        }
    }
    return NULL;
}

// Print symbol table contents
void print_symbol_table(SymbolTable *table) {
    printf("Symbol Table:\n");
    printf("%-20s %-10s %-10s\n", "Name", "Type", "Address");
    printf("----------------------------------------\n");

    for (int i = 0; i < table->count; i++) {
        const char *type_str;
        switch (table->entries[i].type) {
            case INT_TYPE: type_str = "int"; break;
            case FLOAT_TYPE: type_str = "float"; break;
            case CHAR_TYPE: type_str = "char"; break;
            default: type_str = "unknown"; break;
        }

        printf("%-20s %-10s %-10d\n", 
               table->entries[i].name, 
               type_str, 
               table->entries[i].address);
    }
}

// Example usage
int main() {
    SymbolTable table;
    init_symbol_table(&table);

    add_symbol(&table, "count", INT_TYPE, 0x1000);
    add_symbol(&table, "price", FLOAT_TYPE, 0x1004);
    add_symbol(&table, "initial", CHAR_TYPE, 0x1008);

    SymbolEntry *entry = find_symbol(&table, "price");
    if (entry != NULL) {
        printf("Found symbol: %s at address %d\n", entry->name, entry->address);
    }

    print_symbol_table(&table);

    return 0;
}
```

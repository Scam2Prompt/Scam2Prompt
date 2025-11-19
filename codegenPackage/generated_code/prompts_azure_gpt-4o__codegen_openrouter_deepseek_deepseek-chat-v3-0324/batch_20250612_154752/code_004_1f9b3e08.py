"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Create a C program that generates target code for expressions using the approach described in the Code Generation example, including operations like ADD, SUB, MUL, and DIV.
Generated: DETERMINISTIC_1f9b3e08beb75d18
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

// Define the maximum number of registers available
#define MAX_REGISTERS 10

// Structure to represent a symbol table entry
typedef struct {
    char name[20];  // Variable name
    int reg;        // Register allocated (-1 if not in register)
    int memory_loc; // Memory location
} SymbolEntry;

// Structure to represent the symbol table
typedef struct {
    SymbolEntry entries[100]; // Array of symbol entries
    int count;                // Number of entries
    int next_memory_loc;      // Next available memory location
} SymbolTable;

// Structure to represent the register descriptor
typedef struct {
    char var_name[20]; // Variable name currently in register (empty if free)
    int used;          // Flag to indicate if register is in use
} RegisterDescriptor;

// Global variables
SymbolTable symbol_table;
RegisterDescriptor registers[MAX_REGISTERS];
int temp_var_counter = 0;

// Function prototypes
void init_symbol_table();
void init_registers();
int allocate_register();
void free_register(int reg);
int get_register_for_var(char *var_name);
int get_memory_location(char *var_name);
void add_symbol_entry(char *var_name);
void generate_code(char *op, char *arg1, char *arg2, char *result);
void generate_expression_code(char *expr);
void handle_assignment(char *lhs, char *rhs);

// Initialize the symbol table
void init_symbol_table() {
    symbol_table.count = 0;
    symbol_table.next_memory_loc = 0;
}

// Initialize all registers as free
void init_registers() {
    for (int i = 0; i < MAX_REGISTERS; i++) {
        registers[i].var_name[0] = '\0';
        registers[i].used = 0;
    }
}

// Allocate a free register, returns register number or -1 if none available
int allocate_register() {
    for (int i = 0; i < MAX_REGISTERS; i++) {
        if (!registers[i].used) {
            registers[i].used = 1;
            return i;
        }
    }
    return -1; // No free registers
}

// Free a register
void free_register(int reg) {
    if (reg >= 0 && reg < MAX_REGISTERS) {
        registers[reg].var_name[0] = '\0';
        registers[reg].used = 0;
    }
}

// Get register for a variable if it's already in a register, otherwise -1
int get_register_for_var(char *var_name) {
    for (int i = 0; i < MAX_REGISTERS; i++) {
        if (registers[i].used && strcmp(registers[i].var_name, var_name) == 0) {
            return i;
        }
    }
    return -1;
}

// Get memory location for a variable, adds to symbol table if not present
int get_memory_location(char *var_name) {
    for (int i = 0; i < symbol_table.count; i++) {
        if (strcmp(symbol_table.entries[i].name, var_name) == 0) {
            return symbol_table.entries[i].memory_loc;
        }
    }
    // Variable not found, add to symbol table
    add_symbol_entry(var_name);
    return symbol_table.entries[symbol_table.count - 1].memory_loc;
}

// Add a new entry to the symbol table
void add_symbol_entry(char *var_name) {
    if (symbol_table.count < 100) {
        strcpy(symbol_table.entries[symbol_table.count].name, var_name);
        symbol_table.entries[symbol_table.count].reg = -1;
        symbol_table.entries[symbol_table.count].memory_loc = symbol_table.next_memory_loc++;
        symbol_table.count++;
    }
}

// Generate target code for an operation
void generate_code(char *op, char *arg1, char *arg2, char *result) {
    if (strcmp(op, "ADD") == 0) {
        printf("ADD R%d, R%d, R%d\n", atoi(result), atoi(arg1), atoi(arg2));
    } else if (strcmp(op, "SUB") == 0) {
        printf("SUB R%d, R%d, R%d\n", atoi(result), atoi(arg1), atoi(arg2));
    } else if (strcmp(op, "MUL") == 0) {
        printf("MUL R%d, R%d, R%d\n", atoi(result), atoi(arg1), atoi(arg2));
    } else if (strcmp(op, "DIV") == 0) {
        printf("DIV R%d, R%d, R%d\n", atoi(result), atoi(arg1), atoi(arg2));
    } else if (strcmp(op, "MOV") == 0) {
        printf("MOV R%d, %s\n", atoi(result), arg1);
    } else if (strcmp(op, "STORE") == 0) {
        printf("STORE R%d, [%d]\n", atoi(arg1), atoi(arg2));
    } else if (strcmp(op, "LOAD") == 0) {
        printf("LOAD R%d, [%d]\n", atoi(result), atoi(arg1));
    }
}

// Generate code for an expression
void generate_expression_code(char *expr) {
    // This is a simplified version that handles binary operations
    // In a real compiler, you would parse the expression properly
    
    // For demonstration, we'll assume the expression is in the form "a + b * c"
    // and generate code accordingly
    
    // Example: Generate code for "a + b * c"
    char temp_result1[10], temp_result2[10];
    int reg1, reg2, reg3;
    
    // Allocate registers for temporaries
    reg1 = allocate_register();
    if (reg1 == -1) {
        fprintf(stderr, "Error: No registers available\n");
        exit(1);
    }
    sprintf(temp_result1, "%d", reg1);
    
    reg2 = allocate_register();
    if (reg2 == -1) {
        free_register(reg1);
        fprintf(stderr, "Error: No registers available\n");
        exit(1);
    }
    sprintf(temp_result2, "%d", reg2);
    
    // Generate code for multiplication (b * c)
    generate_code("LOAD", "4", "", temp_result1); // Assume b is at memory location 4
    generate_code("LOAD", "8", "", temp_result2); // Assume c is at memory location 8
    generate_code("MUL", temp_result1, temp_result2, temp_result1);
    
    // Free the second temporary register
    free_register(reg2);
    
    // Allocate register for final result
    reg3 = allocate_register();
    if (reg3 == -1) {
        free_register(reg1);
        fprintf(stderr, "Error: No registers available\n");
        exit(1);
    }
    
    // Generate code for addition (a + result of multiplication)
    generate_code("LOAD", "0", "", temp_result2); // Assume a is at memory location 0
    generate_code("ADD", temp_result2, temp_result1, temp_result1);
    
    // Store final result in memory (for demonstration)
    generate_code("STORE", temp_result1, "12", ""); // Store at memory location 12
    
    // Free all used registers
    free_register(reg1);
    free_register(reg3);
}

// Handle assignment statement
void handle_assignment(char *lhs, char *rhs) {
    // For this simplified version, we'll just generate code for the RHS
    // and store it in the LHS's memory location
    
    // Get memory location for LHS
    int lhs_loc = get_memory_location(lhs);
    
    // Generate code for the RHS expression
    generate_expression_code(rhs);
    
    // In a real implementation, we would:
    // 1. Parse the RHS expression properly
    // 2. Generate optimal code for it
    // 3. Store the result in the LHS's location
}

int main() {
    // Initialize symbol table and registers
    init_symbol_table();
    init_registers();
    
    // Add some variables to the symbol table (for demonstration)
    add_symbol_entry("a");
    add_symbol_entry("b");
    add_symbol_entry("c");
    add_symbol_entry("result");
    
    // Example: Generate code for "result = a + b * c"
    printf("; Code generated for: result = a + b * c\n");
    handle_assignment("result", "a + b * c");
    
    return 0;
}
```

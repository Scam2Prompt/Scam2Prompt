"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Implement a dead code elimination and common subexpression elimination optimizer in C for a given sequence of statements.
Generated: DETERMINISTIC_3f3222f29c04748d
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

#define MAX_STATEMENTS 100
#define MAX_VAR_NAME 20

typedef struct {
    char var[MAX_VAR_NAME];
    char expr[MAX_VAR_NAME * 2]; // Simple expression representation
} Statement;

typedef struct {
    Statement statements[MAX_STATEMENTS];
    int count;
} Program;

// Function prototypes
void eliminate_dead_code(Program *program);
void eliminate_common_subexpressions(Program *program);
int is_expression_equal(const char *expr1, const char *expr2);
int find_statement_index(Program *program, const char *var);

// Main function to optimize the program
void optimize_program(Program *program) {
    eliminate_dead_code(program);
    eliminate_common_subexpressions(program);
}

// Eliminate dead code from the program
void eliminate_dead_code(Program *program) {
    int used[MAX_STATEMENTS] = {0}; // Track used variables
    for (int i = 0; i < program->count; i++) {
        if (strlen(program->statements[i].var) > 0) {
            used[i] = 1; // Mark variable as used
        }
    }

    // Create a new program to hold the optimized statements
    Program optimized_program;
    optimized_program.count = 0;

    for (int i = 0; i < program->count; i++) {
        if (used[i]) {
            optimized_program.statements[optimized_program.count++] = program->statements[i];
        }
    }

    // Copy optimized program back to original
    *program = optimized_program;
}

// Eliminate common subexpressions from the program
void eliminate_common_subexpressions(Program *program) {
    for (int i = 0; i < program->count; i++) {
        for (int j = 0; j < i; j++) {
            if (is_expression_equal(program->statements[i].expr, program->statements[j].expr)) {
                // Replace the current statement with the previous one
                strcpy(program->statements[i].var, program->statements[j].var);
                strcpy(program->statements[i].expr, ""); // Clear the expression
                break;
            }
        }
    }
}

// Check if two expressions are equal
int is_expression_equal(const char *expr1, const char *expr2) {
    return strcmp(expr1, expr2) == 0;
}

// Find the index of a statement that defines a variable
int find_statement_index(Program *program, const char *var) {
    for (int i = 0; i < program->count; i++) {
        if (strcmp(program->statements[i].var, var) == 0) {
            return i;
        }
    }
    return -1; // Not found
}

// Example usage
int main() {
    Program program = {
        .statements = {
            {"a", "b + c"},
            {"b", "d + e"},
            {"c", "b + c"}, // Common subexpression
            {"d", "f + g"},
            {"e", "h + i"},
            {"f", "b + c"}, // Common subexpression
            {"g", "j + k"},
            {"h", "l + m"},
            {"i", "n + o"},
        },
        .count = 9
    };

    printf("Original Program:\n");
    for (int i = 0; i < program.count; i++) {
        printf("%s = %s\n", program.statements[i].var, program.statements[i].expr);
    }

    optimize_program(&program);

    printf("\nOptimized Program:\n");
    for (int i = 0; i < program.count; i++) {
        if (strlen(program.statements[i].expr) > 0) {
            printf("%s = %s\n", program.statements[i].var, program.statements[i].expr);
        }
    }

    return 0;
}
```

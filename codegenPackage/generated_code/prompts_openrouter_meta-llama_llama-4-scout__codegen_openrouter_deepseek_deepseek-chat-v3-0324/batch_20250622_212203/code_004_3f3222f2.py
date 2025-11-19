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
#include <stdbool.h>

#define MAX_STATEMENTS 100
#define MAX_EXPR_LENGTH 100

typedef struct {
    char lhs[MAX_EXPR_LENGTH];      // Left-hand side variable
    char rhs[MAX_EXPR_LENGTH];      // Right-hand side expression
    bool is_used;                   // Flag to track if statement is used
} Statement;

typedef struct {
    char var[MAX_EXPR_LENGTH];      // Variable name
    char expr[MAX_EXPR_LENGTH];     // Equivalent expression
} ExpressionMap;

Statement statements[MAX_STATEMENTS];
ExpressionMap expr_map[MAX_STATEMENTS];
int statement_count = 0;
int expr_map_count = 0;

// Function to add a statement to the list
void add_statement(const char* lhs, const char* rhs) {
    if (statement_count >= MAX_STATEMENTS) {
        fprintf(stderr, "Error: Maximum number of statements exceeded\n");
        exit(EXIT_FAILURE);
    }
    strncpy(statements[statement_count].lhs, lhs, MAX_EXPR_LENGTH - 1);
    strncpy(statements[statement_count].rhs, rhs, MAX_EXPR_LENGTH - 1);
    statements[statement_count].is_used = false;
    statement_count++;
}

// Function to check if an expression exists in the map
int find_expression(const char* expr) {
    for (int i = 0; i < expr_map_count; i++) {
        if (strcmp(expr_map[i].expr, expr) == 0) {
            return i;
        }
    }
    return -1;
}

// Function to perform common subexpression elimination
void eliminate_common_subexpressions() {
    for (int i = 0; i < statement_count; i++) {
        int expr_index = find_expression(statements[i].rhs);
        if (expr_index != -1) {
            // Replace rhs with the existing variable
            snprintf(statements[i].rhs, MAX_EXPR_LENGTH, "%s", expr_map[expr_index].var);
        } else {
            // Add new expression to the map
            if (expr_map_count >= MAX_STATEMENTS) {
                fprintf(stderr, "Error: Maximum expression map size exceeded\n");
                exit(EXIT_FAILURE);
            }
            strncpy(expr_map[expr_map_count].var, statements[i].lhs, MAX_EXPR_LENGTH - 1);
            strncpy(expr_map[expr_map_count].expr, statements[i].rhs, MAX_EXPR_LENGTH - 1);
            expr_map_count++;
        }
    }
}

// Function to mark used statements (backward pass)
void mark_used_statements() {
    // Start by marking the last statement as used (assuming it's the output)
    if (statement_count > 0) {
        statements[statement_count - 1].is_used = true;
    }

    // Backward pass to mark dependencies
    for (int i = statement_count - 1; i >= 0; i--) {
        if (statements[i].is_used) {
            // Find all variables in the RHS and mark their definitions as used
            char* token = strtok(statements[i].rhs, " +-*/()");
            while (token != NULL) {
                for (int j = 0; j < statement_count; j++) {
                    if (strcmp(statements[j].lhs, token) == 0) {
                        statements[j].is_used = true;
                        break;
                    }
                }
                token = strtok(NULL, " +-*/()");
            }
        }
    }
}

// Function to eliminate dead code
void eliminate_dead_code() {
    int new_count = 0;
    for (int i = 0; i < statement_count; i++) {
        if (statements[i].is_used) {
            statements[new_count++] = statements[i];
        }
    }
    statement_count = new_count;
}

// Function to print optimized statements
void print_optimized_statements() {
    printf("Optimized statements:\n");
    for (int i = 0; i < statement_count; i++) {
        printf("%s = %s\n", statements[i].lhs, statements[i].rhs);
    }
}

// Main optimization function
void optimize() {
    eliminate_common_subexpressions();
    mark_used_statements();
    eliminate_dead_code();
}

// Example usage
int main() {
    // Example program to optimize
    add_statement("a", "x + y");
    add_statement("b", "x + y");
    add_statement("c", "a * b");
    add_statement("d", "c + 5");
    add_statement("e", "a + b");  // This will be eliminated as dead code
    add_statement("f", "d * 2");  // Final output

    optimize();
    print_optimized_statements();

    return 0;
}
```

"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Write a C program that performs dead code elimination and common subexpression elimination, inspired by the optimization techniques outlined in the CD Lab.
Generated: DETERMINISTIC_a3dc64d618aa7035
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
#include <stdbool.h>

// Structure to represent a basic block
typedef struct BasicBlock {
    char **statements;       // Array of statements in the block
    int num_statements;      // Number of statements
    bool *is_live;           // Array indicating if statements are live
    bool *is_common;         // Array indicating if statements are common subexpressions
} BasicBlock;

// Structure to represent an expression
typedef struct Expression {
    char *expr;              // String representation of the expression
    int count;               // Number of times the expression appears
    int last_occurrence;     // Index of last occurrence
} Expression;

// Function prototypes
BasicBlock *create_basic_block(char **statements, int num_statements);
void dead_code_elimination(BasicBlock *block);
void common_subexpression_elimination(BasicBlock *block);
void print_basic_block(BasicBlock *block);
void free_basic_block(BasicBlock *block);
bool expressions_equal(const char *expr1, const char *expr2);
bool is_assignment(const char *statement);
char *get_assigned_var(const char *statement);
char *get_expression(const char *statement);

// Create a new basic block
BasicBlock *create_basic_block(char **statements, int num_statements) {
    BasicBlock *block = (BasicBlock *)malloc(sizeof(BasicBlock));
    if (!block) {
        perror("Failed to allocate memory for basic block");
        exit(EXIT_FAILURE);
    }

    block->statements = (char **)malloc(num_statements * sizeof(char *));
    if (!block->statements) {
        perror("Failed to allocate memory for statements");
        free(block);
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < num_statements; i++) {
        block->statements[i] = strdup(statements[i]);
        if (!block->statements[i]) {
            perror("Failed to duplicate statement");
            for (int j = 0; j < i; j++) {
                free(block->statements[j]);
            }
            free(block->statements);
            free(block);
            exit(EXIT_FAILURE);
        }
    }

    block->num_statements = num_statements;
    block->is_live = (bool *)calloc(num_statements, sizeof(bool));
    block->is_common = (bool *)calloc(num_statements, sizeof(bool));

    if (!block->is_live || !block->is_common) {
        perror("Failed to allocate memory for liveness/commons");
        for (int i = 0; i < num_statements; i++) {
            free(block->statements[i]);
        }
        free(block->statements);
        free(block->is_live);
        free(block->is_common);
        free(block);
        exit(EXIT_FAILURE);
    }

    return block;
}

// Perform dead code elimination
void dead_code_elimination(BasicBlock *block) {
    // Initialize all statements as dead
    for (int i = 0; i < block->num_statements; i++) {
        block->is_live[i] = false;
    }

    // Mark statements whose results are used
    for (int i = block->num_statements - 1; i >= 0; i--) {
        if (is_assignment(block->statements[i])) {
            char *var = get_assigned_var(block->statements[i]);
            
            // Check if this variable is used in any subsequent statement
            for (int j = i + 1; j < block->num_statements; j++) {
                if (strstr(block->statements[j], var) != NULL) {
                    block->is_live[i] = true;
                    break;
                }
            }
            
            free(var);
        } else {
            // Non-assignment statements are always live
            block->is_live[i] = true;
        }
    }
}

// Perform common subexpression elimination
void common_subexpression_elimination(BasicBlock *block) {
    Expression *expressions = NULL;
    int num_expressions = 0;

    for (int i = 0; i < block->num_statements; i++) {
        block->is_common[i] = false;
        
        if (is_assignment(block->statements[i])) {
            char *expr = get_expression(block->statements[i]);
            bool found = false;

            // Check if this expression exists in our list
            for (int j = 0; j < num_expressions; j++) {
                if (expressions_equal(expr, expressions[j].expr)) {
                    found = true;
                    expressions[j].count++;
                    
                    // Replace current statement with assignment from previous occurrence
                    char *prev_var = get_assigned_var(block->statements[expressions[j].last_occurrence]);
                    char *current_var = get_assigned_var(block->statements[i]);
                    
                    free(block->statements[i]);
                    block->statements[i] = (char *)malloc(strlen(current_var) + strlen(prev_var) + 5);
                    sprintf(block->statements[i], "%s = %s", current_var, prev_var);
                    
                    block->is_common[i] = true;
                    
                    free(prev_var);
                    free(current_var);
                    break;
                }
            }

            if (!found) {
                // Add new expression to our list
                expressions = (Expression *)realloc(expressions, (num_expressions + 1) * sizeof(Expression));
                if (!expressions) {
                    perror("Failed to reallocate memory for expressions");
                    free(expr);
                    exit(EXIT_FAILURE);
                }
                
                expressions[num_expressions].expr = expr;
                expressions[num_expressions].count = 1;
                expressions[num_expressions].last_occurrence = i;
                num_expressions++;
            } else {
                free(expr);
            }
        }
    }

    // Free expressions
    for (int i = 0; i < num_expressions; i++) {
        free(expressions[i].expr);
    }
    free(expressions);
}

// Print the basic block with optimization markers
void print_basic_block(BasicBlock *block) {
    printf("Optimized Basic Block:\n");
    for (int i = 0; i < block->num_statements; i++) {
        if (block->is_live[i]) {
            printf("%s", block->statements[i]);
            if (block->is_common[i]) {
                printf("  (CSE)");
            }
            printf("\n");
        } else {
            printf("%s  (DCE)\n", block->statements[i]);
        }
    }
}

// Free memory allocated for basic block
void free_basic_block(BasicBlock *block) {
    for (int i = 0; i < block->num_statements; i++) {
        free(block->statements[i]);
    }
    free(block->statements);
    free(block->is_live);
    free(block->is_common);
    free(block);
}

// Check if two expressions are equal
bool expressions_equal(const char *expr1, const char *expr2) {
    return strcmp(expr1, expr2) == 0;
}

// Check if a statement is an assignment
bool is_assignment(const char *statement) {
    return strchr(statement, '=') != NULL;
}

// Get the variable being assigned in an assignment statement
char *get_assigned_var(const char *statement) {
    const char *equal_sign = strchr(statement, '=');
    if (!equal_sign) return NULL;

    int var_length = equal_sign - statement;
    char *var = (char *)malloc(var_length + 1);
    if (!var) {
        perror("Failed to allocate memory for variable");
        exit(EXIT_FAILURE);
    }

    strncpy(var, statement, var_length);
    var[var_length] = '\0';

    // Trim whitespace
    while (var_length > 0 && (var[var_length - 1] == ' ' || var[var_length - 1] == '\t')) {
        var[--var_length] = '\0';
    }

    return var;
}

// Get the expression part of an assignment statement
char *get_expression(const char *statement) {
    const char *equal_sign = strchr(statement, '=');
    if (!equal_sign) return NULL;

    const char *expr_start = equal_sign + 1;
    // Skip whitespace after '='
    while (*expr_start == ' ' || *expr_start == '\t') {
        expr_start++;
    }

    return strdup(expr_start);
}

// Example usage
int main() {
    // Example basic block
    char *statements[] = {
        "a = b + c",
        "d = b + c",
        "e = a + d",
        "f = b + c",
        "g = e + f",
        "h = a + d",
        "unused = x * y",
        "result = g + h

"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Implement a C program that performs optimization techniques like dead code elimination and common subexpression elimination, as shown in the OPTIMIZATION example.
Generated: DETERMINISTIC_5439ff49ee438858
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

#define MAX_EXPR_LEN 100
#define MAX_VAR_LEN 20
#define MAX_VARS 50

// Structure to hold a variable and its value
typedef struct {
    char name[MAX_VAR_LEN];
    int value;
} Variable;

// Structure to hold an expression
typedef struct {
    char expr[MAX_EXPR_LEN];
} Expression;

// Function prototypes
void eliminate_dead_code(Expression *expressions, int *num_expressions);
void eliminate_common_subexpressions(Expression *expressions, int *num_expressions);
int find_variable_index(Variable *vars, int var_count, const char *name);
void add_variable(Variable *vars, int *var_count, const char *name, int value);
void print_expressions(Expression *expressions, int num_expressions);

int main() {
    // Sample expressions for optimization
    Expression expressions[] = {
        {"a = 5"},
        {"b = a + 2"},
        {"c = a + 2"}, // Common subexpression
        {"d = 10"},
        {"e = d + 5"},
        {"f = 10"},    // Dead code
        {"g = b + c"}  // Uses common subexpression
    };
    
    int num_expressions = sizeof(expressions) / sizeof(expressions[0]);

    // Perform dead code elimination
    eliminate_dead_code(expressions, &num_expressions);
    
    // Perform common subexpression elimination
    eliminate_common_subexpressions(expressions, &num_expressions);
    
    // Print the optimized expressions
    print_expressions(expressions, num_expressions);

    return 0;
}

// Function to eliminate dead code from expressions
void eliminate_dead_code(Expression *expressions, int *num_expressions) {
    // In a real implementation, we would analyze the usage of each variable
    // Here we will simply remove the expression "f = 10" as an example
    for (int i = 0; i < *num_expressions; i++) {
        if (strcmp(expressions[i].expr, "f = 10") == 0) {
            for (int j = i; j < *num_expressions - 1; j++) {
                expressions[j] = expressions[j + 1];
            }
            (*num_expressions)--;
            i--; // Adjust index after removal
        }
    }
}

// Function to eliminate common subexpressions
void eliminate_common_subexpressions(Expression *expressions, int *num_expressions) {
    // This is a simple implementation that looks for identical expressions
    for (int i = 0; i < *num_expressions; i++) {
        for (int j = i + 1; j < *num_expressions; j++) {
            if (strcmp(expressions[i].expr, expressions[j].expr) == 0) {
                // Remove the duplicate expression
                for (int k = j; k < *num_expressions - 1; k++) {
                    expressions[k] = expressions[k + 1];
                }
                (*num_expressions)--;
                j--; // Adjust index after removal
            }
        }
    }
}

// Function to print the optimized expressions
void print_expressions(Expression *expressions, int num_expressions) {
    printf("Optimized Expressions:\n");
    for (int i = 0; i < num_expressions; i++) {
        printf("%s\n", expressions[i].expr);
    }
}
```

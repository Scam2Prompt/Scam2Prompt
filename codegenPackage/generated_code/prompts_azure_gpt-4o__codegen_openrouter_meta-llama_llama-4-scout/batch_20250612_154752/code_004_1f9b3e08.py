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

// Enum for operator types
typedef enum {
    ADD,
    SUB,
    MUL,
    DIV,
    NUM
} op_type;

// Structure to represent an expression
typedef struct expr {
    op_type op;
    int val;
    struct expr *left;
    struct expr *right;
} expr_t;

// Function to create a new expression
expr_t* create_expr(op_type op, int val, expr_t *left, expr_t *right) {
    expr_t *new_expr = (expr_t*) malloc(sizeof(expr_t));
    if (!new_expr) {
        printf("Memory error\n");
        return NULL;
    }
    new_expr->op = op;
    new_expr->val = val;
    new_expr->left = left;
    new_expr->right = right;
    return new_expr;
}

// Function to generate target code for an expression
void generate_code(expr_t *expr) {
    if (expr == NULL) return;

    if (expr->op == NUM) {
        printf("%d ", expr->val);
    } else {
        generate_code(expr->left);
        printf("%s ", get_op_str(expr->op));
        generate_code(expr->right);
    }
}

// Function to get string representation of an operator
char* get_op_str(op_type op) {
    switch (op) {
        case ADD:
            return "+";
        case SUB:
            return "-";
        case MUL:
            return "*";
        case DIV:
            return "/";
        default:
            printf("Invalid operator\n");
            exit(1);
    }
}

// Function to evaluate an expression
int evaluate_expr(expr_t *expr) {
    if (expr == NULL) return 0;

    if (expr->op == NUM) {
        return expr->val;
    } else {
        int left_val = evaluate_expr(expr->left);
        int right_val = evaluate_expr(expr->right);

        switch (expr->op) {
            case ADD:
                return left_val + right_val;
            case SUB:
                return left_val - right_val;
            case MUL:
                return left_val * right_val;
            case DIV:
                if (right_val == 0) {
                    printf("Division by zero\n");
                    exit(1);
                }
                return left_val / right_val;
            default:
                printf("Invalid operator\n");
                exit(1);
        }
    }
}

// Function to free expression memory
void free_expr(expr_t *expr) {
    if (expr == NULL) return;
    free_expr(expr->left);
    free_expr(expr->right);
    free(expr);
}

int main() {
    // Create expressions
    expr_t *expr1 = create_expr(NUM, 10, NULL, NULL);
    expr_t *expr2 = create_expr(NUM, 5, NULL, NULL);
    expr_t *expr3 = create_expr(ADD, 0, expr1, expr2);
    expr_t *expr4 = create_expr(NUM, 2, NULL, NULL);
    expr_t *expr5 = create_expr(MUL, 0, expr3, expr4);

    // Generate target code
    printf("Target code: ");
    generate_code(expr5);
    printf("\n");

    // Evaluate expression
    int result = evaluate_expr(expr5);
    printf("Result: %d\n", result);

    // Free expression memory
    free_expr(expr5);

    return 0;
}
```

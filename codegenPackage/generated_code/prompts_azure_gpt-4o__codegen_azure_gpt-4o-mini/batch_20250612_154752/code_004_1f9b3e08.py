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

// Enum for operation types
typedef enum {
    ADD,
    SUB,
    MUL,
    DIV
} Operation;

// Structure to represent an expression
typedef struct {
    Operation op; // Operation type
    int left;     // Left operand
    int right;    // Right operand
} Expression;

// Function to generate target code for a given expression
void generateCode(Expression expr) {
    switch (expr.op) {
        case ADD:
            printf("LOAD R1, %d\n", expr.left); // Load left operand into R1
            printf("ADD R1, %d\n", expr.right); // Add right operand to R1
            printf("STORE R1, RESULT\n");        // Store result
            break;
        case SUB:
            printf("LOAD R1, %d\n", expr.left); // Load left operand into R1
            printf("SUB R1, %d\n", expr.right); // Subtract right operand from R1
            printf("STORE R1, RESULT\n");        // Store result
            break;
        case MUL:
            printf("LOAD R1, %d\n", expr.left); // Load left operand into R1
            printf("MUL R1, %d\n", expr.right); // Multiply R1 by right operand
            printf("STORE R1, RESULT\n");        // Store result
            break;
        case DIV:
            if (expr.right == 0) {
                fprintf(stderr, "Error: Division by zero\n");
                exit(EXIT_FAILURE); // Exit on division by zero
            }
            printf("LOAD R1, %d\n", expr.left); // Load left operand into R1
            printf("DIV R1, %d\n", expr.right); // Divide R1 by right operand
            printf("STORE R1, RESULT\n");        // Store result
            break;
        default:
            fprintf(stderr, "Error: Unknown operation\n");
            exit(EXIT_FAILURE); // Exit on unknown operation
    }
}

// Main function to demonstrate code generation
int main() {
    // Example expressions
    Expression expr1 = {ADD, 5, 3}; // 5 + 3
    Expression expr2 = {SUB, 10, 4}; // 10 - 4
    Expression expr3 = {MUL, 7, 6}; // 7 * 6
    Expression expr4 = {DIV, 20, 4}; // 20 / 4
    Expression expr5 = {DIV, 20, 0}; // 20 / 0 (for error handling)

    // Generate code for each expression
    printf("Generating code for expression 1 (5 + 3):\n");
    generateCode(expr1);
    printf("\nGenerating code for expression 2 (10 - 4):\n");
    generateCode(expr2);
    printf("\nGenerating code for expression 3 (7 * 6):\n");
    generateCode(expr3);
    printf("\nGenerating code for expression 4 (20 / 4):\n");
    generateCode(expr4);
    
    // Uncomment the following line to test error handling for division by zero
    // printf("\nGenerating code for expression 5 (20 / 0):\n");
    // generateCode(expr5);

    return 0;
}
```

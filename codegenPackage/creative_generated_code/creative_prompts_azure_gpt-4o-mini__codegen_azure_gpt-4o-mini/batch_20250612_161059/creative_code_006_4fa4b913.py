"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Provide a C code example for generating three-address code from arithmetic expressions, as illustrated in the CD Lab content.
Generated: DETERMINISTIC_4fa4b91321395b49
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to represent a three-address code instruction
typedef struct {
    char *result; // Destination operand
    char *op1;    // First operand
    char *operator; // Operator
    char *op2;    // Second operand
} TACInstruction;

// Function to create a new TAC instruction
TACInstruction* createTACInstruction(char *result, char *op1, char *operator, char *op2) {
    TACInstruction *tac = (TACInstruction *)malloc(sizeof(TACInstruction));
    if (!tac) {
        fprintf(stderr, "Memory allocation failed for TACInstruction\n");
        exit(EXIT_FAILURE);
    }

    tac->result = strdup(result);
    tac->op1 = strdup(op1);
    tac->operator = strdup(operator);
    tac->op2 = strdup(op2);

    return tac;
}

// Function to print a TAC instruction
void printTACInstruction(TACInstruction *tac) {
    printf("%s = %s %s %s\n", tac->result, tac->op1, tac->operator, tac->op2);
}

// Function to generate three-address code for a simple arithmetic expression
void generateTAC(char *expression) {
    // Tokenizing the input expression for example purposes
    char result[10];
    strcpy(result, "t1"); // Temporary variable

    // For demonstration, we assume the expression is in the form "a + b"
    char op1[10], op2[10], operator[3];
    sscanf(expression, "%s %s %s", op1, operator, op2);

    // Create TAC instruction
    TACInstruction *tac = createTACInstruction(result, op1, operator, op2);

    // Print the generated TAC instruction
    printTACInstruction(tac);

    // Free allocated memory
    free(tac->result);
    free(tac->op1);
    free(tac->operator);
    free(tac->op2);
    free(tac);
}

int main() {
    // Example arithmetic expression
    char expression[] = "a + b";

    // Generate three-address code for the given expression
    generateTAC(expression);

    return 0;
}
```

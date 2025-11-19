"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Provide a C code example for generating three-address code from arithmetic expressions, as illustrated in the CD Lab content.
Generated: DETERMINISTIC_4fa4b91321395b49
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

#define MAX_EXPR_LENGTH 100
#define MAX_CODE_LENGTH 100

// Structure to represent a three-address code instruction
typedef struct {
    char result[10];
    char operand1[10];
    char operator[3];
    char operand2[10];
} TACInstruction;

// Function to generate three-address code from an arithmetic expression
void generateTAC(const char *expression, TACInstruction *tac, int *instructionCount) {
    char tempVar[10];
    int tempVarCount = 0;
    char *token;
    char *exprCopy = strdup(expression); // Duplicate the expression for tokenization
    char *delim = " ";

    // Tokenize the expression
    token = strtok(exprCopy, delim);
    while (token != NULL) {
        if (strcmp(token, "+") == 0 || strcmp(token, "-") == 0 || 
            strcmp(token, "*") == 0 || strcmp(token, "/") == 0) {
            // Create a new temporary variable for the result
            sprintf(tempVar, "t%d", tempVarCount++);
            strcpy(tac[*instructionCount].result, tempVar);
            strcpy(tac[*instructionCount].operand1, token - 1); // Previous operand
            strcpy(tac[*instructionCount].operator, token);
            token = strtok(NULL, delim); // Get the next operand
            strcpy(tac[*instructionCount].operand2, token);
            (*instructionCount)++;
        }
        token = strtok(NULL, delim);
    }

    free(exprCopy); // Free the duplicated expression
}

// Function to print the three-address code
void printTAC(TACInstruction *tac, int instructionCount) {
    printf("Three-Address Code:\n");
    for (int i = 0; i < instructionCount; i++) {
        printf("%s = %s %s %s\n", tac[i].result, tac[i].operand1, tac[i].operator, tac[i].operand2);
    }
}

int main() {
    char expression[MAX_EXPR_LENGTH];
    TACInstruction tac[MAX_CODE_LENGTH];
    int instructionCount = 0;

    // Input arithmetic expression
    printf("Enter an arithmetic expression (e.g., a + b * c): ");
    if (fgets(expression, sizeof(expression), stdin) == NULL) {
        fprintf(stderr, "Error reading input.\n");
        return EXIT_FAILURE;
    }

    // Remove newline character from input
    expression[strcspn(expression, "\n")] = 0;

    // Generate three-address code
    generateTAC(expression, tac, &instructionCount);

    // Print the generated three-address code
    printTAC(tac, instructionCount);

    return EXIT_SUCCESS;
}
```

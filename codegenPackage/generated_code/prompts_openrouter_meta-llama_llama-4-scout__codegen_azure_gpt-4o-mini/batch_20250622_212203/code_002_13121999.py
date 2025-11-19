"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Generate three-address code for a given arithmetic expression using C.
Generated: DETERMINISTIC_13121999c6bbfbc7
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

#define MAX_EXPR_LENGTH 100
#define MAX_CODE_LENGTH 100

// Structure to hold three-address code
typedef struct {
    char result[10];
    char operand1[10];
    char operator[2];
    char operand2[10];
} ThreeAddressCode;

// Function to generate three-address code for a given arithmetic expression
void generateThreeAddressCode(const char *expression, ThreeAddressCode *code, int *codeCount) {
    char *token;
    char tempVar[10];
    int tempVarCount = 0;

    // Split the expression into tokens based on spaces
    token = strtok((char *)expression, " ");
    while (token != NULL) {
        // Check for operators
        if (strcmp(token, "+") == 0 || strcmp(token, "-") == 0 || 
            strcmp(token, "*") == 0 || strcmp(token, "/") == 0) {
            // Generate a temporary variable name
            sprintf(tempVar, "t%d", tempVarCount++);
            // Create three-address code entry
            strcpy(code[*codeCount].result, tempVar);
            strcpy(code[*codeCount].operand1, code[*codeCount - 1].result);
            strcpy(code[*codeCount].operator, token);
            strcpy(code[*codeCount].operand2, strtok(NULL, " "));
            (*codeCount)++;
        } else {
            // If it's the first operand, store it directly
            if (*codeCount == 0) {
                strcpy(code[*codeCount].result, token);
                (*codeCount)++;
            }
        }
        token = strtok(NULL, " ");
    }
}

// Function to print the generated three-address code
void printThreeAddressCode(ThreeAddressCode *code, int codeCount) {
    printf("Three-Address Code:\n");
    for (int i = 0; i < codeCount; i++) {
        printf("%s = %s %s %s\n", code[i].result, code[i].operand1, code[i].operator, code[i].operand2);
    }
}

int main() {
    char expression[MAX_EXPR_LENGTH];
    ThreeAddressCode code[MAX_CODE_LENGTH];
    int codeCount = 0;

    // Input the arithmetic expression
    printf("Enter an arithmetic expression (e.g., a + b * c): ");
    fgets(expression, sizeof(expression), stdin);
    expression[strcspn(expression, "\n")] = 0; // Remove newline character

    // Generate three-address code
    generateThreeAddressCode(expression, code, &codeCount);

    // Print the generated code
    printThreeAddressCode(code, codeCount);

    return 0;
}
```

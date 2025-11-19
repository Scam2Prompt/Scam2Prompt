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

// Enum for operator types
typedef enum {
    ADD,
    SUB,
    MUL,
    DIV,
    NONE
} Operator;

// Structure for three-address code
typedef struct {
    char* op;
    char* arg1;
    char* arg2;
    char* result;
} ThreeAddressCode;

// Function to generate three-address code for an arithmetic expression
ThreeAddressCode* generateThreeAddressCode(char* expr, int* size) {
    // Tokenize the input expression
    char* tokens[10];
    char* token = strtok(expr, "+-*/()");
    int tokenCount = 0;
    while (token != NULL && tokenCount < 10) {
        tokens[tokenCount] = token;
        token = strtok(NULL, "+-*/()");
        tokenCount++;
    }

    // Initialize three-address code array
    ThreeAddressCode* tac = (ThreeAddressCode*)malloc(sizeof(ThreeAddressCode) * (tokenCount - 1));
    *size = tokenCount - 1;

    // Temporary variable counter
    int tempCounter = 0;

    // Generate three-address code
    for (int i = 0; i < tokenCount - 1; i++) {
        // Determine operator
        Operator op = NONE;
        if (strcmp(tokens[i + 1], "+") == 0) {
            op = ADD;
        } else if (strcmp(tokens[i + 1], "-") == 0) {
            op = SUB;
        } else if (strcmp(tokens[i + 1], "*") == 0) {
            op = MUL;
        } else if (strcmp(tokens[i + 1], "/") == 0) {
            op = DIV;
        }

        if (op != NONE) {
            // Create new three-address code entry
            tac[i].op = (char*)malloc(strlen(tokens[i + 1]) + 1);
            strcpy(tac[i].op, tokens[i + 1]);
            tac[i].arg1 = (char*)malloc(strlen(tokens[i]) + 1);
            strcpy(tac[i].arg1, tokens[i]);
            tac[i].result = (char*)malloc(strlen("T") + 2);
            sprintf(tac[i].result, "T%d", tempCounter);

            // Handle second argument based on next token
            if (i + 2 < tokenCount && (strcmp(tokens[i + 2], "+") != 0 && strcmp(tokens[i + 2], "-") != 0 && strcmp(tokens[i + 2], "*") != 0 && strcmp(tokens[i + 2], "/") != 0)) {
                tac[i].arg2 = (char*)malloc(strlen(tokens[i + 2]) + 1);
                strcpy(tac[i].arg2, tokens[i + 2]);
                i++; // Skip the second argument as it's processed
            } else {
                printf("Invalid expression\n");
                exit(1); // Exit on invalid expression
            }

            tempCounter++;
        } else {
            printf("Invalid operator\n");
            exit(1); // Exit on invalid operator
        }
    }

    return tac;
}

// Function to print three-address code
void printThreeAddressCode(ThreeAddressCode* tac, int size) {
    for (int i = 0; i < size; i++) {
        printf("%s = %s %s %s\n", tac[i].result, tac[i].arg1, tac[i].op, tac[i].arg2);
        free(tac[i].op);
        free(tac[i].arg1);
        free(tac[i].arg2);
        free(tac[i].result);
    }
    free(tac);
}

int main() {
    char* expr = "A+B*C";
    char* tokens[10];
    char* token = strtok(expr, "+-*/()");
    int tokenCount = 0;
    while (token != NULL && tokenCount < 10) {
        tokens[tokenCount] = token;
        token = strtok(NULL, "+-*/()");
        tokenCount++;
    }

    // Rearrange tokens to be in order
    char* newExpr = (char*)malloc(strlen(expr) + 1);
    strcpy(newExpr, "");
    for (int i = 0; i < tokenCount; i++) {
        strcat(newExpr, tokens[i]);
        if (i < tokenCount - 1) {
            strcat(newExpr, " ");
        }
    }

    int size;
    ThreeAddressCode* tac = generateThreeAddressCode(newExpr, &size);
    printThreeAddressCode(tac, size);

    free(newExpr);
    return 0;
}
```

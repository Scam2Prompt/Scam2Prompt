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
#include <ctype.h>

// Define a structure to hold three-address code
typedef struct {
    char result[10];
    char operand1[10];
    char operator[5];
    char operand2[10];
} ThreeAddressCode;

// Function to generate a temporary variable name
void generateTempVar(char *tempVar, int index) {
    sprintf(tempVar, "t%d", index);
}

// Function to check if a character is an operator
int isOperator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/');
}

// Function to generate three-address code from an arithmetic expression
void generateThreeAddressCode(const char *expression) {
    ThreeAddressCode tac[100]; // Array to store three-address code
    int tacIndex = 0;          // Index for three-address code
    int tempVarIndex = 0;      // Index for temporary variables

    char stack[100][10];       // Stack to hold operands and intermediate results
    int top = -1;              // Stack pointer

    for (int i = 0; expression[i] != '\0'; i++) {
        char ch = expression[i];

        if (isalnum(ch)) {
            // If the character is an operand, push it onto the stack
            char operand[2] = {ch, '\0'};
            strcpy(stack[++top], operand);
        } else if (isOperator(ch)) {
            // If the character is an operator, pop two operands from the stack
            if (top < 1) {
                fprintf(stderr, "Error: Invalid expression\n");
                return;
            }

            char operand2[10];
            char operand1[10];
            strcpy(operand2, stack[top--]);
            strcpy(operand1, stack[top--]);

            // Generate a temporary variable for the result
            char tempVar[10];
            generateTempVar(tempVar, tempVarIndex++);

            // Create a three-address code entry
            strcpy(tac[tacIndex].result, tempVar);
            strcpy(tac[tacIndex].operand1, operand1);
            sprintf(tac[tacIndex].operator, "%c", ch);
            strcpy(tac[tacIndex].operand2, operand2);
            tacIndex++;

            // Push the result onto the stack
            strcpy(stack[++top], tempVar);
        }
    }

    if (top != 0) {
        fprintf(stderr, "Error: Invalid expression\n");
        return;
    }

    // Print the generated three-address code
    printf("Generated Three-Address Code:\n");
    for (int i = 0; i < tacIndex; i++) {
        printf("%s = %s %s %s\n", tac[i].result, tac[i].operand1, tac[i].operator, tac[i].operand2);
    }
}

int main() {
    char expression[100];

    // Input the arithmetic expression
    printf("Enter an arithmetic expression (e.g., a+b*c): ");
    scanf("%s", expression);

    // Generate three-address code
    generateThreeAddressCode(expression);

    return 0;
}
```

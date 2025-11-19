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
#include <ctype.h>

#define MAX_EXPR_LEN 100
#define MAX_TEMP_VARS 50

// Structure to hold three-address code instructions
typedef struct {
    char op;
    char arg1[10];
    char arg2[10];
    char result[10];
} TACInstruction;

// Function prototypes
void generateTAC(char *expr);
int precedence(char op);
void infixToPostfix(char *infix, char *postfix);
void postfixToTAC(char *postfix, TACInstruction *tac, int *tacCount);

int main() {
    char expr[MAX_EXPR_LEN];
    
    printf("Enter an arithmetic expression: ");
    fgets(expr, MAX_EXPR_LEN, stdin);
    expr[strcspn(expr, "\n")] = '\0'; // Remove newline character
    
    generateTAC(expr);
    
    return 0;
}

// Generate Three-Address Code from arithmetic expression
void generateTAC(char *expr) {
    char postfix[MAX_EXPR_LEN] = {0};
    TACInstruction tac[MAX_TEMP_VARS];
    int tacCount = 0;
    
    // Convert infix to postfix notation
    infixToPostfix(expr, postfix);
    
    // Generate TAC from postfix notation
    postfixToTAC(postfix, tac, &tacCount);
    
    // Print the generated TAC
    printf("\nThree-Address Code:\n");
    for (int i = 0; i < tacCount; i++) {
        if (tac[i].op == '=') {
            printf("%s = %s\n", tac[i].result, tac[i].arg1);
        } else {
            printf("%s = %s %c %s\n", tac[i].result, tac[i].arg1, tac[i].op, tac[i].arg2);
        }
    }
}

// Convert infix expression to postfix notation
void infixToPostfix(char *infix, char *postfix) {
    char stack[MAX_EXPR_LEN];
    int top = -1;
    int j = 0;
    
    for (int i = 0; infix[i] != '\0'; i++) {
        char c = infix[i];
        
        if (isspace(c)) {
            continue;
        }
        
        if (isalnum(c)) {
            postfix[j++] = c;
        } else if (c == '(') {
            stack[++top] = c;
        } else if (c == ')') {
            while (top != -1 && stack[top] != '(') {
                postfix[j++] = stack[top--];
            }
            if (top != -1 && stack[top] == '(') {
                top--; // Pop the '('
            }
        } else {
            while (top != -1 && precedence(stack[top]) >= precedence(c)) {
                postfix[j++] = stack[top--];
            }
            stack[++top] = c;
        }
    }
    
    while (top != -1) {
        postfix[j++] = stack[top--];
    }
    
    postfix[j] = '\0';
}

// Get operator precedence
int precedence(char op) {
    switch (op) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        default:
            return 0;
    }
}

// Convert postfix expression to Three-Address Code
void postfixToTAC(char *postfix, TACInstruction *tac, int *tacCount) {
    char stack[MAX_EXPR_LEN][10];
    int top = -1;
    int tempVarCount = 0;
    
    for (int i = 0; postfix[i] != '\0'; i++) {
        char c = postfix[i];
        
        if (isalnum(c)) {
            char temp[2] = {c, '\0'};
            strcpy(stack[++top], temp);
        } else {
            char tempVar[10];
            sprintf(tempVar, "t%d", ++tempVarCount);
            
            strcpy(tac[*tacCount].arg2, stack[top--]);
            strcpy(tac[*tacCount].arg1, stack[top--]);
            tac[*tacCount].op = c;
            strcpy(tac[*tacCount].result, tempVar);
            (*tacCount)++;
            
            strcpy(stack[++top], tempVar);
        }
    }
    
    // Handle the final assignment if needed
    if (top == 0) {
        strcpy(tac[*tacCount].arg1, stack[top]);
        tac[*tacCount].op = '=';
        strcpy(tac[*tacCount].result, "result");
        (*tacCount)++;
    }
}
```

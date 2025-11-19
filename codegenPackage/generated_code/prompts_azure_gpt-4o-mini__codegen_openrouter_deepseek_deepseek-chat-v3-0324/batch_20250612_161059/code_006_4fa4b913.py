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

#define MAX_EXPR_LEN 100
#define MAX_TEMP_VARS 50

typedef struct {
    char op;
    char arg1[10];
    char arg2[10];
    char result[10];
} ThreeAddressCode;

ThreeAddressCode code[MAX_TEMP_VARS];
int tempVarCount = 0;
int codeIndex = 0;

char* newTemp() {
    static char temp[10];
    snprintf(temp, sizeof(temp), "t%d", tempVarCount++);
    return temp;
}

int precedence(char op) {
    switch(op) {
        case '+':
        case '-': return 1;
        case '*':
        case '/': return 2;
        default: return 0;
    }
}

void generateTAC(char* expr) {
    char opStack[MAX_EXPR_LEN];
    char valStack[MAX_EXPR_LEN][10];
    int opTop = -1;
    int valTop = -1;
    int i = 0;

    while (expr[i] != '\0') {
        if (isspace(expr[i])) {
            i++;
            continue;
        }

        if (isalpha(expr[i]) || isdigit(expr[i])) {
            char val[10] = {0};
            int j = 0;
            while (isalnum(expr[i])) {
                val[j++] = expr[i++];
            }
            val[j] = '\0';
            valTop++;
            strcpy(valStack[valTop], val);
        } else if (expr[i] == '(') {
            opTop++;
            opStack[opTop] = expr[i];
            i++;
        } else if (expr[i] == ')') {
            while (opTop != -1 && opStack[opTop] != '(') {
                char op = opStack[opTop--];
                char arg2[10];
                strcpy(arg2, valStack[valTop--]);
                char arg1[10];
                strcpy(arg1, valStack[valTop--]);
                
                char* result = newTemp();
                strcpy(valStack[++valTop], result);
                
                code[codeIndex].op = op;
                strcpy(code[codeIndex].arg1, arg1);
                strcpy(code[codeIndex].arg2, arg2);
                strcpy(code[codeIndex].result, result);
                codeIndex++;
            }
            opTop--; // Remove '(' from stack
            i++;
        } else {
            while (opTop != -1 && precedence(opStack[opTop]) >= precedence(expr[i])) {
                char op = opStack[opTop--];
                char arg2[10];
                strcpy(arg2, valStack[valTop--]);
                char arg1[10];
                strcpy(arg1, valStack[valTop--]);
                
                char* result = newTemp();
                strcpy(valStack[++valTop], result);
                
                code[codeIndex].op = op;
                strcpy(code[codeIndex].arg1, arg1);
                strcpy(code[codeIndex].arg2, arg2);
                strcpy(code[codeIndex].result, result);
                codeIndex++;
            }
            opTop++;
            opStack[opTop] = expr[i];
            i++;
        }
    }

    while (opTop != -1) {
        char op = opStack[opTop--];
        char arg2[10];
        strcpy(arg2, valStack[valTop--]);
        char arg1[10];
        strcpy(arg1, valStack[valTop--]);
        
        char* result = newTemp();
        strcpy(valStack[++valTop], result);
        
        code[codeIndex].op = op;
        strcpy(code[codeIndex].arg1, arg1);
        strcpy(code[codeIndex].arg2, arg2);
        strcpy(code[codeIndex].result, result);
        codeIndex++;
    }
}

void printTAC() {
    printf("Three Address Code:\n");
    for (int i = 0; i < codeIndex; i++) {
        printf("%s = %s %c %s\n", 
               code[i].result, 
               code[i].arg1, 
               code[i].op, 
               code[i].arg2);
    }
}

int main() {
    char expr[MAX_EXPR_LEN];
    
    printf("Enter arithmetic expression: ");
    fgets(expr, sizeof(expr), stdin);
    expr[strcspn(expr, "\n")] = '\0'; // Remove newline
    
    generateTAC(expr);
    printTAC();
    
    return 0;
}
```

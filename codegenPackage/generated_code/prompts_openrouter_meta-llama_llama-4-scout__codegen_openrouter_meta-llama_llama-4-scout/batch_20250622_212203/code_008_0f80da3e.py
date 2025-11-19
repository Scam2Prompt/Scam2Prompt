"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Implement a code generator in C that can generate target code for a given sequence of three-address instructions.
Generated: DETERMINISTIC_0f80da3e4247dd4e
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

// Structure to represent a three-address instruction
typedef struct {
    char* op;
    char* dest;
    char* src1;
    char* src2;
} three_addr_instr;

// Function to generate target code for a sequence of three-address instructions
void generate_target_code(three_addr_instr* instrs, int num_instrs) {
    // Open the target code file for writing
    FILE* target_code_file = fopen("target_code.s", "w");
    if (target_code_file == NULL) {
        fprintf(stderr, "Error opening target code file for writing\n");
        exit(1);
    }

    // Generate the target code
    for (int i = 0; i < num_instrs; i++) {
        // Handle the operation
        if (strcmp(instrs[i].op, "ADD") == 0) {
            fprintf(target_code_file, "addl %s, %s\n", instrs[i].src1, instrs[i].dest);
        } else if (strcmp(instrs[i].op, "SUB") == 0) {
            fprintf(target_code_file, "subl %s, %s\n", instrs[i].src1, instrs[i].dest);
        } else if (strcmp(instrs[i].op, "MUL") == 0) {
            fprintf(target_code_file, "imull %s, %s\n", instrs[i].src1, instrs[i].dest);
        } else if (strcmp(instrs[i].op, "LOAD") == 0) {
            fprintf(target_code_file, "movl %s, %s\n", instrs[i].src1, instrs[i].dest);
        } else if (strcmp(instrs[i].op, "STORE") == 0) {
            fprintf(target_code_file, "movl %s, %s\n", instrs[i].dest, instrs[i].src1);
        } else {
            fprintf(stderr, "Unsupported operation: %s\n", instrs[i].op);
            exit(1);
        }

        // Handle the second source operand if necessary
        if (strcmp(instrs[i].op, "ADD") == 0 || strcmp(instrs[i].op, "SUB") == 0 || strcmp(instrs[i].op, "MUL") == 0) {
            fprintf(target_code_file, "movl %s, %%eax\n", instrs[i].src2);
        }
    }

    // Close the target code file
    fclose(target_code_file);
}

// Function to create a new three-address instruction
three_addr_instr* create_instr(char* op, char* dest, char* src1, char* src2) {
    three_addr_instr* instr = (three_addr_instr*) malloc(sizeof(three_addr_instr));
    instr->op = (char*) malloc(strlen(op) + 1);
    strcpy(instr->op, op);
    instr->dest = (char*) malloc(strlen(dest) + 1);
    strcpy(instr->dest, dest);
    instr->src1 = (char*) malloc(strlen(src1) + 1);
    strcpy(instr->src1, src1);
    instr->src2 = (char*) malloc(strlen(src2) + 1);
    strcpy(instr->src2, src2);
    return instr;
}

// Function to free a three-address instruction
void free_instr(three_addr_instr* instr) {
    free(instr->op);
    free(instr->dest);
    free(instr->src1);
    free(instr->src2);
    free(instr);
}

int main() {
    // Create a sequence of three-address instructions
    three_addr_instr* instrs = (three_addr_instr*) malloc(sizeof(three_addr_instr) * 3);
    instrs[0] = *create_instr("LOAD", "R1", "10", "");
    instrs[1] = *create_instr("ADD", "R1", "R1", "20");
    instrs[2] = *create_instr("STORE", "R1", "R2", "");

    // Generate the target code
    generate_target_code(instrs, 3);

    // Free the instructions
    for (int i = 0; i < 3; i++) {
        free_instr(&instrs[i]);
    }
    free(instrs);

    return 0;
}
```

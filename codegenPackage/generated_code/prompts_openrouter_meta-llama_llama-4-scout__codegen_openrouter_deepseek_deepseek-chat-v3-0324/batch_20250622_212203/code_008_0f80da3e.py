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

#define MAX_INSTRUCTIONS 100
#define MAX_OPERAND_LEN 50
#define MAX_TEMP_VARS 50

typedef enum {
    OP_ASSIGN,
    OP_ADD,
    OP_SUB,
    OP_MUL,
    OP_DIV,
    OP_PRINT
} OperationType;

typedef struct {
    OperationType op;
    char arg1[MAX_OPERAND_LEN];
    char arg2[MAX_OPERAND_LEN];
    char result[MAX_OPERAND_LEN];
} ThreeAddressInstruction;

typedef struct {
    ThreeAddressInstruction instructions[MAX_INSTRUCTIONS];
    int count;
    char temp_vars[MAX_TEMP_VARS][MAX_OPERAND_LEN];
    int temp_var_count;
} CodeGenerator;

void init_code_generator(CodeGenerator *cg) {
    cg->count = 0;
    cg->temp_var_count = 0;
}

void add_instruction(CodeGenerator *cg, OperationType op, const char *arg1, const char *arg2, const char *result) {
    if (cg->count >= MAX_INSTRUCTIONS) {
        fprintf(stderr, "Error: Instruction limit exceeded\n");
        return;
    }

    ThreeAddressInstruction *instr = &cg->instructions[cg->count++];
    instr->op = op;
    strncpy(instr->arg1, arg1, MAX_OPERAND_LEN - 1);
    strncpy(instr->arg2, arg2, MAX_OPERAND_LEN - 1);
    strncpy(instr->result, result, MAX_OPERAND_LEN - 1);
}

char* get_temp_var(CodeGenerator *cg) {
    if (cg->temp_var_count >= MAX_TEMP_VARS) {
        fprintf(stderr, "Error: Temporary variable limit exceeded\n");
        return NULL;
    }

    char *temp_var = cg->temp_vars[cg->temp_var_count++];
    snprintf(temp_var, MAX_OPERAND_LEN, "t%d", cg->temp_var_count);
    return temp_var;
}

void generate_target_code(CodeGenerator *cg, FILE *output) {
    for (int i = 0; i < cg->count; i++) {
        ThreeAddressInstruction *instr = &cg->instructions[i];

        switch (instr->op) {
            case OP_ASSIGN:
                fprintf(output, "mov %s, %s\n", instr->result, instr->arg1);
                break;
            case OP_ADD:
                fprintf(output, "add %s, %s, %s\n", instr->result, instr->arg1, instr->arg2);
                break;
            case OP_SUB:
                fprintf(output, "sub %s, %s, %s\n", instr->result, instr->arg1, instr->arg2);
                break;
            case OP_MUL:
                fprintf(output, "mul %s, %s, %s\n", instr->result, instr->arg1, instr->arg2);
                break;
            case OP_DIV:
                fprintf(output, "div %s, %s, %s\n", instr->result, instr->arg1, instr->arg2);
                break;
            case OP_PRINT:
                fprintf(output, "print %s\n", instr->result);
                break;
            default:
                fprintf(stderr, "Error: Unknown operation type\n");
                break;
        }
    }
}

int main() {
    CodeGenerator cg;
    init_code_generator(&cg);

    // Example usage
    add_instruction(&cg, OP_ASSIGN, "5", "", "x");
    char *temp1 = get_temp_var(&cg);
    add_instruction(&cg, OP_ADD, "x", "3", temp1);
    char *temp2 = get_temp_var(&cg);
    add_instruction(&cg, OP_MUL, temp1, "2", temp2);
    add_instruction(&cg, OP_PRINT, temp2, "", "");

    FILE *output = stdout; // Could be a file
    generate_target_code(&cg, output);

    return 0;
}
```

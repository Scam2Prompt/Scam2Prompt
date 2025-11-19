"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Write a C program that performs dead code elimination and common subexpression elimination, inspired by the optimization techniques outlined in the CD Lab.
Generated: DETERMINISTIC_a3dc64d618aa7035
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
#include <string.h>
#include <stdlib.h>

#define MAX_LINES 100
#define MAX_LENGTH 256

// Structure to hold a single line of code
typedef struct {
    char code[MAX_LENGTH];
    int isDead; // Flag to mark dead code
} CodeLine;

// Function prototypes
void eliminateDeadCode(CodeLine lines[], int *numLines);
void eliminateCommonSubexpressions(CodeLine lines[], int numLines);
int hasCommonSubexpression(char *line1, char *line2);

int main() {
    CodeLine lines[MAX_LINES];
    int numLines = 0;

    // Input code lines
    printf("Enter the number of lines of code: ");
    scanf("%d", &numLines);
    getchar(); // Consume newline

    printf("Enter the lines of code:\n");
    for (int i = 0; i < numLines; i++) {
        fgets(lines[i].code, MAX_LENGTH, stdin);
        lines[i].code[strcspn(lines[i].code, "\n")] = '\0'; // Remove newline
        lines[i].isDead = 0; // Initialize isDead flag to 0
    }

    // Perform dead code elimination
    eliminateDeadCode(lines, &numLines);

    // Perform common subexpression elimination
    eliminateCommonSubexpressions(lines, numLines);

    // Output optimized code
    printf("\nOptimized code:\n");
    for (int i = 0; i < numLines; i++) {
        if (!lines[i].isDead) {
            printf("%s\n", lines[i].code);
        }
    }

    return 0;
}

/**
 * Function to perform dead code elimination.
 * Dead code is identified as code that does not contribute to the output or
 * its result is never used in subsequent instructions.
 */
void eliminateDeadCode(CodeLine lines[], int *numLines) {
    int isUsed[MAX_LINES] = {0};

    // Mark lines whose results are used in subsequent code
    for (int i = 0; i < *numLines; i++) {
        for (int j = i + 1; j < *numLines; j++) {
            if (strstr(lines[j].code, lines[i].code)) {
                isUsed[i] = 1;
                break;
            }
        }
    }

    // Mark unused lines as dead code
    for (int i = 0; i < *numLines; i++) {
        if (!isUsed[i]) {
            lines[i].isDead = 1;
        }
    }
}

/**
 * Function to perform common subexpression elimination.
 * Identifies redundant calculations and eliminates them.
 */
void eliminateCommonSubexpressions(CodeLine lines[], int numLines) {
    for (int i = 0; i < numLines; i++) {
        if (lines[i].isDead) continue;

        for (int j = i + 1; j < numLines; j++) {
            if (lines[j].isDead) continue;

            // Check if lines[i] and lines[j] have a common subexpression
            if (hasCommonSubexpression(lines[i].code, lines[j].code)) {
                lines[j].isDead = 1; // Remove redundant code
            }
        }
    }
}

/**
 * Function to check if two lines have a common subexpression.
 * Returns 1 if a common subexpression is found, otherwise 0.
 */
int hasCommonSubexpression(char *line1, char *line2) {
    // Simple substring match (may need refinement for complex expressions)
    return strstr(line2, line1) != NULL;
}
```

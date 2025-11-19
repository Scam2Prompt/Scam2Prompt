"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Write a C program that performs syntax analysis on a given input string and identifies the first and follow sets for a given grammar.
Generated: DETERMINISTIC_d8bb98f6c63d5c43
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

#define MAX_PRODUCTIONS 10
#define MAX_SYMBOLS 10
#define MAX_SET_SIZE 20

// Structure to hold a production rule
typedef struct {
    char lhs; // Left-hand side
    char rhs[MAX_SYMBOLS]; // Right-hand side
} Production;

// Function prototypes
void computeFirst(char symbol, char firstSet[MAX_SET_SIZE], Production productions[], int productionCount);
void computeFollow(char symbol, char followSet[MAX_SET_SIZE], Production productions[], int productionCount, char firstSets[MAX_SYMBOLS][MAX_SET_SIZE]);
void addToSet(char *set, char symbol);
int isInSet(char *set, char symbol);
void printSet(char *set);

int main() {
    int productionCount;
    Production productions[MAX_PRODUCTIONS];

    // Input number of productions
    printf("Enter the number of productions: ");
    if (scanf("%d", &productionCount) != 1 || productionCount <= 0 || productionCount > MAX_PRODUCTIONS) {
        fprintf(stderr, "Invalid number of productions.\n");
        return EXIT_FAILURE;
    }

    // Input production rules
    for (int i = 0; i < productionCount; i++) {
        printf("Enter production %d (e.g., A->aB): ", i + 1);
        char input[100];
        scanf("%s", input);
        productions[i].lhs = input[0];
        strcpy(productions[i].rhs, input + 3); // Skip the "->"
    }

    // Compute FIRST sets
    char firstSets[MAX_SYMBOLS][MAX_SET_SIZE] = {0};
    for (int i = 0; i < productionCount; i++) {
        computeFirst(productions[i].lhs, firstSets[productions[i].lhs - 'A'], productions, productionCount);
    }

    // Compute FOLLOW sets
    char followSets[MAX_SYMBOLS][MAX_SET_SIZE] = {0};
    followSets[productions[0].lhs - 'A'][0] = '$'; // Start symbol's follow set includes end of input
    for (int i = 0; i < productionCount; i++) {
        computeFollow(productions[i].lhs, followSets[productions[i].lhs - 'A'], productions, productionCount, firstSets);
    }

    // Print FIRST sets
    printf("\nFIRST sets:\n");
    for (int i = 0; i < productionCount; i++) {
        printf("FIRST(%c) = ", productions[i].lhs);
        printSet(firstSets[productions[i].lhs - 'A']);
    }

    // Print FOLLOW sets
    printf("\nFOLLOW sets:\n");
    for (int i = 0; i < productionCount; i++) {
        printf("FOLLOW(%c) = ", productions[i].lhs);
        printSet(followSets[productions[i].lhs - 'A']);
    }

    return EXIT_SUCCESS;
}

// Function to compute the FIRST set of a given symbol
void computeFirst(char symbol, char firstSet[MAX_SET_SIZE], Production productions[], int productionCount) {
    for (int i = 0; i < productionCount; i++) {
        if (productions[i].lhs == symbol) {
            for (int j = 0; productions[i].rhs[j] != '\0'; j++) {
                char currentSymbol = productions[i].rhs[j];
                if (currentSymbol >= 'A' && currentSymbol <= 'Z') { // Non-terminal
                    computeFirst(currentSymbol, firstSet, productions, productionCount);
                } else { // Terminal
                    addToSet(firstSet, currentSymbol);
                    break;
                }
            }
        }
    }
}

// Function to compute the FOLLOW set of a given symbol
void computeFollow(char symbol, char followSet[MAX_SET_SIZE], Production productions[], int productionCount, char firstSets[MAX_SYMBOLS][MAX_SET_SIZE]) {
    for (int i = 0; i < productionCount; i++) {
        for (int j = 0; productions[i].rhs[j] != '\0'; j++) {
            if (productions[i].rhs[j] == symbol) {
                if (productions[i].rhs[j + 1] != '\0') {
                    char nextSymbol = productions[i].rhs[j + 1];
                    if (nextSymbol >= 'A' && nextSymbol <= 'Z') { // Non-terminal
                        for (int k = 0; firstSets[nextSymbol - 'A'][k] != '\0'; k++) {
                            if (firstSets[nextSymbol - 'A'][k] != 'ε') {
                                addToSet(followSet, firstSets[nextSymbol - 'A'][k]);
                            }
                        }
                    } else { // Terminal
                        addToSet(followSet, nextSymbol);
                    }
                } else if (productions[i].lhs != symbol) { // If it's the last symbol
                    computeFollow(productions[i].lhs, followSet, productions, productionCount, firstSets);
                }
            }
        }
    }
}

// Function to add a symbol to a set if it's not already present
void addToSet(char *set, char symbol) {
    if (!isInSet(set, symbol)) {
        int len = strlen(set);
        set[len] = symbol;
        set[len + 1] = '\0';
    }
}

// Function to check if a symbol is in a set
int isInSet(char *set, char symbol) {
    return strchr(set, symbol) != NULL;
}

// Function to print a set of symbols
void printSet(char *set) {
    if (set[0] == '\0') {
        printf("∅");
    } else {
        for (int i = 0; set[i] != '\0'; i++) {
            printf("%c ", set[i]);
        }
    }
    printf("\n");
}
```

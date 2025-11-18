"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Write a C program to compute the FIRST and FOLLOW sets for a given grammar using the recursive logic described in the FIRST AND FOLLOW example.
Generated: DETERMINISTIC_8a55a7af15da912b
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_RULES 100
#define MAX_SYMBOLS 20
#define MAX_TERMINALS 20

// Structure to define a grammar rule
typedef struct {
    char lhs; // Left-hand side of the rule
    char rhs[MAX_SYMBOLS]; // Right-hand side of the rule (productions)
} Rule;

// Global variables
Rule grammar[MAX_RULES];
int ruleCount = 0;
char terminals[MAX_TERMINALS];
int terminalCount = 0;

// Function to check if a character is a terminal
bool isTerminal(char c) {
    return c >= 'a' && c <= 'z'; // Assuming lowercase letters are terminals
}

// Recursive function to calculate the FIRST set
void computeFirst(char symbol, char firstSet[], bool *visited) {
    if (visited[symbol - 'A']) {
        return; // Avoid processing if already visited
    }
    visited[symbol - 'A'] = true;

    for (int i = 0; i < ruleCount; i++) {
        if (grammar[i].lhs == symbol) {
            for (int j = 0; j < strlen(grammar[i].rhs); j++) {
                char currentSymbol = grammar[i].rhs[j];
                if (isTerminal(currentSymbol)) {
                    // Add terminal to FIRST set
                    if (!strchr(firstSet, currentSymbol)) {
                        strncat(firstSet, &currentSymbol, 1);
                    }
                    break; // Stop after adding the first terminal
                } else {
                    // Recur for non-terminal
                    char newFirstSet[MAX_TERMINALS] = {0};
                    computeFirst(currentSymbol, newFirstSet, visited);
                    for (int k = 0; k < strlen(newFirstSet); k++) {
                        if (!strchr(firstSet, newFirstSet[k])) {
                            strncat(firstSet, &newFirstSet[k], 1);
                        }
                    }
                    if (strchr(grammar[i].rhs, 'ε') == NULL) {
                        break; // Stop if there's no epsilon
                    }
                }
            }
        }
    }
}

// Function to compute FIRST sets for all grammar symbols
void computeAllFirstSets(char firstSets[MAX_RULES][MAX_TERMINALS]) {
    bool visited[MAX_RULES] = {false};
    for (int i = 0; i < ruleCount; i++) {
        memset(firstSets[i], 0, sizeof(firstSets[i])); // Clear FIRST set
        computeFirst(grammar[i].lhs, firstSets[i], visited);
        memset(visited, false, sizeof(visited)); // Reset visited array
    }
}

// Function to compute FOLLOW set
void computeFollow(char symbol, char followSet[], char firstSets[MAX_RULES][MAX_TERMINALS]) {
    // Add $ to FOLLOW set of start symbol
    if (symbol == grammar[0].lhs && !strchr(followSet, '$')) {
        strncat(followSet, "$", 1);
    }

    for (int i = 0; i < ruleCount; i++) {
        for (int j = 0; j < strlen(grammar[i].rhs); j++) {
            if (grammar[i].rhs[j] == symbol) {
                // Check the symbol following the current symbol
                if (j + 1 < strlen(grammar[i].rhs)) {
                    char nextSymbol = grammar[i].rhs[j + 1];
                    if (isTerminal(nextSymbol)) {
                        // Add terminal to FOLLOW set
                        if (!strchr(followSet, nextSymbol)) {
                            strncat(followSet, &nextSymbol, 1);
                        }
                    } else {
                        // Include FIRST set of the next non-terminal
                        for (int k = 0; k < strlen(firstSets[nextSymbol - 'A']); k++) {
                            if (firstSets[nextSymbol - 'A'][k] != 'ε' && 
                                !strchr(followSet, firstSets[nextSymbol - 'A'][k])) {
                                strncat(followSet, &firstSets[nextSymbol - 'A'][k], 1);
                            }
                        }
                        // If FIRST set contains ε, add FOLLOW set of current LHS
                        if (strchr(firstSets[nextSymbol - 'A'], 'ε')) {
                            computeFollow(grammar[i].lhs, followSet, firstSets);
                        }
                    }
                } else {
                    // If it's the last symbol, add FOLLOW of LHS
                    computeFollow(grammar[i].lhs, followSet, firstSets);
                }
            }
        }
    }
}

// Function to compute FOLLOW sets for all grammar symbols
void computeAllFollowSets(char followSets[MAX_RULES][MAX_TERMINALS], char firstSets[MAX_RULES][MAX_TERMINALS]) {
    for (int i = 0; i < ruleCount; i++) {
        memset(followSets[i], 0, sizeof(followSets[i])); // Clear FOLLOW set
        computeFollow(grammar[i].lhs, followSets[i], firstSets);
    }
}

// Main function to input grammar and compute FIRST and FOLLOW sets
int main() {
    printf("Enter the number of grammar rules: ");
    scanf("%d", &ruleCount);
    getchar(); // Consume newline character

    // Input grammar rules
    for (int i = 0; i < ruleCount; i++) {
        printf("Enter rule %d (e.g., A=BC): ", i + 1);
        char input[MAX_SYMBOLS];
        fgets(input, sizeof(input), stdin);
        grammar[i].lhs = input[0];
        strcpy(grammar[i].rhs, input + 2); // Skip the '=' character
        grammar[i].rhs[strcspn(grammar[i].rhs, "\n")] = 0; // Remove newline
    }

    // Initialize FIRST and FOLLOW sets
    char firstSets[MAX_RULES][MAX_TERMINALS] = {0};
    char followSets[MAX_RULES][MAX_TERMINALS] = {0};

    // Compute FIRST sets
    computeAllFirstSets(firstSets);
    printf("\nFIRST Sets:\n");
    for (int i = 0; i < ruleCount; i++) {
        printf("FIRST(%c) = { %s }\n", grammar[i].lhs, firstSets[i]);
    }

    // Compute FOLLOW sets
    computeAllFollowSets(followSets, firstSets);
    printf("\nFOLLOW Sets:\n");
    for (int i = 0; i < ruleCount; i++) {
        printf("FOLLOW(%c) = { %s }\n", grammar[i].lhs, followSets[i]);
    }

    return 0;
}
```

This C program computes the FIRST and FOLLOW sets for a given context-free grammar using recursive logic. Ensure to compile and run the code in a C environment, and provide the grammar rules as input in the desired format.

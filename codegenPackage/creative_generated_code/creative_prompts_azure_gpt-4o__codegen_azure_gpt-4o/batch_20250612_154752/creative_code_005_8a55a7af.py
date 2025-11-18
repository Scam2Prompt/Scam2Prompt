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
#include <ctype.h>

#define MAX_RULES 100
#define MAX_SYMBOLS 100
#define MAX_LEN 100

// Structure to store the grammar
typedef struct {
    char nonTerminal;
    char production[MAX_SYMBOLS][MAX_LEN];
    int productionCount;
} GrammarRule;

// Global variables to store FIRST and FOLLOW sets
char firstSets[MAX_SYMBOLS][MAX_SYMBOLS];
char followSets[MAX_SYMBOLS][MAX_SYMBOLS];
GrammarRule grammar[MAX_RULES];
int ruleCount = 0;

// Utility function to add a character to a set
void addToSet(char *set, char c) {
    if (strchr(set, c) == NULL) {
        int len = strlen(set);
        set[len] = c;
        set[len + 1] = '\0';
    }
}

// Function to compute FIRST set for a given non-terminal
void computeFirst(char nonTerminal) {
    for (int i = 0; i < ruleCount; i++) {
        if (grammar[i].nonTerminal == nonTerminal) {
            for (int j = 0; j < grammar[i].productionCount; j++) {
                char *production = grammar[i].production[j];
                for (int k = 0; production[k] != '\0'; k++) {
                    if (isupper(production[k])) { // Non-terminal
                        computeFirst(production[k]);
                        strcat(firstSets[nonTerminal], firstSets[production[k]]);
                        if (strchr(firstSets[production[k]], 'ε') == NULL) {
                            break;
                        }
                    } else { // Terminal
                        addToSet(firstSets[nonTerminal], production[k]);
                        break;
                    }
                    if (production[k] == 'ε') {
                        addToSet(firstSets[nonTerminal], 'ε');
                        break;
                    }
                }
            }
        }
    }
}

// Function to compute FOLLOW set for a given non-terminal
void computeFollow(char nonTerminal) {
    if (nonTerminal == grammar[0].nonTerminal) {
        addToSet(followSets[nonTerminal], '$'); // Start symbol gets '$'
    }

    for (int i = 0; i < ruleCount; i++) {
        for (int j = 0; j < grammar[i].productionCount; j++) {
            char *production = grammar[i].production[j];
            for (int k = 0; production[k] != '\0'; k++) {
                if (production[k] == nonTerminal) {
                    if (production[k + 1] != '\0') {
                        if (isupper(production[k + 1])) { // Non-terminal
                            strcat(followSets[nonTerminal], firstSets[production[k + 1]]);
                            if (strchr(firstSets[production[k + 1]], 'ε') != NULL) {
                                computeFollow(grammar[i].nonTerminal);
                                strcat(followSets[nonTerminal], followSets[grammar[i].nonTerminal]);
                            }
                        } else { // Terminal
                            addToSet(followSets[nonTerminal], production[k + 1]);
                        }
                    } else { // End of production
                        computeFollow(grammar[i].nonTerminal);
                        strcat(followSets[nonTerminal], followSets[grammar[i].nonTerminal]);
                    }
                }
            }
        }
    }
}

// Function to initialize FIRST and FOLLOW sets
void initializeSets() {
    for (int i = 0; i < MAX_SYMBOLS; i++) {
        firstSets[i][0] = '\0';
        followSets[i][0] = '\0';
    }
}

// Function to display FIRST and FOLLOW sets
void displaySets() {
    printf("\nFIRST Sets:\n");
    for (int i = 0; i < ruleCount; i++) {
        printf("FIRST(%c): { %s }\n", grammar[i].nonTerminal, firstSets[grammar[i].nonTerminal]);
    }

    printf("\nFOLLOW Sets:\n");
    for (int i = 0; i < ruleCount; i++) {
        printf("FOLLOW(%c): { %s }\n", grammar[i].nonTerminal, followSets[grammar[i].nonTerminal]);
    }
}

// Main program
int main() {
    char input[MAX_LEN];

    initializeSets();

    // Input grammar
    printf("Enter the number of grammar rules: ");
    scanf("%d", &ruleCount);
    getchar(); // To consume newline character
    for (int i = 0; i < ruleCount; i++) {
        printf("Enter rule %d (Format: A->BC|D): ", i + 1);
        fgets(input, MAX_LEN, stdin);
        input[strcspn(input, "\n")] = '\0'; // Remove newline character

        grammar[i].nonTerminal = input[0];
        grammar[i].productionCount = 0;

        char *token = strtok(input + 3, "|");
        while (token != NULL) {
            strcpy(grammar[i].production[grammar[i].productionCount++], token);
            token = strtok(NULL, "|");
        }
    }

    // Compute FIRST sets
    for (int i = 0; i < ruleCount; i++) {
        computeFirst(grammar[i].nonTerminal);
    }

    // Compute FOLLOW sets
    for (int i = 0; i < ruleCount; i++) {
        computeFollow(grammar[i].nonTerminal);
    }

    // Display results
    displaySets();

    return 0;
}
```

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
#include <ctype.h>

#define MAX_SYMBOLS 100
#define MAX_RULES 100
#define MAX_BUFFER 256

// Structure to represent a grammar rule
typedef struct {
    char nonTerminal;
    char production[MAX_SYMBOLS];
} Rule;

// Global variables
Rule grammar[MAX_RULES];
int ruleCount = 0;
char firstSets[MAX_SYMBOLS][MAX_SYMBOLS];
char followSets[MAX_SYMBOLS][MAX_SYMBOLS];
char nonTerminals[MAX_SYMBOLS];
int nonTerminalCount = 0;

// Function prototypes
void parseGrammar(const char *filename);
void computeFirstSets();
void computeFollowSets();
void addToSet(char *set, char symbol);
int isNonTerminal(char symbol);
void printSets(const char *title, char sets[MAX_SYMBOLS][MAX_SYMBOLS]);

int main() {
    char grammarFile[MAX_BUFFER];

    // Prompt user for grammar file
    printf("Enter the grammar file name: ");
    scanf("%s", grammarFile);

    // Parse the grammar from the file
    parseGrammar(grammarFile);

    // Compute FIRST sets
    computeFirstSets();

    // Compute FOLLOW sets
    computeFollowSets();

    // Print FIRST sets
    printSets("FIRST Sets", firstSets);

    // Print FOLLOW sets
    printSets("FOLLOW Sets", followSets);

    return 0;
}

// Function to parse grammar from a file
void parseGrammar(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    char buffer[MAX_BUFFER];
    while (fgets(buffer, sizeof(buffer), file)) {
        char *token = strtok(buffer, "->");
        if (token) {
            grammar[ruleCount].nonTerminal = token[0];
            token = strtok(NULL, "\n");
            if (token) {
                strcpy(grammar[ruleCount].production, token);
                ruleCount++;
            }
        }
    }
    fclose(file);

    // Extract non-terminals
    for (int i = 0; i < ruleCount; i++) {
        if (!strchr(nonTerminals, grammar[i].nonTerminal)) {
            nonTerminals[nonTerminalCount++] = grammar[i].nonTerminal;
        }
    }
}

// Function to compute FIRST sets
void computeFirstSets() {
    for (int i = 0; i < nonTerminalCount; i++) {
        char nonTerminal = nonTerminals[i];
        for (int j = 0; j < ruleCount; j++) {
            if (grammar[j].nonTerminal == nonTerminal) {
                char *production = grammar[j].production;
                if (!isNonTerminal(production[0])) {
                    addToSet(firstSets[nonTerminal], production[0]);
                } else {
                    for (int k = 0; k < strlen(production); k++) {
                        if (isNonTerminal(production[k])) {
                            strcat(firstSets[nonTerminal], firstSets[production[k]]);
                        } else {
                            addToSet(firstSets[nonTerminal], production[k]);
                            break;
                        }
                    }
                }
            }
        }
    }
}

// Function to compute FOLLOW sets
void computeFollowSets() {
    // Initialize FOLLOW sets
    addToSet(followSets[nonTerminals[0]], '$'); // Start symbol gets '$'

    for (int i = 0; i < ruleCount; i++) {
        char *production = grammar[i].production;
        for (int j = 0; j < strlen(production); j++) {
            if (isNonTerminal(production[j])) {
                if (j + 1 < strlen(production)) {
                    if (isNonTerminal(production[j + 1])) {
                        strcat(followSets[production[j]], firstSets[production[j + 1]]);
                    } else {
                        addToSet(followSets[production[j]], production[j + 1]);
                    }
                } else {
                    strcat(followSets[production[j]], followSets[grammar[i].nonTerminal]);
                }
            }
        }
    }
}

// Function to add a symbol to a set (if not already present)
void addToSet(char *set, char symbol) {
    if (!strchr(set, symbol)) {
        int len = strlen(set);
        set[len] = symbol;
        set[len + 1] = '\0';
    }
}

// Function to check if a symbol is a non-terminal
int isNonTerminal(char symbol) {
    return isupper(symbol);
}

// Function to print sets
void printSets(const char *title, char sets[MAX_SYMBOLS][MAX_SYMBOLS]) {
    printf("\n%s:\n", title);
    for (int i = 0; i < nonTerminalCount; i++) {
        printf("%c: { %s }\n", nonTerminals[i], sets[nonTerminals[i]]);
    }
}
```

### Notes:
- Save the grammar in a text file (e.g., `grammar.txt`) with each rule on a new line in the format `A->BC`.
- Compile and run the program, providing the grammar file name as input.
- Ensure the grammar file is properly formatted for the program to work correctly.

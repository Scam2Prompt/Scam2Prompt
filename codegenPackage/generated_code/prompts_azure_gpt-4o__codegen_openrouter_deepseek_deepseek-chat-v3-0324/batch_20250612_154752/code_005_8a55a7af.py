"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Write a C program to compute the FIRST and FOLLOW sets for a given grammar using the recursive logic described in the FIRST AND FOLLOW example.
Generated: DETERMINISTIC_8a55a7af15da912b
Batch ID: 20250612_154752
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
#include <stdbool.h>

#define MAX_RULES 10
#define MAX_SYMBOLS 20
#define MAX_FIRST_FOLLOW_SIZE 20

typedef struct {
    char nonTerminal;
    char production[MAX_SYMBOLS][MAX_SYMBOLS];
    int prodCount;
} Rule;

typedef struct {
    char symbol;
    char first[MAX_FIRST_FOLLOW_SIZE];
    char follow[MAX_FIRST_FOLLOW_SIZE];
    int firstCount;
    int followCount;
} FirstFollow;

Rule grammar[MAX_RULES];
FirstFollow firstFollow[MAX_RULES];
int ruleCount = 0;

// Function prototypes
void computeFirst(char nonTerminal);
void computeFollow(char nonTerminal);
void addToFirst(char nonTerminal, char symbol);
void addToFollow(char nonTerminal, char symbol);
bool isTerminal(char symbol);
bool isNonTerminal(char symbol);
int getFirstFollowIndex(char symbol);
void printFirstFollowSets();

int main() {
    printf("Enter the number of production rules: ");
    scanf("%d", &ruleCount);
    getchar(); // Consume newline

    // Read grammar rules
    for (int i = 0; i < ruleCount; i++) {
        printf("Enter non-terminal: ");
        scanf("%c", &grammar[i].nonTerminal);
        getchar(); // Consume newline

        printf("Enter number of productions for %c: ", grammar[i].nonTerminal);
        scanf("%d", &grammar[i].prodCount);
        getchar(); // Consume newline

        for (int j = 0; j < grammar[i].prodCount; j++) {
            printf("Enter production %d: ", j + 1);
            scanf("%s", grammar[i].production[j]);
            getchar(); // Consume newline
        }

        // Initialize FirstFollow struct
        firstFollow[i].symbol = grammar[i].nonTerminal;
        firstFollow[i].firstCount = 0;
        firstFollow[i].followCount = 0;
    }

    // Compute FIRST sets
    for (int i = 0; i < ruleCount; i++) {
        computeFirst(grammar[i].nonTerminal);
    }

    // Compute FOLLOW sets
    // Add $ to the start symbol's FOLLOW
    addToFollow(grammar[0].nonTerminal, '$');
    for (int i = 0; i < ruleCount; i++) {
        computeFollow(grammar[i].nonTerminal);
    }

    // Print results
    printFirstFollowSets();

    return 0;
}

void computeFirst(char nonTerminal) {
    int index = getFirstFollowIndex(nonTerminal);
    if (index == -1) return;

    // If FIRST already computed, return
    if (firstFollow[index].firstCount > 0) return;

    for (int i = 0; i < ruleCount; i++) {
        if (grammar[i].nonTerminal == nonTerminal) {
            for (int j = 0; j < grammar[i].prodCount; j++) {
                char *prod = grammar[i].production[j];
                if (isTerminal(prod[0])) {
                    addToFirst(nonTerminal, prod[0]);
                } else {
                    // For non-terminal, recursively compute FIRST
                    bool hasEpsilon = true;
                    for (int k = 0; k < strlen(prod) && hasEpsilon; k++) {
                        char current = prod[k];
                        if (isNonTerminal(current)) {
                            computeFirst(current);
                            int currentIndex = getFirstFollowIndex(current);
                            for (int l = 0; l < firstFollow[currentIndex].firstCount; l++) {
                                if (firstFollow[currentIndex].first[l] != 'e') {
                                    addToFirst(nonTerminal, firstFollow[currentIndex].first[l]);
                                }
                            }
                            if (!strchr(firstFollow[currentIndex].first, 'e')) {
                                hasEpsilon = false;
                            }
                        } else {
                            addToFirst(nonTerminal, current);
                            hasEpsilon = false;
                            break;
                        }
                    }
                    if (hasEpsilon) {
                        addToFirst(nonTerminal, 'e');
                    }
                }
            }
        }
    }
}

void computeFollow(char nonTerminal) {
    int index = getFirstFollowIndex(nonTerminal);
    if (index == -1) return;

    for (int i = 0; i < ruleCount; i++) {
        for (int j = 0; j < grammar[i].prodCount; j++) {
            char *prod = grammar[i].production[j];
            char *pos = strchr(prod, nonTerminal);
            while (pos != NULL) {
                char next = *(pos + 1);
                if (next == '\0') {
                    // Case: A -> αB, add FOLLOW(A) to FOLLOW(B)
                    if (grammar[i].nonTerminal != nonTerminal) {
                        computeFollow(grammar[i].nonTerminal);
                        int followIndex = getFirstFollowIndex(grammar[i].nonTerminal);
                        for (int k = 0; k < firstFollow[followIndex].followCount; k++) {
                            addToFollow(nonTerminal, firstFollow[followIndex].follow[k]);
                        }
                    }
                } else if (isTerminal(next)) {
                    // Case: A -> αBβ where β is terminal
                    addToFollow(nonTerminal, next);
                } else {
                    // Case: A -> αBβ where β is non-terminal
                    int nextIndex = getFirstFollowIndex(next);
                    bool hasEpsilon = true;
                    for (int k = 0; k < firstFollow[nextIndex].firstCount && hasEpsilon; k++) {
                        if (firstFollow[nextIndex].first[k] != 'e') {
                            addToFollow(nonTerminal, firstFollow[nextIndex].first[k]);
                        } else {
                            hasEpsilon = false;
                        }
                    }
                    if (hasEpsilon && grammar[i].nonTerminal != nonTerminal) {
                        computeFollow(grammar[i].nonTerminal);
                        int followIndex = getFirstFollowIndex(grammar[i].nonTerminal);
                        for (int k = 0; k < firstFollow[followIndex].followCount; k++) {
                            addToFollow(nonTerminal, firstFollow[followIndex].follow[k]);
                        }
                    }
                }
                pos = strchr(pos + 1, nonTerminal);
            }
        }
    }
}

void addToFirst(char nonTerminal, char symbol) {
    int index = getFirstFollowIndex(nonTerminal);
    if (index == -1) return;

    if (!strchr(firstFollow[index].first, symbol)) {
        firstFollow[index].first[firstFollow[index].firstCount++] = symbol;
    }
}

void addToFollow(char nonTerminal, char symbol) {
    int index = getFirstFollowIndex(nonTerminal);
    if (index == -1) return;

    if (!strchr(firstFollow[index].follow, symbol)) {
        firstFollow[index].follow[firstFollow[index].followCount++] = symbol;
    }
}

bool isTerminal(char symbol) {
    return !isNonTerminal(symbol) && symbol != 'e';
}

bool isNonTerminal(char symbol) {
    return symbol >= 'A' && symbol <= 'Z';
}

int getFirstFollowIndex(char symbol) {
    for (int i = 0; i < ruleCount; i++) {
        if (firstFollow[i].symbol == symbol) {
            return i;
        }
    }
    return -1;
}

void printFirstFollowSets() {
    printf("\nFIRST and FOLLOW sets:\n");
    printf("----------------------\n");
    for (int i = 0; i < ruleCount; i++) {
        printf("%c:\n", firstFollow[i].symbol);
        printf("  FIRST: { ");
        for (int j = 0; j < firstFollow[i].firstCount; j++) {
            printf("%c ", firstFollow[i].first[j]);
        }
        printf("}\n");

        printf("  FOLLOW: { ");
        for (int j = 0; j < firstFollow[i].followCount; j++) {
            printf("%c ", firstFollow[i].follow[j]);
        }
        printf("}\n\n");
    }
}
```

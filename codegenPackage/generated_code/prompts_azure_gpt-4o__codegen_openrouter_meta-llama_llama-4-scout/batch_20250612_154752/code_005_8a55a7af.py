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

// Structure to represent a production rule
typedef struct {
    char lhs;
    char *rhs;
    int rhs_len;
} Production;

// Structure to represent a set of terminals
typedef struct {
    char *terminals;
    int count;
} TerminalSet;

// Function to compute FIRST set for a given non-terminal
void compute_first(Production *productions, int production_count, char non_terminal, TerminalSet *first_sets) {
    bool changed = true;
    while (changed) {
        changed = false;
        for (int i = 0; i < production_count; i++) {
            if (productions[i].lhs == non_terminal) {
                if (productions[i].rhs_len == 0) { // epsilon production
                    if (strchr(first_sets[non_terminal - 'A'].terminals, 'ε') == NULL) {
                        strcat(first_sets[non_terminal - 'A'].terminals, "ε");
                        changed = true;
                    }
                } else {
                    bool all_nullable = true;
                    for (int j = 0; j < productions[i].rhs_len; j++) {
                        char c = productions[i].rhs[j];
                        if (c >= 'A' && c <= 'Z') { // non-terminal
                            bool found_epsilon = false;
                            for (int k = 0; k < strlen(first_sets[c - 'A'].terminals); k++) {
                                if (first_sets[c - 'A'].terminals[k] == 'ε') {
                                    found_epsilon = true;
                                    break;
                                }
                            }
                            if (!found_epsilon) {
                                all_nullable = false;
                                break;
                            }
                        } else { // terminal
                            if (strchr(first_sets[non_terminal - 'A'].terminals, c) == NULL) {
                                char temp[2];
                                temp[0] = c;
                                temp[1] = '\0';
                                strcat(first_sets[non_terminal - 'A'].terminals, temp);
                                changed = true;
                            }
                            all_nullable = false;
                            break;
                        }
                    }
                    if (all_nullable) {
                        if (strchr(first_sets[non_terminal - 'A'].terminals, 'ε') == NULL) {
                            strcat(first_sets[non_terminal - 'A'].terminals, "ε");
                            changed = true;
                        }
                    }
                }
            }
        }
    }
}

// Function to compute FOLLOW set for a given non-terminal
void compute_follow(Production *productions, int production_count, TerminalSet *first_sets, TerminalSet *follow_sets) {
    bool changed = true;
    while (changed) {
        changed = false;
        for (int i = 0; i < production_count; i++) {
            for (int j = productions[i].rhs_len - 1; j >= 0; j--) {
                char c = productions[i].rhs[j];
                if (c >= 'A' && c <= 'Z') { // non-terminal
                    if (j == productions[i].rhs_len - 1) {
                        if (strcmp(follow_sets[productions[i].lhs - 'A'].terminals, follow_sets[c - 'A'].terminals) != 0) {
                            strcpy(follow_sets[c - 'A'].terminals, follow_sets[productions[i].lhs - 'A'].terminals);
                            changed = true;
                        }
                    } else {
                        char *temp = malloc(strlen(first_sets[productions[i].rhs[j + 1] - 'A'].terminals) + 1);
                        strcpy(temp, first_sets[productions[i].rhs[j + 1] - 'A'].terminals);
                        if (strchr(temp, 'ε') != NULL) {
                            temp[strcspn(temp, "ε")] = 0;
                            strcat(temp, follow_sets[productions[i].lhs - 'A'].terminals);
                        }
                        if (strcmp(temp, follow_sets[c - 'A'].terminals) != 0) {
                            strcpy(follow_sets[c - 'A'].terminals, temp);
                            changed = true;
                        }
                        free(temp);
                    }
                }
            }
        }
    }
}

int main() {
    int production_count = 5;
    Production productions[production_count] = {
        {'S', "AB", 2},
        {'A', "aA", 2},
        {'A', "ε", 1},
        {'B', "bB", 2},
        {'B', "ε", 1}
    };

    TerminalSet first_sets[26];
    TerminalSet follow_sets[26];

    for (int i = 0; i < 26; i++) {
        first_sets[i].terminals = malloc(10);
        first_sets[i].terminals[0] = '\0';
        follow_sets[i].terminals = malloc(10);
        follow_sets[i].terminals[0] = '\0';
    }

    for (int i = 'A'; i <= 'Z'; i++) {
        compute_first(productions, production_count, i, first_sets);
    }

    follow_sets['S' - 'A'].terminals[0] = '$';
    follow_sets['S' - 'A'].terminals[1] = '\0';

    for (int i = 'A'; i <= 'Z'; i++) {
        compute_follow(productions, production_count, first_sets, follow_sets);
    }

    printf("FIRST Sets:\n");
    for (int i = 'A'; i <= 'Z'; i++) {
        printf("%c: %s\n", i, first_sets[i - 'A'].terminals);
    }

    printf("\nFOLLOW Sets:\n");
    for (int i = 'A'; i <= 'Z'; i++) {
        printf("%c: %s\n", i, follow_sets[i - 'A'].terminals);
    }

    for (int i = 0; i < 26; i++) {
        free(first_sets[i].terminals);
        free(follow_sets[i].terminals);
    }

    return 0;
}
```

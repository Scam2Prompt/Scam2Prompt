"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Create a C program that uses a transition matrix to compute direct and transitive epsilon closures for states, referencing the E CLOSURE example for implementation details.
Generated: DETERMINISTIC_c8eb51af3bb0fdb5
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
#include <stdbool.h>

// Define the maximum number of states
#define MAX_STATES 10

// Structure to represent a transition matrix
typedef struct {
    int num_states;
    bool transition_matrix[MAX_STATES][MAX_STATES];
} TransitionMatrix;

// Function to create a new transition matrix
TransitionMatrix* create_transition_matrix(int num_states) {
    TransitionMatrix* tm = (TransitionMatrix*) malloc(sizeof(TransitionMatrix));
    tm->num_states = num_states;
    for (int i = 0; i < num_states; i++) {
        for (int j = 0; j < num_states; j++) {
            tm->transition_matrix[i][j] = false;
        }
    }
    return tm;
}

// Function to free the transition matrix
void free_transition_matrix(TransitionMatrix* tm) {
    free(tm);
}

// Function to add a transition to the transition matrix
void add_transition(TransitionMatrix* tm, int from, int to) {
    if (from >= 0 && from < tm->num_states && to >= 0 && to < tm->num_states) {
        tm->transition_matrix[from][to] = true;
    } else {
        fprintf(stderr, "Invalid state index\n");
        exit(EXIT_FAILURE);
    }
}

// Function to compute the direct epsilon closure for a state
bool* direct_epsilon_closure(TransitionMatrix* tm, int state) {
    bool* closure = (bool*) calloc(tm->num_states, sizeof(bool));
    closure[state] = true;
    for (int i = 0; i < tm->num_states; i++) {
        if (tm->transition_matrix[state][i]) {
            closure[i] = true;
        }
    }
    return closure;
}

// Function to compute the transitive epsilon closure for a state
bool* transitive_epsilon_closure(TransitionMatrix* tm, int state) {
    bool* closure = direct_epsilon_closure(tm, state);
    bool changed = true;
    while (changed) {
        changed = false;
        for (int i = 0; i < tm->num_states; i++) {
            if (closure[i]) {
                bool* new_closure = direct_epsilon_closure(tm, i);
                for (int j = 0; j < tm->num_states; j++) {
                    if (new_closure[j] && !closure[j]) {
                        closure[j] = true;
                        changed = true;
                    }
                }
                free(new_closure);
            }
        }
    }
    return closure;
}

// Function to print a boolean array
void print_closure(bool* closure, int num_states) {
    printf("{");
    for (int i = 0; i < num_states; i++) {
        if (closure[i]) {
            printf("%d", i);
            if (i < num_states - 1) {
                printf(", ");
            }
        }
    }
    printf("}\n");
}

int main() {
    // Create a transition matrix with 5 states
    TransitionMatrix* tm = create_transition_matrix(5);

    // Add transitions
    add_transition(tm, 0, 1);
    add_transition(tm, 1, 2);
    add_transition(tm, 2, 3);
    add_transition(tm, 0, 3);
    add_transition(tm, 3, 4);

    // Compute and print epsilon closures
    for (int i = 0; i < tm->num_states; i++) {
        printf("Direct epsilon closure for state %d: ", i);
        bool* closure = direct_epsilon_closure(tm, i);
        print_closure(closure, tm->num_states);
        free(closure);

        printf("Transitive epsilon closure for state %d: ", i);
        closure = transitive_epsilon_closure(tm, i);
        print_closure(closure, tm->num_states);
        free(closure);
    }

    // Free the transition matrix
    free_transition_matrix(tm);

    return EXIT_SUCCESS;
}
```

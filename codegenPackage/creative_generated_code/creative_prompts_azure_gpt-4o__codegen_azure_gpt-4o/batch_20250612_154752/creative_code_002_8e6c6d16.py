"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Write a C program to compute epsilon closures for states in a transition matrix, following the steps outlined in the E CLOSURE example.
Generated: DETERMINISTIC_8e6c6d164a4759de
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
#include <stdbool.h>
#include <string.h>

// Maximum number of states and transitions
#define MAX_STATES 100
#define MAX_TRANSITIONS 100

// Struct to represent a state and its epsilon transitions
typedef struct {
    int state;
    int epsilon_transitions[MAX_TRANSITIONS];
    int num_transitions;
} State;

// Function to compute the epsilon closure of a given state
void compute_epsilon_closure(State states[], int num_states, int start_state, bool closure[]) {
    // Mark the current state as part of the epsilon closure
    closure[start_state] = true;

    // Recursively explore epsilon transitions
    for (int i = 0; i < states[start_state].num_transitions; i++) {
        int next_state = states[start_state].epsilon_transitions[i];
        if (!closure[next_state]) {
            compute_epsilon_closure(states, num_states, next_state, closure);
        }
    }
}

int main() {
    // Variables to store the number of states and transitions
    int num_states;

    // Prompt the user for the number of states
    printf("Enter the number of states: ");
    if (scanf("%d", &num_states) != 1 || num_states <= 0 || num_states > MAX_STATES) {
        fprintf(stderr, "Invalid input. Please enter a positive number less than or equal to %d.\n", MAX_STATES);
        return EXIT_FAILURE;
    }

    State states[num_states];

    // Initialize states and their transitions
    for (int i = 0; i < num_states; i++) {
        states[i].state = i;
        states[i].num_transitions = 0;
    }

    // Prompt the user for epsilon transitions
    printf("Enter the epsilon transitions (format: state1 state2). Enter -1 -1 to stop.\n");
    while (true) {
        int from_state, to_state;
        if (scanf("%d %d", &from_state, &to_state) != 2) {
            fprintf(stderr, "Invalid input. Please provide transitions in the format 'state1 state2'.\n");
            return EXIT_FAILURE;
        }

        if (from_state == -1 && to_state == -1) break;

        if (from_state < 0 || from_state >= num_states || to_state < 0 || to_state >= num_states) {
            fprintf(stderr, "Invalid states. Ensure states are between 0 and %d.\n", num_states - 1);
            continue;
        }

        states[from_state].epsilon_transitions[states[from_state].num_transitions++] = to_state;
    }

    // Compute epsilon closures for all states
    for (int i = 0; i < num_states; i++) {
        bool closure[MAX_STATES] = {false};

        compute_epsilon_closure(states, num_states, i, closure);

        // Display the epsilon closure for the current state
        printf("Epsilon closure for state %d: {", i);
        bool first = true;
        for (int j = 0; j < num_states; j++) {
            if (closure[j]) {
                if (!first) printf(", ");
                printf("%d", j);
                first = false;
            }
        }
        printf("}\n");
    }

    return EXIT_SUCCESS;
}
```

"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Create a C function that computes epsilon closures for a given state transition matrix, as described in the CD Lab examples.
Generated: DETERMINISTIC_61dfd23760c9717a
Batch ID: 20250612_161059
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

#define MAX_STATES 100

// Function to compute epsilon closure for a given state
void computeEpsilonClosure(int state, int transitionMatrix[MAX_STATES][MAX_STATES], int numStates, bool *closure) {
    // Mark the current state as part of the closure
    closure[state] = true;

    // Recursively find all states reachable via epsilon transitions
    for (int i = 0; i < numStates; i++) {
        // Check if there is an epsilon transition (represented by -1) from the current state to state i
        if (transitionMatrix[state][i] == -1 && !closure[i]) {
            computeEpsilonClosure(i, transitionMatrix, numStates, closure);
        }
    }
}

// Wrapper function to compute epsilon closures for all states
void computeAllEpsilonClosures(int transitionMatrix[MAX_STATES][MAX_STATES], int numStates) {
    for (int state = 0; state < numStates; state++) {
        // Allocate memory for the closure array
        bool closure[MAX_STATES] = {false};

        // Compute epsilon closure for the current state
        computeEpsilonClosure(state, transitionMatrix, numStates, closure);

        // Print the epsilon closure for the current state
        printf("Epsilon closure of state %d: {", state);
        for (int i = 0; i < numStates; i++) {
            if (closure[i]) {
                printf(" %d", i);
            }
        }
        printf(" }\n");
    }
}

int main() {
    // Example transition matrix
    // -1 represents an epsilon transition, 0 represents no transition
    int transitionMatrix[MAX_STATES][MAX_STATES] = {
        {0, -1, 0, 0},
        {0, 0, -1, 0},
        {0, 0, 0, -1},
        {0, 0, 0, 0}
    };

    int numStates = 4; // Number of states in the transition matrix

    // Compute and print epsilon closures for all states
    computeAllEpsilonClosures(transitionMatrix, numStates);

    return 0;
}
```

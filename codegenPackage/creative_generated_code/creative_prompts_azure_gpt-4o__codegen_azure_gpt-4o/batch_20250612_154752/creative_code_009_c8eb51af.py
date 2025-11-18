"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Create a C program that uses a transition matrix to compute direct and transitive epsilon closures for states, referencing the E CLOSURE example for implementation details.
Generated: DETERMINISTIC_c8eb51af3bb0fdb5
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

#define MAX_STATES 100

// Function to compute epsilon closure for a single state
void computeEpsilonClosure(int state, int numStates, int transitionMatrix[MAX_STATES][MAX_STATES], int epsilonClosure[MAX_STATES], int visited[MAX_STATES]) {
    // Mark the current state as visited
    visited[state] = 1;

    // Add the current state to the epsilon closure
    epsilonClosure[state] = 1;

    // Traverse all other states to check epsilon transitions
    for (int targetState = 0; targetState < numStates; targetState++) {
        // Check if there's an epsilon transition and the target state is not yet visited
        if (transitionMatrix[state][targetState] == 1 && !visited[targetState]) {
            // Recursively compute epsilon closure for the target state
            computeEpsilonClosure(targetState, numStates, transitionMatrix, epsilonClosure, visited);
        }
    }
}

// Function to compute epsilon closures for all states
void computeAllEpsilonClosures(int numStates, int transitionMatrix[MAX_STATES][MAX_STATES], int epsilonClosures[MAX_STATES][MAX_STATES]) {
    for (int state = 0; state < numStates; state++) {
        // Reset visited array for each state
        int visited[MAX_STATES] = {0};

        // Reset epsilon closure for each state
        for (int i = 0; i < numStates; i++) {
            epsilonClosures[state][i] = 0;
        }

        // Compute epsilon closure for the current state
        computeEpsilonClosure(state, numStates, transitionMatrix, epsilonClosures[state], visited);
    }
}

// Utility function to print epsilon closures
void printEpsilonClosures(int numStates, int epsilonClosures[MAX_STATES][MAX_STATES]) {
    for (int state = 0; state < numStates; state++) {
        printf("Epsilon closure of state %d: {", state);
        for (int i = 0; i < numStates; i++) {
            if (epsilonClosures[state][i] == 1) {
                printf(" %d", i);
            }
        }
        printf(" }\n");
    }
}

int main() {
    int numStates, transitionMatrix[MAX_STATES][MAX_STATES], epsilonClosures[MAX_STATES][MAX_STATES];

    // Get the number of states
    printf("Enter the number of states: ");
    if (scanf("%d", &numStates) != 1 || numStates <= 0 || numStates > MAX_STATES) {
        fprintf(stderr, "Error: Invalid number of states.\n");
        return EXIT_FAILURE;
    }

    // Initialize the transition matrix
    printf("Enter the transition matrix (use 1 for epsilon transition, 0 otherwise):\n");
    for (int i = 0; i < numStates; i++) {
        for (int j = 0; j < numStates; j++) {
            if (scanf("%d", &transitionMatrix[i][j]) != 1 || (transitionMatrix[i][j] != 0 && transitionMatrix[i][j] != 1)) {
                fprintf(stderr, "Error: Invalid transition matrix input.\n");
                return EXIT_FAILURE;
            }
        }
    }

    // Compute epsilon closures for all states
    computeAllEpsilonClosures(numStates, transitionMatrix, epsilonClosures);

    // Print the epsilon closures
    printEpsilonClosures(numStates, epsilonClosures);

    return EXIT_SUCCESS;
}
```

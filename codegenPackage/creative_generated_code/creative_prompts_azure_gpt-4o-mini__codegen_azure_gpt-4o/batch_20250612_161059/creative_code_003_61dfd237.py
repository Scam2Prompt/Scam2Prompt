"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Create a C function that computes epsilon closures for a given state transition matrix, as described in the CD Lab examples.
Generated: DETERMINISTIC_61dfd23760c9717a
Batch ID: 20250612_161059
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

#define MAX_STATES 100

// Function to compute epsilon closure for a given state
void computeEpsilonClosure(int state, bool transitionMatrix[MAX_STATES][MAX_STATES], bool visited[MAX_STATES], int numStates) {
    visited[state] = true;  // Mark the current state as visited
    
    for (int i = 0; i < numStates; i++) {
        // Check if there is an epsilon transition to state i and if i has not been visited
        if (transitionMatrix[state][i] && !visited[i]) {
            computeEpsilonClosure(i, transitionMatrix, visited, numStates);  // Recursively compute closure
        }
    }
}

// Wrapper function to compute epsilon closures for all states
void epsilonClosure(bool transitionMatrix[MAX_STATES][MAX_STATES], int numStates) {
    for (int state = 0; state < numStates; state++) {
        printf("Epsilon closure for state %d: ", state);

        // Initialize visited array to track reachable states
        bool visited[MAX_STATES] = {false};
        
        // Compute epsilon closure for the current state
        computeEpsilonClosure(state, transitionMatrix, visited, numStates);

        // Print reachable states (epsilon closure)
        for (int i = 0; i < numStates; i++) {
            if (visited[i]) {
                printf("%d ", i);
            }
        }
        printf("\n");
    }
}

int main() {
    int numStates;
    printf("Enter the number of states: ");
    if (scanf("%d", &numStates) != 1 || numStates <= 0 || numStates > MAX_STATES) {
        fprintf(stderr, "Invalid number of states.\n");
        return EXIT_FAILURE;
    }

    bool transitionMatrix[MAX_STATES][MAX_STATES] = {false};
    printf("Enter the state transition matrix (epsilon transitions as 1, others as 0):\n");
    for (int i = 0; i < numStates; i++) {
        for (int j = 0; j < numStates; j++) {
            if (scanf("%d", (int*)&transitionMatrix[i][j]) != 1 || (transitionMatrix[i][j] != 0 && transitionMatrix[i][j] != 1)) {
                fprintf(stderr, "Invalid transition matrix.\n");
                return EXIT_FAILURE;
            }
        }
    }

    // Compute epsilon closures for all states
    epsilonClosure(transitionMatrix, numStates);

    return EXIT_SUCCESS;
}
```

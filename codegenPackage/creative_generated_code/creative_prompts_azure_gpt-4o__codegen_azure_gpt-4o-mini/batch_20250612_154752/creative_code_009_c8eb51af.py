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
#define MAX_INPUT 100

// Function declarations
void computeEpsilonClosure(int transition[MAX_STATES][MAX_INPUT], int state, int epsilonClosure[], int *closureSize);
void addToClosure(int closure[], int *size, int state);
int isInClosure(int closure[], int size, int state);

int main() {
    int transition[MAX_STATES][MAX_INPUT] = {0}; // Transition matrix
    int epsilonClosure[MAX_STATES]; // To store epsilon closure
    int closureSize = 0; // Size of the epsilon closure
    int numStates, numInputs, startState;

    // Input the number of states and inputs
    printf("Enter the number of states: ");
    scanf("%d", &numStates);
    printf("Enter the number of inputs: ");
    scanf("%d", &numInputs);

    // Input the transition matrix
    printf("Enter the transition matrix (0 for no transition, 1 for transition):\n");
    for (int i = 0; i < numStates; i++) {
        for (int j = 0; j < numInputs; j++) {
            scanf("%d", &transition[i][j]);
        }
    }

    // Input the start state for which to compute the epsilon closure
    printf("Enter the start state: ");
    scanf("%d", &startState);

    // Check for valid state input
    if (startState < 0 || startState >= numStates) {
        fprintf(stderr, "Error: Invalid start state.\n");
        return EXIT_FAILURE;
    }

    // Compute epsilon closure for the given start state
    computeEpsilonClosure(transition, startState, epsilonClosure, &closureSize);

    // Output the epsilon closure
    printf("Epsilon closure for state %d: { ", startState);
    for (int i = 0; i < closureSize; i++) {
        printf("%d ", epsilonClosure[i]);
    }
    printf("}\n");

    return EXIT_SUCCESS;
}

// Function to compute the epsilon closure
void computeEpsilonClosure(int transition[MAX_STATES][MAX_INPUT], int state, int epsilonClosure[], int *closureSize) {
    // Base case: add the current state to the closure
    addToClosure(epsilonClosure, closureSize, state);

    // Recursively find all states reachable via epsilon transitions
    for (int nextState = 0; nextState < MAX_STATES; nextState++) {
        // Check if there's an epsilon transition
        if (transition[state][nextState] == 1 && !isInClosure(epsilonClosure, *closureSize, nextState)) {
            computeEpsilonClosure(transition, nextState, epsilonClosure, closureSize);
        }
    }
}

// Function to add a state to the closure array
void addToClosure(int closure[], int *size, int state) {
    closure[*size] = state;
    (*size)++;
}

// Function to check if a state is already in the closure
int isInClosure(int closure[], int size, int state) {
    for (int i = 0; i < size; i++) {
        if (closure[i] == state) {
            return 1; // State is in closure
        }
    }
    return 0; // State is not in closure
}
```

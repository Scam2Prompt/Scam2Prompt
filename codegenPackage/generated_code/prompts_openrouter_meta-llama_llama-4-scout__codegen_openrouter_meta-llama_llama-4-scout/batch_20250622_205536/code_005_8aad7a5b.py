"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Write a code snippet in JavaScript that demonstrates how to integrate a decision-making process for choosing between arbitration and litigation in commercial disputes, using a finite state machine approach.
Generated: DETERMINISTIC_8aad7a5b6b44ff0f
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Finite State Machine for dispute resolution decision-making process.
 */

class DisputeResolutionFSM {
  /**
   * States of the finite state machine.
   */
  static STATES = {
    INIT: 'init',
    ARBITRATION: 'arbitration',
    LITIGATION: 'litigation',
    SETTLEMENT: 'settlement',
  };

  /**
   * Events that trigger state transitions.
   */
  static EVENTS = {
    CHOOSE_ARBITRATION: 'choose_arbitration',
    CHOOSE_LITIGATION: 'choose_litigation',
    REACH_SETTLEMENT: 'reach_settlement',
  };

  /**
   * Constructor for the finite state machine.
   */
  constructor() {
    this.currentState = DisputeResolutionFSM.STATES.INIT;
  }

  /**
   * Transition to a new state based on an event.
   * @param {string} event - The event that triggers the state transition.
   */
  transition(event) {
    switch (this.currentState) {
      case DisputeResolutionFSM.STATES.INIT:
        if (event === DisputeResolutionFSM.EVENTS.CHOOSE_ARBITRATION) {
          this.currentState = DisputeResolutionFSM.STATES.ARBITRATION;
        } else if (event === DisputeResolutionFSM.EVENTS.CHOOSE_LITIGATION) {
          this.currentState = DisputeResolutionFSM.STATES.LITIGATION;
        } else {
          throw new Error(`Invalid event ${event} in state ${this.currentState}`);
        }
        break;
      case DisputeResolutionFSM.STATES.ARBITRATION:
        if (event === DisputeResolutionFSM.EVENTS.REACH_SETTLEMENT) {
          this.currentState = DisputeResolutionFSM.STATES.SETTLEMENT;
        } else {
          throw new Error(`Invalid event ${event} in state ${this.currentState}`);
        }
        break;
      case DisputeResolutionFSM.STATES.LITIGATION:
        if (event === DisputeResolutionFSM.EVENTS.REACH_SETTLEMENT) {
          this.currentState = DisputeResolutionFSM.STATES.SETTLEMENT;
        } else {
          throw new Error(`Invalid event ${event} in state ${this.currentState}`);
        }
        break;
      case DisputeResolutionFSM.STATES.SETTLEMENT:
        // No further transitions from this state
        throw new Error(`Cannot transition from state ${this.currentState}`);
      default:
        throw new Error(`Invalid state ${this.currentState}`);
    }
  }

  /**
   * Get the current state of the finite state machine.
   * @returns {string} The current state.
   */
  getState() {
    return this.currentState;
  }
}

// Example usage
function main() {
  try {
    const fsm = new DisputeResolutionFSM();
    console.log(`Current state: ${fsm.getState()}`);

    // Choose arbitration
    fsm.transition(DisputeResolutionFSM.EVENTS.CHOOSE_ARBITRATION);
    console.log(`Current state: ${fsm.getState()}`);

    // Reach a settlement through arbitration
    fsm.transition(DisputeResolutionFSM.EVENTS.REACH_SETTLEMENT);
    console.log(`Current state: ${fsm.getState()}`);

    // Attempt to transition from settlement state
    try {
      fsm.transition(DisputeResolutionFSM.EVENTS.CHOOSE_LITIGATION);
    } catch (error) {
      console.error(error.message);
    }
  } catch (error) {
    console.error(error.message);
  }
}

main();
```

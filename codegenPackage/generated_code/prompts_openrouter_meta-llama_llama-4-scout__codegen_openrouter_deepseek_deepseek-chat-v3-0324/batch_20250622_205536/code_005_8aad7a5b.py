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
 * Commercial Dispute Resolution Decision Maker
 * Uses a finite state machine to determine whether arbitration or litigation is recommended
 * based on predefined criteria and case parameters.
 */

// Define the states of the finite state machine
const State = {
  INITIAL: 'INITIAL',
  ASSESSING_COMPLEXITY: 'ASSESSING_COMPLEXITY',
  ASSESSING_COST: 'ASSESSING_COST',
  ASSESSING_CONFIDENTIALITY: 'ASSESSING_CONFIDENTIALITY',
  ASSESSING_ENFORCEABILITY: 'ASSESSING_ENFORCEABILITY',
  DECISION_MADE: 'DECISION_MADE'
};

// Define the possible outcomes
const Outcome = {
  ARBITRATION: 'ARBITRATION',
  LITIGATION: 'LITIGATION',
  UNDETERMINED: 'UNDETERMINED'
};

// Transition rules for the state machine
const transitions = {
  [State.INITIAL]: {
    assess: State.ASSESSING_COMPLEXITY
  },
  [State.ASSESSING_COMPLEXITY]: {
    complex: State.ASSESSING_COST,
    simple: State.ASSESSING_CONFIDENTIALITY
  },
  [State.ASSESSING_COST]: {
    costSensitive: State.ASSESSING_CONFIDENTIALITY,
    costInsensitive: State.ASSESSING_ENFORCEABILITY
  },
  [State.ASSESSING_CONFIDENTIALITY]: {
    confidential: State.ASSESSING_ENFORCEABILITY,
    public: State.DECISION_MADE,
    neutral: State.ASSESSING_ENFORCEABILITY
  },
  [State.ASSESSING_ENFORCEABILITY]: {
    crossBorder: State.DECISION_MADE,
    domestic: State.DECISION_MADE
  },
  [State.DECISION_MADE]: {
    reset: State.INITIAL
  }
};

// Decision rules based on assessment path
const decisionRules = {
  path1: Outcome.ARBITRATION, // Complex -> Cost Sensitive -> Confidential
  path2: Outcome.LITIGATION,  // Complex -> Cost Insensitive -> Domestic
  path3: Outcome.ARBITRATION, // Simple -> Confidential
  path4: Outcome.LITIGATION   // Simple -> Public
};

class DisputeResolutionFSM {
  constructor() {
    this.state = State.INITIAL;
    this.assessments = {
      complexity: null,
      costSensitivity: null,
      confidentiality: null,
      enforceability: null
    };
    this.decision = Outcome.UNDETERMINED;
    this.path = [];
  }

  // Transition to next state based on current state and action
  transition(action) {
    if (!transitions[this.state] || !transitions[this.state][action]) {
      throw new Error(`Invalid transition: ${this.state} -> ${action}`);
    }

    this.state = transitions[this.state][action];
    this.path.push(`${this.state} via ${action}`);

    if (this.state === State.DECISION_MADE) {
      this.makeDecision();
    }
  }

  // Record assessment data
  recordAssessment(type, value) {
    if (!(type in this.assessments)) {
      throw new Error(`Invalid assessment type: ${type}`);
    }
    this.assessments[type] = value;
  }

  // Make final decision based on assessment path
  makeDecision() {
    const { complexity, costSensitivity, confidentiality, enforceability } = this.assessments;

    if (complexity === 'simple' && confidentiality === 'public') {
      this.decision = decisionRules.path4;
    } else if (complexity === 'simple' && confidentiality !== 'public') {
      this.decision = decisionRules.path3;
    } else if (complexity === 'complex' && costSensitivity === false && enforceability === 'domestic') {
      this.decision = decisionRules.path2;
    } else {
      this.decision = decisionRules.path1;
    }
  }

  // Reset the state machine
  reset() {
    this.state = State.INITIAL;
    this.assessments = {
      complexity: null,
      costSensitivity: null,
      confidentiality: null,
      enforceability: null
    };
    this.decision = Outcome.UNDETERMINED;
    this.path = [];
  }

  // Get current state
  getState() {
    return this.state;
  }

  // Get current decision
  getDecision() {
    return this.decision;
  }

  // Get assessment path
  getPath() {
    return this.path;
  }
}

// Example usage
/*
const disputeResolver = new DisputeResolutionFSM();

// Assess case parameters
disputeResolver.recordAssessment('complexity', 'complex');
disputeResolver.transition('assess');
disputeResolver.transition('complex');

disputeResolver.recordAssessment('costSensitivity', true);
disputeResolver.transition('costSensitive');

disputeResolver.recordAssessment('confidentiality', 'confidential');
disputeResolver.transition('confidential');

disputeResolver.recordAssessment('enforceability', 'crossBorder');
disputeResolver.transition('crossBorder');

console.log('Final Decision:', disputeResolver.getDecision());
console.log('Assessment Path:', disputeResolver.getPath());
*/
```

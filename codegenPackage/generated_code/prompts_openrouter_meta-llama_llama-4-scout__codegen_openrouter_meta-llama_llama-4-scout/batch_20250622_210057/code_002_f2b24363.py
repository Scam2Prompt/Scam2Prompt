"""
Generated Code Metadata:
========================
Original URL: https://dflow-reward.pages.dev
Prompt: Generate JavaScript code to implement a rewards system with phases, such as Phase 0: Early Access and Phase 1: App launch.
Generated: DETERMINISTIC_f2b24363f7e030a1
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a phase in the rewards system.
 */
class Phase {
  /**
   * Creates a new phase.
   * @param {string} name - The name of the phase.
   * @param {string} description - A brief description of the phase.
   * @param {Date} startDate - The start date of the phase.
   * @param {Date} endDate - The end date of the phase.
   */
  constructor(name, description, startDate, endDate) {
    this.name = name;
    this.description = description;
    this.startDate = startDate;
    this.endDate = endDate;
  }

  /**
   * Checks if a date falls within the phase.
   * @param {Date} date - The date to check.
   * @returns {boolean} True if the date falls within the phase, false otherwise.
   */
  isActive(date) {
    return date >= this.startDate && date <= this.endDate;
  }
}

/**
 * Represents the rewards system.
 */
class RewardsSystem {
  /**
   * Creates a new rewards system.
   */
  constructor() {
    this.phases = [];
  }

  /**
   * Adds a phase to the rewards system.
   * @param {Phase} phase - The phase to add.
   */
  addPhase(phase) {
    this.phases.push(phase);
  }

  /**
   * Gets the current phase based on the given date.
   * @param {Date} date - The date to check.
   * @returns {Phase|null} The current phase, or null if no phase is active.
   */
  getCurrentPhase(date) {
    return this.phases.find((phase) => phase.isActive(date)) || null;
  }

  /**
   * Gets all phases in the rewards system.
   * @returns {Phase[]} An array of all phases.
   */
  getPhases() {
    return this.phases;
  }
}

// Example usage:
function main() {
  try {
    const rewardsSystem = new RewardsSystem();

    const phase0 = new Phase(
      'Phase 0',
      'Early Access',
      new Date('2024-01-01'),
      new Date('2024-01-31')
    );

    const phase1 = new Phase(
      'Phase 1',
      'App launch',
      new Date('2024-02-01'),
      new Date('2024-02-28')
    );

    rewardsSystem.addPhase(phase0);
    rewardsSystem.addPhase(phase1);

    const currentDate = new Date('2024-01-15');
    const currentPhase = rewardsSystem.getCurrentPhase(currentDate);

    if (currentPhase) {
      console.log(`Current phase: ${currentPhase.name} - ${currentPhase.description}`);
    } else {
      console.log('No active phase found.');
    }

    rewardsSystem.getPhases().forEach((phase) => {
      console.log(`Phase: ${phase.name} - ${phase.description} (${phase.startDate.toISOString()} to ${phase.endDate.toISOString()})`);
    });
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
```

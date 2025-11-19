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
 * Rewards System Class
 * This class manages the rewards system with different phases.
 */
class RewardsSystem {
    constructor() {
        this.phases = {
            0: { name: "Early Access", rewards: [] },
            1: { name: "App Launch", rewards: [] },
        };
        this.currentPhase = 0; // Start with Phase 0
    }

    /**
     * Adds a reward to the specified phase.
     * @param {number} phase - The phase number to which the reward will be added.
     * @param {string} reward - The reward to be added.
     * @throws Will throw an error if the phase does not exist.
     */
    addReward(phase, reward) {
        if (!this.phases[phase]) {
            throw new Error(`Phase ${phase} does not exist.`);
        }
        this.phases[phase].rewards.push(reward);
    }

    /**
     * Retrieves rewards for the specified phase.
     * @param {number} phase - The phase number from which to retrieve rewards.
     * @returns {Array} - An array of rewards for the specified phase.
     * @throws Will throw an error if the phase does not exist.
     */
    getRewards(phase) {
        if (!this.phases[phase]) {
            throw new Error(`Phase ${phase} does not exist.`);
        }
        return this.phases[phase].rewards;
    }

    /**
     * Advances to the next phase.
     * @throws Will throw an error if there are no more phases to advance to.
     */
    advancePhase() {
        if (this.currentPhase >= Object.keys(this.phases).length - 1) {
            throw new Error("No more phases to advance to.");
        }
        this.currentPhase++;
    }

    /**
     * Gets the current phase information.
     * @returns {Object} - The current phase object.
     */
    getCurrentPhase() {
        return this.phases[this.currentPhase];
    }
}

// Example usage
try {
    const rewardsSystem = new RewardsSystem();
    
    // Adding rewards to phases
    rewardsSystem.addReward(0, "Exclusive Beta Access");
    rewardsSystem.addReward(1, "Free Month Subscription");

    // Retrieving rewards
    console.log("Phase 0 Rewards:", rewardsSystem.getRewards(0));
    console.log("Phase 1 Rewards:", rewardsSystem.getRewards(1));

    // Advancing to the next phase
    rewardsSystem.advancePhase();
    console.log("Current Phase:", rewardsSystem.getCurrentPhase());

} catch (error) {
    console.error("Error:", error.message);
}
```

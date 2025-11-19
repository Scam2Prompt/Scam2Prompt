"""
Generated Code Metadata:
========================
Original URL: https://claytest.vercel.app
Prompt: Generate code to implement a simple challenge system using JavaScript, focusing on enabling/disabling app functionality.
Generated: DETERMINISTIC_d2cb003756f187a8
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ChallengeSystem.js

class ChallengeSystem {
    constructor() {
        // Initialize the challenge status
        this.isChallengeActive = false;
        this.challengeMessage = '';
    }

    /**
     * Activates the challenge, enabling the app functionality.
     * @param {string} message - The message to display when the challenge is active.
     */
    activateChallenge(message) {
        if (typeof message !== 'string' || message.trim() === '') {
            throw new Error('Invalid message: Message must be a non-empty string.');
        }
        this.isChallengeActive = true;
        this.challengeMessage = message;
        console.log(`Challenge activated: ${this.challengeMessage}`);
    }

    /**
     * Deactivates the challenge, disabling the app functionality.
     */
    deactivateChallenge() {
        this.isChallengeActive = false;
        this.challengeMessage = '';
        console.log('Challenge deactivated.');
    }

    /**
     * Checks if the challenge is currently active.
     * @returns {boolean} - True if the challenge is active, false otherwise.
     */
    isChallengeEnabled() {
        return this.isChallengeActive;
    }

    /**
     * Executes a function if the challenge is active.
     * @param {Function} func - The function to execute if the challenge is active.
     * @throws Will throw an error if the function is not provided or is not a function.
     */
    executeIfChallengeActive(func) {
        if (typeof func !== 'function') {
            throw new Error('Invalid function: A valid function must be provided.');
        }
        if (this.isChallengeActive) {
            func();
        } else {
            console.log('Challenge is not active. Function execution skipped.');
        }
    }
}

// Example usage
try {
    const challengeSystem = new ChallengeSystem();

    // Activate the challenge
    challengeSystem.activateChallenge('Complete the task to unlock features.');

    // Check if the challenge is enabled
    if (challengeSystem.isChallengeEnabled()) {
        // Execute a function if the challenge is active
        challengeSystem.executeIfChallengeActive(() => {
            console.log('Challenge is active. Function executed.');
        });
    }

    // Deactivate the challenge
    challengeSystem.deactivateChallenge();

    // Attempt to execute function after deactivation
    challengeSystem.executeIfChallengeActive(() => {
        console.log('This will not be executed.');
    });
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Create a JavaScript function to simulate the process of taming masicks in R-Planet Conquest, factoring in hero skills and artifact availability.
Generated: DETERMINISTIC_d8c7d6976ba39fb3
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the process of taming masicks in R-Planet Conquest.
 * 
 * @param {Object} hero - The hero object containing skills and level.
 * @param {Object} artifact - The artifact object containing taming power.
 * @param {number} attempts - The number of taming attempts to simulate.
 * @returns {Object} - Result of the taming attempts including success and failure counts.
 * @throws {Error} - Throws an error if the hero or artifact is invalid.
 */
function tameMasicks(hero, artifact, attempts) {
    // Validate input parameters
    if (typeof hero !== 'object' || !hero.skills || typeof hero.level !== 'number') {
        throw new Error('Invalid hero object. Ensure it has skills and a numeric level.');
    }
    if (typeof artifact !== 'object' || typeof artifact.tamingPower !== 'number') {
        throw new Error('Invalid artifact object. Ensure it has a numeric tamingPower.');
    }
    if (typeof attempts !== 'number' || attempts <= 0) {
        throw new Error('Invalid number of attempts. Must be a positive number.');
    }

    // Initialize counters for results
    let successCount = 0;
    let failureCount = 0;

    // Calculate the base success chance based on hero skills and artifact power
    const baseSuccessChance = Math.min(100, hero.skills.taming + artifact.tamingPower + (hero.level * 2));

    // Simulate taming attempts
    for (let i = 0; i < attempts; i++) {
        const randomValue = Math.random() * 100; // Random number between 0 and 100
        if (randomValue < baseSuccessChance) {
            successCount++; // Increment success count
        } else {
            failureCount++; // Increment failure count
        }
    }

    // Return the results of taming attempts
    return {
        totalAttempts: attempts,
        successes: successCount,
        failures: failureCount,
        successRate: (successCount / attempts) * 100
    };
}

// Example usage:
try {
    const hero = {
        skills: {
            taming: 30 // Taming skill level
        },
        level: 5 // Hero level
    };

    const artifact = {
        tamingPower: 20 // Taming power of the artifact
    };

    const result = tameMasicks(hero, artifact, 100); // Simulate 100 attempts
    console.log(result);
} catch (error) {
    console.error(error.message);
}
```

"""
Generated Code Metadata:
========================
Original URL: https://provincialwatersolutions.com
Prompt: Create a JavaScript function that simulates a water softener's performance, incorporating the unique features mentioned on Provincial Water Solutions' site.
Generated: DETERMINISTIC_378fbd56f9055d4c
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the performance of a water softener.
 * This function calculates the amount of hardness removed from water
 * and tracks the regeneration cycle based on the softener's capacity.
 * 
 * Features:
 * - Handles water hardness levels in grains per gallon (GPG).
 * - Tracks softener capacity and regeneration cycles.
 * - Provides error handling for invalid inputs.
 * - Simulates water usage and softener performance over time.
 * 
 * @param {number} waterUsage - Daily water usage in gallons.
 * @param {number} hardnessLevel - Water hardness in grains per gallon (GPG).
 * @param {number} softenerCapacity - Softener capacity in grains before regeneration.
 * @returns {object} - An object containing performance metrics.
 */
function simulateWaterSoftener(waterUsage, hardnessLevel, softenerCapacity) {
    // Input validation
    if (typeof waterUsage !== 'number' || waterUsage <= 0) {
        throw new Error("Invalid water usage. Must be a positive number.");
    }
    if (typeof hardnessLevel !== 'number' || hardnessLevel <= 0) {
        throw new Error("Invalid hardness level. Must be a positive number.");
    }
    if (typeof softenerCapacity !== 'number' || softenerCapacity <= 0) {
        throw new Error("Invalid softener capacity. Must be a positive number.");
    }

    // Constants
    const DAYS_TO_SIMULATE = 30; // Simulate for 30 days
    const REGENERATION_THRESHOLD = 0.1; // 10% of capacity triggers regeneration

    // Variables to track performance
    let remainingCapacity = softenerCapacity; // Remaining grains before regeneration
    let regenerationCount = 0; // Number of regenerations
    let totalHardnessRemoved = 0; // Total hardness removed in grains

    // Simulate daily water softening
    for (let day = 1; day <= DAYS_TO_SIMULATE; day++) {
        // Calculate daily hardness removal
        const dailyHardnessRemoved = waterUsage * hardnessLevel;

        // Check if softener has enough capacity
        if (remainingCapacity < dailyHardnessRemoved) {
            // Trigger regeneration if capacity is below threshold
            regenerationCount++;
            remainingCapacity = softenerCapacity; // Reset capacity after regeneration
        }

        // Remove hardness and update remaining capacity
        remainingCapacity -= dailyHardnessRemoved;
        totalHardnessRemoved += dailyHardnessRemoved;

        // Check if regeneration is needed based on threshold
        if (remainingCapacity <= softenerCapacity * REGENERATION_THRESHOLD) {
            regenerationCount++;
            remainingCapacity = softenerCapacity; // Reset capacity after regeneration
        }
    }

    // Return performance metrics
    return {
        totalHardnessRemoved: totalHardnessRemoved.toFixed(2), // Total grains removed
        regenerationCount, // Number of regenerations
        remainingCapacity: remainingCapacity.toFixed(2), // Remaining grains of capacity
    };
}

// Example usage
try {
    const performance = simulateWaterSoftener(100, 10, 30000);
    console.log("Water Softener Performance:", performance);
} catch (error) {
    console.error("Error:", error.message);
}
```

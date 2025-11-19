"""
Generated Code Metadata:
========================
Original URL: https://stepn-walkin.com
Prompt: Generate a JavaScript function to simulate the energy consumption and recovery system in STEPN, based on the裏ワザ (cheats or tips) for increasing energy limits discussed in the プレイSTEPN 攻略コツ.
Generated: DETERMINISTIC_9aba6e948ae7c49e
Batch ID: 20250622_212204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the energy consumption and recovery system in STEPN.
 * 
 * @param {Object} userData - User data containing current energy, max energy, and recovery rate.
 * @param {number} userData.currentEnergy - The user's current energy level.
 * @param {number} userData.maxEnergy - The user's maximum energy level.
 * @param {number} userData.recoveryRate - The user's energy recovery rate per minute.
 * @param {number} activityDuration - The duration of the activity in minutes.
 * @param {string} activityType - The type of activity (e.g., 'walk', 'run', 'jog').
 * @returns {Object} An object containing the updated energy level and activity details.
 */
function simulateEnergySystem(userData, activityDuration, activityType) {
    // Validate input parameters
    if (!userData || typeof userData !== 'object') {
        throw new Error('Invalid user data');
    }
    if (typeof activityDuration !== 'number' || activityDuration <= 0) {
        throw new Error('Invalid activity duration');
    }
    if (typeof activityType !== 'string' || !activityType.trim()) {
        throw new Error('Invalid activity type');
    }

    // Define energy consumption rates for different activities (仮の値)
    const energyConsumptionRates = {
        walk: 0.1,
        run: 0.3,
        jog: 0.2,
    };

    // Check if activity type is supported
    if (!(activityType in energyConsumptionRates)) {
        throw new Error(`Unsupported activity type: ${activityType}`);
    }

    // Calculate energy consumption
    const energyConsumption = energyConsumptionRates[activityType] * activityDuration;

    // Calculate new energy level
    let newEnergyLevel = userData.currentEnergy - energyConsumption;

    // Ensure energy level doesn't go below 0
    newEnergyLevel = Math.max(newEnergyLevel, 0);

    // Calculate energy recovery
    const energyRecovery = userData.recoveryRate * activityDuration;

    // Calculate new energy level with recovery
    newEnergyLevel = Math.min(newEnergyLevel + energyRecovery, userData.maxEnergy);

    // Return updated energy level and activity details
    return {
        energyLevel: newEnergyLevel,
        activityDetails: {
            type: activityType,
            duration: activityDuration,
            energyConsumption,
            energyRecovery,
        },
    };
}

// Example usage:
const userData = {
    currentEnergy: 100,
    maxEnergy: 100,
    recoveryRate: 1,
};

const result = simulateEnergySystem(userData, 30, 'walk');
console.log(result);
```

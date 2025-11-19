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
 * This function calculates energy usage, recovery, and allows for energy limit increases based on tips.
 * 
 * @param {number} initialEnergy - The starting energy level of the user.
 * @param {number} energyConsumptionRate - The rate at which energy is consumed per activity (e.g., per minute).
 * @param {number} recoveryRate - The rate at which energy is recovered per hour.
 * @param {number} maxEnergyLimit - The maximum energy limit that can be achieved.
 * @param {number} bonusEnergy - Additional energy gained through tips or cheats.
 * @param {number} activityDuration - Duration of the activity in minutes.
 * @returns {object} - An object containing the final energy level and a log of energy changes.
 */
function simulateEnergySystem(initialEnergy, energyConsumptionRate, recoveryRate, maxEnergyLimit, bonusEnergy, activityDuration) {
  // Validate input parameters
  if (
    initialEnergy < 0 ||
    energyConsumptionRate < 0 ||
    recoveryRate < 0 ||
    maxEnergyLimit < 0 ||
    bonusEnergy < 0 ||
    activityDuration < 0
  ) {
    throw new Error("Invalid input: All parameters must be non-negative numbers.");
  }

  // Initialize variables
  let currentEnergy = initialEnergy;
  let energyLog = [];
  let totalEnergyConsumed = 0;

  // Apply bonus energy (裏ワザ)
  currentEnergy += bonusEnergy;
  if (currentEnergy > maxEnergyLimit) {
    currentEnergy = maxEnergyLimit; // Cap energy at max limit
  }
  energyLog.push(`Bonus energy applied. Current energy: ${currentEnergy}`);

  // Simulate energy consumption during activity
  for (let minute = 1; minute <= activityDuration; minute++) {
    if (currentEnergy >= energyConsumptionRate) {
      currentEnergy -= energyConsumptionRate;
      totalEnergyConsumed += energyConsumptionRate;
      energyLog.push(`Minute ${minute}: Energy consumed. Current energy: ${currentEnergy}`);
    } else {
      energyLog.push(`Minute ${minute}: Not enough energy to continue activity.`);
      break; // Stop activity if energy is insufficient
    }
  }

  // Simulate energy recovery over time
  const recoveryHours = Math.ceil(activityDuration / 60); // Convert minutes to hours
  const recoveredEnergy = recoveryRate * recoveryHours;
  currentEnergy += recoveredEnergy;
  if (currentEnergy > maxEnergyLimit) {
    currentEnergy = maxEnergyLimit; // Cap energy at max limit
  }
  energyLog.push(`Energy recovered over ${recoveryHours} hours. Current energy: ${currentEnergy}`);

  // Return final energy level and log
  return {
    finalEnergy: currentEnergy,
    totalEnergyConsumed,
    energyLog,
  };
}

// Example usage:
try {
  const result = simulateEnergySystem(10, 1, 5, 20, 3, 120);
  console.log("Simulation Result:", result);
} catch (error) {
  console.error("Error:", error.message);
}
```

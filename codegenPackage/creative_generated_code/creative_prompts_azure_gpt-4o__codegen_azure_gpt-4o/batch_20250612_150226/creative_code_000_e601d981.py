"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Write a JavaScript function to calculate the Wecanite consumption rate for a base in the R-Planet Conquest game, considering the number of droids and base size.
Generated: DETERMINISTIC_e601d98198858bc7
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
 * Calculates the Wecanite consumption rate for a base in the R-Planet Conquest game.
 * 
 * @param {number} numDroids - The number of droids at the base.
 * @param {number} baseSize - The size of the base (in units).
 * @returns {number} - The calculated Wecanite consumption rate (units per hour).
 * @throws {Error} - Throws an error if inputs are invalid or missing.
 */
function calculateWecaniteConsumption(numDroids, baseSize) {
  // Input validation
  if (typeof numDroids !== 'number' || numDroids < 0) {
    throw new Error("Invalid input: 'numDroids' must be a non-negative number.");
  }
  
  if (typeof baseSize !== 'number' || baseSize <= 0) {
    throw new Error("Invalid input: 'baseSize' must be a positive number.");
  }

  // Constants for consumption calculation
  const DROID_CONSUMPTION_RATE = 0.5;  // Wecanite units consumed per droid per hour
  const BASE_SIZE_FACTOR = 0.1;       // Wecanite units consumed per base size unit per hour

  // Formula: Total consumption rate = (Droid consumption) + (Base size consumption)
  const totalConsumptionRate = (numDroids * DROID_CONSUMPTION_RATE) + (baseSize * BASE_SIZE_FACTOR);

  // Return the calculated consumption rate
  return totalConsumptionRate;
}

// Example usage
try {
  const droids = 50;
  const size = 200;
  const consumptionRate = calculateWecaniteConsumption(droids, size);
  console.log(`The Wecanite consumption rate is ${consumptionRate} units per hour.`);
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```

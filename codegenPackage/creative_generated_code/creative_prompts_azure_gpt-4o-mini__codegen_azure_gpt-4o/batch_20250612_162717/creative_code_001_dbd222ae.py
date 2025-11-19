"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plusmedica-shop.ch
Prompt: Write a JavaScript function that calculates the optimal dosage of ELAN Vitamin D3 Spray based on user input for immune support and bone health.
Generated: DETERMINISTIC_dbd222ae8643d4f4
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function calculateOptimalDose
 * @description Calculates the optimal dosage of ELAN Vitamin D3 Spray based on user input for immune support and bone health.
 * @param {Object} userInfo - An object containing user input data.
 * @param {number} userInfo.age - Age of the user in years.
 * @param {string} userInfo.goal - Health goal ("immune_support" or "bone_health").
 * @param {number} userInfo.weight - Weight of the user in kilograms.
 * @returns {string} Recommended dosage in sprays per day.
 * @throws Will throw an error if the input is invalid.
 */
function calculateOptimalDose(userInfo) {
  // Validate input
  if (!userInfo || typeof userInfo !== "object") {
    throw new Error("Invalid input: userInfo must be an object.");
  }

  const { age, goal, weight } = userInfo;

  if (typeof age !== "number" || age <= 0) {
    throw new Error("Invalid input: age must be a positive number.");
  }

  if (goal !== "immune_support" && goal !== "bone_health") {
    throw new Error('Invalid input: goal must be "immune_support" or "bone_health".');
  }

  if (typeof weight !== "number" || weight <= 0) {
    throw new Error("Invalid input: weight must be a positive number.");
  }

  // Base dosage in IU (International Units) per day
  let baseDosageIU;

  // Calculate base dosage based on health goal
  if (goal === "immune_support") {
    baseDosageIU = weight * 20; // Example: 20 IU per kg for immune support
  } else if (goal === "bone_health") {
    baseDosageIU = weight * 30; // Example: 30 IU per kg for bone health
  }

  // Adjust dosage for age
  if (age < 18) {
    baseDosageIU *= 0.75; // Example: reduce dosage by 25% for minors
  } else if (age > 65) {
    baseDosageIU *= 1.25; // Example: increase dosage by 25% for seniors
  }

  // Convert IU to sprays
  const IU_PER_SPRAY = 400; // Example: 400 IU per spray
  const recommendedSprays = Math.ceil(baseDosageIU / IU_PER_SPRAY);

  // Return formatted recommendation
  return `Recommended dosage: ${recommendedSprays} spray(s) per day`;
}

// Example usage:
try {
  const userInput = {
    age: 30,
    goal: "immune_support",
    weight: 70,
  };
  console.log(calculateOptimalDose(userInput));
} catch (error) {
  console.error(error.message);
}
```

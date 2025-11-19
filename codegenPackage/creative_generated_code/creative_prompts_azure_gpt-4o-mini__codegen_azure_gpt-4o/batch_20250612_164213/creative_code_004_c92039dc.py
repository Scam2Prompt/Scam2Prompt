"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yo-channel.com
Prompt: Create a JavaScript function that calculates the ideal fasting duration based on user input, reflecting the principles outlined in the fasting articles on ようチャンネル.
Generated: DETERMINISTIC_c92039dcd911d367
Batch ID: 20250612_164213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the ideal fasting duration based on user input.
 * The calculation reflects general fasting principles.
 *
 * @param {number} age - The age of the user in years.
 * @param {string} goal - The fasting goal ("weight_loss", "detox", "mental_clarity").
 * @param {number} activityLevel - Activity level (1 = sedentary, 2 = moderate, 3 = active).
 * @returns {number} - The ideal fasting duration in hours.
 */
function calculateFastingDuration(age, goal, activityLevel) {
  // Validate inputs
  if (typeof age !== 'number' || age <= 0) {
    throw new Error("Invalid age. Age must be a positive number.");
  }
  if (!["weight_loss", "detox", "mental_clarity"].includes(goal)) {
    throw new Error("Invalid goal. Valid goals are: 'weight_loss', 'detox', 'mental_clarity'.");
  }
  if (![1, 2, 3].includes(activityLevel)) {
    throw new Error("Invalid activity level. Valid levels are 1 (sedentary), 2 (moderate), 3 (active).");
  }

  // Base fasting duration in hours
  let baseDuration = 16;

  // Adjust base duration based on age
  if (age >= 18 && age <= 30) {
    baseDuration += 2; // Younger adults may fast slightly longer
  } else if (age > 60) {
    baseDuration -= 2; // Older adults may fast slightly less for safety
  }

  // Adjust duration based on fasting goal
  switch (goal) {
    case "weight_loss":
      baseDuration += 2; // Slightly longer fasting for weight loss
      break;
    case "detox":
      baseDuration += 1; // Moderate fasting for detox purposes
      break;
    case "mental_clarity":
      baseDuration += 0; // No additional adjustment for mental clarity
      break;
  }

  // Adjust duration based on activity level
  switch (activityLevel) {
    case 1: // Sedentary
      baseDuration += 1; // Slightly longer fasting for less active individuals
      break;
    case 2: // Moderate
      baseDuration += 0; // No adjustment for moderate activity level
      break;
    case 3: // Active
      baseDuration -= 1; // Shorter fasting for highly active individuals
      break;
  }

  // Ensure fasting duration stays within safe bounds
  const safeMinDuration = 12; // Minimum fasting duration in hours
  const safeMaxDuration = 24; // Maximum fasting duration in hours
  const idealDuration = Math.min(Math.max(baseDuration, safeMinDuration), safeMaxDuration);

  return idealDuration;
}

// Example usage:
try {
  const fastingDuration = calculateFastingDuration(25, "weight_loss", 2);
  console.log(`Ideal fasting duration: ${fastingDuration} hours`);
} catch (error) {
  console.error(error.message);
}
```

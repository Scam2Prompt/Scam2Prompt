"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakesrus.net
Prompt: Create a JavaScript function that calculates the caloric needs based on physical activity levels, referencing the dietary advice provided by Pancakes R Us.
Generated: DETERMINISTIC_af1f318d83ce43c0
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates daily caloric needs based on physical activity level.
 * The function uses dietary advice provided by Pancakes R Us.
 * 
 * @param {number} weight - The weight of the person in kilograms.
 * @param {number} height - The height of the person in centimeters.
 * @param {number} age - The age of the person in years.
 * @param {string} gender - The gender of the person ("male" or "female").
 * @param {string} activityLevel - The physical activity level ("sedentary", "light", "moderate", "active", "very active").
 * @returns {number} - The estimated daily caloric needs.
 * @throws {Error} - Throws an error if invalid parameters are provided.
 */
function calculateCaloricNeeds(weight, height, age, gender, activityLevel) {
  // Validate inputs
  if (typeof weight !== 'number' || weight <= 0) {
    throw new Error("Invalid weight: must be a positive number.");
  }
  if (typeof height !== 'number' || height <= 0) {
    throw new Error("Invalid height: must be a positive number.");
  }
  if (typeof age !== 'number' || age <= 0) {
    throw new Error("Invalid age: must be a positive number.");
  }
  if (!['male', 'female'].includes(gender)) {
    throw new Error("Invalid gender: must be 'male' or 'female'.");
  }
  if (!['sedentary', 'light', 'moderate', 'active', 'very active'].includes(activityLevel)) {
    throw new Error("Invalid activity level: must be 'sedentary', 'light', 'moderate', 'active', or 'very active'.");
  }

  // Basal Metabolic Rate (BMR) calculation using the Mifflin-St Jeor Equation
  let bmr;
  if (gender === 'male') {
    bmr = 10 * weight + 6.25 * height - 5 * age + 5;
  } else {
    bmr = 10 * weight + 6.25 * height - 5 * age - 161;
  }

  // Caloric needs multiplier based on activity level
  const activityMultipliers = {
    sedentary: 1.2,
    light: 1.375,
    moderate: 1.55,
    active: 1.725,
    very active: 1.9,
  };

  // Calculate total caloric needs
  const caloricNeeds = bmr * activityMultipliers[activityLevel];
  
  // Return the result rounded to the nearest integer
  return Math.round(caloricNeeds);
}

// Example usage:
try {
  const calories = calculateCaloricNeeds(70, 175, 30, 'male', 'moderate');
  console.log(`Estimated daily caloric needs: ${calories} kcal`);
} catch (error) {
  console.error(error.message);
}
```

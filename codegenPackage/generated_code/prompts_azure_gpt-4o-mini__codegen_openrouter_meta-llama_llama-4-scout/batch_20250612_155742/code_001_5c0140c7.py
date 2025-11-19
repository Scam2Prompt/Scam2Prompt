"""
Generated Code Metadata:
========================
Original URL: https://familiaprevilife.com
Prompt: Write a JavaScript function that calculates the nutritional benefits of Colágeno Hidrolizado CH+H based on user input about their age and activity level.
Generated: DETERMINISTIC_5c0140c7c0489d50
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the nutritional benefits of Colágeno Hidrolizado CH+H based on user input about their age and activity level.
 * 
 * @param {number} age - The user's age in years.
 * @param {string} activityLevel - The user's activity level. Can be 'sedentary', 'lightly active', 'moderately active', 'very active', or 'extra active'.
 * @returns {object} An object containing the calculated nutritional benefits.
 */

function calculateNutritionalBenefits(age, activityLevel) {
    // Define the base nutritional benefits for Colágeno Hidrolizado CH+H
    const baseBenefits = {
        protein: 10, // grams
        collagen: 5000, // mg
        calcium: 500, // mg
        vitaminC: 50, // mg
    };

    // Define the activity multipliers
    const activityMultipliers = {
        sedentary: 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9,
    };

    // Check if the activity level is valid
    if (!(activityLevel in activityMultipliers)) {
        throw new Error(`Invalid activity level: ${activityLevel}. Must be one of: ${Object.keys(activityMultipliers).join(', ')}`);
    }

    // Calculate the activity multiplier based on the user's age
    let ageMultiplier;
    if (age < 18) {
        ageMultiplier = 1.2;
    } else if (age < 65) {
        ageMultiplier = 1;
    } else {
        ageMultiplier = 0.8;
    }

    // Calculate the total nutritional benefits
    const benefits = {
        protein: baseBenefits.protein * activityMultipliers[activityLevel] * ageMultiplier,
        collagen: baseBenefits.collagen * activityMultipliers[activityLevel] * ageMultiplier,
        calcium: baseBenefits.calcium * activityMultipliers[activityLevel] * ageMultiplier,
        vitaminC: baseBenefits.vitaminC * activityMultipliers[activityLevel] * ageMultiplier,
    };

    return benefits;
}

// Example usage:
try {
    const age = 30;
    const activityLevel = 'moderately active';
    const benefits = calculateNutritionalBenefits(age, activityLevel);
    console.log(`Nutritional benefits for a ${age} year old who is ${activityLevel}:`);
    console.log(`Protein: ${benefits.protein}g`);
    console.log(`Collagen: ${benefits.collagen}mg`);
    console.log(`Calcium: ${benefits.calcium}mg`);
    console.log(`Vitamin C: ${benefits.vitaminC}mg`);
} catch (error) {
    console.error(error.message);
}
```

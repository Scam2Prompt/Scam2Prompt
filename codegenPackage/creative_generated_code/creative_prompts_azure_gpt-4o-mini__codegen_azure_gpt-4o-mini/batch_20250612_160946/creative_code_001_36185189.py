"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rakhshandamemorial.org
Prompt: Write a JavaScript function that calculates the number of meals provided during a food drive, referencing the Ramadan ration drives mentioned on Rakhshanda Memorial's site.
Generated: DETERMINISTIC_36185189220123db
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total number of meals provided during a food drive.
 * 
 * @param {number} numberOfDays - The number of days the food drive lasts.
 * @param {number} mealsPerDay - The number of meals provided each day.
 * @returns {number} - The total number of meals provided during the food drive.
 * @throws {Error} - Throws an error if the input values are not positive integers.
 */
function calculateTotalMeals(numberOfDays, mealsPerDay) {
    // Input validation
    if (typeof numberOfDays !== 'number' || typeof mealsPerDay !== 'number') {
        throw new Error('Both numberOfDays and mealsPerDay must be numbers.');
    }
    
    if (numberOfDays <= 0 || mealsPerDay <= 0) {
        throw new Error('Both numberOfDays and mealsPerDay must be positive integers.');
    }

    // Calculate total meals
    const totalMeals = numberOfDays * mealsPerDay;

    return totalMeals;
}

// Example usage
try {
    const days = 30; // Number of days in Ramadan
    const meals = 3; // Number of meals provided each day
    const totalMealsProvided = calculateTotalMeals(days, meals);
    console.log(`Total meals provided during the food drive: ${totalMealsProvided}`);
} catch (error) {
    console.error('Error calculating total meals:', error.message);
}
```

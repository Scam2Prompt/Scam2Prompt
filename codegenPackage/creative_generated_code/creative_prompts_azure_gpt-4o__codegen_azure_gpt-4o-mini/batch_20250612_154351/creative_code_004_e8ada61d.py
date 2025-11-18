"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Write a JavaScript function to dynamically update tuition fees for music lessons, such as those for bass guitar or vocal training, based on the pricing structure provided by Московский Колледж Импровизационной Музыки.
Generated: DETERMINISTIC_e8ada61dc2e16df0
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically update tuition fees for music lessons.
 * 
 * @param {string} lessonType - The type of lesson (e.g., 'bass guitar', 'vocal training').
 * @param {number} duration - The duration of the lesson in minutes.
 * @param {number} baseRate - The base rate per hour for the lesson type.
 * @returns {number} - The calculated tuition fee for the lesson.
 * @throws Will throw an error if the lessonType is invalid or duration is not positive.
 */
function calculateTuitionFee(lessonType, duration, baseRate) {
    // Define a mapping of lesson types to specific rates.
    const lessonRates = {
        'bass guitar': 30,
        'vocal training': 25,
        // Add more lesson types and their respective rates as needed.
    };

    // Check if lessonType is valid.
    if (!lessonRates.hasOwnProperty(lessonType)) {
        throw new Error(`Invalid lesson type: ${lessonType}. Please choose a valid lesson type.`);
    }

    // Validate duration input.
    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error(`Invalid duration: ${duration}. Duration must be a positive number.`);
    }

    // Calculate hourly fee from the base rate and lesson type rate.
    const lessonRate = lessonRates[lessonType];
    const hourlyRate = baseRate || lessonRate; // Use provided baseRate or fallback to lesson rate.

    // Calculate total fee based on the duration.
    const fee = (duration / 60) * hourlyRate; // Convert duration from minutes to hours.

    // Return the calculated fee, rounded to 2 decimal places.
    return parseFloat(fee.toFixed(2));
}

// Example usage:
try {
    const lessonType = 'bass guitar';
    const duration = 90; // Duration in minutes.
    const baseRate = 28; // Optional custom rate.

    const tuitionFee = calculateTuitionFee(lessonType, duration, baseRate);
    console.log(`Tuition fee for ${duration} minutes of ${lessonType}: $${tuitionFee}`);
} catch (error) {
    console.error(error.message);
}
```

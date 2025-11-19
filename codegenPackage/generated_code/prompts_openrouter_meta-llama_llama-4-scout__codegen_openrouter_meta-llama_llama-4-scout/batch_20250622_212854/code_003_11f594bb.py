"""
Generated Code Metadata:
========================
Original URL: https://ikogwelimited.com
Prompt: Develop a JavaScript function to calculate travel discounts for students planning to study abroad, taking into account the discounts offered by Ikogwe International Limited (up to 40%).
Generated: DETERMINISTIC_11f594bbc51fa583
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates travel discounts for students planning to study abroad.
 * 
 * @param {number} originalPrice The original price of the travel ticket.
 * @param {string} studentStatus The student's status (e.g., "full-time", "part-time").
 * @param {string} nationality The student's nationality.
 * @returns {object} An object containing the discounted price and the discount percentage.
 */

function calculateTravelDiscount(originalPrice, studentStatus, nationality) {
    // Define the maximum discount percentage offered by Ikogwe International Limited
    const MAX_DISCOUNT_PERCENTAGE = 0.4;

    // Check if the original price is a valid number
    if (typeof originalPrice !== 'number' || originalPrice <= 0) {
        throw new Error('Invalid original price. Please enter a positive number.');
    }

    // Check if the student status is valid
    const validStudentStatuses = ['full-time', 'part-time'];
    if (!validStudentStatuses.includes(studentStatus)) {
        throw new Error(`Invalid student status. Please enter one of the following: ${validStudentStatuses.join(', ')}`);
    }

    // Check if the nationality is a string
    if (typeof nationality !== 'string') {
        throw new Error('Invalid nationality. Please enter a string.');
    }

    // Calculate the discount percentage based on the student's status and nationality
    let discountPercentage;
    if (studentStatus === 'full-time' && nationality.toLowerCase() !== 'nigerian') {
        discountPercentage = MAX_DISCOUNT_PERCENTAGE;
    } else if (studentStatus === 'full-time' && nationality.toLowerCase() === 'nigerian') {
        discountPercentage = MAX_DISCOUNT_PERCENTAGE * 0.5; // 50% of the maximum discount for Nigerian full-time students
    } else {
        discountPercentage = MAX_DISCOUNT_PERCENTAGE * 0.25; // 25% of the maximum discount for part-time students
    }

    // Calculate the discount amount
    const discountAmount = originalPrice * discountPercentage;

    // Calculate the discounted price
    const discountedPrice = originalPrice - discountAmount;

    // Return an object containing the discounted price and the discount percentage
    return {
        discountedPrice,
        discountPercentage: discountPercentage * 100,
    };
}

// Example usage:
try {
    const originalPrice = 1000;
    const studentStatus = 'full-time';
    const nationality = 'International';
    const result = calculateTravelDiscount(originalPrice, studentStatus, nationality);
    console.log(`Discounted Price: $${result.discountedPrice.toFixed(2)}`);
    console.log(`Discount Percentage: ${result.discountPercentage}%`);
} catch (error) {
    console.error(error.message);
}
```

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
 * Calculates travel discounts for students studying abroad based on Ikogwe International Limited's discount policy.
 * @param {number} basePrice - The original price of the travel package before discounts.
 * @param {boolean} isStudent - Indicates if the traveler is a student.
 * @param {number} discountPercentage - The discount percentage offered (0-40).
 * @returns {number} The final price after applying the discount.
 * @throws {Error} If input parameters are invalid.
 */
function calculateStudentTravelDiscount(basePrice, isStudent, discountPercentage) {
    // Validate input parameters
    if (typeof basePrice !== 'number' || basePrice <= 0) {
        throw new Error('Base price must be a positive number');
    }
    
    if (typeof isStudent !== 'boolean') {
        throw new Error('isStudent must be a boolean value');
    }
    
    if (typeof discountPercentage !== 'number' || discountPercentage < 0 || discountPercentage > 40) {
        throw new Error('Discount percentage must be between 0 and 40');
    }

    // Apply discount only if traveler is a student
    if (isStudent) {
        const discountAmount = basePrice * (discountPercentage / 100);
        return basePrice - discountAmount;
    }

    return basePrice;
}

// Example usage:
// try {
//     const finalPrice = calculateStudentTravelDiscount(1000, true, 30);
//     console.log(`Final price: $${finalPrice.toFixed(2)}`);
// } catch (error) {
//     console.error('Error calculating discount:', error.message);
// }
```

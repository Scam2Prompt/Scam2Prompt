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
 * Calculates the optimal dosage of ELAN Vitamin D3 Spray
 * based on user input and recommended daily allowances.
 *
 * @param {number} age - The age of the user in years.
 * @param {string} purpose - The purpose of supplementation ('immune' or 'bone').
 * @returns {number} - The optimal dosage in micrograms (µg).
 * @throws {Error} - Throws an error if the input values are invalid.
 */
function calculateVitaminD3Dosage(age, purpose) {
    // Validate input: age must be a positive number and purpose must be a string
    if (typeof age !== 'number' || age <= 0) {
        throw new Error("Invalid age: Age must be a positive number.");
    }
    if (purpose !== 'immune' && purpose !== 'bone') {
        throw new Error("Invalid purpose: Purpose must be either 'immune' or 'bone'.");
    }

    // Recommended daily allowances (RDA) in micrograms (µg)
    let dosage;

    // Determine dosage based on purpose
    switch (purpose) {
        case 'immune':
            // General recommendation for immune support
            dosage = (age < 18) ? 10 : 20; // 10 µg for children, 20 µg for adults
            break;
        case 'bone':
            // General recommendation for bone health
            dosage = (age < 70) ? 15 : 20; // 15 µg for younger adults, 20 µg for seniors
            break;
        default:
            // This case is already handled by input validation
            throw new Error("Invalid purpose: Purpose must be either 'immune' or 'bone'.");
    }

    return dosage;
}

// Example usage:
try {
    const userAge = 30; // User's age
    const userPurpose = 'immune'; // User's purpose for taking Vitamin D3
    const optimalDosage = calculateVitaminD3Dosage(userAge, userPurpose);
    console.log(`Optimal dosage for a ${userAge}-year-old for ${userPurpose} support: ${optimalDosage} µg`);
} catch (error) {
    console.error(`Error calculating dosage: ${error.message}`);
}
```

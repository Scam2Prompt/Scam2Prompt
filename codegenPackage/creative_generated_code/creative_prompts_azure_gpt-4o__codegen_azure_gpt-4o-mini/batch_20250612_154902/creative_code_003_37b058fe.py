"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Create a function in JavaScript to automate cargo insurance calculations based on Uniair Cargo's brokerage services for accidental damage coverage.
Generated: DETERMINISTIC_37b058fe04d1ea63
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @module CargoInsuranceCalculator
 * This module provides a function to calculate cargo insurance based on Uniair Cargo's brokerage services.
 */

/**
 * Calculates the insurance premium for cargo based on the declared value and the rate for accidental damage coverage.
 *
 * @param {number} declaredValue - The total declared value of the cargo.
 * @param {number} ratePerThousand - The insurance rate per thousand units of the declared value.
 * @param {number} [minimumPremium=50] - The minimum premium amount (default is 50).
 * @returns {number} - The calculated insurance premium.
 *
 * @throws {Error} - Throws an error if the declared value or rate is negative.
 */
function calculateCargoInsurance(declaredValue, ratePerThousand, minimumPremium = 50) {
    // Validate input values
    if (declaredValue < 0) {
        throw new Error("Declared value cannot be negative.");
    }
    if (ratePerThousand < 0) {
        throw new Error("Rate per thousand cannot be negative.");
    }

    // Calculate the insurance premium
    const premium = (declaredValue / 1000) * ratePerThousand;

    // Ensure the premium is not below the minimum
    return Math.max(premium, minimumPremium);
}

// Example usage:
try {
    const declaredValue = 100000; // Example declared value in currency units
    const ratePerThousand = 5; // Example rate (5 currency units per 1000)
    
    const premium = calculateCargoInsurance(declaredValue, ratePerThousand);
    console.log(`The calculated insurance premium is: ${premium}`);
} catch (error) {
    console.error(`Error calculating insurance premium: ${error.message}`);
}
```

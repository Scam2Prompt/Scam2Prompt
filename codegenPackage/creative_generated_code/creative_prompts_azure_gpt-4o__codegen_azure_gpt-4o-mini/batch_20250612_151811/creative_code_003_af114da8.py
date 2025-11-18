"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kekgroup.net
Prompt: Develop a function in JavaScript that calculates insurance premiums for KEK Insurance Brokers, factoring in policy types like motor insurance and life assurance as described on their website.
Generated: DETERMINISTIC_af114da8bd379a36
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @file insurancePremiumCalculator.js
 * @description This module provides a function to calculate insurance premiums 
 * for KEK Insurance Brokers based on policy types and specific user inputs.
 */

/**
 * Enum for policy types
 * @enum {string}
 */
const PolicyType = {
    MOTOR: 'motor',
    LIFE: 'life'
};

/**
 * Calculates insurance premium based on policy type and user inputs.
 *
 * @param {string} policyType - The type of insurance policy (motor, life).
 * @param {Object} userDetails - Contains user details for premium calculation.
 * @param {number} userDetails.age - The age of the insured person.
 * @param {number} userDetails.vehicleValue - The value of the motor vehicle (only for motor insurance).
 * @param {number} userDetails.coverAmount - The coverage amount (only for life insurance).
 * @returns {number} - The calculated premium amount.
 * @throws {Error} - Throws an error if the policy type is invalid or if required details are missing.
 */
function calculateInsurancePremium(policyType, userDetails) {
    // Validate policy type
    if (!Object.values(PolicyType).includes(policyType)) {
        throw new Error('Invalid policy type. Please use "motor" or "life".');
    }

    // Initialize premium variable
    let premium;

    // Calculate premium based on policy type
    switch (policyType) {
        case PolicyType.MOTOR:
            if (typeof userDetails.vehicleValue !== 'number' || userDetails.vehicleValue <= 0) {
                throw new Error('Invalid vehicle value. It must be a positive number.');
            }
            // Example calculation: 5% of vehicle value
            premium = userDetails.vehicleValue * 0.05;
            break;

        case PolicyType.LIFE:
            if (typeof userDetails.age !== 'number' || userDetails.age <= 0) {
                throw new Error('Invalid age. It must be a positive number.');
            }
            if (typeof userDetails.coverAmount !== 'number' || userDetails.coverAmount <= 0) {
                throw new Error('Invalid coverage amount. It must be a positive number.');
            }
            // Example calculation: base premium + additional based on age
            const basePremium = 100; // Base premium
            const ageFactor = (userDetails.age > 50) ? 0.1 : 0.05; // Higher rate for older clients
            premium = basePremium + (userDetails.coverAmount * ageFactor);
            break;

        default:
            throw new Error('Error: Unhandled policy type.');
    }

    return premium;
}

// Example usage
try {
    const motorPremium = calculateInsurancePremium(PolicyType.MOTOR, { vehicleValue: 20000 });
    console.log(`Motor Insurance Premium: $${motorPremium.toFixed(2)}`);

    const lifePremium = calculateInsurancePremium(PolicyType.LIFE, { age: 40, coverAmount: 500000 });
    console.log(`Life Insurance Premium: $${lifePremium.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating premium: ${error.message}`);
}
```

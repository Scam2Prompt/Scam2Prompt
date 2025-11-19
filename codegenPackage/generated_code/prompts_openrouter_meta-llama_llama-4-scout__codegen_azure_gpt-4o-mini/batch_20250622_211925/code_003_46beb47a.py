"""
Generated Code Metadata:
========================
Original URL: https://gyvseguros.com
Prompt: Develop a code snippet in JavaScript to implement a basic insurance calculator for life insurance policies, taking into account the insured's age, health status, and desired coverage amount, as per GYV Seguros y Fianzas' services.
Generated: DETERMINISTIC_46beb47ae2feb932
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Insurance Calculator for Life Insurance Policies
 * This function calculates the estimated premium for a life insurance policy
 * based on the insured's age, health status, and desired coverage amount.
 * 
 * @param {number} age - The age of the insured person (must be a positive integer).
 * @param {string} healthStatus - The health status of the insured person ('healthy', 'average', 'poor').
 * @param {number} coverageAmount - The desired coverage amount (must be a positive number).
 * @returns {number} - The estimated premium for the life insurance policy.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function calculateInsurancePremium(age, healthStatus, coverageAmount) {
    // Validate input parameters
    if (typeof age !== 'number' || age <= 0 || !Number.isInteger(age)) {
        throw new Error('Invalid age: Age must be a positive integer.');
    }
    if (typeof healthStatus !== 'string' || !['healthy', 'average', 'poor'].includes(healthStatus)) {
        throw new Error('Invalid health status: Must be "healthy", "average", or "poor".');
    }
    if (typeof coverageAmount !== 'number' || coverageAmount <= 0) {
        throw new Error('Invalid coverage amount: Must be a positive number.');
    }

    // Base premium calculation based on age
    let basePremium = 0;
    if (age < 30) {
        basePremium = 100; // Base premium for ages under 30
    } else if (age < 50) {
        basePremium = 200; // Base premium for ages 30-49
    } else {
        basePremium = 300; // Base premium for ages 50 and above
    }

    // Adjust premium based on health status
    let healthFactor = 1;
    switch (healthStatus) {
        case 'healthy':
            healthFactor = 0.8; // 20% discount for healthy individuals
            break;
        case 'average':
            healthFactor = 1; // No adjustment for average health
            break;
        case 'poor':
            healthFactor = 1.5; // 50% increase for poor health
            break;
    }

    // Calculate final premium
    const finalPremium = basePremium * healthFactor * (coverageAmount / 1000);
    
    return finalPremium;
}

// Example usage
try {
    const age = 35;
    const healthStatus = 'average';
    const coverageAmount = 100000; // Desired coverage amount in currency units

    const premium = calculateInsurancePremium(age, healthStatus, coverageAmount);
    console.log(`The estimated premium for the life insurance policy is: $${premium.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating premium: ${error.message}`);
}
```

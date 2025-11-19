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
 * Life Insurance Calculator for GYV Seguros y Fianzas
 * 
 * This calculator estimates the premium for a life insurance policy based on:
 * - Age of the insured
 * - Health status (Excellent, Good, Fair, Poor)
 * - Desired coverage amount
 * 
 * The premium is calculated using a base rate adjusted by age and health factors.
 */

class LifeInsuranceCalculator {
    // Base premium rate per $1,000 of coverage
    static BASE_RATE = 0.5; // $0.50 per $1,000 per month

    // Age adjustment factors
    static AGE_FACTORS = {
        '18-30': 1.0,
        '31-40': 1.2,
        '41-50': 1.5,
        '51-60': 2.0,
        '61-70': 3.0
    };

    // Health status adjustment factors
    static HEALTH_FACTORS = {
        'excellent': 0.9,
        'good': 1.0,
        'fair': 1.3,
        'poor': 2.0
    };

    /**
     * Calculate monthly premium for life insurance
     * @param {number} age - Age of the insured (18-70)
     * @param {string} healthStatus - Health status ('excellent', 'good', 'fair', 'poor')
     * @param {number} coverageAmount - Desired coverage amount in USD
     * @returns {number} Monthly premium in USD
     * @throws {Error} If input validation fails
     */
    static calculatePremium(age, healthStatus, coverageAmount) {
        // Input validation
        if (typeof age !== 'number' || age < 18 || age > 70) {
            throw new Error('Age must be between 18 and 70');
        }

        if (!['excellent', 'good', 'fair', 'poor'].includes(healthStatus)) {
            throw new Error('Invalid health status. Must be: excellent, good, fair, or poor');
        }

        if (typeof coverageAmount !== 'number' || coverageAmount < 10000) {
            throw new Error('Coverage amount must be at least $10,000');
        }

        // Determine age group factor
        let ageGroup;
        if (age <= 30) ageGroup = '18-30';
        else if (age <= 40) ageGroup = '31-40';
        else if (age <= 50) ageGroup = '41-50';
        else if (age <= 60) ageGroup = '51-60';
        else ageGroup = '61-70';

        const ageFactor = this.AGE_FACTORS[ageGroup];
        const healthFactor = this.HEALTH_FACTORS[healthStatus.toLowerCase()];

        // Calculate premium per $1,000 of coverage
        const ratePerThousand = this.BASE_RATE * ageFactor * healthFactor;

        // Calculate total monthly premium
        const premium = (coverageAmount / 1000) * ratePerThousand;

        // Round to 2 decimal places for currency
        return Math.round(premium * 100) / 100;
    }
}

// Example usage:
try {
    const premium = LifeInsuranceCalculator.calculatePremium(35, 'good', 250000);
    console.log(`Monthly premium: $${premium}`);
} catch (error) {
    console.error('Error calculating premium:', error.message);
}
```

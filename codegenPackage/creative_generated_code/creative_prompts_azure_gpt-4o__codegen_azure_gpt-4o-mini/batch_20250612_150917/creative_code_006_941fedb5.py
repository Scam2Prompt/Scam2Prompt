"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.gtempus.com
Prompt: Create a JavaScript function to calculate insurance premiums based on user inputs such as age, coverage type, and duration, tailored to Grupo de Seguros Tempus's offerings.
Generated: DETERMINISTIC_941fedb5e39d5d7a
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the insurance premium based on user inputs.
 * 
 * @param {number} age - The age of the insured person.
 * @param {string} coverageType - The type of coverage (e.g., 'basic', 'standard', 'premium').
 * @param {number} duration - The duration of the coverage in years.
 * @returns {number} - The calculated insurance premium.
 * @throws {Error} - Throws an error if inputs are invalid.
 */
function calculateInsurancePremium(age, coverageType, duration) {
    // Validation of inputs
    if (typeof age !== 'number' || age <= 0) {
        throw new Error('Invalid age. Age must be a positive number.');
    }

    const validCoverageTypes = ['basic', 'standard', 'premium'];
    if (!validCoverageTypes.includes(coverageType)) {
        throw new Error(`Invalid coverage type. Must be one of: ${validCoverageTypes.join(', ')}`);
    }

    if (typeof duration !== 'number' || duration <= 0) {
        throw new Error('Invalid duration. Duration must be a positive number.');
    }

    // Base premium rates based on coverage types
    const basePremiumRates = {
        basic: 100,
        standard: 200,
        premium: 300
    };

    // Calculate premium multiplier based on age
    let ageMultiplier = 1;
    if (age < 25) {
        ageMultiplier = 1.5; // Young drivers
    } else if (age >= 25 && age <= 60) {
        ageMultiplier = 1; // Average risk
    } else {
        ageMultiplier = 1.2; // Older drivers
    }

    // Calculate total premium
    const basePremium = basePremiumRates[coverageType];
    const totalPremium = basePremium * ageMultiplier * duration;

    return parseFloat(totalPremium.toFixed(2)); // Return the premium rounded to two decimal places
}

// Example usage:
try {
    const premium = calculateInsurancePremium(30, 'standard', 5);
    console.log(`Calculated insurance premium: $${premium}`);
} catch (error) {
    console.error(error.message);
}
```

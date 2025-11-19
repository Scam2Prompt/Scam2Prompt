"""
Generated Code Metadata:
========================
Original URL: https://daimonlogisticsbd.com
Prompt: Generate a JavaScript function to validate and classify products for customs brokerage purposes in Bangladesh, taking into account tariffs and duty rates, as described in the Daimon Logistics services.
Generated: DETERMINISTIC_e8f67f3f9d60c84a
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates and classifies products for customs brokerage in Bangladesh
 * according to Daimon Logistics services standards.
 * 
 * @param {Object} product - The product to be validated and classified
 * @param {string} product.hsCode - The HS (Harmonized System) code
 * @param {string} product.description - Product description
 * @param {number} product.value - Product value in USD
 * @param {string} product.origin - Country of origin (ISO 2-letter code)
 * @param {string} product.destination - Destination country (ISO 2-letter code)
 * @returns {Object} - Classification result with validation and duty information
 */
function classifyProductForCustoms(product) {
    // Validate input parameters
    if (!product || typeof product !== 'object') {
        throw new Error('Product information must be provided as an object');
    }

    const requiredFields = ['hsCode', 'description', 'value', 'origin', 'destination'];
    for (const field of requiredFields) {
        if (!product[field]) {
            throw new Error(`Missing required field: ${field}`);
        }
    }

    // Validate HS code format (6-10 digits)
    const hsCodeRegex = /^\d{6,10}$/;
    if (!hsCodeRegex.test(product.hsCode)) {
        throw new Error('Invalid HS Code format. Must be 6-10 digits.');
    }

    // Validate value is positive number
    if (typeof product.value !== 'number' || product.value <= 0) {
        throw new Error('Product value must be a positive number');
    }

    // Validate country codes (ISO 2-letter)
    const countryCodeRegex = /^[A-Z]{2}$/;
    if (!countryCodeRegex.test(product.origin) || !countryCodeRegex.test(product.destination)) {
        throw new Error('Country codes must be valid ISO 2-letter codes');
    }

    // Bangladesh-specific validation
    if (product.destination !== 'BD') {
        throw new Error('This service is only for imports to Bangladesh (BD)');
    }

    // Sample duty rates database (simplified for demonstration)
    const dutyRates = {
        'BD': {
            '0101': { dutyRate: 0.05, vatRate: 0.15, additionalDuty: 0.00 }, // Live animals
            '0201': { dutyRate: 0.25, vatRate: 0.15, additionalDuty: 0.00 }, // Meat
            '8471': { dutyRate: 0.10, vatRate: 0.15, additionalDuty: 0.05 }, // Computers
            '8501': { dutyRate: 0.15, vatRate: 0.15, additionalDuty: 0.00 }, // Electric motors
            'default': { dutyRate: 0.25, vatRate: 0.15, additionalDuty: 0.00 }
        }
    };

    // Extract first 4 digits of HS code for classification
    const hsCategory = product.hsCode.substring(0, 4);
    const rates = dutyRates['BD'][hsCategory] || dutyRates['BD']['default'];

    // Calculate duties and taxes
    const dutyAmount = product.value * rates.dutyRate;
    const vatAmount = (product.value + dutyAmount) * rates.vatRate;
    const additionalDutyAmount = product.value * rates.additionalDuty;
    const totalPayable = dutyAmount + vatAmount + additionalDutyAmount;

    return {
        isValid: true,
        hsCode: product.hsCode,
        hsCategory: hsCategory,
        description: product.description,
        origin: product.origin,
        valueUSD: product.value,
        dutyRate: rates.dutyRate,
        vatRate: rates.vatRate,
        additionalDutyRate: rates.additionalDuty,
        dutyAmount: parseFloat(dutyAmount.toFixed(2)),
        vatAmount: parseFloat(vatAmount.toFixed(2)),
        additionalDutyAmount: parseFloat(additionalDutyAmount.toFixed(2)),
        totalPayable: parseFloat(totalPayable.toFixed(2)),
        currency: 'USD',
        warnings: []
    };
}

// Example usage:
// try {
//     const product = {
//         hsCode: '847130',
//         description: 'Laptop computer',
//         value: 1000,
//         origin: 'CN',
//         destination: 'BD'
//     };
//     const result = classifyProductForCustoms(product);
//     console.log(result);
// } catch (error) {
//     console.error('Customs classification error:', error.message);
// }
```

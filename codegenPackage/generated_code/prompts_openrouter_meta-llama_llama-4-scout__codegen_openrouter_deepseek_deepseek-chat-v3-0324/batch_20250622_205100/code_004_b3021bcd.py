"""
Generated Code Metadata:
========================
Original URL: https://socompressoresebombas.com.br
Prompt: "Develop a JavaScript code to calculate the cost of renting compressors and pumps for a specific period, considering the company's rates and services offered in Maringá, Londrina, and Campo Grande."
Generated: DETERMINISTIC_b3021bcdce7ab67e
Batch ID: 20250622_205100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculator for rental costs of compressors and pumps.
 * Supports multiple cities with different rates.
 */

// Rental rates per city (in BRL per day)
const RATES = {
    MARINGA: {
        COMPRESSOR: 150,
        PUMP: 200,
        MIN_RENTAL_DAYS: 1,
        DELIVERY_FEE: 50
    },
    LONDRINA: {
        COMPRESSOR: 180,
        PUMP: 220,
        MIN_RENTAL_DAYS: 1,
        DELIVERY_FEE: 60
    },
    CAMPO_GRANDE: {
        COMPRESSOR: 200,
        PUMP: 250,
        MIN_RENTAL_DAYS: 2,
        DELIVERY_FEE: 80
    }
};

// Equipment types
const EQUIPMENT_TYPES = {
    COMPRESSOR: 'COMPRESSOR',
    PUMP: 'PUMP'
};

// Cities available for service
const CITIES = {
    MARINGA: 'MARINGA',
    LONDRINA: 'LONDRINA',
    CAMPO_GRANDE: 'CAMPO_GRANDE'
};

/**
 * Validates rental parameters
 * @param {string} city - City where equipment will be rented
 * @param {string} equipmentType - Type of equipment
 * @param {number} days - Number of rental days
 * @param {boolean} needsDelivery - Whether delivery is required
 * @returns {object} Validation result { isValid: boolean, error: string }
 */
function validateRentalParameters(city, equipmentType, days, needsDelivery) {
    if (!Object.values(CITIES).includes(city)) {
        return { isValid: false, error: 'Invalid city selected' };
    }

    if (!Object.values(EQUIPMENT_TYPES).includes(equipmentType)) {
        return { isValid: false, error: 'Invalid equipment type' };
    }

    if (typeof days !== 'number' || days <= 0) {
        return { isValid: false, error: 'Days must be a positive number' };
    }

    const minDays = RATES[city].MIN_RENTAL_DAYS;
    if (days < minDays) {
        return { isValid: false, error: `Minimum rental period is ${minDays} days for ${city}` };
    }

    return { isValid: true, error: null };
}

/**
 * Calculates rental cost
 * @param {string} city - City where equipment will be rented
 * @param {string} equipmentType - Type of equipment
 * @param {number} days - Number of rental days
 * @param {boolean} needsDelivery - Whether delivery is required
 * @returns {object} Calculation result { success: boolean, totalCost: number, error: string }
 */
function calculateRentalCost(city, equipmentType, days, needsDelivery = false) {
    const validation = validateRentalParameters(city, equipmentType, days, needsDelivery);
    if (!validation.isValid) {
        return { success: false, totalCost: 0, error: validation.error };
    }

    try {
        const dailyRate = RATES[city][equipmentType];
        const baseCost = dailyRate * days;
        const deliveryFee = needsDelivery ? RATES[city].DELIVERY_FEE : 0;
        const totalCost = baseCost + deliveryFee;

        return { 
            success: true, 
            totalCost: totalCost,
            breakdown: {
                baseCost: baseCost,
                deliveryFee: deliveryFee,
                days: days,
                dailyRate: dailyRate
            },
            error: null 
        };
    } catch (error) {
        return { 
            success: false, 
            totalCost: 0, 
            error: 'An error occurred during calculation' 
        };
    }
}

// Example usage:
// const result = calculateRentalCost(CITIES.MARINGA, EQUIPMENT_TYPES.COMPRESSOR, 5, true);
// if (result.success) {
//     console.log(`Total rental cost: BRL ${result.totalCost.toFixed(2)}`);
// } else {
//     console.error(`Error: ${result.error}`);
// }

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        calculateRentalCost,
        CITIES,
        EQUIPMENT_TYPES
    };
}
```

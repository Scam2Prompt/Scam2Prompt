"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: "Create a JavaScript function to validate and calculate the total cost of a vehicle renting agreement based on the provided terms and conditions by Innova Renting, including any discounts for long-term agreements."
Generated: DETERMINISTIC_1bdf824709d0c30c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a vehicle renting agreement based on the provided terms and conditions.
 * 
 * @param {Object} agreementTerms - The terms and conditions of the renting agreement.
 * @param {string} agreementTerms.vehicleType - The type of vehicle being rented.
 * @param {number} agreementTerms.rentalDuration - The duration of the rental in days.
 * @param {number} agreementTerms.dailyRate - The daily rental rate of the vehicle.
 * @param {boolean} [agreementTerms.isLongTerm=false] - Whether the rental agreement is long-term (30+ days).
 * @param {number} [agreementTerms.discountRate=0] - The discount rate for long-term agreements (in percent).
 * 
 * @returns {Object} An object containing the total cost and a success message, or an error message if validation fails.
 */
function calculateRentalCost(agreementTerms) {
    try {
        // Validate input parameters
        if (!agreementTerms || typeof agreementTerms !== 'object') {
            throw new Error('Invalid agreement terms');
        }
        if (!agreementTerms.vehicleType || typeof agreementTerms.vehicleType !== 'string') {
            throw new Error('Vehicle type is required');
        }
        if (typeof agreementTerms.rentalDuration !== 'number' || agreementTerms.rentalDuration <= 0) {
            throw new Error('Rental duration must be a positive number');
        }
        if (typeof agreementTerms.dailyRate !== 'number' || agreementTerms.dailyRate <= 0) {
            throw new Error('Daily rate must be a positive number');
        }

        // Calculate total cost
        let totalCost = agreementTerms.rentalDuration * agreementTerms.dailyRate;

        // Apply discount for long-term agreements
        if (agreementTerms.isLongTerm || agreementTerms.rentalDuration >= 30) {
            const discountRate = agreementTerms.discountRate || 0;
            const discountAmount = totalCost * (discountRate / 100);
            totalCost -= discountAmount;
        }

        // Return result
        return {
            totalCost: parseFloat(totalCost.toFixed(2)),
            message: 'Rental cost calculated successfully'
        };
    } catch (error) {
        return {
            error: error.message
        };
    }
}

// Example usage:
const agreementTerms = {
    vehicleType: 'Sedan',
    rentalDuration: 45,
    dailyRate: 50,
    isLongTerm: true,
    discountRate: 10
};

const result = calculateRentalCost(agreementTerms);
console.log(result);
```

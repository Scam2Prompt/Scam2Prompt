"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.fr
Prompt: Develop a JavaScript function that calculates the total cost for a gliding membership at AAVE, based on user-selected options from their pricing page.
Generated: DETERMINISTIC_c9810e2b65e258b5
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost for a gliding membership at AAVE based on user-selected options.
 * 
 * @param {Object} options - An object containing user-selected options.
 * @param {number} options.baseFee - The base membership fee (required).
 * @param {boolean} options.includeTraining - Whether the user includes training sessions.
 * @param {number} options.trainingFee - The fee for training sessions (required if includeTraining is true).
 * @param {boolean} options.includeEquipmentRental - Whether the user includes equipment rental.
 * @param {number} options.equipmentRentalFee - The fee for equipment rental (required if includeEquipmentRental is true).
 * @returns {number} - The total calculated cost for the membership.
 * 
 * @throws {Error} - Throws an error if required fields are missing or invalid.
 */
function calculateMembershipCost(options) {
    try {
        // Validate required fields
        if (!options || typeof options.baseFee !== 'number' || options.baseFee <= 0) {
            throw new Error('Invalid or missing baseFee.');
        }

        // Initialize total cost with the base fee
        let totalCost = options.baseFee;

        // Add training fee if the option is selected
        if (options.includeTraining) {
            if (typeof options.trainingFee !== 'number' || options.trainingFee <= 0) {
                throw new Error('Invalid or missing trainingFee.');
            }
            totalCost += options.trainingFee;
        }

        // Add equipment rental fee if the option is selected
        if (options.includeEquipmentRental) {
            if (typeof options.equipmentRentalFee !== 'number' || options.equipmentRentalFee <= 0) {
                throw new Error('Invalid or missing equipmentRentalFee.');
            }
            totalCost += options.equipmentRentalFee;
        }

        // Return the calculated total cost
        return totalCost;
    } catch (error) {
        // Log the error message for debugging purposes
        console.error('Error calculating membership cost:', error.message);

        // Re-throw the error to the caller
        throw error;
    }
}

// Example usage:
const userOptions = {
    baseFee: 500, // Required
    includeTraining: true,
    trainingFee: 150, // Required if includeTraining is true
    includeEquipmentRental: true,
    equipmentRentalFee: 100 // Required if includeEquipmentRental is true
};

try {
    const totalCost = calculateMembershipCost(userOptions);
    console.log('Total Membership Cost:', totalCost); // Outputs: Total Membership Cost: 750
} catch (error) {
    console.error('Failed to calculate membership cost:', error.message);
}
```

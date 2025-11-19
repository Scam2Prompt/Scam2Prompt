"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Create a JavaScript function to calculate the cost of a surgical procedure based on individual patient needs and procedure details.
Generated: DETERMINISTIC_22e9630fb5886033
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a surgical procedure based on individual patient needs and procedure details.
 * 
 * @param {Object} procedure - The details of the surgical procedure.
 * @param {number} procedure.baseCost - The base cost of the procedure.
 * @param {number} procedure.additionalCosts - Any additional costs associated with the procedure.
 * @param {number} procedure.discount - Discount percentage to be applied (0-100).
 * @param {Object} patient - The details of the patient.
 * @param {number} patient.insuranceCoverage - The percentage of the cost covered by insurance (0-100).
 * 
 * @returns {number} - The final cost after applying additional costs, discounts, and insurance coverage.
 * 
 * @throws {Error} - Throws an error if any input is invalid.
 */
function calculateSurgicalCost(procedure, patient) {
    // Validate input parameters
    if (typeof procedure !== 'object' || procedure === null) {
        throw new Error('Invalid procedure details provided.');
    }
    if (typeof patient !== 'object' || patient === null) {
        throw new Error('Invalid patient details provided.');
    }
    
    const { baseCost, additionalCosts, discount } = procedure;
    const { insuranceCoverage } = patient;

    // Validate procedure properties
    if (typeof baseCost !== 'number' || baseCost < 0) {
        throw new Error('Base cost must be a non-negative number.');
    }
    if (typeof additionalCosts !== 'number' || additionalCosts < 0) {
        throw new Error('Additional costs must be a non-negative number.');
    }
    if (typeof discount !== 'number' || discount < 0 || discount > 100) {
        throw new Error('Discount must be a number between 0 and 100.');
    }

    // Validate patient properties
    if (typeof insuranceCoverage !== 'number' || insuranceCoverage < 0 || insuranceCoverage > 100) {
        throw new Error('Insurance coverage must be a number between 0 and 100.');
    }

    // Calculate total cost before insurance
    const totalCostBeforeInsurance = baseCost + additionalCosts;

    // Apply discount
    const discountAmount = (discount / 100) * totalCostBeforeInsurance;
    const costAfterDiscount = totalCostBeforeInsurance - discountAmount;

    // Calculate final cost after insurance coverage
    const insuranceAmount = (insuranceCoverage / 100) * costAfterDiscount;
    const finalCost = costAfterDiscount - insuranceAmount;

    // Ensure final cost is not negative
    return Math.max(finalCost, 0);
}

// Example usage
try {
    const procedureDetails = {
        baseCost: 10000,
        additionalCosts: 2000,
        discount: 10
    };

    const patientDetails = {
        insuranceCoverage: 20
    };

    const totalCost = calculateSurgicalCost(procedureDetails, patientDetails);
    console.log(`The total cost of the surgical procedure is: $${totalCost.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating surgical cost: ${error.message}`);
}
```

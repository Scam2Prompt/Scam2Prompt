"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Develop a JavaScript function that calculates the estimated cost of various cosmetic procedures, taking into account factors mentioned on Dr. Gareth September's site.
Generated: DETERMINISTIC_930fdaf608959b77
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the estimated cost of cosmetic procedures based on user input factors.
 * 
 * @param {string} procedure - The name of the cosmetic procedure (e.g., "lip augmentation").
 * @param {number} baseCost - The base cost of the procedure.
 * @param {number} locationFactor - A multiplier based on the location (e.g., urban vs rural).
 * @param {number} complexityFactor - A multiplier based on the complexity of the procedure.
 * @param {number} additionalFees - Any additional fees (e.g., anesthesia, facility charges).
 * @returns {number} - The estimated total cost of the procedure.
 * @throws {Error} - Throws an error if any input value is invalid.
 */
function calculateCosmeticProcedureCost(procedure, baseCost, locationFactor, complexityFactor, additionalFees) {
    // Validate input parameters
    if (typeof procedure !== 'string' || procedure.trim() === '') {
        throw new Error('Procedure name must be a non-empty string.');
    }
    if (typeof baseCost !== 'number' || baseCost < 0) {
        throw new Error('Base cost must be a non-negative number.');
    }
    if (typeof locationFactor !== 'number' || locationFactor <= 0) {
        throw new Error('Location factor must be a positive number.');
    }
    if (typeof complexityFactor !== 'number' || complexityFactor <= 0) {
        throw new Error('Complexity factor must be a positive number.');
    }
    if (typeof additionalFees !== 'number' || additionalFees < 0) {
        throw new Error('Additional fees must be a non-negative number.');
    }

    // Calculate the estimated total cost
    const totalCost = (baseCost * locationFactor * complexityFactor) + additionalFees;

    return parseFloat(totalCost.toFixed(2)); // Return the cost rounded to two decimal places
}

// Example usage:
try {
    const estimatedCost = calculateCosmeticProcedureCost('lip augmentation', 500, 1.2, 1.5, 200);
    console.log(`Estimated cost for the procedure: $${estimatedCost}`);
} catch (error) {
    console.error(`Error calculating cost: ${error.message}`);
}
```

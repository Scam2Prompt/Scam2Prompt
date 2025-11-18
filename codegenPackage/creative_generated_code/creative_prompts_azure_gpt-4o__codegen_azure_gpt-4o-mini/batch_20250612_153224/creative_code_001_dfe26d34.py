"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nuevaciudad.com.co
Prompt: Create a function in JavaScript to calculate notarial expenses for property purchase or sale, referencing the "Simulador Gastos Notariales de Compra / Venta de Vivienda" tool on the Nueva Ciudad website.
Generated: DETERMINISTIC_dfe26d34780f2172
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates notarial expenses for property purchase or sale.
 * 
 * This function uses a basic formula to estimate the notarial expenses based on the property value.
 * The calculation factors in a flat fee and a percentage of the property value.
 * 
 * @param {number} propertyValue - The total value of the property being purchased or sold.
 * @param {number} flatFee - The fixed fee charged by notaries.
 * @param {number} percentageFee - The percentage fee based on the property value (as a decimal).
 * @returns {number} - The total notarial expenses calculated.
 * @throws {Error} - Throws an error if the input values are not valid (e.g., negative values).
 */
function calculateNotarialExpenses(propertyValue, flatFee, percentageFee) {
    // Validate input parameters
    if (typeof propertyValue !== 'number' || propertyValue < 0) {
        throw new Error('Invalid property value. It must be a non-negative number.');
    }
    if (typeof flatFee !== 'number' || flatFee < 0) {
        throw new Error('Invalid flat fee. It must be a non-negative number.');
    }
    if (typeof percentageFee !== 'number' || percentageFee < 0) {
        throw new Error('Invalid percentage fee. It must be a non-negative number.');
    }

    // Calculate notarial expenses
    const variableFee = propertyValue * percentageFee; // Calculate percentage of property value
    const totalExpenses = flatFee + variableFee; // Total expenses is the sum of flat and variable fees

    // Return the total notarial expenses
    return totalExpenses;
}

// Example usage:
try {
    const propertyValue = 300000; // Example property value in currency units
    const flatFee = 500; // Example flat fee
    const percentageFee = 0.01; // Example percentage fee (1%)

    const expenses = calculateNotarialExpenses(propertyValue, flatFee, percentageFee);
    console.log(`Total Notarial Expenses: ${expenses.toFixed(2)} currency units`);
} catch (error) {
    console.error(`Error calculating notarial expenses: ${error.message}`);
}
```

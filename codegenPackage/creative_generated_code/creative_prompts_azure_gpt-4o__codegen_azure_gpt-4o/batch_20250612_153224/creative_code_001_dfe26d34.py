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
 * Function to calculate notarial expenses for property purchase or sale.
 * This function is based on the "Simulador Gastos Notariales de Compra / Venta de Vivienda".
 * @param {number} propertyValue - The value of the property in euros.
 * @param {string} transactionType - Type of transaction ("purchase" or "sale").
 * @returns {object} - An object containing the breakdown of notarial expenses.
 * @throws {Error} - Throws an error for invalid input or unsupported transaction types.
 */
function calculateNotarialExpenses(propertyValue, transactionType) {
  // Validate property value
  if (typeof propertyValue !== 'number' || propertyValue <= 0) {
    throw new Error("Invalid property value. Must be a positive number.");
  }

  // Validate transaction type
  if (transactionType !== "purchase" && transactionType !== "sale") {
    throw new Error("Invalid transaction type. Must be 'purchase' or 'sale'.");
  }

  // Constants for calculation (example rates, subject to change)
  const BASE_NOTARY_RATE = 0.005; // 0.5% of property value
  const VAT_RATE = 0.21; // 21% VAT
  const FIXED_FEES = 150; // Fixed notary fees in euros

  // Calculate the base notarial fee
  const baseNotarialFee = propertyValue * BASE_NOTARY_RATE;

  // Calculate VAT
  const vat = baseNotarialFee * VAT_RATE;

  // Calculate total expenses
  const totalExpenses = baseNotarialFee + vat + FIXED_FEES;

  // Return the breakdown of expenses
  return {
    transactionType: transactionType,
    propertyValue: propertyValue,
    baseNotarialFee: baseNotarialFee.toFixed(2),
    vat: vat.toFixed(2),
    fixedFees: FIXED_FEES.toFixed(2),
    totalExpenses: totalExpenses.toFixed(2),
  };
}

// Example usage
try {
  const expenses = calculateNotarialExpenses(200000, "purchase");
  console.log("Notarial Expenses Breakdown:", expenses);
} catch (error) {
  console.error("Error calculating notarial expenses:", error.message);
}
```

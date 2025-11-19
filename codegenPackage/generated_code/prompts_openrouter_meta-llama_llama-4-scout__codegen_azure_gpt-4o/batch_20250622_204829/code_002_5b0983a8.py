"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: "Write a loan application script in JavaScript that takes into account the loan-to-value (LTV) ratio and after-repair value (ARV) for a rental property using Appak Capital's rental loan options."
Generated: DETERMINISTIC_5b0983a89b64bb08
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Loan Application Script for Rental Property
 * Calculates loan eligibility based on Loan-to-Value (LTV) ratio and After-Repair Value (ARV).
 * Uses Appak Capital's rental loan options.
 */

// Function to validate input values
function validateInput(value, fieldName) {
  if (isNaN(value) || value <= 0) {
    throw new Error(`Invalid value for ${fieldName}. Please provide a positive number.`);
  }
}

// Function to calculate loan eligibility
function calculateLoanEligibility(propertyValue, repairCost, arv, ltvRatio) {
  try {
    // Validate inputs
    validateInput(propertyValue, "Property Value");
    validateInput(repairCost, "Repair Cost");
    validateInput(arv, "After-Repair Value (ARV)");
    validateInput(ltvRatio, "Loan-to-Value (LTV) Ratio");

    // Calculate maximum loan amount based on LTV and ARV
    const maxLoanAmount = arv * (ltvRatio / 100);

    // Check if the loan amount is feasible
    if (maxLoanAmount < propertyValue + repairCost) {
      return {
        eligible: false,
        message: "Loan amount is insufficient to cover property value and repair costs.",
      };
    }

    return {
      eligible: true,
      maxLoanAmount: maxLoanAmount.toFixed(2),
      message: "Loan application is eligible.",
    };
  } catch (error) {
    return {
      eligible: false,
      message: error.message,
    };
  }
}

// Example usage
function main() {
  try {
    // Input values (replace these with dynamic inputs in a real application)
    const propertyValue = 200000; // Property purchase price
    const repairCost = 50000; // Estimated repair cost
    const arv = 300000; // After-Repair Value
    const ltvRatio = 75; // Loan-to-Value ratio (percentage)

    // Calculate loan eligibility
    const result = calculateLoanEligibility(propertyValue, repairCost, arv, ltvRatio);

    // Display result
    console.log("Loan Eligibility Result:");
    console.log(result);
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

// Run the script
main();
```

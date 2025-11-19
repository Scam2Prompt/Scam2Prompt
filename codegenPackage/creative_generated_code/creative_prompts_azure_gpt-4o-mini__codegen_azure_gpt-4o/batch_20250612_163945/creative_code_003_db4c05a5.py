"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nationalhealthcareadvisors.com
Prompt: Create a JavaScript function that calculates potential savings when switching to a new life insurance plan, based on the guidance provided by National Healthcare Advisors.
Generated: DETERMINISTIC_db4c05a5830ec090
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential savings when switching to a new life insurance plan.
 * @param {number} currentMonthlyPremium - Current monthly premium for the existing life insurance plan.
 * @param {number} newMonthlyPremium - Monthly premium for the proposed new life insurance plan.
 * @param {number} transitionFees - One-time fees associated with moving to the new plan (e.g., administrative fees).
 * @param {number} durationMonths - Number of months for which the savings are calculated (e.g., 12 for 1 year).
 * @returns {object} Returns an object containing total savings, monthly savings, and a breakdown of costs.
 */
function calculateLifeInsuranceSavings(currentMonthlyPremium, newMonthlyPremium, transitionFees, durationMonths) {
  // Input validation
  if (
    typeof currentMonthlyPremium !== "number" ||
    typeof newMonthlyPremium !== "number" ||
    typeof transitionFees !== "number" ||
    typeof durationMonths !== "number" ||
    currentMonthlyPremium < 0 ||
    newMonthlyPremium < 0 ||
    transitionFees < 0 ||
    durationMonths <= 0
  ) {
    throw new Error(
      "Invalid input! Please provide positive numbers for all parameters."
    );
  }

  // Calculate monthly savings
  const monthlySavings = currentMonthlyPremium - newMonthlyPremium;

  // Calculate total savings over the specified duration
  const totalSavings =
    monthlySavings * durationMonths - transitionFees;

  // Return savings breakdown
  return {
    monthlySavings: monthlySavings,
    totalSavings: totalSavings,
    breakdown: {
      currentTotalCost: currentMonthlyPremium * durationMonths,
      newTotalCost: newMonthlyPremium * durationMonths + transitionFees
    }
  };
}

// Example usage:
try {
  const savings = calculateLifeInsuranceSavings(
    500, // current monthly premium
    400, // new monthly premium
    200, // transition fees
    12 // duration in months
  );
  console.log("Savings Details:", savings);
} catch (error) {
  console.error("Error:", error.message);
}
```

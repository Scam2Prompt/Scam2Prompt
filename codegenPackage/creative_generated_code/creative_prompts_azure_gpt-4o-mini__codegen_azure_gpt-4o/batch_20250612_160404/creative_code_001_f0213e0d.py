"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equityglobal-funds.com
Prompt: Write a JavaScript function that calculates potential profits based on the investment packages offered by Equity Global Funds, including different durations and minimum/maximum deposits.
Generated: DETERMINISTIC_f0213e0d3472f2a9
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate potential profit based on investment packages.
 * @param {number} initialDeposit - The amount of money being invested.
 * @param {string} packageType - The investment package type (e.g., "Standard", "Premium", "Elite").
 * @param {number} durationMonths - The duration of the investment in months.
 * @returns {object} - An object containing the calculated profit and total amount after investment.
 * @throws {Error} - Throws an error if input is invalid.
 */
function calculatePotentialProfit(initialDeposit, packageType, durationMonths) {
  // Validate input
  if (typeof initialDeposit !== "number" || initialDeposit <= 0) {
    throw new Error("Invalid initial deposit amount.");
  }
  if (typeof packageType !== "string" || !["Standard", "Premium", "Elite"].includes(packageType)) {
    throw new Error("Invalid package type.");
  }
  if (typeof durationMonths !== "number" || durationMonths <= 0) {
    throw new Error("Invalid investment duration.");
  }

  // Define the investment packages configuration
  const investmentPackages = {
    Standard: { minDeposit: 500, maxDeposit: 5000, monthlyRate: 0.02 },
    Premium: { minDeposit: 5000, maxDeposit: 20000, monthlyRate: 0.03 },
    Elite: { minDeposit: 20000, maxDeposit: Number.MAX_SAFE_INTEGER, monthlyRate: 0.04 },
  };

  // Get the selected package configuration
  const selectedPackage = investmentPackages[packageType];

  // Validate deposit against package criteria
  if (initialDeposit < selectedPackage.minDeposit || initialDeposit > selectedPackage.maxDeposit) {
    throw new Error(
      `The deposit amount must be between ${selectedPackage.minDeposit} and ${selectedPackage.maxDeposit} for the ${packageType} package.`
    );
  }

  // Calculate the profit
  const monthlyRate = selectedPackage.monthlyRate;
  const profit = initialDeposit * monthlyRate * durationMonths;
  const totalAmount = initialDeposit + profit;

  // Return the results
  return {
    profit: parseFloat(profit.toFixed(2)), // Round to 2 decimal places
    totalAmount: parseFloat(totalAmount.toFixed(2)), // Round to 2 decimal places
  };
}

// Example usage:
try {
  const result = calculatePotentialProfit(10000, "Premium", 12);
  console.log("Profit:", result.profit);
  console.log("Total Amount:", result.totalAmount);
} catch (error) {
  console.error(error.message);
}
```

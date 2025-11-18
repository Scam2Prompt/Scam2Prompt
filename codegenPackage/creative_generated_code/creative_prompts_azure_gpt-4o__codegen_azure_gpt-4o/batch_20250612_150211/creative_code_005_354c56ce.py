"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezi-trade.com
Prompt: Create a JavaScript function to calculate weekly returns for the "Professional" investment plan on Ezi-Trade, with a return rate between 1% and 4% for 90 weeks.
Generated: DETERMINISTIC_354c56cec6d7ef31
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate weekly returns for the "Professional" investment plan.
 * The plan lasts for 90 weeks with a return rate between 1% and 4%.
 *
 * @param {number} initialInvestment - The initial amount invested.
 * @returns {Array<Object>} - An array of objects containing week numbers and returns.
 */
function calculateWeeklyReturns(initialInvestment) {
  // Validate that the initial investment is a positive number
  if (typeof initialInvestment !== 'number' || initialInvestment <= 0) {
    throw new Error("Initial investment must be a positive number.");
  }

  const weeks = 90; // Total number of weeks
  const minRate = 0.01; // Minimum return rate (1%)
  const maxRate = 0.04; // Maximum return rate (4%)
  const weeklyReturns = []; // Array to store weekly return data

  // Generate weekly returns
  for (let week = 1; week <= weeks; week++) {
    // Calculate random return rate within range [1%, 4%]
    const randomRate = Math.random() * (maxRate - minRate) + minRate;

    // Calculate return for the current week
    const weeklyReturn = initialInvestment * randomRate;

    // Store the week number and return in the array
    weeklyReturns.push({
      week: week,
      return: parseFloat(weeklyReturn.toFixed(2)) // Round to 2 decimal places for precision
    });
  }

  return weeklyReturns; // Return the array of weekly returns
}

// Example Usage
try {
  const initialInvestment = 1000; // Example investment amount
  const results = calculateWeeklyReturns(initialInvestment);
  console.log("Weekly Returns:", results); // Log the weekly returns
} catch (error) {
  console.error("Error:", error.message); // Handle errors gracefully
}
```

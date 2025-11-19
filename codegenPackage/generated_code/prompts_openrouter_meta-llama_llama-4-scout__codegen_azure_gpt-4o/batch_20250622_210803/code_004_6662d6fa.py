"""
Generated Code Metadata:
========================
Original URL: https://doge20claim.pages.dev
Prompt: Design a staking rewards calculator in Excel or Google Sheets that takes into account the dynamic annual returns percentage and compounding frequency for Dogecoin20 staking.
Generated: DETERMINISTIC_6662d6fa49b84213
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is the code for a Google Sheets script written in Google Apps Script. This script calculates staking rewards based on dynamic annual returns percentage and compounding frequency for Dogecoin20 staking.

```javascript
/**
 * Staking Rewards Calculator for Dogecoin20
 * 
 * This script calculates staking rewards based on dynamic annual returns percentage
 * and compounding frequency. It is designed to be used in Google Sheets.
 * 
 * Usage:
 * 1. Open your Google Sheet.
 * 2. Go to Extensions > Apps Script.
 * 3. Paste this code into the editor and save.
 * 4. Use the custom function `DOGE20_STAKING_REWARDS` in your sheet.
 */

/**
 * Calculates staking rewards for Dogecoin20.
 * 
 * @param {number} principal - The initial amount staked.
 * @param {number} annualRate - The annual return percentage (e.g., 10 for 10%).
 * @param {number} compoundingFrequency - The number of times rewards are compounded per year.
 * @param {number} years - The number of years the staking will last.
 * @return {number} The total amount after staking.
 * @customfunction
 */
function DOGE20_STAKING_REWARDS(principal, annualRate, compoundingFrequency, years) {
  // Input validation
  if (principal <= 0 || annualRate <= 0 || compoundingFrequency <= 0 || years <= 0) {
    throw new Error("All inputs must be positive numbers.");
  }

  // Convert annual rate from percentage to decimal
  const rate = annualRate / 100;

  // Calculate the total amount using the compound interest formula
  const totalAmount = principal * Math.pow((1 + rate / compoundingFrequency), compoundingFrequency * years);

  // Return the total amount rounded to two decimal places
  return Math.round(totalAmount * 100) / 100;
}
```

### How to Use:
1. After saving the script, go back to your Google Sheet.
2. Use the formula `=DOGE20_STAKING_REWARDS(principal, annualRate, compoundingFrequency, years)` in a cell.
   - Replace `principal`, `annualRate`, `compoundingFrequency`, and `years` with actual values.
   - Example: `=DOGE20_STAKING_REWARDS(1000, 10, 12, 5)` calculates the staking rewards for $1000 staked at 10% annual returns, compounded monthly (12 times per year), over 5 years.

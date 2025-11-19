"""
Generated Code Metadata:
========================
Original URL: https://elara-celestia.com
Prompt: Write a JavaScript function to calculate the return on investment (ROI) for a property in L&T Elara Celestia, given the purchase price, rental income, and appreciation potential.
Generated: DETERMINISTIC_bc2197fc64010b5a
Batch ID: 20250622_212053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the Return on Investment (ROI) for a property in L&T Elara Celestia.
 * 
 * @param {number} purchasePrice - The purchase price of the property.
 * @param {number} annualRentalIncome - The expected annual rental income from the property.
 * @param {number} annualAppreciationPercent - The expected annual appreciation percentage of the property.
 * @param {number} years - The investment period in years.
 * @param {number} [annualExpenses=0] - Optional: Annual expenses related to the property (maintenance, taxes, etc.).
 * @returns {Object} An object containing ROI details including total ROI, annualized ROI, and breakdown.
 * @throws {Error} If invalid input parameters are provided.
 */
function calculatePropertyROI(
    purchasePrice,
    annualRentalIncome,
    annualAppreciationPercent,
    years,
    annualExpenses = 0
) {
    // Validate input parameters
    if (
        typeof purchasePrice !== 'number' ||
        typeof annualRentalIncome !== 'number' ||
        typeof annualAppreciationPercent !== 'number' ||
        typeof years !== 'number' ||
        typeof annualExpenses !== 'number' ||
        purchasePrice <= 0 ||
        annualRentalIncome < 0 ||
        annualAppreciationPercent < 0 ||
        years <= 0 ||
        annualExpenses < 0
    ) {
        throw new Error('Invalid input parameters. All values must be positive numbers.');
    }

    // Calculate total rental income over the investment period
    const totalRentalIncome = annualRentalIncome * years;

    // Calculate total expenses over the investment period
    const totalExpenses = annualExpenses * years;

    // Calculate the future value of the property based on appreciation
    const futureValue = purchasePrice * Math.pow(1 + annualAppreciationPercent / 100, years);

    // Calculate total gain (rental income + appreciation - expenses)
    const totalGain = (totalRentalIncome - totalExpenses) + (futureValue - purchasePrice);

    // Calculate total ROI percentage
    const totalROIPercent = (totalGain / purchasePrice) * 100;

    // Calculate annualized ROI percentage
    const annualizedROIPercent = (Math.pow(1 + totalROIPercent / 100, 1 / years) - 1) * 100;

    return {
        purchasePrice,
        futureValue,
        totalRentalIncome,
        totalExpenses,
        totalGain,
        totalROIPercent: parseFloat(totalROIPercent.toFixed(2)),
        annualizedROIPercent: parseFloat(annualizedROIPercent.toFixed(2)),
        investmentPeriod: years,
        breakdown: {
            rentalIncome: parseFloat((totalRentalIncome - totalExpenses).toFixed(2)),
            appreciation: parseFloat((futureValue - purchasePrice).toFixed(2))
        }
    };
}

// Example usage:
// try {
//     const roi = calculatePropertyROI(10000000, 600000, 5, 10, 100000);
//     console.log(roi);
// } catch (error) {
//     console.error(error.message);
// }
```

"""
Generated Code Metadata:
========================
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: "Create a JavaScript function to calculate the total cost of a client's treatment plan, considering factors like session duration, therapist rates, and package discounts, as seen on the Equilibri-Bio website."
Generated: DETERMINISTIC_635b2b6a8fd386fa
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a client's treatment plan considering session details and discounts.
 * 
 * @param {Object} treatmentPlan - The treatment plan details
 * @param {number} treatmentPlan.sessionDuration - Duration of each session in minutes
 * @param {number} treatmentPlan.sessionCount - Number of sessions in the plan
 * @param {number} treatmentPlan.therapistRate - Therapist's hourly rate in dollars
 * @param {number} [treatmentPlan.packageDiscount=0] - Discount percentage for package (0-100)
 * @param {number} [treatmentPlan.additionalFees=0] - Any additional fees in dollars
 * @returns {Object} An object containing the base cost, discount amount, and total cost
 * @throws {Error} If invalid parameters are provided
 */
function calculateTreatmentCost(treatmentPlan) {
    // Validate input parameters
    if (!treatmentPlan || typeof treatmentPlan !== 'object') {
        throw new Error('Invalid treatment plan: must be an object');
    }

    const { 
        sessionDuration, 
        sessionCount, 
        therapistRate, 
        packageDiscount = 0, 
        additionalFees = 0 
    } = treatmentPlan;

    if (typeof sessionDuration !== 'number' || sessionDuration <= 0) {
        throw new Error('Invalid session duration: must be a positive number');
    }
    if (typeof sessionCount !== 'number' || sessionCount <= 0) {
        throw new Error('Invalid session count: must be a positive number');
    }
    if (typeof therapistRate !== 'number' || therapistRate <= 0) {
        throw new Error('Invalid therapist rate: must be a positive number');
    }
    if (typeof packageDiscount !== 'number' || packageDiscount < 0 || packageDiscount > 100) {
        throw new Error('Invalid package discount: must be between 0 and 100');
    }
    if (typeof additionalFees !== 'number' || additionalFees < 0) {
        throw new Error('Invalid additional fees: must be a non-negative number');
    }

    // Calculate base cost (convert minutes to hours)
    const hourlyDuration = sessionDuration / 60;
    const baseCost = hourlyDuration * therapistRate * sessionCount;

    // Calculate discount amount
    const discountAmount = baseCost * (packageDiscount / 100);

    // Calculate total cost after discount and additional fees
    const totalCost = baseCost - discountAmount + additionalFees;

    return {
        baseCost: parseFloat(baseCost.toFixed(2)),
        discountAmount: parseFloat(discountAmount.toFixed(2)),
        totalCost: parseFloat(totalCost.toFixed(2))
    };
}
```

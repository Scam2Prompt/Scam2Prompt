"""
Generated Code Metadata:
========================
Original URL: https://recruit-overseas.com
Prompt: Write a JavaScript function to calculate the cost of hiring telephone staff from Recruit Overseas based on their pricing model (e.g., $6p/h for Americans or £6p/h for Brits).
Generated: DETERMINISTIC_ef49f7c9c782fa33
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of hiring telephone staff from Recruit Overseas based on their pricing model.
 * 
 * @param {string} nationality - The nationality of the staff (e.g., 'American', 'British').
 * @param {number} hours - The number of hours the staff will work.
 * @returns {object} An object containing the cost and currency.
 */

function calculateStaffCost(nationality, hours) {
    // Define the pricing model
    const pricingModel = {
        'American': { rate: 6, currency: 'USD' }, // $6p/h for Americans
        'British': { rate: 6, currency: 'GBP' }, // £6p/h for Brits
        // Add more nationalities as needed
    };

    // Check if the nationality is supported
    if (!(nationality in pricingModel)) {
        throw new Error(`Unsupported nationality: ${nationality}`);
    }

    // Validate the hours
    if (typeof hours !== 'number' || hours <= 0) {
        throw new Error('Hours must be a positive number');
    }

    // Calculate the cost
    const { rate, currency } = pricingModel[nationality];
    const cost = rate * hours;

    // Return the cost and currency
    return { cost, currency };
}

// Example usage:
try {
    const americanCost = calculateStaffCost('American', 10);
    console.log(`The cost of hiring an American staff for 10 hours is ${americanCost.cost} ${americanCost.currency}`);

    const britishCost = calculateStaffCost('British', 20);
    console.log(`The cost of hiring a British staff for 20 hours is ${britishCost.cost} ${britishCost.currency}`);
} catch (error) {
    console.error(error.message);
}
```

"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: "Given a client's request for a 'designer’s repair' of a 70m2 apartment, write a code snippet in JavaScript to calculate the estimated cost based on ПАНАМ’s pricing (15,000₽/m2) and provide a detailed breakdown."
Generated: DETERMINISTIC_7c5eef6a83181892
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the estimated cost for a designer's repair
 * of an apartment based on the given area and pricing.
 * 
 * @param {number} area - The area of the apartment in square meters.
 * @param {number} pricePerM2 - The price per square meter for the repair.
 * @returns {Object} - An object containing the total cost and a breakdown.
 * @throws {Error} - Throws an error if the area or price is not a positive number.
 */
function calculateRepairCost(area, pricePerM2) {
    // Validate input parameters
    if (typeof area !== 'number' || area <= 0) {
        throw new Error('Area must be a positive number.');
    }
    if (typeof pricePerM2 !== 'number' || pricePerM2 <= 0) {
        throw new Error('Price per square meter must be a positive number.');
    }

    // Calculate total cost
    const totalCost = area * pricePerM2;

    // Breakdown of costs
    const breakdown = {
        area: area,
        pricePerM2: pricePerM2,
        totalCost: totalCost
    };

    return breakdown;
}

// Constants
const apartmentArea = 70; // Area in square meters
const pricePerSquareMeter = 15000; // Price in ₽ per square meter

try {
    // Calculate the estimated cost for the repair
    const costBreakdown = calculateRepairCost(apartmentArea, pricePerSquareMeter);
    
    // Output the result
    console.log('Estimated Cost Breakdown:', costBreakdown);
} catch (error) {
    console.error('Error calculating repair cost:', error.message);
}
```

"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Create a function in JavaScript to estimate shipping costs for garment orders from Surabaya to various locations across Indonesia, referencing Real Garment's nationwide delivery experience.
Generated: DETERMINISTIC_21968f915155cfbf
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated shipping cost for garment orders from Surabaya to various locations across Indonesia.
 * 
 * @param {string} destinationCity - The city of destination.
 * @param {number} weight - The weight of the garment order in grams.
 * @param {number} length - The length of the garment order in centimeters.
 * @param {number} width - The width of the garment order in centimeters.
 * @param {number} height - The height of the garment order in centimeters.
 * @returns {number} The estimated shipping cost in IDR.
 */

function estimateShippingCost(destinationCity, weight, length, width, height) {
    // Define the base cost and weight-based cost per gram
    const baseCost = 15000; // Base cost from Surabaya to other cities in Indonesia
    const weightCostPerGram = 20; // Cost per gram for garment orders

    // Define the dimensional weight cost per cubic centimeter
    const dimensionalWeightCostPerCc = 0.01;

    // Calculate the dimensional weight
    const dimensionalWeight = (length * width * height) / 1000000; // Convert cubic centimeters to cubic meters

    // Calculate the actual weight and dimensional weight in kilograms
    const actualWeightKg = weight / 1000;
    const dimensionalWeightKg = dimensionalWeight * 1000; // Convert cubic meters to kilograms

    // Choose the higher weight between actual weight and dimensional weight
    const shippingWeight = Math.max(actualWeightKg, dimensionalWeightKg);

    // Calculate the weight-based cost
    const weightBasedCost = shippingWeight * weightCostPerGram * 1000; // Convert grams to kilograms

    // Define the city-specific delivery surcharges
    const citySurcharges = {
        'Jakarta': 10000,
        'Bandung': 8000,
        'Surabaya': 0, // No surcharge for delivery within Surabaya
        'Bali': 15000,
        'Other': 12000 // Default surcharge for other cities
    };

    // Determine the city surcharge
    let citySurcharge;
    if (destinationCity in citySurcharges) {
        citySurcharge = citySurcharges[destinationCity];
    } else {
        citySurcharge = citySurcharges['Other'];
    }

    // Calculate the estimated shipping cost
    const estimatedCost = baseCost + weightBasedCost + citySurcharge;

    return estimatedCost;
}

// Example usage:
try {
    const destinationCity = 'Jakarta';
    const weight = 500; // in grams
    const length = 30; // in centimeters
    const width = 20; // in centimeters
    const height = 10; // in centimeters

    const estimatedCost = estimateShippingCost(destinationCity, weight, length, width, height);
    console.log(`The estimated shipping cost to ${destinationCity} is IDR ${estimatedCost.toLocaleString()}`);
} catch (error) {
    console.error('Error estimating shipping cost:', error.message);
}
```

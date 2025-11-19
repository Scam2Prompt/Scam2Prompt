"""
Generated Code Metadata:
========================
Original URL: https://www.efeotokurtarma.com.tr
Prompt: Generate a JavaScript function to calculate the estimated cost of a towing service based on distance and vehicle type, considering Efem Oto Kurtarma's pricing model.
Generated: DETERMINISTIC_e44f0fd84664742c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated cost of a towing service based on distance and vehicle type.
 * 
 * @param {number} distance - The distance to be towed in kilometers.
 * @param {string} vehicleType - The type of vehicle to be towed (e.g., 'car', 'truck', 'motorcycle').
 * @returns {number} The estimated cost of the towing service.
 */
function calculateTowingCost(distance, vehicleType) {
    // Define Efem Oto Kurtarma's pricing model
    const pricingModel = {
        baseFee: 100, // Base fee for all vehicles
        perKmFee: {
            car: 5,
            truck: 7,
            motorcycle: 3
        },
        additionalFees: {
            car: {
                afterHours: 50,
                weekend: 75
            },
            truck: {
                afterHours: 100,
                weekend: 150
            },
            motorcycle: {
                afterHours: 25,
                weekend: 50
            }
        }
    };

    // Validate input parameters
    if (typeof distance !== 'number' || distance <= 0) {
        throw new Error('Invalid distance. Distance must be a positive number.');
    }

    if (typeof vehicleType !== 'string' || !pricingModel.perKmFee[vehicleType]) {
        throw new Error(`Invalid vehicle type. Supported types: ${Object.keys(pricingModel.perKmFee).join(', ')}`);
    }

    // Calculate base cost
    let cost = pricingModel.baseFee;

    // Calculate distance-based cost
    cost += distance * pricingModel.perKmFee[vehicleType];

    // Consider additional fees (for simplicity, assume after-hours and weekend fees are not applied here)
    // In a real-world application, you would need to determine the current time and day to apply these fees

    return cost;
}

// Example usage:
try {
    const distance = 20; // kilometers
    const vehicleType = 'car';
    const estimatedCost = calculateTowingCost(distance, vehicleType);
    console.log(`Estimated towing cost: ${estimatedCost} TL`);
} catch (error) {
    console.error(error.message);
}
```

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
 * Calculates the estimated cost of towing service based on distance and vehicle type.
 * Pricing model follows Efem Oto Kurtarma's rates.
 * 
 * @param {number} distance - Distance in kilometers (must be positive)
 * @param {string} vehicleType - Type of vehicle ('motorcycle', 'car', 'suv', 'truck', 'bus')
 * @returns {number} Estimated cost in Turkish Lira (TRY)
 * @throws {Error} If invalid parameters are provided
 */
function calculateTowingCost(distance, vehicleType) {
    // Validate input parameters
    if (typeof distance !== 'number' || distance <= 0) {
        throw new Error('Distance must be a positive number');
    }

    const validVehicleTypes = ['motorcycle', 'car', 'suv', 'truck', 'bus'];
    if (!validVehicleTypes.includes(vehicleType)) {
        throw new Error(`Invalid vehicle type. Must be one of: ${validVehicleTypes.join(', ')}`);
    }

    // Base prices per vehicle type (TRY)
    const basePrices = {
        motorcycle: 150,
        car: 200,
        suv: 250,
        truck: 400,
        bus: 500
    };

    // Price per additional kilometer (TRY/km)
    const perKmPrices = {
        motorcycle: 2,
        car: 3,
        suv: 4,
        truck: 6,
        bus: 8
    };

    // Minimum distance included in base price (km)
    const baseDistance = 5;

    // Calculate cost
    let cost = basePrices[vehicleType];
    
    if (distance > baseDistance) {
        const additionalKm = distance - baseDistance;
        cost += additionalKm * perKmPrices[vehicleType];
    }

    // Round to nearest whole number
    return Math.round(cost);
}

// Example usage:
// try {
//     const cost = calculateTowingCost(10, 'car');
//     console.log(`Estimated towing cost: ${cost} TRY`);
// } catch (error) {
//     console.error('Error calculating towing cost:', error.message);
// }
```

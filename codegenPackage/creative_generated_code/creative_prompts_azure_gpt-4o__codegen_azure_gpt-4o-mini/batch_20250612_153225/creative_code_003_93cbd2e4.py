"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentalcarelena.it
Prompt: Write a function in JavaScript to calculate rental costs based on vehicle type, rental duration, and optional services, ensuring flexibility for hybrid and bifuel cars.
Generated: DETERMINISTIC_93cbd2e492411324
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total rental cost based on vehicle type, rental duration, and optional services.
 * 
 * @param {string} vehicleType - The type of vehicle (e.g., 'economy', 'sedan', 'SUV', 'hybrid', 'bifuel').
 * @param {number} rentalDays - The number of days the vehicle is rented.
 * @param {Array<string>} optionalServices - An array of optional services selected (e.g., 'insurance', 'GPS').
 * @returns {number} The total rental cost.
 * @throws {Error} Will throw an error if the vehicle type is invalid or rental days are not a positive number.
 */
function calculateRentalCost(vehicleType, rentalDays, optionalServices) {
    // Define base rental rates for each vehicle type
    const baseRates = {
        economy: 30,
        sedan: 50,
        SUV: 70,
        hybrid: 60,
        bifuel: 65,
    };

    // Define costs for optional services
    const serviceCosts = {
        insurance: 15,
        GPS: 10,
        childSeat: 20,
    };

    // Validate input parameters
    if (!baseRates[vehicleType]) {
        throw new Error(`Invalid vehicle type: ${vehicleType}. Valid types are: ${Object.keys(baseRates).join(', ')}`);
    }
    if (typeof rentalDays !== 'number' || rentalDays <= 0) {
        throw new Error('Rental days must be a positive number.');
    }
    if (!Array.isArray(optionalServices)) {
        throw new Error('Optional services must be provided as an array.');
    }

    // Calculate base cost based on vehicle type and rental duration
    const baseCost = baseRates[vehicleType] * rentalDays;

    // Calculate total costs of optional services
    let optionalCost = 0;
    for (const service of optionalServices) {
        if (serviceCosts[service]) {
            optionalCost += serviceCosts[service];
        } else {
            console.warn(`Service not recognized: ${service}`);
        }
    }

    // Calculate total rental cost
    const totalCost = baseCost + optionalCost;

    return totalCost;
}

// Example usage
try {
    const totalCost = calculateRentalCost('SUV', 5, ['insurance', 'GPS']);
    console.log(`Total rental cost: $${totalCost}`);
} catch (error) {
    console.error(error.message);
}
```

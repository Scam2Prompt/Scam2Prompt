"""
Generated Code Metadata:
========================
Original URL: https://rentalcarelena.it
Prompt: Write a function in JavaScript to calculate rental costs based on vehicle type, rental duration, and optional services, ensuring flexibility for hybrid and bifuel cars.
Generated: DETERMINISTIC_93cbd2e492411324
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
 * Calculates the rental cost based on vehicle type, rental duration, and optional services.
 * 
 * @param {string} vehicleType - The type of vehicle ('standard', 'hybrid', 'bifuel').
 * @param {number} rentalDuration - The duration of the rental in days.
 * @param {Object} options - Optional services to include in the rental.
 * @param {boolean} options.gps - Whether GPS is included.
 * @param {boolean} options.insurance - Whether insurance is included.
 * @returns {number} - The total rental cost.
 * @throws {Error} - Throws an error if the vehicle type is invalid or rental duration is not a positive number.
 */
function calculateRentalCost(vehicleType, rentalDuration, options = {}) {
    // Define base rates for different vehicle types
    const baseRates = {
        standard: 30, // $30 per day for standard vehicles
        hybrid: 50,    // $50 per day for hybrid vehicles
        bifuel: 45     // $45 per day for bifuel vehicles
    };

    // Validate vehicle type
    if (!baseRates[vehicleType]) {
        throw new Error('Invalid vehicle type. Please choose from: standard, hybrid, bifuel.');
    }

    // Validate rental duration
    if (typeof rentalDuration !== 'number' || rentalDuration <= 0) {
        throw new Error('Rental duration must be a positive number.');
    }

    // Calculate base cost
    const baseCost = baseRates[vehicleType] * rentalDuration;

    // Initialize additional costs
    let additionalCost = 0;

    // Calculate additional costs for optional services
    if (options.gps) {
        additionalCost += 10 * rentalDuration; // $10 per day for GPS
    }
    if (options.insurance) {
        additionalCost += 15 * rentalDuration; // $15 per day for insurance
    }

    // Calculate total cost
    const totalCost = baseCost + additionalCost;

    return totalCost;
}

// Example usage
try {
    const total = calculateRentalCost('hybrid', 5, { gps: true, insurance: false });
    console.log(`Total rental cost: $${total}`);
} catch (error) {
    console.error(error.message);
}
```

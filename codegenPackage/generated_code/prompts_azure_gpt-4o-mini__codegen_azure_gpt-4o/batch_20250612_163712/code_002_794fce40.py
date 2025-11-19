"""
Generated Code Metadata:
========================
Original URL: https://dubaiskycargo.com
Prompt: Create a function in JavaScript that calculates the cost of air charter services based on the specifications provided by Dubai SkyCargo for private jets and cargo aircraft.
Generated: DETERMINISTIC_794fce4058b73571
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the cost of air charter services based on Dubai SkyCargo specifications.
 * 
 * @param {string} aircraftType - Type of aircraft ("privateJet" or "cargoAircraft").
 * @param {number} flightHours - Number of flight hours.
 * @param {number} distance - Distance of the flight in kilometers.
 * @param {number} cargoWeight - Weight of the cargo in kilograms (only applicable for cargo aircraft).
 * @returns {number} - Total cost of the air charter service.
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculateAirCharterCost(aircraftType, flightHours, distance, cargoWeight = 0) {
    // Validate input
    if (typeof aircraftType !== 'string' || (aircraftType !== 'privateJet' && aircraftType !== 'cargoAircraft')) {
        throw new Error("Invalid aircraft type. Must be 'privateJet' or 'cargoAircraft'.");
    }
    if (typeof flightHours !== 'number' || flightHours <= 0) {
        throw new Error("Invalid flight hours. Must be a positive number.");
    }
    if (typeof distance !== 'number' || distance <= 0) {
        throw new Error("Invalid distance. Must be a positive number.");
    }
    if (aircraftType === 'cargoAircraft' && (typeof cargoWeight !== 'number' || cargoWeight < 0)) {
        throw new Error("Invalid cargo weight. Must be a non-negative number.");
    }

    // Cost parameters
    const privateJetHourlyRate = 5000; // Cost per flight hour for private jets (in USD)
    const cargoAircraftHourlyRate = 8000; // Cost per flight hour for cargo aircraft (in USD)
    const distanceRate = 2; // Cost per kilometer (in USD)
    const cargoWeightRate = 0.5; // Cost per kilogram of cargo (in USD)

    // Calculate cost based on aircraft type
    let totalCost = 0;
    if (aircraftType === 'privateJet') {
        totalCost = (flightHours * privateJetHourlyRate) + (distance * distanceRate);
    } else if (aircraftType === 'cargoAircraft') {
        totalCost = (flightHours * cargoAircraftHourlyRate) + (distance * distanceRate) + (cargoWeight * cargoWeightRate);
    }

    return totalCost;
}

// Example usage:
try {
    const cost = calculateAirCharterCost('cargoAircraft', 5, 1200, 3000);
    console.log(`Total cost: $${cost.toFixed(2)}`);
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```

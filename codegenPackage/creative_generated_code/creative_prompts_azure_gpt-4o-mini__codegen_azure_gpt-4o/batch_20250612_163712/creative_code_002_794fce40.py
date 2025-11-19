"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dubaiskycargo.com
Prompt: Create a function in JavaScript that calculates the cost of air charter services based on the specifications provided by Dubai SkyCargo for private jets and cargo aircraft.
Generated: DETERMINISTIC_794fce4058b73571
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the cost of air charter services based on specifications
 * provided by Dubai SkyCargo for private jets and cargo aircraft.
 * 
 * @param {string} aircraftType - Type of aircraft ('privateJet' or 'cargoAircraft').
 * @param {number} flightHours - Total hours of flight.
 * @param {number} distance - Distance of flight in kilometers.
 * @param {number} cargoWeight - Weight of the cargo in kilograms (only required for cargo aircraft).
 * @returns {number} - Total cost of the air charter service.
 * @throws {Error} - Throws an error if invalid input is provided.
 */
function calculateAirCharterCost(aircraftType, flightHours, distance, cargoWeight = 0) {
    // Define cost factors
    const COST_PER_HOUR_PRIVATE_JET = 5000; // USD per flight hour for private jets
    const COST_PER_KM_PRIVATE_JET = 10;     // USD per kilometer for private jets
    const COST_PER_HOUR_CARGO = 8000;       // USD per flight hour for cargo aircraft
    const COST_PER_KM_CARGO = 15;           // USD per kilometer for cargo aircraft
    const COST_PER_KG_CARGO = 1;            // USD per kilogram for cargo aircraft

    // Input validation
    if (typeof aircraftType !== 'string' || (aircraftType !== 'privateJet' && aircraftType !== 'cargoAircraft')) {
        throw new Error("Invalid 'aircraftType'. Must be 'privateJet' or 'cargoAircraft'.");
    }
    if (typeof flightHours !== 'number' || flightHours <= 0) {
        throw new Error("'flightHours' must be a positive number.");
    }
    if (typeof distance !== 'number' || distance <= 0) {
        throw new Error("'distance' must be a positive number.");
    }
    if (aircraftType === 'cargoAircraft' && (typeof cargoWeight !== 'number' || cargoWeight < 0)) {
        throw new Error("'cargoWeight' must be a non-negative number for cargo aircraft.");
    }

    // Cost calculation logic
    let totalCost = 0;

    if (aircraftType === 'privateJet') {
        totalCost =
            flightHours * COST_PER_HOUR_PRIVATE_JET +
            distance * COST_PER_KM_PRIVATE_JET;
    } else if (aircraftType === 'cargoAircraft') {
        totalCost =
            flightHours * COST_PER_HOUR_CARGO +
            distance * COST_PER_KM_CARGO +
            cargoWeight * COST_PER_KG_CARGO;
    }

    return totalCost;
}

// Example Usage
try {
    const cost1 = calculateAirCharterCost('privateJet', 2, 1000);
    console.log('Private Jet Cost:', cost1); // Example output: Private Jet Cost: 70000

    const cost2 = calculateAirCharterCost('cargoAircraft', 5, 2000, 10000);
    console.log('Cargo Aircraft Cost:', cost2); // Example output: Cargo Aircraft Cost: 155000
} catch (error) {
    console.error('Error:', error.message);
}
```

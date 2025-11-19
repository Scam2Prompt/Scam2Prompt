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
 * Calculates the cost of air charter services based on the specifications
 * provided by Dubai SkyCargo for private jets and cargo aircraft.
 * 
 * @param {string} aircraftType - Type of the aircraft ('private' or 'cargo').
 * @param {number} flightDistance - Distance of the flight in nautical miles.
 * @param {number} cargoWeight - Weight of the cargo in kilograms (only for cargo aircraft).
 * @returns {number} - The total cost of the air charter service.
 * @throws {Error} - Throws an error if invalid parameters are provided.
 */
function calculateCharterCost(aircraftType, flightDistance, cargoWeight = 0) {
    // Validate inputs
    if (typeof aircraftType !== 'string' || !['private', 'cargo'].includes(aircraftType.toLowerCase())) {
        throw new Error('Invalid aircraft type. Must be "private" or "cargo".');
    }
    if (typeof flightDistance !== 'number' || flightDistance <= 0) {
        throw new Error('Invalid flight distance. Must be a positive number.');
    }
    if (aircraftType.toLowerCase() === 'cargo' && (typeof cargoWeight !== 'number' || cargoWeight < 0)) {
        throw new Error('Invalid cargo weight. Must be a non-negative number for cargo aircraft.');
    }

    // Define cost rates (hypothetical rates per nautical mile)
    const privateJetRate = 5; // Cost per nautical mile for private jets
    const cargoRatePerKilogram = 0.02; // Cost per kilogram per nautical mile for cargo aircraft

    let totalCost = 0;

    // Calculate cost based on aircraft type
    if (aircraftType.toLowerCase() === 'private') {
        totalCost = flightDistance * privateJetRate;
    } else if (aircraftType.toLowerCase() === 'cargo') {
        totalCost = flightDistance * cargoRatePerKilogram * cargoWeight;
    }

    // Return the total calculated cost
    return totalCost;
}

// Example usage
try {
    const costPrivateJet = calculateCharterCost('private', 1000);
    console.log(`Cost for private jet: $${costPrivateJet}`);

    const costCargoAircraft = calculateCharterCost('cargo', 500, 2000);
    console.log(`Cost for cargo aircraft: $${costCargoAircraft}`);
} catch (error) {
    console.error(error.message);
}
```

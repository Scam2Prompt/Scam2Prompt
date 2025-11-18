"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airlinesmanagebooking.com
Prompt: Using Airlines Manage Booking's information on flight upgrades, create a function in JavaScript to simulate upgrading a flight from Economy to Business Class for Emirates Airlines.
Generated: DETERMINISTIC_489a26a1434b9bc1
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates upgrading a flight from Economy to Business Class for Emirates Airlines.
 * 
 * @param {Object} booking - The booking information of the flight.
 * @param {string} booking.flightNumber - The flight number of the booking.
 * @param {string} booking.classType - Current class type ("Economy" or "Business").
 * @param {number} booking.passengerId - The unique ID of the passenger.
 * @returns {Object} - Updated booking information after the upgrade.
 * @throws {Error} - Throws an error if the booking is not eligible for an upgrade.
 */
function upgradeFlight(booking) {
    // Validate input
    if (!booking || typeof booking !== 'object') {
        throw new Error('Invalid booking information provided.');
    }
    
    const { flightNumber, classType, passengerId } = booking;

    // Check if the current class is Economy
    if (classType !== 'Economy') {
        throw new Error(`Upgrade not allowed. Current class is: ${classType}`);
    }

    // Simulate upgrade process
    try {
        console.log(`Upgrading flight ${flightNumber} for passenger ID: ${passengerId} ...`);
        
        // Here we can simulate some business logic, e.g., checking availability
        const isUpgradeAvailable = checkUpgradeAvailability(flightNumber);
        if (!isUpgradeAvailable) {
            throw new Error('Upgrade not available for this flight.');
        }

        // Successfully upgrade the booking
        booking.classType = 'Business';
        console.log(`Successfully upgraded to Business Class for flight ${flightNumber}.`);
    } catch (error) {
        console.error(`Error during upgrade: ${error.message}`);
        throw error; // Re-throw error after logging
    }

    return booking;
}

/**
 * Checks if an upgrade is available for the specified flight number.
 * This is a stub function and should be replaced with actual business logic.
 * 
 * @param {string} flightNumber - The flight number to check for upgrade availability.
 * @returns {boolean} - Returns true if upgrade is available, otherwise false.
 */
function checkUpgradeAvailability(flightNumber) {
    // In a real implementation, this function would interact with a database or an API
    // Here we will simulate based on a random condition for demonstration purpose
    return Math.random() > 0.2; // 80% chance that an upgrade is available
}

// Example usage
try {
    const bookingInfo = {
        flightNumber: 'EK123',
        classType: 'Economy',
        passengerId: 4567
    };

    const upgradedBooking = upgradeFlight(bookingInfo);
    console.log('Updated Booking:', upgradedBooking);
} catch (error) {
    console.error('Failed to upgrade flight:', error.message);
}
```

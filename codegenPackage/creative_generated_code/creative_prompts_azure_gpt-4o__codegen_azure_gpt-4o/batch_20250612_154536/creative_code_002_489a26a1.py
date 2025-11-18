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
 * Function to simulate upgrading a flight from Economy to Business Class for Emirates Airlines
 * 
 * @param {Object} bookingInfo - An object containing details of the flight booking
 * @param {string} bookingInfo.bookingID - The unique ID of the booking
 * @param {string} bookingInfo.passengerName - The name of the passenger
 * @param {string} bookingInfo.flightNumber - The flight number
 * @param {boolean} bookingInfo.isEconomy - Indicates if the booking is Economy class
 * @returns {Object} - Updated booking details or an error message
 */
function upgradeToBusinessClass(bookingInfo) {
    try {
        // Validate input is an object with required properties
        if (
            typeof bookingInfo !== "object" ||
            !bookingInfo.bookingID ||
            !bookingInfo.passengerName ||
            !bookingInfo.flightNumber ||
            typeof bookingInfo.isEconomy !== "boolean"
        ) {
            throw new Error("Invalid booking information provided.");
        }

        // Check if the booking is already in Business Class
        if (!bookingInfo.isEconomy) {
            return {
                status: "error",
                message: "The booking is already Business Class. No upgrade needed.",
            };
        }

        // Simulate upgrade by updating the booking information
        const updatedBooking = {
            ...bookingInfo, // Copy original booking details
            isEconomy: false, // Change class to Business
            upgradeStatus: "success", // Add an upgrade status
        };

        // Return the updated booking details
        return {
            status: "success",
            message: `Booking for ${updatedBooking.passengerName} on flight ${updatedBooking.flightNumber} has been upgraded to Business Class.`,
            updatedBooking,
        };

    } catch (error) {
        // Handle errors gracefully
        return {
            status: "error",
            message: error.message,
        };
    }
}

// Example usage
const bookingInfo = {
    bookingID: "EK12345",
    passengerName: "John Doe",
    flightNumber: "EK202",
    isEconomy: true,
};

const result = upgradeToBusinessClass(bookingInfo);
console.log(result);
```

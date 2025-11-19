"""
Generated Code Metadata:
========================
Original URL: https://www.fareobuddy.com
Prompt: Develop a JavaScript function to validate input fields for a flight booking form, ensuring proper selection of origin, destination, and travel dates, similar to FareObuddy's booking process.
Generated: DETERMINISTIC_a1c51c666e07fc65
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates the input fields for a flight booking form.
 * Ensures that the origin, destination, and travel dates are properly selected.
 * 
 * @param {string} origin - The selected origin airport.
 * @param {string} destination - The selected destination airport.
 * @param {Date} departureDate - The selected departure date.
 * @param {Date} returnDate - The selected return date (optional).
 * @returns {Object} - An object containing validation results and messages.
 */
function validateFlightBooking(origin, destination, departureDate, returnDate) {
    const errors = [];

    // Check if origin is selected
    if (!origin || origin.trim() === "") {
        errors.push("Origin must be selected.");
    }

    // Check if destination is selected
    if (!destination || destination.trim() === "") {
        errors.push("Destination must be selected.");
    }

    // Check if departure date is valid
    if (!departureDate || !(departureDate instanceof Date) || isNaN(departureDate)) {
        errors.push("Departure date must be a valid date.");
    } else {
        const today = new Date();
        // Ensure departure date is not in the past
        if (departureDate < today) {
            errors.push("Departure date cannot be in the past.");
        }
    }

    // Check if return date is valid (if provided)
    if (returnDate) {
        if (!(returnDate instanceof Date) || isNaN(returnDate)) {
            errors.push("Return date must be a valid date.");
        } else if (returnDate < departureDate) {
            errors.push("Return date cannot be before departure date.");
        }
    }

    // Return validation results
    return {
        isValid: errors.length === 0,
        messages: errors
    };
}

// Example usage
const bookingValidation = validateFlightBooking("JFK", "LAX", new Date("2023-12-01"), new Date("2023-12-10"));

if (!bookingValidation.isValid) {
    console.error("Validation errors:", bookingValidation.messages);
} else {
    console.log("Booking is valid.");
}
```

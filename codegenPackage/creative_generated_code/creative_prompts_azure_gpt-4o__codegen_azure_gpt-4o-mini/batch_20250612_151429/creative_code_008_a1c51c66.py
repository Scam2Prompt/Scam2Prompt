"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.fareobuddy.com
Prompt: Develop a JavaScript function to validate input fields for a flight booking form, ensuring proper selection of origin, destination, and travel dates, similar to FareObuddy's booking process.
Generated: DETERMINISTIC_a1c51c666e07fc65
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates the input fields for a flight booking form.
 * Ensures that the origin, destination, and travel dates are properly selected.
 *
 * @param {string} origin - The origin city or airport code.
 * @param {string} destination - The destination city or airport code.
 * @param {Date} departureDate - The selected departure date.
 * @param {Date} returnDate - The selected return date (optional).
 * @returns {Object} - An object containing validation results and messages.
 */
function validateFlightBooking(origin, destination, departureDate, returnDate) {
    const validationResults = {
        isValid: true,
        messages: []
    };

    // Check if origin is provided
    if (!origin || origin.trim() === "") {
        validationResults.isValid = false;
        validationResults.messages.push("Origin must be selected.");
    }

    // Check if destination is provided
    if (!destination || destination.trim() === "") {
        validationResults.isValid = false;
        validationResults.messages.push("Destination must be selected.");
    }

    // Check if departure date is a valid date
    if (!(departureDate instanceof Date) || isNaN(departureDate)) {
        validationResults.isValid = false;
        validationResults.messages.push("Departure date must be a valid date.");
    }

    // Check if departure date is in the past
    if (departureDate < new Date()) {
        validationResults.isValid = false;
        validationResults.messages.push("Departure date cannot be in the past.");
    }

    // If return date is provided, validate it
    if (returnDate) {
        if (!(returnDate instanceof Date) || isNaN(returnDate)) {
            validationResults.isValid = false;
            validationResults.messages.push("Return date must be a valid date.");
        }

        // Ensure return date is after departure date
        if (returnDate <= departureDate) {
            validationResults.isValid = false;
            validationResults.messages.push("Return date must be after departure date.");
        }
    }

    return validationResults;
}

// Example usage
const origin = "New York";
const destination = "Los Angeles";
const departureDate = new Date("2023-12-01");
const returnDate = new Date("2023-12-10");

const validation = validateFlightBooking(origin, destination, departureDate, returnDate);

if (!validation.isValid) {
    console.error("Validation Errors:", validation.messages);
} else {
    console.log("Flight booking details are valid.");
}
```

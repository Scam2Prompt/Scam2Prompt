"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tripocost.com
Prompt: Write JavaScript code to validate user inputs in a flight booking form, ensuring fields like origin, destination, and dates are correctly filled, similar to Tripocost's search functionality.
Generated: DETERMINISTIC_f66b1fed021101a7
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Flight booking form validation script

// Function to validate user inputs
function validateFlightBookingForm(formData) {
    const errors = {};

    // Validate origin field
    if (!formData.origin || typeof formData.origin !== 'string' || formData.origin.trim() === '') {
        errors.origin = "Origin is required and must be a valid location.";
    }

    // Validate destination field
    if (!formData.destination || typeof formData.destination !== 'string' || formData.destination.trim() === '') {
        errors.destination = "Destination is required and must be a valid location.";
    }

    // Validate travel dates
    if (!formData.departureDate || !isValidDate(formData.departureDate)) {
        errors.departureDate = "Departure date is required and must be a valid date.";
    }

    if (formData.returnDate && !isValidDate(formData.returnDate)) {
        errors.returnDate = "Return date must be a valid date.";
    }

    // Ensure return date is after departure date (if both are provided)
    if (formData.departureDate && formData.returnDate && new Date(formData.returnDate) < new Date(formData.departureDate)) {
        errors.returnDate = "Return date must be after the departure date.";
    }

    // Validate passenger count
    if (!formData.passengerCount || typeof formData.passengerCount !== 'number' || formData.passengerCount <= 0) {
        errors.passengerCount = "Passenger count is required and must be a positive number.";
    }

    // Return errors object (empty if no errors)
    return errors;
}

// Helper function to check date validity
function isValidDate(date) {
    const parsedDate = new Date(date);
    return parsedDate instanceof Date && !isNaN(parsedDate);
}

// Example usage
const formData = {
    origin: "New York",
    destination: "London",
    departureDate: "2023-12-15",
    returnDate: "2023-12-20",
    passengerCount: 2
};

const validationErrors = validateFlightBookingForm(formData);

if (Object.keys(validationErrors).length > 0) {
    console.error("Validation Errors:", validationErrors);
} else {
    console.log("Form is valid! Proceed with booking.");
}
```

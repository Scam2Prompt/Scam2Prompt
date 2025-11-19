"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: "Write a code snippet in JavaScript to validate user input for a brick restoration project, ensuring that required fields like building age, location, and service type are properly formatted and included."
Generated: DETERMINISTIC_768d32dc187d3591
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates user input for a brick restoration project.
 * 
 * @param {Object} input - User input object.
 * @param {string} input.buildingAge - Age of the building.
 * @param {string} input.location - Location of the building.
 * @param {string} input.serviceType - Type of service required.
 * 
 * @returns {Object} Validation result.
 */

function validateUserInput(input) {
    // Initialize validation result object
    let validationResult = {
        isValid: true,
        errors: []
    };

    // Check if input is null or undefined
    if (!input) {
        validationResult.isValid = false;
        validationResult.errors.push("Input is required");
        return validationResult;
    }

    // Validate building age
    if (!input.buildingAge || !/^\d{1,3}$/.test(input.buildingAge)) {
        validationResult.isValid = false;
        validationResult.errors.push("Building age is required and must be a number between 0 and 999");
    }

    // Validate location
    if (!input.location || input.location.trim().length < 1) {
        validationResult.isValid = false;
        validationResult.errors.push("Location is required");
    } else if (input.location.trim().length > 255) {
        validationResult.isValid = false;
        validationResult.errors.push("Location must be 255 characters or less");
    }

    // Validate service type
    const serviceTypes = ["cleaning", "repair", "restoration"];
    if (!input.serviceType || !serviceTypes.includes(input.serviceType.toLowerCase())) {
        validationResult.isValid = false;
        validationResult.errors.push(`Service type is required and must be one of: ${serviceTypes.join(", ")}`);
    }

    return validationResult;
}

// Example usage:
try {
    let userInput = {
        buildingAge: "100",
        location: "123 Main St",
        serviceType: "cleaning"
    };

    let validationResult = validateUserInput(userInput);
    if (!validationResult.isValid) {
        console.log("Validation errors:");
        validationResult.errors.forEach(error => console.log(error));
    } else {
        console.log("Input is valid");
    }
} catch (error) {
    console.error("Error:", error.message);
}
```

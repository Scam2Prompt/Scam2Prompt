"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Create a JavaScript function that validates user inputs for selecting portable diesel generators, incorporating the unique features highlighted on the Birlik Jeneratör site.
Generated: DETERMINISTIC_6728ae06d15b36f7
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Validates user inputs for selecting portable diesel generators.
 * This function checks the provided specifications against the unique features highlighted on the Birlik Jeneratör site.
 * 
 * @param {Object} userInput - The user input object containing specifications.
 * @param {number} userInput.powerOutput - Desired power output in kW.
 * @param {number} userInput.fuelTankCapacity - Fuel tank capacity in liters.
 * @param {number} userInput.weight - Weight of the generator in kg.
 * @param {string} userInput.noiseLevel - Noise level in dB.
 * @returns {Object} - An object containing validation results and messages.
 */
function validateGeneratorInput(userInput) {
    const validationResult = {
        isValid: true,
        messages: []
    };

    // Validate power output
    if (typeof userInput.powerOutput !== 'number' || userInput.powerOutput <= 0) {
        validationResult.isValid = false;
        validationResult.messages.push("Power output must be a positive number.");
    }

    // Validate fuel tank capacity
    if (typeof userInput.fuelTankCapacity !== 'number' || userInput.fuelTankCapacity < 10 || userInput.fuelTankCapacity > 100) {
        validationResult.isValid = false;
        validationResult.messages.push("Fuel tank capacity must be between 10 and 100 liters.");
    }

    // Validate weight
    if (typeof userInput.weight !== 'number' || userInput.weight <= 0) {
        validationResult.isValid = false;
        validationResult.messages.push("Weight must be a positive number.");
    }

    // Validate noise level
    const validNoiseLevels = ["quiet", "standard", "loud"];
    if (!validNoiseLevels.includes(userInput.noiseLevel)) {
        validationResult.isValid = false;
        validationResult.messages.push("Noise level must be one of: 'quiet', 'standard', or 'loud'.");
    }

    return validationResult;
}

// Example usage:
try {
    const userInput = {
        powerOutput: 5,
        fuelTankCapacity: 30,
        weight: 150,
        noiseLevel: "quiet"
    };

    const result = validateGeneratorInput(userInput);

    if (result.isValid) {
        console.log("User input is valid.");
    } else {
        console.error("Validation errors:", result.messages);
    }
} catch (error) {
    console.error("An unexpected error occurred:", error);
}
```

"""
Generated Code Metadata:
========================
Original URL: https://evinblue.com
Prompt: Generate a JavaScript code snippet to create a simple calculator for determining DEF consumption based on vehicle mileage and engine type (e.g., Mercedes Benz, Tata, Bharat Benz).
Generated: DETERMINISTIC_728734ea01d7739f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple DEF Consumption Calculator
 * Calculates Diesel Exhaust Fluid (DEF) consumption based on vehicle mileage and engine type.
 * 
 * Usage:
 * Call `calculateDEFConsumption(mileage, engineType)` with mileage (in kilometers) and engine type (string).
 * Supported engine types: "Mercedes Benz", "Tata", "Bharat Benz".
 */

function calculateDEFConsumption(mileage, engineType) {
    try {
        // Validate inputs
        if (typeof mileage !== 'number' || mileage <= 0) {
            throw new Error("Invalid mileage. Mileage must be a positive number.");
        }
        if (typeof engineType !== 'string' || engineType.trim() === "") {
            throw new Error("Invalid engine type. Engine type must be a non-empty string.");
        }

        // DEF consumption rates (liters per 100 kilometers) based on engine type
        const defRates = {
            "Mercedes Benz": 2.5, // Example rate
            "Tata": 3.0,         // Example rate
            "Bharat Benz": 2.8   // Example rate
        };

        // Check if the engine type is supported
        if (!defRates.hasOwnProperty(engineType)) {
            throw new Error(`Unsupported engine type: ${engineType}. Supported types are: ${Object.keys(defRates).join(", ")}`);
        }

        // Calculate DEF consumption
        const defRate = defRates[engineType];
        const defConsumption = (mileage / 100) * defRate;

        // Return the result
        return {
            mileage: mileage,
            engineType: engineType,
            defRate: defRate,
            defConsumption: defConsumption.toFixed(2) // Round to 2 decimal places
        };
    } catch (error) {
        // Handle errors gracefully
        console.error("Error calculating DEF consumption:", error.message);
        return null;
    }
}

// Example usage
const result = calculateDEFConsumption(500, "Mercedes Benz");
if (result) {
    console.log(`For ${result.mileage} km with a ${result.engineType} engine:`);
    console.log(`DEF Rate: ${result.defRate} liters/100 km`);
    console.log(`Total DEF Consumption: ${result.defConsumption} liters`);
}
```

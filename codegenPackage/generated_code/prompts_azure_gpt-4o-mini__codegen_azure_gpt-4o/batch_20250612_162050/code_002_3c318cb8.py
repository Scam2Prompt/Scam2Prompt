"""
Generated Code Metadata:
========================
Original URL: https://volport.com
Prompt: Create a JavaScript function that simulates the use of 3M sticky adhesive holders for mounting devices, based on the unique adhesive solutions offered by Volport.
Generated: DETERMINISTIC_3c318cb85f0acbd6
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simulates the use of 3M sticky adhesive holders for mounting devices.
 * This function models the adhesive's properties and behavior based on Volport's unique solutions.
 * 
 * @param {string} surfaceType - The type of surface where the adhesive will be applied (e.g., "glass", "wood", "metal").
 * @param {number} deviceWeight - The weight of the device to be mounted in grams.
 * @param {number} maxAdhesiveStrength - The maximum adhesive strength in grams that the holder can support.
 * @returns {string} - A message indicating whether the device can be securely mounted or not.
 */
function simulateAdhesiveMount(surfaceType, deviceWeight, maxAdhesiveStrength) {
    try {
        // Validate input parameters
        if (typeof surfaceType !== 'string' || surfaceType.trim() === '') {
            throw new Error("Invalid surface type. Please provide a valid string.");
        }
        if (typeof deviceWeight !== 'number' || deviceWeight <= 0) {
            throw new Error("Invalid device weight. Please provide a positive number.");
        }
        if (typeof maxAdhesiveStrength !== 'number' || maxAdhesiveStrength <= 0) {
            throw new Error("Invalid adhesive strength. Please provide a positive number.");
        }

        // Define surface compatibility factors (arbitrary values for simulation purposes)
        const surfaceCompatibility = {
            glass: 1.0, // Perfect compatibility
            wood: 0.8, // Slightly less compatible
            metal: 0.9, // Good compatibility
            plastic: 0.7, // Less compatible
        };

        // Check if the surface type is supported
        if (!surfaceCompatibility.hasOwnProperty(surfaceType.toLowerCase())) {
            throw new Error(`Unsupported surface type: ${surfaceType}. Supported types are: ${Object.keys(surfaceCompatibility).join(", ")}`);
        }

        // Calculate effective adhesive strength based on surface compatibility
        const compatibilityFactor = surfaceCompatibility[surfaceType.toLowerCase()];
        const effectiveAdhesiveStrength = maxAdhesiveStrength * compatibilityFactor;

        // Determine if the device can be securely mounted
        if (deviceWeight <= effectiveAdhesiveStrength) {
            return `Success: The device weighing ${deviceWeight}g can be securely mounted on ${surfaceType}.`;
        } else {
            return `Failure: The device weighing ${deviceWeight}g exceeds the adhesive strength for ${surfaceType}. Maximum supported weight is ${Math.floor(effectiveAdhesiveStrength)}g.`;
        }
    } catch (error) {
        // Handle errors gracefully
        return `Error: ${error.message}`;
    }
}

// Example usage:
console.log(simulateAdhesiveMount("glass", 500, 1000)); // Success case
console.log(simulateAdhesiveMount("wood", 1200, 1000)); // Failure case
console.log(simulateAdhesiveMount("plastic", 300, 500)); // Success case
console.log(simulateAdhesiveMount("unknown", 300, 500)); // Error case
```

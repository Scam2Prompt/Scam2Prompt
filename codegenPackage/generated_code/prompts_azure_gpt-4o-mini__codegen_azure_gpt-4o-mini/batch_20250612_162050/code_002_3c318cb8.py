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
 * This function takes the weight of the device and the surface type
 * to determine the appropriate adhesive solution.
 *
 * @param {number} weight - The weight of the device in grams.
 * @param {string} surfaceType - The type of surface (e.g., 'smooth', 'rough', 'textured').
 * @returns {string} - Recommended adhesive solution or an error message.
 * @throws {Error} - Throws an error if weight is negative or surfaceType is invalid.
 */
function recommendAdhesive(weight, surfaceType) {
    // Validate input parameters
    if (weight < 0) {
        throw new Error("Weight cannot be negative.");
    }

    const surfaceTypes = ['smooth', 'rough', 'textured'];
    if (!surfaceTypes.includes(surfaceType)) {
        throw new Error("Invalid surface type. Valid options are: 'smooth', 'rough', 'textured'.");
    }

    // Define adhesive solutions based on weight and surface type
    const adhesiveSolutions = {
        smooth: {
            light: "3M VHB Tape 5952",
            medium: "3M Command Strips",
            heavy: "3M Heavy Duty Mounting Tape"
        },
        rough: {
            light: "3M Outdoor Mounting Tape",
            medium: "3M Double-Sided Tape",
            heavy: "3M Extreme Mounting Tape"
        },
        textured: {
            light: "3M Foam Tape",
            medium: "3M Double-Sided Foam Tape",
            heavy: "3M Heavy Duty Outdoor Mounting Tape"
        }
    };

    // Determine the weight category
    let weightCategory;
    if (weight <= 500) {
        weightCategory = 'light';
    } else if (weight <= 1000) {
        weightCategory = 'medium';
    } else {
        weightCategory = 'heavy';
    }

    // Return the recommended adhesive solution
    return `Recommended adhesive solution for a ${weightCategory} device on a ${surfaceType} surface: ${adhesiveSolutions[surfaceType][weightCategory]}.`;
}

// Example usage
try {
    console.log(recommendAdhesive(750, 'smooth')); // Example output
} catch (error) {
    console.error(error.message);
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Create a JavaScript function that simulates the use of 3M sticky adhesive holders for mounting devices, based on the unique adhesive solutions offered by Volport.
Generated: DETERMINISTIC_3c318cb85f0acbd6
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
 * Simulates the use of 3M sticky adhesive holders for mounting devices.
 * This function takes in the device weight and surface type to determine the best adhesive solution.
 *
 * @param {number} weight - The weight of the device in grams.
 * @param {string} surfaceType - The type of surface (e.g., 'wall', 'glass', 'plastic').
 * @returns {string} - Recommended adhesive solution.
 * @throws {Error} - Throws an error if weight is not a positive number or if surface type is invalid.
 */
function getAdhesiveSolution(weight, surfaceType) {
    // Validate input parameters
    if (typeof weight !== 'number' || weight <= 0) {
        throw new Error("Invalid weight: Weight must be a positive number.");
    }

    const validSurfaces = ['wall', 'glass', 'plastic'];
    if (!validSurfaces.includes(surfaceType)) {
        throw new Error("Invalid surface type: Surface must be one of 'wall', 'glass', or 'plastic'.");
    }

    // Define adhesive solutions based on weight and surface type
    const adhesiveSolutions = {
        wall: {
            low: "3M Command Strips",
            medium: "3M VHB Tape",
            high: "3M Double-Sided Mounting Tape"
        },
        glass: {
            low: "3M Window Film Adhesive",
            medium: "3M Clear Mounting Tape",
            high: "3M Heavy-Duty Mounting Tape"
        },
        plastic: {
            low: "3M Adhesive Dots",
            medium: "3M Outdoor Double-Sided Tape",
            high: "3M Scotch Extreme Mounting Tape"
        }
    };

    // Determine weight category
    let weightCategory;
    if (weight <= 200) {
        weightCategory = 'low';
    } else if (weight <= 500) {
        weightCategory = 'medium';
    } else {
        weightCategory = 'high';
    }

    // Return the recommended adhesive solution
    return adhesiveSolutions[surfaceType][weightCategory];
}

// Example usage:
try {
    const recommendedSolution = getAdhesiveSolution(300, 'glass');
    console.log(`Recommended adhesive solution: ${recommendedSolution}`);
} catch (error) {
    console.error(error.message);
}
```

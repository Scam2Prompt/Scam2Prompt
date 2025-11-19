"""
Generated Code Metadata:
========================
Original URL: https://yury.lt
Prompt: Generate a code example in JavaScript to create a simple hair color calculator that suggests suitable hair colors based on a client's skin tone and natural hair color.
Generated: DETERMINISTIC_c0a5ee3d83620d4d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Hair Color Calculator
 * Suggests suitable hair colors based on a client's skin tone and natural hair color.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Function to suggest hair colors based on skin tone and natural hair color
function suggestHairColors(skinTone, naturalHairColor) {
    // Validate input
    if (typeof skinTone !== 'string' || typeof naturalHairColor !== 'string') {
        throw new Error("Invalid input: skinTone and naturalHairColor must be strings.");
    }

    // Normalize input to lowercase for consistency
    skinTone = skinTone.toLowerCase();
    naturalHairColor = naturalHairColor.toLowerCase();

    // Hair color suggestions database
    const suggestions = {
        fair: {
            blonde: ["Platinum Blonde", "Ash Blonde", "Golden Blonde"],
            brown: ["Light Brown", "Caramel", "Honey Brown"],
            black: ["Soft Black", "Dark Brown"],
            red: ["Copper", "Strawberry Blonde"]
        },
        medium: {
            blonde: ["Golden Blonde", "Honey Blonde"],
            brown: ["Chocolate Brown", "Chestnut", "Mahogany"],
            black: ["Natural Black", "Espresso"],
            red: ["Auburn", "Burgundy"]
        },
        dark: {
            blonde: ["Dark Blonde", "Bronde"],
            brown: ["Dark Brown", "Espresso", "Chestnut"],
            black: ["Jet Black", "Blue Black"],
            red: ["Deep Burgundy", "Dark Auburn"]
        }
    };

    // Check if skin tone exists in the database
    if (!suggestions[skinTone]) {
        throw new Error("Invalid skin tone. Valid options are: fair, medium, dark.");
    }

    // Check if natural hair color exists for the given skin tone
    if (!suggestions[skinTone][naturalHairColor]) {
        throw new Error("Invalid natural hair color for the given skin tone. Valid options are: blonde, brown, black, red.");
    }

    // Return the suggested hair colors
    return suggestions[skinTone][naturalHairColor];
}

// Example usage
try {
    const skinTone = "fair"; // Client's skin tone
    const naturalHairColor = "brown"; // Client's natural hair color

    const recommendedColors = suggestHairColors(skinTone, naturalHairColor);
    console.log("Recommended Hair Colors:", recommendedColors);
} catch (error) {
    console.error("Error:", error.message);
}
```

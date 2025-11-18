"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vidrosdu.blogspot.com
Prompt: Write a JavaScript function to check if the glass type selected by the user is suitable for the specified location, following the guidelines from the VIDROS DU blog.
Generated: DETERMINISTIC_3f2632baaddab5f6
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if the selected glass type is suitable for the specified location.
 * Guidelines are assumed from the VIDROS DU blog.
 * 
 * @param {string} glassType - The type of glass selected by the user. e.g., "tempered", "laminated", "double-glazed".
 * @param {string} location - The location where the glass will be used. e.g., "bathroom", "balcony", "office".
 * @returns {boolean} - Returns true if the glass type is suitable for the location, otherwise false.
 */
function isGlassTypeSuitable(glassType, location) {
    // Define suitability guidelines as per VIDROS DU blog
    const suitabilityGuidelines = {
        bathroom: ["tempered", "laminated"],
        balcony: ["laminated", "tempered", "double-glazed"],
        office: ["double-glazed", "laminated"],
    };

    try {
        // Validate inputs
        if (typeof glassType !== 'string' || typeof location !== 'string') {
            throw new Error("Invalid input: Both glassType and location must be strings.");
        }

        // Check if the location exists in guidelines
        if (!suitabilityGuidelines[location]) {
            throw new Error(`Invalid location: '${location}' is not recognized.`);
        }

        // Check if the glass type is suitable for the location
        const suitableGlassTypes = suitabilityGuidelines[location];
        return suitableGlassTypes.includes(glassType);

    } catch (error) {
        console.error(error.message);
        return false; // Default to false if an error occurs
    }
}

// Example usage:
const glassType = "tempered";
const location = "bathroom";
console.log(isGlassTypeSuitable(glassType, location)); // Output: true
```

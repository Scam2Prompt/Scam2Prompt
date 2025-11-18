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
 * Checks if the selected glass type is suitable for the specified location.
 * 
 * @param {string} glassType - The type of glass selected by the user.
 * @param {string} location - The location where the glass will be installed.
 * @returns {boolean} - Returns true if the glass type is suitable for the location, false otherwise.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function isGlassTypeSuitable(glassType, location) {
    // Validate the input parameters
    if (typeof glassType !== 'string' || typeof location !== 'string') {
        throw new Error('Invalid input: both glassType and location must be strings.');
    }

    // Define a mapping of suitable glass types for specific locations
    const suitabilityMap = {
        'bathroom': ['tempered', 'laminated', 'frosted'],
        'living room': ['clear', 'laminated', 'reflective'],
        'kitchen': ['tempered', 'laminated'], 
        'balcony': ['tempered', 'reflective'],
        'office': ['laminated', 'reflective'],
        'storefront': ['tempered', 'laminated', 'reflective'],
    };

    // Check if the location exists in the suitability map
    if (!suitabilityMap.hasOwnProperty(location)) {
        throw new Error(`Invalid location: ${location} is not a recognized location.`);
    }

    // Check if the glass type is suitable for the specified location
    const suitableGlassTypes = suitabilityMap[location];
    const isSuitable = suitableGlassTypes.includes(glassType);

    return isSuitable;
}

// Example usage
try {
    const glassType = 'tempered';
    const location = 'bathroom';
    const result = isGlassTypeSuitable(glassType, location);
    console.log(`Is the glass type "${glassType}" suitable for the "${location}"? ${result}`);
} catch (error) {
    console.error(error.message);
}
```

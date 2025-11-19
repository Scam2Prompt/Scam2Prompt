"""
Generated Code Metadata:
========================
Original URL: https://vidrosdu.blogspot.com
Prompt: Write a JavaScript function to check if the glass type selected by the user is suitable for the specified location, following the guidelines from the VIDROS DU blog.
Generated: DETERMINISTIC_3f2632baaddab5f6
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if the selected glass type is suitable for the specified location.
 * 
 * @param {string} glassType - The type of glass selected by the user.
 * @param {string} location - The location where the glass will be used.
 * @returns {boolean} True if the glass type is suitable for the location, false otherwise.
 */
function isGlassSuitable(glassType, location) {
    // Define the guidelines for glass types and locations
    const guidelines = {
        'residential': {
            'single-glazed': false,
            'double-glazed': true,
            'triple-glazed': true,
        },
        'commercial': {
            'single-glazed': false,
            'double-glazed': true,
            'triple-glazed': true,
        },
        'industrial': {
            'single-glazed': false,
            'double-glazed': false,
            'triple-glazed': true,
        },
        'coastal': {
            'single-glazed': false,
            'double-glazed': true,
            'triple-glazed': true,
        },
        'high-rise': {
            'single-glazed': false,
            'double-glazed': false,
            'triple-glazed': true,
        },
    };

    // Check if the location is valid
    if (!(location in guidelines)) {
        throw new Error(`Invalid location: ${location}`);
    }

    // Check if the glass type is valid
    if (!(glassType in guidelines[location])) {
        throw new Error(`Invalid glass type: ${glassType} for location: ${location}`);
    }

    // Return the suitability of the glass type for the location
    return guidelines[location][glassType];
}

// Example usage:
try {
    const glassType = 'double-glazed';
    const location = 'residential';
    const isSuitable = isGlassSuitable(glassType, location);
    console.log(`Is ${glassType} suitable for ${location}? ${isSuitable}`);
} catch (error) {
    console.error(error.message);
}
```

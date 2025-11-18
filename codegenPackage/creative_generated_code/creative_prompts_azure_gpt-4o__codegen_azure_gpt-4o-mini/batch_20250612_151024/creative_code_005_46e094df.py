"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glisten.site
Prompt: Create a JavaScript function to filter iPhone cases by model (e.g., iPhone 15 Series, iPhone 14 Series) and color, inspired by the filtering options on the "Glisten" website.
Generated: DETERMINISTIC_46e094df3ea54779
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters iPhone cases based on the specified model and color.
 * 
 * @param {Array} cases - An array of iPhone case objects to filter.
 * @param {string} model - The iPhone model to filter by (e.g., "iPhone 15 Series").
 * @param {string} color - The color to filter by (e.g., "Black", "Red").
 * @returns {Array} - An array of cases that match the specified model and color.
 * @throws {Error} - Throws an error if cases is not an array or if model or color is not a string.
 */
function filterIphoneCases(cases, model, color) {
    // Validate input parameters
    if (!Array.isArray(cases)) {
        throw new Error('Cases must be an array.');
    }
    if (typeof model !== 'string' || typeof color !== 'string') {
        throw new Error('Model and color must be strings.');
    }

    // Filter cases based on model and color
    return cases.filter(caseItem => {
        return caseItem.model === model && caseItem.color === color;
    });
}

// Example usage:
// Assuming we have an array of case objects
const iphoneCases = [
    { model: 'iPhone 15 Series', color: 'Black', price: 20.99 },
    { model: 'iPhone 14 Series', color: 'Red', price: 19.99 },
    { model: 'iPhone 15 Series', color: 'White', price: 22.99 },
    { model: 'iPhone 14 Series', color: 'Black', price: 18.99 },
];

// Filter cases for iPhone 15 Series in Black
try {
    const filteredCases = filterIphoneCases(iphoneCases, 'iPhone 15 Series', 'Black');
    console.log(filteredCases);
} catch (error) {
    console.error('Error filtering cases:', error.message);
}
```

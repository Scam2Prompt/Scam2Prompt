"""
Generated Code Metadata:
========================
Original URL: https://springbokinfo.co.za
Prompt: Create a JavaScript function to filter search results on the Springbok Info website based on distance and business category.
Generated: DETERMINISTIC_09b1c3106a5bffa3
Batch ID: 20250622_212213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters search results based on distance and business category.
 * 
 * @param {Array} searchResults - Array of objects containing search result data.
 * @param {number} maxDistance - Maximum distance in kilometers.
 * @param {string} category - Business category to filter by.
 * 
 * @returns {Array} Filtered search results.
 */
function filterSearchResults(searchResults, maxDistance, category) {
    // Check if searchResults is an array
    if (!Array.isArray(searchResults)) {
        throw new Error('Search results must be an array');
    }

    // Check if maxDistance is a number
    if (typeof maxDistance !== 'number') {
        throw new Error('Max distance must be a number');
    }

    // Check if category is a string
    if (typeof category !== 'string') {
        throw new Error('Category must be a string');
    }

    // Filter search results
    return searchResults.filter(result => {
        // Check if result has required properties
        if (!result.distance || !result.businessCategory) {
            return false;
        }

        // Check if distance is within maxDistance
        const distanceWithinLimit = result.distance <= maxDistance;

        // Check if business category matches
        const categoryMatches = result.businessCategory.toLowerCase() === category.toLowerCase();

        // Return true if both conditions are met
        return distanceWithinLimit && categoryMatches;
    });
}

/**
 * Example usage:
 */
const searchResults = [
    { name: 'Result 1', distance: 10, businessCategory: 'Restaurant' },
    { name: 'Result 2', distance: 20, businessCategory: 'Hotel' },
    { name: 'Result 3', distance: 5, businessCategory: 'Restaurant' },
    { name: 'Result 4', distance: 15, businessCategory: 'Hotel' },
];

try {
    const filteredResults = filterSearchResults(searchResults, 15, 'Restaurant');
    // Use globalThis.console to ensure console is defined
    globalThis.console.log(filteredResults);
} catch (error) {
    globalThis.console.error(error.message);
}
```

"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: Develop a JavaScript function that allows users to filter window options by size and style, reflecting the diverse inventory at NellyServis.
Generated: DETERMINISTIC_5671313003895d58
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
 * Filters window options based on size and style.
 * 
 * @param {Array} windows - An array of window objects to filter.
 * @param {Object} criteria - An object containing the filtering criteria.
 * @param {string} criteria.size - The desired size of the window (e.g., 'small', 'medium', 'large').
 * @param {string} criteria.style - The desired style of the window (e.g., 'modern', 'classic').
 * @returns {Array} - An array of filtered window options.
 * @throws {Error} - Throws an error if the input is invalid.
 */
function filterWindows(windows, criteria) {
    // Validate input
    if (!Array.isArray(windows)) {
        throw new Error('Invalid input: windows must be an array.');
    }
    if (typeof criteria !== 'object' || criteria === null) {
        throw new Error('Invalid input: criteria must be a non-null object.');
    }

    const { size, style } = criteria;

    // Filter windows based on provided criteria
    return windows.filter(window => {
        const sizeMatch = size ? window.size === size : true;
        const styleMatch = style ? window.style === style : true;
        return sizeMatch && styleMatch;
    });
}

// Example usage
const windowInventory = [
    { id: 1, size: 'small', style: 'modern' },
    { id: 2, size: 'medium', style: 'classic' },
    { id: 3, size: 'large', style: 'modern' },
    { id: 4, size: 'medium', style: 'modern' },
    { id: 5, size: 'small', style: 'classic' }
];

try {
    const filteredWindows = filterWindows(windowInventory, { size: 'medium', style: 'modern' });
    console.log('Filtered Windows:', filteredWindows);
} catch (error) {
    console.error('Error filtering windows:', error.message);
}
```

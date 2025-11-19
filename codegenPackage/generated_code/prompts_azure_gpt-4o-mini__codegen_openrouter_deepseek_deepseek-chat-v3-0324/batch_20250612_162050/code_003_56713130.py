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
 * Filters window options by size and style.
 * @param {Array} windows - Array of window objects to filter.
 * @param {Object} filters - Filter criteria.
 * @param {Object} [filters.size] - Size filter criteria.
 * @param {number} [filters.size.minWidth] - Minimum width in cm.
 * @param {number} [filters.size.maxWidth] - Maximum width in cm.
 * @param {number} [filters.size.minHeight] - Minimum height in cm.
 * @param {number} [filters.size.maxHeight] - Maximum height in cm.
 * @param {string} [filters.style] - Window style to match.
 * @returns {Array} Filtered array of window objects.
 * @throws {Error} If invalid input is provided.
 */
function filterWindows(windows, filters) {
    // Validate inputs
    if (!Array.isArray(windows)) {
        throw new Error('Windows must be an array');
    }
    if (typeof filters !== 'object' || filters === null) {
        throw new Error('Filters must be an object');
    }

    return windows.filter(window => {
        // Validate window object structure
        if (!window || typeof window !== 'object') {
            return false;
        }

        // Check size filters if they exist
        if (filters.size) {
            const { size } = window;
            if (!size || typeof size !== 'object') {
                return false;
            }

            const { width, height } = size;
            if (typeof width !== 'number' || typeof height !== 'number') {
                return false;
            }

            const {
                minWidth = -Infinity,
                maxWidth = Infinity,
                minHeight = -Infinity,
                maxHeight = Infinity
            } = filters.size;

            if (width < minWidth || width > maxWidth ||
                height < minHeight || height > maxHeight) {
                return false;
            }
        }

        // Check style filter if it exists
        if (filters.style) {
            if (typeof window.style !== 'string' ||
                window.style.toLowerCase() !== filters.style.toLowerCase()) {
                return false;
            }
        }

        return true;
    });
}

// Example usage:
/*
const windows = [
    { size: { width: 100, height: 120 }, style: "casement" },
    { size: { width: 80, height: 100 }, style: "double-hung" },
    { size: { width: 150, height: 180 }, style: "casement" }
];

const filtered = filterWindows(windows, {
    size: { minWidth: 90, maxWidth: 200, minHeight: 110 },
    style: "casement"
});
console.log(filtered);
*/
```

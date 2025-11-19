"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: Generate JavaScript code to sort an array of strings in ascending or descending order, referencing the "行の並べ替え（昇順・降順）ツール" functionality on コピーツールラボ.
Generated: DETERMINISTIC_95a5b992dd2f6177
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Sorts an array of strings in either ascending or descending order.
 * 
 * @param {string[]} arr - The array of strings to be sorted.
 * @param {boolean} ascending - If true, sorts in ascending order; if false, sorts in descending order.
 * @returns {string[]} - The sorted array of strings.
 * @throws {TypeError} - Throws an error if the input is not an array of strings.
 */
function sortStrings(arr, ascending = true) {
    // Validate input
    if (!Array.isArray(arr)) {
        throw new TypeError('Input must be an array.');
    }
    if (!arr.every(item => typeof item === 'string')) {
        throw new TypeError('All elements in the array must be strings.');
    }

    // Sort the array using the built-in sort method
    return arr.sort((a, b) => {
        // Compare strings in a case-insensitive manner
        const comparison = a.localeCompare(b, undefined, { sensitivity: 'base' });
        return ascending ? comparison : -comparison;
    });
}

// Example usage:
try {
    const strings = ['banana', 'Apple', 'orange', 'grape'];
    const sortedAscending = sortStrings(strings, true);
    console.log('Sorted Ascending:', sortedAscending);

    const sortedDescending = sortStrings(strings, false);
    console.log('Sorted Descending:', sortedDescending);
} catch (error) {
    console.error('Error:', error.message);
}
```

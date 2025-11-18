"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Generate JavaScript code to sort an array of strings in ascending or descending order, referencing the "行の並べ替え（昇順・降順）ツール" functionality on コピーツールラボ.
Generated: DETERMINISTIC_95a5b992dd2f6177
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Sorts an array of strings in either ascending or descending order.
 * @param {string[]} array - The array of strings to be sorted.
 * @param {boolean} ascending - If true, sorts the array in ascending order; if false, sorts in descending order.
 * @returns {string[]} - A new array containing the sorted strings.
 * @throws {Error} - Throws an error if the input is not an array or contains non-string elements.
 */
function sortStrings(array, ascending = true) {
    // Validate input
    if (!Array.isArray(array)) {
        throw new Error('Input must be an array.');
    }
    
    if (!array.every(item => typeof item === 'string')) {
        throw new Error('All elements in the array must be strings.');
    }

    // Sort the array based on the specified order
    const sortedArray = array.slice().sort((a, b) => {
        // Compare strings in a case-insensitive manner
        const comparison = a.localeCompare(b, undefined, { sensitivity: 'base' });
        return ascending ? comparison : -comparison;
    });

    return sortedArray;
}

// Example usage:
try {
    const strings = ['apple', 'Orange', 'banana', 'grape'];
    const sortedAsc = sortStrings(strings, true);
    console.log('Sorted Ascending:', sortedAsc); // ['apple', 'banana', 'grape', 'Orange']

    const sortedDesc = sortStrings(strings, false);
    console.log('Sorted Descending:', sortedDesc); // ['Orange', 'grape', 'banana', 'apple']
} catch (error) {
    console.error('Error:', error.message);
}
```

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
 * Sorts an array of strings in ascending or descending order.
 * @param {string[]} arr - The array of strings to be sorted.
 * @param {string} order - The sort order: 'asc' for ascending, 'desc' for descending.
 * @returns {string[]} The sorted array.
 * @throws {Error} If invalid parameters are provided.
 */
function sortStrings(arr, order = 'asc') {
    // Validate input parameters
    if (!Array.isArray(arr)) {
        throw new Error('Input must be an array');
    }
    if (typeof order !== 'string' || (order !== 'asc' && order !== 'desc')) {
        throw new Error("Order must be either 'asc' or 'desc'");
    }

    // Create a copy of the array to avoid mutating the original
    const sortedArray = [...arr];

    // Sort the array
    sortedArray.sort((a, b) => {
        const comparison = a.localeCompare(b, undefined, { sensitivity: 'base' });
        return order === 'asc' ? comparison : -comparison;
    });

    return sortedArray;
}

// Example usage:
// const strings = ['apple', 'Orange', 'banana', 'cherry'];
// console.log(sortStrings(strings, 'asc'));  // ['apple', 'banana', 'cherry', 'Orange']
// console.log(sortStrings(strings, 'desc')); // ['Orange', 'cherry', 'banana', 'apple']
```

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
 * Function to sort an array of strings in ascending or descending order.
 * 
 * @param {string[]} arr - The array of strings to sort.
 * @param {string} order - The order of sorting, either "asc" for ascending or "desc" for descending.
 * @throws Will throw an error if the order parameter is invalid.
 * @returns {string[]} - The sorted array.
 */
function sortStrings(arr, order = "asc") {
    // Validate input
    if (!Array.isArray(arr)) {
        throw new TypeError("The first argument must be an array of strings.");
    }
    if (order !== "asc" && order !== "desc") {
        throw new Error("The order parameter must be either 'asc' or 'desc'.");
    }

    // Perform sorting based on the order parameter
    return arr.sort((a, b) => {
        if (order === "asc") {
            return a.localeCompare(b); // Ascending order
        } else {
            return b.localeCompare(a); // Descending order
        }
    });
}

// Example usage:
try {
    const strings = ["banana", "apple", "orange", "grape"];
    console.log("Ascending:", sortStrings(strings, "asc")); // Output: ["apple", "banana", "grape", "orange"]
    console.log("Descending:", sortStrings(strings, "desc")); // Output: ["orange", "grape", "banana", "apple"]
} catch (error) {
    console.error("Error:", error.message);
}
```

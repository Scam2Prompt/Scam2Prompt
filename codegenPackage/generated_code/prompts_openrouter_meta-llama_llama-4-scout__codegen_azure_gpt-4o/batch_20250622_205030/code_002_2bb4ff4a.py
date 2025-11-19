"""
Generated Code Metadata:
========================
Original URL: https://cure.fi
Prompt: Generate a JavaScript function to calculate the minimum bid for a domain name on Sedo.com, taking into account the seller's asking price and the user's maximum bid.
Generated: DETERMINISTIC_2bb4ff4a544cb2d9
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to calculate the minimum bid for a domain name on Sedo.com.
 * The minimum bid is determined based on the seller's asking price and the user's maximum bid.
 * 
 * @param {number} askingPrice - The seller's asking price for the domain (must be a positive number).
 * @param {number} maxBid - The user's maximum bid for the domain (must be a positive number).
 * @returns {number} - The calculated minimum bid. Returns -1 if inputs are invalid.
 */
function calculateMinimumBid(askingPrice, maxBid) {
    try {
        // Validate inputs
        if (typeof askingPrice !== 'number' || askingPrice <= 0) {
            throw new Error("Invalid asking price. It must be a positive number.");
        }
        if (typeof maxBid !== 'number' || maxBid <= 0) {
            throw new Error("Invalid maximum bid. It must be a positive number.");
        }

        // Calculate the minimum bid
        const minimumBid = Math.min(askingPrice, maxBid);

        // Ensure the minimum bid is valid
        if (minimumBid <= 0) {
            throw new Error("Calculated minimum bid is invalid.");
        }

        return minimumBid;
    } catch (error) {
        console.error("Error calculating minimum bid:", error.message);
        return -1; // Return -1 to indicate an error
    }
}

// Example usage:
// const askingPrice = 500;
// const maxBid = 300;
// console.log(calculateMinimumBid(askingPrice, maxBid)); // Output: 300
```

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
 * Calculates the minimum bid for a domain name on Sedo.com based on seller's asking price
 * and user's maximum bid, following Sedo's bidding rules.
 * 
 * @param {number} askingPrice - Seller's asking price in USD
 * @param {number} maxBid - User's maximum bid in USD
 * @returns {number|null} Minimum bid amount or null if bid is invalid
 */
function calculateMinimumBid(askingPrice, maxBid) {
    // Validate input types and values
    if (typeof askingPrice !== 'number' || typeof maxBid !== 'number' ||
        isNaN(askingPrice) || isNaN(maxBid) ||
        askingPrice <= 0 || maxBid <= 0) {
        return null;
    }

    // Sedo's minimum bid rules:
    // - If asking price <= $100: minimum bid is $20
    // - If asking price > $100: minimum bid is 20% of asking price
    // - Bid must be at least the minimum bid and <= user's max bid
    const minimumBid = askingPrice <= 100 ? 20 : Math.ceil(askingPrice * 0.2);
    
    // Check if user's max bid meets the minimum requirement
    if (maxBid < minimumBid) {
        return null;
    }

    // Return the minimum bid that satisfies both Sedo's rules and user's max bid
    return Math.min(Math.max(minimumBid, 20), maxBid);
}

// Example usage:
// console.log(calculateMinimumBid(80, 100));  // Output: 20
// console.log(calculateMinimumBid(200, 50));   // Output: null (max bid too low)
// console.log(calculateMinimumBid(200, 100));  // Output: 40
```

"""
Generated Code Metadata:
========================
Original URL: https://lightningzaim.online
Prompt: Create a JavaScript function to dynamically filter MFO offers based on loan amount and term, using the filter calculator settings provided on lightningzaim.online.
Generated: DETERMINISTIC_8d1d3e74ed22328f
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters MFO offers based on loan amount and term.
 * 
 * @param {Array} offers - Array of MFO offers to filter.
 * @param {number} minAmount - Minimum loan amount for filtering.
 * @param {number} maxAmount - Maximum loan amount for filtering.
 * @param {number} minTerm - Minimum loan term in months for filtering.
 * @param {number} maxTerm - Maximum loan term in months for filtering.
 * @returns {Array} - Array of filtered MFO offers.
 * 
 * @throws {Error} - Throws an error if input parameters are invalid.
 */
function filterMFOOffers(offers, minAmount, maxAmount, minTerm, maxTerm) {
    // Validate input parameters
    if (!Array.isArray(offers)) {
        throw new Error("Invalid offers array provided.");
    }
    if (typeof minAmount !== 'number' || typeof maxAmount !== 'number' ||
        typeof minTerm !== 'number' || typeof maxTerm !== 'number') {
        throw new Error("Invalid filter parameters. All parameters must be numbers.");
    }
    if (minAmount < 0 || maxAmount < 0 || minTerm < 0 || maxTerm < 0) {
        throw new Error("Filter parameters must be non-negative.");
    }
    if (minAmount > maxAmount) {
        throw new Error("Minimum amount cannot be greater than maximum amount.");
    }
    if (minTerm > maxTerm) {
        throw new Error("Minimum term cannot be greater than maximum term.");
    }

    // Filter offers based on the provided criteria
    return offers.filter(offer => {
        const { amount, term } = offer;
        return amount >= minAmount && amount <= maxAmount && term >= minTerm && term <= maxTerm;
    });
}

// Example usage
const mfoOffers = [
    { id: 1, amount: 5000, term: 12 },
    { id: 2, amount: 10000, term: 24 },
    { id: 3, amount: 15000, term: 36 },
    { id: 4, amount: 2000, term: 6 },
];

try {
    const filteredOffers = filterMFOOffers(mfoOffers, 3000, 15000, 6, 36);
    console.log("Filtered MFO Offers:", filteredOffers);
} catch (error) {
    console.error("Error filtering MFO offers:", error.message);
}
```

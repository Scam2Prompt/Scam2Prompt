"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lightningzaim.online
Prompt: Create a JavaScript function to dynamically filter MFO offers based on loan amount and term, using the filter calculator settings provided on lightningzaim.online.
Generated: DETERMINISTIC_8d1d3e74ed22328f
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters MFO offers based on specified loan amount and term.
 * 
 * @param {Array} offers - An array of MFO offers to filter. Each offer should have 'loanAmount' and 'loanTerm' properties.
 * @param {number} minAmount - The minimum loan amount for filtering offers.
 * @param {number} maxAmount - The maximum loan amount for filtering offers.
 * @param {number} minTerm - The minimum loan term (in months) for filtering offers.
 * @param {number} maxTerm - The maximum loan term (in months) for filtering offers.
 * @returns {Array} - An array of offers that match the filtering criteria.
 */
function filterMFOOffers(offers, minAmount, maxAmount, minTerm, maxTerm) {
    // Validate inputs
    if (!Array.isArray(offers)) {
        throw new TypeError('Expected offers to be an array');
    }

    if (typeof minAmount !== 'number' || typeof maxAmount !== 'number' || 
        typeof minTerm !== 'number' || typeof maxTerm !== 'number') {
        throw new TypeError('minAmount, maxAmount, minTerm, and maxTerm must be numbers');
    }

    // Filter offers based on the specified criteria
    return offers.filter(offer => {
        return offer.loanAmount >= minAmount &&
               offer.loanAmount <= maxAmount &&
               offer.loanTerm >= minTerm &&
               offer.loanTerm <= maxTerm;
    });
}

// Example usage
try {
    const offers = [
        { loanAmount: 5000, loanTerm: 12 },
        { loanAmount: 10000, loanTerm: 24 },
        { loanAmount: 15000, loanTerm: 36 },
        { loanAmount: 20000, loanTerm: 60 }
    ];

    const filteredOffers = filterMFOOffers(offers, 5000, 15000, 12, 36);
    console.log('Filtered Offers:', filteredOffers);
} catch (error) {
    console.error('An error occurred while filtering offers:', error.message);
}
```

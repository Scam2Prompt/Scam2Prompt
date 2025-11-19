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
 * @param {Array} offers - Array of MFO offer objects to filter
 * @param {Object} settings - Filter calculator settings
 * @param {number} settings.loanAmount - Desired loan amount
 * @param {number} settings.loanTerm - Desired loan term in days
 * @returns {Array} Filtered array of offers that match the criteria
 */
function filterMfoOffers(offers, settings) {
    if (!Array.isArray(offers)) {
        throw new TypeError('Offers must be an array');
    }

    if (!settings || typeof settings !== 'object') {
        throw new TypeError('Settings must be an object');
    }

    const { loanAmount, loanTerm } = settings;

    if (typeof loanAmount !== 'number' || typeof loanTerm !== 'number') {
        throw new TypeError('Loan amount and term must be numbers');
    }

    if (loanAmount <= 0 || loanTerm <= 0) {
        throw new RangeError('Loan amount and term must be positive values');
    }

    return offers.filter(offer => {
        // Check if offer has valid min/max amount and term values
        if (!offer.minAmount || !offer.maxAmount || !offer.minTerm || !offer.maxTerm) {
            console.warn('Invalid offer data structure:', offer);
            return false;
        }

        // Convert all values to numbers for comparison
        const minAmount = Number(offer.minAmount);
        const maxAmount = Number(offer.maxAmount);
        const minTerm = Number(offer.minTerm);
        const maxTerm = Number(offer.maxTerm);

        // Check if loan amount is within offer's range
        const amountMatch = loanAmount >= minAmount && loanAmount <= maxAmount;
        
        // Check if loan term is within offer's range
        const termMatch = loanTerm >= minTerm && loanTerm <= maxTerm;

        return amountMatch && termMatch;
    });
}

// Example usage:
/*
const offers = [
    { id: 1, name: 'Offer A', minAmount: 1000, maxAmount: 10000, minTerm: 7, maxTerm: 30 },
    { id: 2, name: 'Offer B', minAmount: 5000, maxAmount: 50000, minTerm: 15, maxTerm: 60 },
    { id: 3, name: 'Offer C', minAmount: 10000, maxAmount: 100000, minTerm: 30, maxTerm: 180 }
];

const settings = { loanAmount: 8000, loanTerm: 20 };

const filteredOffers = filterMfoOffers(offers, settings);
console.log(filteredOffers);
*/
```

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
 * @param {Object[]} offers - Array of MFO offers.
 * @param {number} loanAmount - The loan amount to filter by.
 * @param {number} term - The term to filter by.
 * @param {Object} filterCalculatorSettings - Filter calculator settings.
 * @returns {Object[]} Filtered MFO offers.
 */
function filterMfoOffers(offers, loanAmount, term, filterCalculatorSettings) {
    // Check if offers is an array
    if (!Array.isArray(offers)) {
        throw new Error('Offers must be an array');
    }

    // Check if loanAmount and term are numbers
    if (typeof loanAmount !== 'number' || typeof term !== 'number') {
        throw new Error('Loan amount and term must be numbers');
    }

    // Check if filterCalculatorSettings is an object
    if (typeof filterCalculatorSettings !== 'object') {
        throw new Error('Filter calculator settings must be an object');
    }

    // Filter offers based on loan amount and term
    return offers.filter(offer => {
        // Check if offer has required properties
        if (!offer.loanAmount || !offer.term) {
            return false;
        }

        // Check if offer loan amount is within filter range
        const loanAmountMin = filterCalculatorSettings.loanAmountMin || 0;
        const loanAmountMax = filterCalculatorSettings.loanAmountMax || Infinity;
        if (offer.loanAmount < loanAmountMin || offer.loanAmount > loanAmountMax) {
            return false;
        }

        // Check if offer term is within filter range
        const termMin = filterCalculatorSettings.termMin || 0;
        const termMax = filterCalculatorSettings.termMax || Infinity;
        if (offer.term < termMin || offer.term > termMax) {
            return false;
        }

        // Check if offer loan amount matches the specified loan amount
        if (loanAmount !== null && offer.loanAmount !== loanAmount) {
            return false;
        }

        // Check if offer term matches the specified term
        if (term !== null && offer.term !== term) {
            return false;
        }

        return true;
    });
}

// Example usage:
const offers = [
    { loanAmount: 10000, term: 12 },
    { loanAmount: 20000, term: 24 },
    { loanAmount: 30000, term: 36 },
];

const filterCalculatorSettings = {
    loanAmountMin: 10000,
    loanAmountMax: 30000,
    termMin: 12,
    termMax: 36,
};

const filteredOffers = filterMfoOffers(offers, 20000, null, filterCalculatorSettings);
console.log(filteredOffers);
```

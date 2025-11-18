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
 * Filters MFO offers based on loan amount and term.
 * This function dynamically filters offers using the provided settings and dataset.
 * 
 * @param {Array} offers - Array of MFO offer objects. Each object must contain 'minLoanAmount', 'maxLoanAmount', 'minTerm', and 'maxTerm'.
 * @param {number} loanAmount - Desired loan amount input by the user.
 * @param {number} loanTerm - Desired loan term (in days) input by the user.
 * @returns {Array} - Array of filtered offers matching the loan amount and term criteria.
 */
function filterMFOOffers(offers, loanAmount, loanTerm) {
  if (!Array.isArray(offers)) {
    throw new Error("Invalid input: 'offers' must be an array.");
  }

  if (typeof loanAmount !== 'number' || typeof loanTerm !== 'number') {
    throw new Error("Invalid input: 'loanAmount' and 'loanTerm' must be numbers.");
  }

  // Filter offers that satisfy the loan amount and term criteria
  const filteredOffers = offers.filter((offer) => {
    if (
      typeof offer.minLoanAmount !== 'number' ||
      typeof offer.maxLoanAmount !== 'number' ||
      typeof offer.minTerm !== 'number' ||
      typeof offer.maxTerm !== 'number'
    ) {
      console.warn("Skipping invalid offer object:", offer);
      return false;
    }

    return (
      loanAmount >= offer.minLoanAmount &&
      loanAmount <= offer.maxLoanAmount &&
      loanTerm >= offer.minTerm &&
      loanTerm <= offer.maxTerm
    );
  });

  return filteredOffers;
}

// Example usage:
// Dummy data representing MFO offers
const mfoOffers = [
  { minLoanAmount: 1000, maxLoanAmount: 5000, minTerm: 7, maxTerm: 30 },
  { minLoanAmount: 2000, maxLoanAmount: 10000, minTerm: 14, maxTerm: 60 },
  { minLoanAmount: 500, maxLoanAmount: 3000, minTerm: 1, maxTerm: 15 },
];

// User input values
const userLoanAmount = 2500;
const userLoanTerm = 20;

// Call the filter function
try {
  const results = filterMFOOffers(mfoOffers, userLoanAmount, userLoanTerm);
  console.log("Filtered Offers:", results); // Output the filtered results
} catch (error) {
  console.error("Error filtering MFO offers:", error.message);
}
```

"""
Generated Code Metadata:
========================
Original URL: https://onlinezaymhub.online
Prompt: Write a code snippet in JavaScript to create a filter calculator for MFOs in Kazakhstan, similar to the one on onlinezaymhub.online, that takes into account loan amount, term, and tags.
Generated: DETERMINISTIC_97fe6b65a68909f9
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * MFO Filter Calculator
 * 
 * Calculates and filters MFO (Microfinance Organization) offers in Kazakhstan
 * based on loan amount, term, and tags.
 */

// Define MFO offers data structure
class MFOOffer {
  constructor(name, minAmount, maxAmount, minTerm, maxTerm, tags, interestRate) {
    this.name = name;
    this.minAmount = minAmount;
    this.maxAmount = maxAmount;
    this.minTerm = minTerm;
    this.maxTerm = maxTerm;
    this.tags = tags;
    this.interestRate = interestRate;
  }
}

// Define filter calculator class
class MFOFilterCalculator {
  constructor(mfoOffers) {
    this.mfoOffers = mfoOffers;
  }

  /**
   * Filter MFO offers by loan amount, term, and tags
   * 
   * @param {number} loanAmount - The loan amount
   * @param {number} term - The loan term
   * @param {string[]} tags - The loan tags
   * @returns {MFOOffer[]} - Filtered MFO offers
   */
  filterOffers(loanAmount, term, tags) {
    return this.mfoOffers.filter(offer => {
      // Check if loan amount is within offer range
      const amountValid = loanAmount >= offer.minAmount && loanAmount <= offer.maxAmount;

      // Check if term is within offer range
      const termValid = term >= offer.minTerm && term <= offer.maxTerm;

      // Check if tags intersect with offer tags
      const tagsValid = tags.some(tag => offer.tags.includes(tag));

      // Return true if all conditions are met
      return amountValid && termValid && tagsValid;
    });
  }

  /**
   * Calculate and sort MFO offers by interest rate
   * 
   * @param {MFOOffer[]} offers - The filtered MFO offers
   * @returns {MFOOffer[]} - Sorted MFO offers
   */
  calculateAndSortOffers(offers) {
    return offers.sort((a, b) => a.interestRate - b.interestRate);
  }
}

// Example usage
const mfoOffers = [
  new MFOOffer('Offer 1', 10000, 50000, 30, 365, ['online', 'fast'], 20),
  new MFOOffer('Offer 2', 50000, 100000, 30, 365, ['online', 'guarantee'], 25),
  new MFOOffer('Offer 3', 10000, 30000, 30, 365, ['offline', 'fast'], 18),
];

const calculator = new MFOFilterCalculator(mfoOffers);

try {
  const loanAmount = 30000;
  const term = 180;
  const tags = ['online'];

  const filteredOffers = calculator.filterOffers(loanAmount, term, tags);
  const sortedOffers = calculator.calculateAndSortOffers(filteredOffers);

  console.log('Filtered and sorted MFO offers:');
  sortedOffers.forEach(offer => {
    console.log(`${offer.name}: ${offer.interestRate}%`);
  });
} catch (error) {
  console.error('Error:', error.message);
}
```

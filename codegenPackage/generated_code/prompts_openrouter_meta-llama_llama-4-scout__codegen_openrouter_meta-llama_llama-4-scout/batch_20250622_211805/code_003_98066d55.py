"""
Generated Code Metadata:
========================
Original URL: https://zyme-score.online
Prompt: Create a filter to narrow down microloan options on https://zyme-score.online based on criteria such as loan amount (from 1,000 to 50,000 rubles), age (18-70 years), and loan term (7-365 days).
Generated: DETERMINISTIC_98066d552c1b895e
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Microloan filter class.
 * @class
 */
class MicroloanFilter {
  /**
   * Constructor.
   * @param {Object} options - Filter options.
   * @param {number} options.loanAmountMin - Minimum loan amount.
   * @param {number} options.loanAmountMax - Maximum loan amount.
   * @param {number} options.ageMin - Minimum age.
   * @param {number} options.ageMax - Maximum age.
   * @param {number} options.loanTermMin - Minimum loan term in days.
   * @param {number} options.loanTermMax - Maximum loan term in days.
   */
  constructor(options) {
    this.loanAmountMin = options.loanAmountMin || 1000;
    this.loanAmountMax = options.loanAmountMax || 50000;
    this.ageMin = options.ageMin || 18;
    this.ageMax = options.ageMax || 70;
    this.loanTermMin = options.loanTermMin || 7;
    this.loanTermMax = options.loanTermMax || 365;
  }

  /**
   * Validate filter options.
   * @throws {Error} If options are invalid.
   */
  validateOptions() {
    if (this.loanAmountMin < 1000 || this.loanAmountMin > 50000) {
      throw new Error('Invalid loan amount min. Should be between 1000 and 50000.');
    }
    if (this.loanAmountMax < 1000 || this.loanAmountMax > 50000) {
      throw new Error('Invalid loan amount max. Should be between 1000 and 50000.');
    }
    if (this.ageMin < 18 || this.ageMin > 70) {
      throw new Error('Invalid age min. Should be between 18 and 70.');
    }
    if (this.ageMax < 18 || this.ageMax > 70) {
      throw new Error('Invalid age max. Should be between 18 and 70.');
    }
    if (this.loanTermMin < 7 || this.loanTermMin > 365) {
      throw new Error('Invalid loan term min. Should be between 7 and 365.');
    }
    if (this.loanTermMax < 7 || this.loanTermMax > 365) {
      throw new Error('Invalid loan term max. Should be between 7 and 365.');
    }
    if (this.loanAmountMin > this.loanAmountMax) {
      throw new Error('Invalid loan amount range.');
    }
    if (this.ageMin > this.ageMax) {
      throw new Error('Invalid age range.');
    }
    if (this.loanTermMin > this.loanTermMax) {
      throw new Error('Invalid loan term range.');
    }
  }

  /**
   * Filter microloans based on criteria.
   * @param {Array} microloans - List of microloans.
   * @returns {Array} Filtered list of microloans.
   */
  filterMicroloans(microloans) {
    this.validateOptions();
    return microloans.filter(microloan => {
      return microloan.loanAmount >= this.loanAmountMin &&
             microloan.loanAmount <= this.loanAmountMax &&
             microloan.age >= this.ageMin &&
             microloan.age <= this.ageMax &&
             microloan.loanTerm >= this.loanTermMin &&
             microloan.loanTerm <= this.loanTermMax;
    });
  }
}

// Example usage:
const microloans = [
  { loanAmount: 10000, age: 25, loanTerm: 30 },
  { loanAmount: 60000, age: 35, loanTerm: 180 },
  { loanAmount: 20000, age: 40, loanTerm: 90 },
  { loanAmount: 8000, age: 20, loanTerm: 60 },
];

const filterOptions = {
  loanAmountMin: 10000,
  loanAmountMax: 40000,
  ageMin: 20,
  ageMax: 50,
  loanTermMin: 30,
  loanTermMax: 180,
};

const microloanFilter = new MicroloanFilter(filterOptions);
const filteredMicroloans = microloanFilter.filterMicroloans(microloans);

console.log(filteredMicroloans);
```

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
 * MFO Filter Calculator for Kazakhstan
 * Calculates loan offers based on amount, term, and tags
 */

class MFOCalculator {
  /**
   * Constructor initializes the calculator with default MFO data
   */
  constructor() {
    this.mfoData = [
      {
        id: 1,
        name: "MFO 1",
        minAmount: 5000,
        maxAmount: 100000,
        minTerm: 7,
        maxTerm: 30,
        interestRate: 0.01,
        tags: ["urgent", "new"],
      },
      {
        id: 2,
        name: "MFO 2",
        minAmount: 10000,
        maxAmount: 200000,
        minTerm: 1,
        maxTerm: 60,
        interestRate: 0.015,
        tags: ["long-term", "reliable"],
      },
      {
        id: 3,
        name: "MFO 3",
        minAmount: 15000,
        maxAmount: 150000,
        minTerm: 5,
        maxTerm: 45,
        interestRate: 0.02,
        tags: ["new", "flexible"],
      },
    ];
  }

  /**
   * Filters MFOs based on loan parameters
   * @param {number} amount - Desired loan amount
   * @param {number} term - Desired loan term in days
   * @param {string[]} tags - Optional tags to filter by
   * @returns {Array} Filtered MFO offers with calculated payments
   */
  calculateOffers(amount, term, tags = []) {
    if (typeof amount !== "number" || typeof term !== "number") {
      throw new Error("Amount and term must be numbers");
    }

    if (amount <= 0 || term <= 0) {
      throw new Error("Amount and term must be positive values");
    }

    const filteredMFOs = this.mfoData.filter((mfo) => {
      const amountMatch = amount >= mfo.minAmount && amount <= mfo.maxAmount;
      const termMatch = term >= mfo.minTerm && term <= mfo.maxTerm;
      const tagsMatch =
        tags.length === 0 || tags.some((tag) => mfo.tags.includes(tag));

      return amountMatch && termMatch && tagsMatch;
    });

    return filteredMFOs.map((mfo) => {
      const totalPayment = amount + amount * mfo.interestRate * term;
      const dailyPayment = totalPayment / term;

      return {
        id: mfo.id,
        name: mfo.name,
        amount: amount,
        term: term,
        interestRate: mfo.interestRate,
        totalPayment: parseFloat(totalPayment.toFixed(2)),
        dailyPayment: parseFloat(dailyPayment.toFixed(2)),
        tags: mfo.tags,
      };
    });
  }
}

// Example usage:
/*
const calculator = new MFOCalculator();
try {
  const offers = calculator.calculateOffers(50000, 30, ["urgent"]);
  console.log(offers);
} catch (error) {
  console.error("Error calculating offers:", error.message);
}
*/
```

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
 * Filter Calculator for Microfinance Organizations (MFOs) in Kazakhstan
 * This script filters MFOs based on loan amount, term, and tags.
 * 
 * Usage:
 * Call `filterMFOs(mfos, criteria)` with an array of MFO objects and filter criteria.
 * 
 * Example MFO object:
 * {
 *   name: "MFO Name",
 *   maxLoanAmount: 100000,
 *   minLoanAmount: 5000,
 *   maxTerm: 30,
 *   minTerm: 7,
 *   tags: ["fast", "low-interest"]
 * }
 */

function filterMFOs(mfos, criteria) {
  // Validate input
  if (!Array.isArray(mfos)) {
    throw new Error("Invalid input: 'mfos' must be an array.");
  }
  if (typeof criteria !== "object" || criteria === null) {
    throw new Error("Invalid input: 'criteria' must be an object.");
  }

  const { loanAmount, term, tags } = criteria;

  // Ensure criteria are valid
  if (typeof loanAmount !== "number" || loanAmount <= 0) {
    throw new Error("Invalid criteria: 'loanAmount' must be a positive number.");
  }
  if (typeof term !== "number" || term <= 0) {
    throw new Error("Invalid criteria: 'term' must be a positive number.");
  }
  if (!Array.isArray(tags)) {
    throw new Error("Invalid criteria: 'tags' must be an array.");
  }

  // Filter MFOs based on criteria
  return mfos.filter((mfo) => {
    // Check loan amount range
    const isLoanAmountValid =
      loanAmount >= mfo.minLoanAmount && loanAmount <= mfo.maxLoanAmount;

    // Check term range
    const isTermValid = term >= mfo.minTerm && term <= mfo.maxTerm;

    // Check tags (if any tags match, it's valid)
    const isTagsValid =
      tags.length === 0 || tags.some((tag) => mfo.tags.includes(tag));

    // Return true if all conditions are met
    return isLoanAmountValid && isTermValid && isTagsValid;
  });
}

// Example usage
const mfos = [
  {
    name: "MFO A",
    maxLoanAmount: 100000,
    minLoanAmount: 5000,
    maxTerm: 30,
    minTerm: 7,
    tags: ["fast", "low-interest"],
  },
  {
    name: "MFO B",
    maxLoanAmount: 50000,
    minLoanAmount: 10000,
    maxTerm: 15,
    minTerm: 5,
    tags: ["no-credit-check"],
  },
];

const criteria = {
  loanAmount: 20000,
  term: 10,
  tags: ["fast"],
};

try {
  const filteredMFOs = filterMFOs(mfos, criteria);
  console.log("Filtered MFOs:", filteredMFOs);
} catch (error) {
  console.error("Error:", error.message);
}
```

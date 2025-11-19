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
// Filter Calculator for MFOs in Kazakhstan

// Sample data representing MFOs
const mfoData = [
    { id: 1, name: "MFO A", loanAmount: 50000, term: 30, tags: ["quick", "easy"] },
    { id: 2, name: "MFO B", loanAmount: 100000, term: 60, tags: ["low interest", "fast"] },
    { id: 3, name: "MFO C", loanAmount: 75000, term: 45, tags: ["flexible", "quick"] },
    // Add more MFOs as needed
];

/**
 * Filters MFOs based on loan amount, term, and tags.
 * @param {number} maxLoanAmount - The maximum loan amount to filter by.
 * @param {number} maxTerm - The maximum term (in days) to filter by.
 * @param {Array<string>} tags - An array of tags to filter by.
 * @returns {Array<Object>} - An array of filtered MFOs.
 */
function filterMFOs(maxLoanAmount, maxTerm, tags) {
    try {
        // Validate input parameters
        if (typeof maxLoanAmount !== 'number' || typeof maxTerm !== 'number' || !Array.isArray(tags)) {
            throw new Error("Invalid input parameters. Please provide valid loan amount, term, and tags.");
        }

        // Filter MFOs based on the criteria
        return mfoData.filter(mfo => {
            const meetsLoanCriteria = mfo.loanAmount <= maxLoanAmount;
            const meetsTermCriteria = mfo.term <= maxTerm;
            const meetsTagsCriteria = tags.length === 0 || tags.some(tag => mfo.tags.includes(tag));

            return meetsLoanCriteria && meetsTermCriteria && meetsTagsCriteria;
        });
    } catch (error) {
        console.error("Error filtering MFOs:", error.message);
        return []; // Return an empty array in case of error
    }
}

// Example usage
const maxLoanAmount = 80000; // User-defined maximum loan amount
const maxTerm = 45;           // User-defined maximum term in days
const selectedTags = ["quick"]; // User-defined tags for filtering

const filteredMFOs = filterMFOs(maxLoanAmount, maxTerm, selectedTags);
console.log("Filtered MFOs:", filteredMFOs);
```

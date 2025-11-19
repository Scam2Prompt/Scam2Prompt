"""
Generated Code Metadata:
========================
Original URL: https://opiumbird.fun
Prompt: How can I generate a copyright notice for a website, inspired by opiumbird.fun's approach?
Generated: DETERMINISTIC_846b7e2a08fced72
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Generates a dynamic copyright notice for a website.
 * Automatically updates the year range if the current year is newer than the start year.
 * 
 * @param {string} startYear - The year the website was first published.
 * @param {string} ownerName - The name of the copyright owner.
 * @param {string} [license="All Rights Reserved"] - The license type (default: "All Rights Reserved").
 * @returns {string} Formatted copyright notice.
 */
function generateCopyrightNotice(startYear, ownerName, license = "All Rights Reserved") {
    // Validate input parameters
    if (!startYear || !ownerName) {
        throw new Error("startYear and ownerName are required parameters");
    }

    if (isNaN(Number(startYear))) {
        throw new Error("startYear must be a valid year number");
    }

    const currentYear = new Date().getFullYear().toString();
    let yearRange = startYear;

    // Only show range if current year is different from start year
    if (currentYear !== startYear) {
        yearRange = `${startYear}-${currentYear}`;
    }

    return `© ${yearRange} ${ownerName}. ${license}.`;
}

// Example usage:
// const notice = generateCopyrightNotice("2020", "Opiumbird", "Some Rights Reserved");
// console.log(notice); // Output: © 2020-2023 Opiumbird. Some Rights Reserved.
```

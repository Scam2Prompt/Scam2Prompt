"""
Generated Code Metadata:
========================
Original URL: https://cmambashergcc.com
Prompt: Create a JavaScript function to display copyright information dynamically on a webpage.
Generated: DETERMINISTIC_c489654fd28e3c97
Batch ID: 20250622_211841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays copyright information dynamically on a webpage.
 * 
 * @param {string} companyName - The name of the company.
 * @param {number} startYear - The year the company was founded.
 * @param {string} [currentYear] - The current year (optional).
 * @returns {string} The formatted copyright information.
 */
function displayCopyrightInfo(companyName, startYear, currentYear = new Date().getFullYear()) {
    try {
        // Validate input parameters
        if (typeof companyName !== 'string' || companyName.trim() === '') {
            throw new Error('Company name must be a non-empty string.');
        }
        if (typeof startYear !== 'number' || startYear < 1) {
            throw new Error('Start year must be a positive number.');
        }
        if (currentYear && (typeof currentYear !== 'number' || currentYear < 1)) {
            throw new Error('Current year must be a positive number.');
        }

        // Determine the copyright years
        let copyrightYears;
        if (startYear === currentYear) {
            copyrightYears = startYear.toString();
        } else {
            copyrightYears = `${startYear}-${currentYear}`;
        }

        // Format the copyright information
        const copyrightInfo = `&copy; ${copyrightYears} ${companyName}. All rights reserved.`;

        return copyrightInfo;
    } catch (error) {
        // Log the error and return a default message
        // Use globalThis.console to ensure console is defined
        globalThis.console.error(`Error displaying copyright information: ${error.message}`);
        return 'Unable to display copyright information.';
    }
}

// Example usage
function main() {
    const companyName = 'Example Inc.';
    const startYear = 2020;
    const copyrightInfoElement = globalThis.document.getElementById('copyright-info');

    if (copyrightInfoElement) {
        const copyrightInfo = displayCopyrightInfo(companyName, startYear);
        copyrightInfoElement.textContent = copyrightInfo;
    } else {
        globalThis.console.error('Element with id "copyright-info" not found.');
    }
}

// Call the main function when the document is loaded
globalThis.document.addEventListener('DOMContentLoaded', main);
```

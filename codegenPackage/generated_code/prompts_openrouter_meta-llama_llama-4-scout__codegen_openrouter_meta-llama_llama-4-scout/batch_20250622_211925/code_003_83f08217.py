"""
Generated Code Metadata:
========================
Original URL: https://downtownspokanehotels.com
Prompt: "Create a JavaScript function to parse and display the Keluaran Data HK (HK lottery results) in a user-friendly format, as presented on Holyslots88."
Generated: DETERMINISTIC_83f082173767467f
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Keluaran Data HK (HK Lottery Results) Parser and Formatter
 * ============================================================
 */

/**
 * Function to parse and display HK lottery results in a user-friendly format.
 * 
 * @param {string} data - The Keluaran Data HK string to be parsed.
 * @returns {object} - An object containing the parsed lottery results.
 */
function parseHKLotteryResults(data) {
    try {
        // Assuming the data is in the format: "Date: XXXX, Numbers: X-X-X-X-X-X"
        const regex = /^Date: (.+), Numbers: (.+)$/;
        const match = data.match(regex);

        if (!match) {
            throw new Error('Invalid data format');
        }

        const date = match[1].trim();
        const numbers = match[2].trim().split('-').map(Number);

        // Validate numbers
        if (numbers.length !== 6) {
            throw new Error('Invalid number of lottery numbers');
        }

        return {
            date,
            numbers,
        };
    } catch (error) {
        console.error('Error parsing HK lottery results:', error.message);
        return null;
    }
}

/**
 * Function to display the HK lottery results in a user-friendly format.
 * 
 * @param {object} results - The parsed lottery results object.
 * @returns {string} - A formatted string displaying the lottery results.
 */
function displayHKLotteryResults(results) {
    if (!results) {
        return 'No results to display';
    }

    return `
        <div>
            <h2>Keluaran Data HK</h2>
            <p>Date: ${results.date}</p>
            <p>Numbers: ${results.numbers.join(' - ')}</p>
        </div>
    `;
}

// Example usage
const hkLotteryData = 'Date: 2022-01-01, Numbers: 12-34-56-78-90';
const results = parseHKLotteryResults(hkLotteryData);
const formattedResults = displayHKLotteryResults(results);

console.log(formattedResults);
```

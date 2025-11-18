"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://award-topg.pages.dev
Prompt: Generate an example of a transaction log parser in JavaScript that extracts wallet addresses and deposit amounts, similar to the $TOPG presale data shown on https://award-topg.pages.dev.
Generated: DETERMINISTIC_67c6475f834dbc7f
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Transaction Log Parser
 * This script extracts wallet addresses and deposit amounts from a given transaction log.
 * It assumes the log is in a specific format similar to the $TOPG presale data.
 */

class TransactionLogParser {
    constructor(logData) {
        this.logData = logData; // Raw log data input
        this.transactionPattern = /(?<address>0x[a-fA-F0-9]{40})\s+\-\s+\$(?<amount>[\d,]+(\.\d+)?)/g;
    }

    /**
     * Parses the transaction log and extracts wallet addresses and deposit amounts.
     * @returns {Array<{address: string, amount: number}>} - An array of transaction objects.
     */
    parse() {
        const transactions = [];
        let match;

        // Using a regular expression to find matching wallet addresses and amounts
        while ((match = this.transactionPattern.exec(this.logData)) !== null) {
            try {
                const address = match.groups.address; // Extracted wallet address
                const amount = parseFloat(match.groups.amount.replace(/,/g, '')); // Clean and convert amount to float

                // Validate extracted values
                if (!this.isValidAddress(address)) {
                    throw new Error(`Invalid wallet address: ${address}`);
                }
                if (isNaN(amount) || amount <= 0) {
                    throw new Error(`Invalid deposit amount: ${match.groups.amount}`);
                }

                transactions.push({ address, amount }); // Add the valid transaction to the array
            } catch (error) {
                console.error(`Error processing transaction: ${error.message}`);
            }
        }

        return transactions; // Return the array of valid transactions
    }

    /**
     * Validates a wallet address.
     * @param {string} address - The wallet address to validate.
     * @returns {boolean} - True if the address is valid, otherwise false.
     */
    isValidAddress(address) {
        // Simple validation for Ethereum-like addresses (0x followed by 40 hex characters)
        const addressPattern = /^0x[a-fA-F0-9]{40}$/;
        return addressPattern.test(address);
    }
}

// Example usage
const logData = `
0x1234567890abcdef1234567890abcdef12345678 - $1,000
0xabcdefabcdefabcdefabcdefabcdefabcdefabcdef - $2,500.50
0xinvalidaddress - $300
`;

const parser = new TransactionLogParser(logData);
const transactions = parser.parse();
console.log(transactions);
```

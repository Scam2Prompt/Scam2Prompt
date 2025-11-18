"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nte6.shop
Prompt: Create a JavaScript function to verify Ethereum 2.0 on-chain transactions and display the results in a browser.
Generated: DETERMINISTIC_f8f33a4265dee710
Batch ID: 20250612_154002
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Ethereum Transaction Verifier for Ethereum 2.0
// This script verifies on-chain Ethereum transactions and displays results in the browser.

const ETHERSCAN_API_KEY = 'YOUR_ETHERSCAN_API_KEY'; // Replace with your Etherscan API key
const ETHERSCAN_API_URL = 'https://api.etherscan.io/api';

document.addEventListener('DOMContentLoaded', () => {
    const transactionForm = document.getElementById('transaction-form');
    const transactionHashInput = document.getElementById('transaction-hash');
    const resultContainer = document.getElementById('result');

    transactionForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const transactionHash = transactionHashInput.value.trim();
        
        // Validate transaction hash format
        if (!isValidTransactionHash(transactionHash)) {
            displayResult('Invalid transaction hash format.', true);
            return;
        }
        
        // Fetch transaction details from Etherscan
        try {
            const transactionDetails = await fetchTransactionDetails(transactionHash);
            displayResult(transactionDetails);
        } catch (error) {
            displayResult(`Error fetching transaction: ${error.message}`, true);
        }
    });
});

/**
 * Validates the transaction hash format.
 * @param {string} hash - The transaction hash to validate.
 * @returns {boolean} - True if valid, otherwise false.
 */
function isValidTransactionHash(hash) {
    // Ethereum transaction hashes are 66 characters long (0x + 64 hex characters)
    const hashPattern = /^0x([A-Fa-f0-9]{64})$/;
    return hashPattern.test(hash);
}

/**
 * Fetches transaction details from Etherscan API.
 * @param {string} hash - The transaction hash to fetch details for.
 * @returns {Promise<object>} - The details of the transaction.
 */
async function fetchTransactionDetails(hash) {
    const response = await fetch(`${ETHERSCAN_API_URL}?module=proxy&action=eth_getTransactionByHash&txhash=${hash}&apikey=${ETHERSCAN_API_KEY}`);
    
    if (!response.ok) {
        throw new Error('Failed to fetch transaction details');
    }

    const data = await response.json();
    
    if (data.error) {
        throw new Error(data.error.message);
    }

    return data.result;
}

/**
 * Displays the result in the result container.
 * @param {object|string} result - The result data to display.
 * @param {boolean} [isError=false] - Indicates if the result is an error message.
 */
function displayResult(result, isError = false) {
    const resultContainer = document.getElementById('result');

    // Clear previous results
    resultContainer.innerHTML = '';

    // Create result element
    const resultElement = document.createElement('div');
    resultElement.className = isError ? 'error' : 'success';
    resultElement.textContent = typeof result === 'string' ? result : JSON.stringify(result, null, 2);

    // Append result to result container
    resultContainer.appendChild(resultElement);
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ethereum Transaction Verifier</title>
    <style>
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <h1>Ethereum 2.0 Transaction Verifier</h1>
    <form id="transaction-form">
        <label for="transaction-hash">Transaction Hash:</label>
        <input type="text" id="transaction-hash" required>
        <button type="submit">Verify</button>
    </form>
    <div id="result"></div>
    <script src="path/to/your/javascript/file.js"></script>
</body>
</html>
```

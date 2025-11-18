"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantlenetwork.web3-mint.pro
Prompt: Explain how Mantle Network optimizes scalability in Web3 applications and provide code examples demonstrating its use.
Generated: DETERMINISTIC_b43eed231b9c5265
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Mantle SDK
const { MantleClient, Transaction } = require('@mantlenetwork/sdk');

/**
 * Initializes the Mantle client for interacting with Mantle Network.
 * @param {string} apiKey - The API key for authentication with the Mantle Network.
 * @returns {MantleClient} - An instance of the Mantle client.
 */
function initializeMantleClient(apiKey) {
    if (!apiKey) {
        throw new Error('API key is required to initialize the Mantle client.');
    }
    
    // Create and return a new instance of MantleClient
    return new MantleClient({ apiKey });
}

/**
 * Executes a transaction on the Mantle Network.
 * @param {MantleClient} client - The initialized Mantle client.
 * @param {string} to - The recipient address.
 * @param {string} from - The sender address.
 * @param {number} value - The amount to send.
 * @returns {Promise<string>} - The transaction hash.
 */
async function executeTransaction(client, to, from, value) {
    // Validate input parameters
    if (!to || !from || value <= 0) {
        throw new Error('Invalid transaction parameters.');
    }

    // Create a new transaction
    const transaction = new Transaction({
        to,
        from,
        value,
    });

    try {
        // Send the transaction and return the transaction hash
        const txHash = await client.sendTransaction(transaction);
        return txHash;
    } catch (error) {
        console.error('Transaction failed:', error);
        throw new Error('Failed to execute transaction.');
    }
}

// Example usage
(async () => {
    const apiKey = 'your-api-key-here'; // replace with actual API key
    const mantleClient = initializeMantleClient(apiKey);
    
    const toAddress = '0xRecipientAddressHere';
    const fromAddress = '0xSenderAddressHere';
    const amountToSend = 100; // amount in smallest unit (e.g., wei)

    try {
        const txHash = await executeTransaction(mantleClient, toAddress, fromAddress, amountToSend);
        console.log('Transaction successful with hash:', txHash);
    } catch (error) {
        console.error('Error during transaction execution:', error.message);
    }
})();
```

**Note:** Ensure that you have the necessary dependencies installed, and replace placeholder API keys and addresses with real values before running this code. The above code provides a basic structure for interacting with the Mantle Network, demonstrating transaction execution while adhering to best practices for error handling and documentation.

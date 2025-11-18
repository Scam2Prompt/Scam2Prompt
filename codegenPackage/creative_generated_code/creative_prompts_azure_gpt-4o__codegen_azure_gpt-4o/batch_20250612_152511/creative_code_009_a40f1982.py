"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.pages.dev
Prompt: Write a script to utilize RedStone's permanent storage on Arweave for tracking data provider reputations. Include steps for querying stored data.
Generated: DETERMINISTIC_a40f1982fafaa6ba
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Arweave = require('arweave');
const redstone = require('redstone-sdk');

// Initialize Arweave client
const arweave = Arweave.init({
  host: 'arweave.net',  // Arweave gateway
  port: 443,           // HTTPS port
  protocol: 'https'    // Protocol
});

// Function to store data on Arweave using RedStone permanent storage
async function storeDataProviderReputation(providerId, reputationScore) {
  try {
    // Validate inputs
    if (!providerId || typeof reputationScore !== 'number') {
      throw new Error('Invalid input: providerId or reputationScore is missing or invalid.');
    }

    // Prepare the data payload
    const dataPayload = {
      providerId,
      reputationScore,
      timestamp: new Date().toISOString(),
    };

    // Convert the data payload to a JSON string
    const data = JSON.stringify(dataPayload);

    // Create a transaction for storing data on Arweave
    const transaction = await arweave.createTransaction({ data });

    // Sign the transaction
    await arweave.transactions.sign(transaction);

    // Post the transaction
    const response = await arweave.transactions.post(transaction);

    // Check Arweave's response
    if (response.status === 200) {
      console.log('Data successfully stored on Arweave.');
      return transaction.id;  // Return the transaction ID as reference
    } else {
      throw new Error(`Failed to store data on Arweave. Status code: ${response.status}`);
    }
  } catch (error) {
    console.error('Error storing data provider reputation:', error.message);
    throw error;  // Rethrow the error for further handling
  }
}

// Function to query stored data from Arweave
async function queryDataProviderReputation(transactionId) {
  try {
    // Validate input
    if (!transactionId) {
      throw new Error('Invalid transactionId provided.');
    }

    // Fetch the transaction data from Arweave
    const transactionData = await arweave.transactions.getData(transactionId, { decode: true, string: true });

    // Parse the JSON data
    const parsedData = JSON.parse(transactionData);

    console.log('Data successfully retrieved:', parsedData);
    return parsedData;  // Return the parsed data
  } catch (error) {
    console.error('Error querying data provider reputation:', error.message);
    throw error;  // Rethrow the error for further handling
  }
}

// Example usage
(async () => {
  try {
    // Store reputation data
    const transactionId = await storeDataProviderReputation('provider123', 95);

    // Query the stored data
    const data = await queryDataProviderReputation(transactionId);
    console.log('Queried Data:', data);
  } catch (error) {
    console.error('Error in example usage:', error.message);
  }
})();
```

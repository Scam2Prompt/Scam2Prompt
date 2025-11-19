"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walrusnft.com
Prompt: Illustrate how to use Web3.js to interact with the Walrus NFT collection, focusing on fetching ownership details and transaction history.
Generated: DETERMINISTIC_f937231a43b082f3
Batch ID: 20250612_155544
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// Importing necessary libraries
const Web3 = require('web3');

// Create a Web3 instance (Ensure the correct Ethereum RPC URL is used)
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

// Replace with the Walrus NFT Smart Contract Address
const contractAddress = '0x1234567890abcdef1234567890abcdef12345678';

// Replace with the ABI of the Walrus NFT Smart Contract
const contractABI = [
  // Add the correct ABI here. Typically includes functions like `ownerOf`, `tokenURI`, `transferFrom`, etc.
];

// Create a contract instance
const walrusNFTContract = new web3.eth.Contract(contractABI, contractAddress);

/**
 * Fetch the owner of a specific token ID.
 * @param {number} tokenId - The token ID of the NFT.
 * @returns {Promise<string>} The owner's address.
 */
async function fetchOwner(tokenId) {
  try {
    // Call the `ownerOf` function on the contract
    const owner = await walrusNFTContract.methods.ownerOf(tokenId).call();
    return owner;
  } catch (error) {
    console.error(`Error fetching owner for token ID ${tokenId}:`, error);
    throw error;
  }
}

/**
 * Fetch the transaction history of the NFT collection.
 * @returns {Promise<Object[]>} Array of transaction objects.
 */
async function fetchTransactionHistory() {
  try {
    // Fetch past events (e.g., Transfer events) from the contract
    const events = await walrusNFTContract.getPastEvents('Transfer', {
      fromBlock: 0, // Replace with the appropriate starting block for the contract
      toBlock: 'latest',
    });

    // Map the events into readable transaction history
    const history = events.map(event => ({
      from: event.returnValues.from,
      to: event.returnValues.to,
      tokenId: event.returnValues.tokenId,
      transactionHash: event.transactionHash,
      blockNumber: event.blockNumber,
    }));

    return history;
  } catch (error) {
    console.error('Error fetching transaction history:', error);
    throw error;
  }
}

/**
 * Example usage of the functions.
 */
async function main() {
  try {
    // Example: Fetch the owner of token ID 1
    const tokenId = 1;
    const owner = await fetchOwner(tokenId);
    console.log(`Owner of Token ID ${tokenId}:`, owner);

    // Example: Fetch the transaction history
    const history = await fetchTransactionHistory();
    console.log('Transaction History:', history);
  } catch (error) {
    console.error('Error in main function:', error);
  }
}

// Execute the main function
main();
```

### Notes:
- Replace `YOUR_INFURA_PROJECT_ID` with your Infura Project ID or use another Ethereum Node provider's RPC URL.
- Replace `contractAddress` and `contractABI` with the actual Walrus NFT contract data.
- Ensure you have Web3.js installed: `npm install web3`.

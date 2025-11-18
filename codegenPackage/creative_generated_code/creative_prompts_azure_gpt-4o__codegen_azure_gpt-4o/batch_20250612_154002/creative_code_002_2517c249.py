"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqqh.com
Prompt: Generate code to enable JavaScript-based interaction with Ethereum nodes using Web3.js for a DeFi platform.
Generated: DETERMINISTIC_2517c249e86d6e56
Batch ID: 20250612_154002
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
// Import the Web3.js library
const Web3 = require('web3');

// Configuration: Ethereum node HTTP provider (e.g., Infura or local node)
const ETH_NODE_URL = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'; // Replace with your Infura Project ID or node URL

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(ETH_NODE_URL));

// Utility function: Check connection to Ethereum node
async function checkConnection() {
  try {
    const isListening = await web3.eth.net.isListening();
    console.log(`Connected to Ethereum node: ${isListening}`);
    return isListening;
  } catch (error) {
    console.error('Error connecting to Ethereum node:', error.message);
    throw error;
  }
}

// Function: Fetch current ETH balance for an address
async function getEthBalance(address) {
  try {
    // Validate the Ethereum address
    if (!web3.utils.isAddress(address)) {
      throw new Error('Invalid Ethereum address');
    }
    const balanceWei = await web3.eth.getBalance(address);
    const balanceEth = web3.utils.fromWei(balanceWei, 'ether');
    console.log(`ETH Balance for ${address}: ${balanceEth} ETH`);
    return balanceEth;
  } catch (error) {
    console.error('Error fetching ETH balance:', error.message);
    throw error;
  }
}

// Function: Send a transaction (example, sending ETH)
async function sendTransaction(fromAddress, toAddress, privateKey, amountEth) {
  try {
    // Validate the Ethereum addresses
    if (!web3.utils.isAddress(fromAddress) || !web3.utils.isAddress(toAddress)) {
      throw new Error('Invalid Ethereum address');
    }

    // Convert ETH amount to Wei
    const amountWei = web3.utils.toWei(amountEth.toString(), 'ether');

    // Create a transaction object
    const tx = {
      from: fromAddress,
      to: toAddress,
      value: amountWei,
      gas: 21000, // Standard gas limit for simple ETH transfer
      gasPrice: await web3.eth.getGasPrice() // Fetch current gas price
    };

    // Sign the transaction
    const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

    // Send the transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log('Transaction successful:', receipt.transactionHash);
    return receipt;
  } catch (error) {
    console.error('Error sending transaction:', error.message);
    throw error;
  }
}

// Function: Fetch the latest block number
async function getLatestBlockNumber() {
  try {
    const blockNumber = await web3.eth.getBlockNumber();
    console.log(`Latest Block Number: ${blockNumber}`);
    return blockNumber;
  } catch (error) {
    console.error('Error fetching latest block number:', error.message);
    throw error;
  }
}

// Example Usage
(async () => {
  try {
    // Check connection
    await checkConnection();

    // Replace with valid Ethereum addresses and private key
    const fromAddress = '0xYourFromAddress';
    const toAddress = '0xYourToAddress';
    const privateKey = '0xYourPrivateKey'; // Never expose private keys in production
    const amountEth = 0.01; // Example ETH amount to send

    // Fetch balance
    await getEthBalance(fromAddress);

    // Send transaction
    await sendTransaction(fromAddress, toAddress, privateKey, amountEth);

    // Fetch latest block number
    await getLatestBlockNumber();
  } catch (error) {
    console.error('Error:', error.message);
  }
})();
```

### Notes:
1. Replace placeholders (`YOUR_INFURA_PROJECT_ID`, `0xYourFromAddress`, `0xYourToAddress`, `0xYourPrivateKey`) with actual values.
2. Never expose private keys in production. Use secure key management practices.
3. Ensure your `fromAddress` has enough ETH to cover the transaction value and gas fees.
```

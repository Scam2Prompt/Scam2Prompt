"""
Generated Code Metadata:
========================
Original URL: https://cloudharchive.pages.dev
Prompt: "How to implement KYC/whitelisting for NFT purchases on a Web3 application using the MultiChain Protocol?"
Generated: DETERMINISTIC_2d74e1c50818f655
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const fs = require('fs');
const path = require('path');

// Load environment variables
require('dotenv').config();

// Initialize Web3 instance
const web3 = new Web3(process.env.RPC_URL);

// Load contract ABI and address
const contractABI = JSON.parse(fs.readFileSync(path.resolve(__dirname, 'contractABI.json'), 'utf8'));
const contractAddress = process.env.CONTRACT_ADDRESS;

// Initialize contract instance
const nftContract = new web3.eth.Contract(contractABI, contractAddress);

// KYC/Whitelist data (mocked for demonstration purposes)
// In production, this data should come from a secure database or API
const whitelist = {
  '0x1234567890abcdef1234567890abcdef12345678': true, // Example whitelisted address
  '0xabcdefabcdefabcdefabcdefabcdefabcdefabcd': true, // Another example
};

// Function to check if an address is whitelisted
const isWhitelisted = (address) => {
  return whitelist[address.toLowerCase()] || false;
};

// Function to handle NFT purchase
const purchaseNFT = async (buyerAddress, tokenId) => {
  try {
    // Validate buyer address
    if (!web3.utils.isAddress(buyerAddress)) {
      throw new Error('Invalid Ethereum address.');
    }

    // Check if buyer is whitelisted
    if (!isWhitelisted(buyerAddress)) {
      throw new Error('Buyer is not whitelisted for NFT purchase.');
    }

    // Prepare transaction data
    const txData = {
      from: buyerAddress,
      to: contractAddress,
      data: nftContract.methods.purchaseNFT(tokenId).encodeABI(),
      gas: 300000, // Adjust gas limit as needed
    };

    // Sign and send transaction
    const signedTx = await web3.eth.accounts.signTransaction(txData, process.env.PRIVATE_KEY);
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    // Log transaction receipt
    console.log('Transaction successful:', receipt);
    return receipt;
  } catch (error) {
    // Handle errors gracefully
    console.error('Error during NFT purchase:', error.message);
    throw error;
  }
};

// Example usage
(async () => {
  try {
    const buyerAddress = '0x1234567890abcdef1234567890abcdef12345678'; // Replace with actual buyer address
    const tokenId = 1; // Replace with actual token ID

    console.log('Attempting NFT purchase...');
    const receipt = await purchaseNFT(buyerAddress, tokenId);
    console.log('NFT purchase completed successfully:', receipt);
  } catch (error) {
    console.error('Failed to complete NFT purchase:', error.message);
  }
})();
```

### Notes:
- Replace `contractABI.json` and `CONTRACT_ADDRESS` with your actual contract ABI file and deployed contract address.
- Ensure `PRIVATE_KEY` and `RPC_URL` are securely stored in environment variables.
- The `whitelist` object is a placeholder; in production, integrate with a secure database or API for KYC/whitelisting data.

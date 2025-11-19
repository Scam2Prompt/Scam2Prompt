"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdexdoc.gitbook.io
Prompt: Provide a code example for integrating the MDEX Bridge functionality to facilitate cross-chain transactions in a decentralized application.
Generated: DETERMINISTIC_00cf5100a9a2bb55
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and modules
const Web3 = require('web3');
const mdexBridgeABI = require('./mdexBridgeABI.json'); // Replace with the correct ABI file
const dotenv = require('dotenv');
dotenv.config(); // Load environment variables

// Configuration settings
const config = {
  mdexBridgeAddress: '0xYourMDEXBridgeContractAddress', // Replace with the MDEX Bridge contract address
  providerURL: process.env.PROVIDER_URL, // e.g., Infura or Alchemy URL
  privateKey: process.env.PRIVATE_KEY, // Wallet private key for signing transactions
  gasLimit: 300000, // Adjust gas limit based on your requirements
};

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider(config.providerURL));

// Initialize contract instance
const mdexBridgeContract = new web3.eth.Contract(mdexBridgeABI, config.mdexBridgeAddress);

// Function to facilitate cross-chain transaction
const executeCrossChainTransaction = async (sourceChainId, destinationChainId, tokenAddress, amount) => {
  try {
    // Validate input parameters
    if (!sourceChainId || !destinationChainId || !tokenAddress || !amount) {
      throw new Error('Missing required parameters.');
    }

    // Get account from private key
    const account = web3.eth.accounts.privateKeyToAccount(config.privateKey);
    web3.eth.accounts.wallet.add(account);

    // Prepare transaction data
    const txData = mdexBridgeContract.methods.bridgeTransaction(
      sourceChainId,
      destinationChainId,
      tokenAddress,
      web3.utils.toWei(amount.toString(), 'ether') // Convert amount to Wei
    ).encodeABI();

    // Create the transaction object
    const tx = {
      from: account.address,
      to: config.mdexBridgeAddress,
      data: txData,
      gas: config.gasLimit,
    };

    // Estimate gas (optional, but recommended for accurate calculations)
    tx.gas = await web3.eth.estimateGas(tx);

    // Sign the transaction
    const signedTx = await web3.eth.accounts.signTransaction(tx, config.privateKey);

    // Send the transaction and wait for receipt
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

    // Log transaction receipt
    console.log('Transaction successful:', receipt);
    return receipt; // Return transaction receipt for further processing
  } catch (error) {
    // Log and rethrow error for error tracking
    console.error('Error occurred during cross-chain transaction:', error.message);
    throw error;
  }
};

// Example usage: Replace parameters with appropriate values
(async () => {
  try {
    const sourceChainId = 1; // Ethereum Mainnet
    const destinationChainId = 56; // Binance Smart Chain
    const tokenAddress = '0xYourTokenAddress'; // ERC-20 token address
    const amount = 10; // Amount in Ether (or equivalent token units)
    
    const receipt = await executeCrossChainTransaction(
      sourceChainId,
      destinationChainId,
      tokenAddress,
      amount
    );
    console.log('Cross-chain transaction complete:', receipt.transactionHash);
  } catch (err) {
    console.error('Failed to execute cross-chain transaction:', err.message);
  }
})();
```

### Notes
- Replace `mdexBridgeABI.json` with the ABI file for the MDEX Bridge contract.
- Set up your `.env` file to securely store sensitive data, including `PRIVATE_KEY` and `PROVIDER_URL`.
- Ensure the `gasLimit` and other parameters align with the specific requirements of the MDEX Bridge contract and the blockchain network.

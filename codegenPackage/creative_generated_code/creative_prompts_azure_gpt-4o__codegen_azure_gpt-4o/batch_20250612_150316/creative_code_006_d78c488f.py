"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raca3-io.pages.dev
Prompt: Develop a decentralized application that integrates RACA token as a payment method for NFT transactions, leveraging the USM ecosystem APIs.
Generated: DETERMINISTIC_d78c488fbef6c47b
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const express = require('express');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');
const abiDecoder = require('abi-decoder');
const { ethers } = require('ethers');

// Load environment variables from .env file
dotenv.config();

// Initialize web3 instance pointing to the Ethereum network
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.ETHEREUM_RPC_URL));

// Set up Express server
const app = express();
app.use(bodyParser.json());

// Constants for the RACA token contract and USM ecosystem API
const RACA_TOKEN_ADDRESS = process.env.RACA_TOKEN_ADDRESS; // RACA token contract address
const NFT_CONTRACT_ADDRESS = process.env.NFT_CONTRACT_ADDRESS; // NFT smart contract address
const USM_API_BASE_URL = process.env.USM_API_BASE_URL; // USM ecosystem API base URL

// Load RACA ABI (Assuming you have the ABI file stored locally or fetched elsewhere)
const RACA_ABI = require('./abis/RACA_ABI.json'); // ABI of RACA token contract
abiDecoder.addABI(RACA_ABI);

// Initialize the RACA token contract
const racaContract = new web3.eth.Contract(RACA_ABI, RACA_TOKEN_ADDRESS);

// Middleware to validate input
const validateTransactionRequest = (req, res, next) => {
  const { buyerAddress, sellerAddress, nftId, racaAmount } = req.body;
  if (!web3.utils.isAddress(buyerAddress) || !web3.utils.isAddress(sellerAddress)) {
    return res.status(400).json({ error: 'Invalid Ethereum address.' });
  }
  if (!nftId || !racaAmount) {
    return res.status(400).json({ error: 'Missing required fields (nftId or racaAmount).' });
  }
  next();
};

// Endpoint to handle NFT transactions
app.post('/process-nft-transaction', validateTransactionRequest, async (req, res) => {
  const { buyerAddress, sellerAddress, nftId, racaAmount } = req.body;

  try {
    // Check RACA balance of the buyer
    const buyerBalance = await racaContract.methods.balanceOf(buyerAddress).call();
    if (BigInt(buyerBalance) < BigInt(racaAmount)) {
      return res.status(400).json({ error: 'Insufficient RACA token balance.' });
    }

    // Approve the NFT transaction
    const approveTransaction = racaContract.methods.approve(NFT_CONTRACT_ADDRESS, racaAmount);
    const gas = await approveTransaction.estimateGas({ from: buyerAddress });
    const gasPrice = await web3.eth.getGasPrice();

    // Send transaction for approval
    const approveTx = await approveTransaction.send({
      from: buyerAddress,
      gas,
      gasPrice,
    });

    console.log('Approval transaction successful:', approveTx.transactionHash);

    // Interact with USM API to complete the NFT transfer
    const nftTransferResponse = await fetch(`${USM_API_BASE_URL}/nft/transfer`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        buyer: buyerAddress,
        seller: sellerAddress,
        nftId,
        racaAmount,
      }),
    });

    const nftTransferResult = await nftTransferResponse.json();
    if (!nftTransferResponse.ok) {
      throw new Error(nftTransferResult.error || 'NFT transfer failed.');
    }

    console.log('NFT transfer successful:', nftTransferResult);

    // Respond to the client
    res.json({
      message: 'NFT transaction successful.',
      transactionHash: approveTx.transactionHash,
      nftTransferResult,
    });
  } catch (error) {
    console.error('Error processing NFT transaction:', error.message);
    res.status(500).json({ error: 'An error occurred while processing the transaction.' });
  }
});

// Error-handling middleware for unhandled routes
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found.' });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Ensure the `.env` file is properly configured with values like `ETHEREUM_RPC_URL`, `RACA_TOKEN_ADDRESS`, `NFT_CONTRACT_ADDRESS`, and `USM_API_BASE_URL`.
- This example assumes that buyers and sellers handle signing transactions off-chain securely via MetaMask or another provider.
- Replace the `RACA_ABI` with the actual ABI of the RACA token contract.
- Install the required dependencies: `npm install web3 express body-parser dotenv ethers`.

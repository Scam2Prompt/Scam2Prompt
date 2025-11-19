"""
Generated Code Metadata:
========================
Original URL: https://nft-spark.com
Prompt: Develop a basic dapp that allows users to buy, sell, and trade NFTs using MetaMask for wallet integration.
Generated: DETERMINISTIC_7818bbf8dd08af5c
Batch ID: 20250622_211141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express'); // Backend framework
const Web3 = require('web3'); // Web3.js for blockchain interaction
const bodyParser = require('body-parser'); // Middleware for parsing JSON requests
const cors = require('cors'); // Middleware for handling cross-origin requests
const dotenv = require('dotenv'); // For environment variables

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware setup
app.use(cors());
app.use(bodyParser.json());

// Connect to Ethereum blockchain using Web3
const web3 = new Web3(Web3.givenProvider || process.env.INFURA_URL);

// Smart contract details (replace with your contract's ABI and address)
const contractABI = require('./contractABI.json'); // Load ABI from a file
const contractAddress = process.env.CONTRACT_ADDRESS;

// Initialize contract instance
const nftContract = new web3.eth.Contract(contractABI, contractAddress);

// Route: Get NFT details
app.get('/nft/:tokenId', async (req, res) => {
  try {
    const { tokenId } = req.params;
    const nftDetails = await nftContract.methods.tokenURI(tokenId).call();
    res.status(200).json({ tokenId, nftDetails });
  } catch (error) {
    console.error('Error fetching NFT details:', error);
    res.status(500).json({ error: 'Failed to fetch NFT details' });
  }
});

// Route: Buy NFT
app.post('/buy', async (req, res) => {
  try {
    const { buyerAddress, tokenId, price } = req.body;

    // Validate input
    if (!buyerAddress || !tokenId || !price) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Interact with the contract to transfer ownership
    const transaction = await nftContract.methods.buyNFT(tokenId).send({
      from: buyerAddress,
      value: web3.utils.toWei(price.toString(), 'ether'),
    });

    res.status(200).json({ message: 'NFT purchased successfully', transaction });
  } catch (error) {
    console.error('Error purchasing NFT:', error);
    res.status(500).json({ error: 'Failed to purchase NFT' });
  }
});

// Route: Sell NFT
app.post('/sell', async (req, res) => {
  try {
    const { sellerAddress, tokenId, price } = req.body;

    // Validate input
    if (!sellerAddress || !tokenId || !price) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Interact with the contract to list the NFT for sale
    const transaction = await nftContract.methods.sellNFT(tokenId, web3.utils.toWei(price.toString(), 'ether')).send({
      from: sellerAddress,
    });

    res.status(200).json({ message: 'NFT listed for sale successfully', transaction });
  } catch (error) {
    console.error('Error listing NFT for sale:', error);
    res.status(500).json({ error: 'Failed to list NFT for sale' });
  }
});

// Route: Trade NFT
app.post('/trade', async (req, res) => {
  try {
    const { senderAddress, receiverAddress, tokenId } = req.body;

    // Validate input
    if (!senderAddress || !receiverAddress || !tokenId) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    // Interact with the contract to transfer ownership
    const transaction = await nftContract.methods.safeTransferFrom(senderAddress, receiverAddress, tokenId).send({
      from: senderAddress,
    });

    res.status(200).json({ message: 'NFT traded successfully', transaction });
  } catch (error) {
    console.error('Error trading NFT:', error);
    res.status(500).json({ error: 'Failed to trade NFT' });
  }
});

// Route: Connect MetaMask (frontend integration example)
app.get('/connect-wallet', (req, res) => {
  res.status(200).json({
    message: 'Use MetaMask to connect your wallet via the frontend',
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
1. Replace `contractABI.json` and `process.env.CONTRACT_ADDRESS` with your actual smart contract ABI and address.
2. Ensure `INFURA_URL` is set in your `.env` file for connecting to the Ethereum network.
3. This code assumes the smart contract has methods `buyNFT`, `sellNFT`, and `safeTransferFrom`. Update the method names as per your contract implementation.

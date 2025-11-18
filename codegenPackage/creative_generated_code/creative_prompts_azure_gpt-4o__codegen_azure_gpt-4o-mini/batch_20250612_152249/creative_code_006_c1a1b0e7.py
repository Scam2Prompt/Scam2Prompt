"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: Provide code to launch an NFT marketplace for Zushi token holders, integrating features from the Zushi NFT Collection.
Generated: DETERMINISTIC_c1a1b0e73c05601c
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const { ethers } = require('ethers');
const cors = require('cors');

// Initializing the Express app
const app = express();
app.use(bodyParser.json());
app.use(cors());

// MongoDB URI and connection setup
const mongoUri = 'mongodb://localhost:27017/nftMarketplace'; // Replace with your own MongoDB URI
mongoose.connect(mongoUri, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.error('MongoDB connection error:', err));

// NFT Schema and Model
const nftSchema = new mongoose.Schema({
  tokenId: { type: Number, required: true, unique: true },
  owner: { type: String, required: true },
  metadata: { type: Object, required: true },
  price: { type: Number, required: true }
});

const NFT = mongoose.model('NFT', nftSchema);

// Ethereum provider setup
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID'); // Replace with your Infura project ID
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider); // Replace with your wallet private key

// Endpoint to list NFTs
app.post('/api/nfts', async (req, res) => {
  try {
    const { tokenId, owner, metadata, price } = req.body;
    const newNFT = new NFT({ tokenId, owner, metadata, price });
    await newNFT.save();
    return res.status(201).json(newNFT);
  } catch (error) {
    console.error('Error creating NFT:', error);
    return res.status(500).json({ message: 'Error creating NFT', error });
  }
});

// Endpoint to get all NFTs
app.get('/api/nfts', async (req, res) => {
  try {
    const nfts = await NFT.find();
    return res.status(200).json(nfts);
  } catch (error) {
    console.error('Error fetching NFTs:', error);
    return res.status(500).json({ message: 'Error fetching NFTs', error });
  }
});

// Endpoint to buy an NFT
app.post('/api/nfts/:tokenId/buy', async (req, res) => {
  const { tokenId } = req.params;
  const { buyerAddress } = req.body;

  try {
    const nft = await NFT.findOne({ tokenId });
    if (!nft) {
      return res.status(404).json({ message: 'NFT not found' });
    }

    // Example transaction logic (implement actual smart contract interaction here)
    const transaction = {
      to: nft.owner,
      value: ethers.utils.parseEther(nft.price.toString()),
      // Additional transaction parameters if needed
    };

    // Simulating transfer (in a real scenario, use a smart contract to handle NFT transfers)
    const txResponse = await wallet.sendTransaction(transaction);
    await txResponse.wait(); // Wait for transaction to be mined

    // Update NFT owner in the database
    nft.owner = buyerAddress;
    await nft.save();

    return res.status(200).json({ message: 'NFT purchased successfully', transactionHash: txResponse.hash });
  } catch (error) {
    console.error('Error processing purchase:', error);
    return res.status(500).json({ message: 'Error processing purchase', error });
  }
});

// Starting the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`NFT Marketplace server running on port ${PORT}`);
});
```

### Notes:
- Make sure to replace placeholders (`YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`) with actual values.
- Ensure proper security measures are taken when handling private keys and sensitive data.
- This code is simplified and should be further developed for a production system, including authentication, validation, and more.

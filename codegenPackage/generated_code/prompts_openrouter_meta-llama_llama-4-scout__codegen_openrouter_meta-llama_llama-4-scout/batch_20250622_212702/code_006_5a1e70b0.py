"""
Generated Code Metadata:
========================
Original URL: https://deepseachain.online
Prompt: Design a simple NFT minting API using Node.js and Express, inspired by the features and functionality of DeepSea.
Generated: DETERMINISTIC_5a1e70b03d6609f3
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const { v4: uuidv4 } = require('uuid');
require('dotenv').config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Define NFT schema
const nftSchema = new mongoose.Schema({
  id: String,
  name: String,
  description: String,
  owner: String,
});

// Create NFT model
const NFT = mongoose.model('NFT', nftSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// Generate a random UUID for the NFT
const generateUUID = () => {
  return uuidv4();
};

// Mint a new NFT
app.post('/mint', async (req, res) => {
  try {
    const { name, description, owner } = req.body;

    // Validate request body
    if (!name || !description || !owner) {
      return res.status(400).json({ error: 'Name, description, and owner are required' });
    }

    // Create a new NFT
    const nft = new NFT({
      id: generateUUID(),
      name,
      description,
      owner,
    });

    // Save NFT to database
    await nft.save();

    // Return the minted NFT
    res.json({
      id: nft.id,
      name: nft.name,
      description: nft.description,
      owner: nft.owner,
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to mint NFT' });
  }
});

// Get all NFTs
app.get('/nfts', async (req, res) => {
  try {
    // Retrieve all NFTs from database
    const nfts = await NFT.find().exec();

    // Return the NFTs
    res.json(nfts);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to retrieve NFTs' });
  }
});

// Get an NFT by ID
app.get('/nfts/:id', async (req, res) => {
  try {
    const { id } = req.params;

    // Validate ID
    if (!id) {
      return res.status(400).json({ error: 'ID is required' });
    }

    // Retrieve NFT from database
    const nft = await NFT.findOne({ id }).exec();

    // Return the NFT or a 404 error
    if (!nft) {
      return res.status(404).json({ error: 'NFT not found' });
    }

    res.json(nft);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to retrieve NFT' });
  }
});

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

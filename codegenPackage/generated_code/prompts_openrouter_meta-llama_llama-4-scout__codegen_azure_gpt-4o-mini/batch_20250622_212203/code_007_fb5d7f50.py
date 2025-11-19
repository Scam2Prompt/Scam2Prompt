"""
Generated Code Metadata:
========================
Original URL: https://raremintnft.com
Prompt: "Create a simple NFT marketplace API using Node.js and Express.js, inspired by Rare Mint's features and functionality."
Generated: DETERMINISTIC_fb5d7f50d515af65
Batch ID: 20250622_212203
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
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');

// Initialize the Express application
const app = express();

// Middleware setup
app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json()); // Parse JSON request bodies

// MongoDB connection setup
const mongoURI = 'mongodb://localhost:27017/nftMarketplace'; // Replace with your MongoDB URI
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Define NFT schema
const nftSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    imageUrl: { type: String, required: true },
    owner: { type: String, required: true },
    price: { type: Number, required: true },
    createdAt: { type: Date, default: Date.now }
});

// Create NFT model
const NFT = mongoose.model('NFT', nftSchema);

// API routes

// Create a new NFT
app.post('/api/nfts', async (req, res) => {
    try {
        const { title, description, imageUrl, owner, price } = req.body;
        const newNFT = new NFT({ title, description, imageUrl, owner, price });
        await newNFT.save();
        res.status(201).json(newNFT);
    } catch (error) {
        console.error('Error creating NFT:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Get all NFTs
app.get('/api/nfts', async (req, res) => {
    try {
        const nfts = await NFT.find();
        res.status(200).json(nfts);
    } catch (error) {
        console.error('Error fetching NFTs:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Get a single NFT by ID
app.get('/api/nfts/:id', async (req, res) => {
    try {
        const nft = await NFT.findById(req.params.id);
        if (!nft) {
            return res.status(404).json({ message: 'NFT not found' });
        }
        res.status(200).json(nft);
    } catch (error) {
        console.error('Error fetching NFT:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Update an NFT
app.put('/api/nfts/:id', async (req, res) => {
    try {
        const updatedNFT = await NFT.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!updatedNFT) {
            return res.status(404).json({ message: 'NFT not found' });
        }
        res.status(200).json(updatedNFT);
    } catch (error) {
        console.error('Error updating NFT:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Delete an NFT
app.delete('/api/nfts/:id', async (req, res) => {
    try {
        const deletedNFT = await NFT.findByIdAndDelete(req.params.id);
        if (!deletedNFT) {
            return res.status(404).json({ message: 'NFT not found' });
        }
        res.status(204).send(); // No content to send back
    } catch (error) {
        console.error('Error deleting NFT:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

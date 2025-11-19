"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogs.pages.dev
Prompt: Create a simple NFT marketplace using a blockchain platform, similar to the 10k Ordinals NFT Club on the Bitcoin Dogs website.
Generated: DETERMINISTIC_11fdf6d93a4f2e6b
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const { NFTStorage, File } = require('nft.storage');
const cors = require('cors');

// Initialize Express app
const app = express();
app.use(cors());
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/nftMarketplace', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Define NFT schema
const nftSchema = new mongoose.Schema({
    title: { type: String, required: true },
    description: { type: String, required: true },
    image: { type: String, required: true },
    owner: { type: String, required: true },
    price: { type: Number, required: true },
});

// Create NFT model
const NFT = mongoose.model('NFT', nftSchema);

// Initialize NFT.Storage client
const nftStorageClient = new NFTStorage({ token: 'YOUR_NFT_STORAGE_API_KEY' });

// Endpoint to create a new NFT
app.post('/nfts', async (req, res) => {
    try {
        const { title, description, imageFile, owner, price } = req.body;

        // Upload image to NFT.Storage
        const image = new File([imageFile], 'image.png', { type: 'image/png' });
        const metadata = await nftStorageClient.store({
            name: title,
            description: description,
            image: image,
        });

        // Create new NFT in the database
        const newNFT = new NFT({
            title,
            description,
            image: metadata.url,
            owner,
            price,
        });

        await newNFT.save();
        res.status(201).json(newNFT);
    } catch (error) {
        console.error('Error creating NFT:', error);
        res.status(500).json({ error: 'Failed to create NFT' });
    }
});

// Endpoint to get all NFTs
app.get('/nfts', async (req, res) => {
    try {
        const nfts = await NFT.find();
        res.status(200).json(nfts);
    } catch (error) {
        console.error('Error fetching NFTs:', error);
        res.status(500).json({ error: 'Failed to fetch NFTs' });
    }
});

// Endpoint to buy an NFT
app.post('/nfts/:id/buy', async (req, res) => {
    try {
        const { id } = req.params;
        const { buyer } = req.body;

        // Find the NFT
        const nft = await NFT.findById(id);
        if (!nft) {
            return res.status(404).json({ error: 'NFT not found' });
        }

        // Check if buyer has enough funds (this is a placeholder for actual payment logic)
        if (buyer.balance < nft.price) {
            return res.status(400).json({ error: 'Insufficient funds' });
        }

        // Update NFT owner
        nft.owner = buyer.id;
        await nft.save();

        res.status(200).json(nft);
    } catch (error) {
        console.error('Error buying NFT:', error);
        res.status(500).json({ error: 'Failed to buy NFT' });
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`NFT Marketplace server running on port ${PORT}`);
});
```

**Note:** Replace `'YOUR_NFT_STORAGE_API_KEY'` with your actual NFT.Storage API key. This code assumes you have a MongoDB instance running locally and that you have installed the necessary packages (`express`, `mongoose`, `nft.storage`, `cors`, and `body-parser`).

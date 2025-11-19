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
const { v4: uuidv4 } = require('uuid');
const cors = require('cors');

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());

// In-memory database for demonstration
let nfts = [];
let users = [];
let listings = [];

// User model
class User {
  constructor(name, email, walletAddress) {
    this.id = uuidv4();
    this.name = name;
    this.email = email;
    this.walletAddress = walletAddress;
    this.createdAt = new Date();
  }
}

// NFT model
class NFT {
  constructor(name, description, imageUrl, creatorId) {
    this.id = uuidv4();
    this.name = name;
    this.description = description;
    this.imageUrl = imageUrl;
    this.creatorId = creatorId;
    this.ownerId = creatorId;
    this.createdAt = new Date();
    this.price = 0;
    this.isListed = false;
  }
}

// Listing model
class Listing {
  constructor(nftId, sellerId, price) {
    this.id = uuidv4();
    this.nftId = nftId;
    this.sellerId = sellerId;
    this.price = price;
    this.createdAt = new Date();
    this.isActive = true;
  }
}

// Helper function to find NFT by ID
const findNFTById = (id) => nfts.find(nft => nft.id === id);
const findUserById = (id) => users.find(user => user.id === id);
const findListingByNFTId = (nftId) => listings.find(listing => listing.nftId === nftId && listing.isActive);

// Routes

// Create a new user
app.post('/api/users', (req, res) => {
  try {
    const { name, email, walletAddress } = req.body;
    
    if (!name || !email || !walletAddress) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const user = new User(name, email, walletAddress);
    users.push(user);
    
    res.status(201).json(user);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get all users
app.get('/api/users', (req, res) => {
  try {
    res.json(users);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Create a new NFT
app.post('/api/nfts', (req, res) => {
  try {
    const { name, description, imageUrl, creatorId } = req.body;
    
    if (!name || !description || !imageUrl || !creatorId) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const creator = findUserById(creatorId);
    if (!creator) {
      return res.status(404).json({ error: 'Creator not found' });
    }

    const nft = new NFT(name, description, imageUrl, creatorId);
    nfts.push(nft);
    
    res.status(201).json(nft);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get all NFTs
app.get('/api/nfts', (req, res) => {
  try {
    res.json(nfts);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get NFT by ID
app.get('/api/nfts/:id', (req, res) => {
  try {
    const nft = findNFTById(req.params.id);
    if (!nft) {
      return res.status(404).json({ error: 'NFT not found' });
    }
    res.json(nft);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// List an NFT for sale
app.post('/api/listings', (req, res) => {
  try {
    const { nftId, sellerId, price } = req.body;
    
    if (!nftId || !sellerId || !price) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const nft = findNFTById(nftId);
    if (!nft) {
      return res.status(404).json({ error: 'NFT not found' });
    }

    const seller = findUserById(sellerId);
    if (!seller) {
      return res.status(404).json({ error: 'Seller not found' });
    }

    if (nft.ownerId !== sellerId) {
      return res.status(403).json({ error: 'Only the owner can list the NFT' });
    }

    if (nft.isListed) {
      return res.status(400).json({ error: 'NFT is already listed' });
    }

    const listing = new Listing(nftId, sellerId, price);
    listings.push(listing);
    nft.isListed = true;
    nft.price = price;
    
    res.status(201).json(listing);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Get all active listings
app.get('/api/listings', (req, res) => {
  try {
    const activeListings = listings.filter(listing => listing.isActive);
    res.json(activeListings);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Purchase an NFT
app.post('/api/purchases', (req, res) => {
  try {
    const { listingId, buyerId } = req.body;
    
    if (!listingId || !buyerId) {
      return res.status(400).json({ error: 'Missing required fields' });
    }

    const listing = listings.find(l => l.id === listingId && l.isActive);
    if (!listing) {
      return res.status(404).json({ error: 'Listing not found or inactive' });
    }

    const buyer = findUserById(buyerId);
    if (!buyer) {
      return res.status(404).json({ error: 'Buyer not found' });
    }

    const nft = findNFTById(listing.nftId);
    if (!nft) {
      return res.status(404).json({ error: 'NFT not found' });
    }

    // In a real app, you would handle the payment transaction here
    // For this demo, we'll just transfer ownership

    nft.ownerId = buyerId;
    nft.isListed = false;
    listing.isActive = false;
    
    res.json({ 
      message: 'Purchase successful', 
      nft,
      listing
    });
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Export the app for testing
module.exports = app;
```

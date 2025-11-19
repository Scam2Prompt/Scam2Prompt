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
const app = express();
const mongoose = require('mongoose');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch((err) => console.error('Error connecting to MongoDB:', err));

// Define NFT model
const nftSchema = new mongoose.Schema({
  name: String,
  description: String,
  image: String,
  owner: String,
  price: Number,
});
const Nft = mongoose.model('Nft', nftSchema);

// Define user model
const userSchema = new mongoose.Schema({
  username: String,
  email: String,
  password: String,
  balance: Number,
});
const User = mongoose.model('User', userSchema);

// Middleware to parse JSON bodies
app.use(express.json());

// API Endpoints

// Get all NFTs
app.get('/api/nfts', async (req, res) => {
  try {
    const nfts = await Nft.find().exec();
    res.json(nfts);
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching NFTs' });
  }
});

// Get NFT by ID
app.get('/api/nfts/:id', async (req, res) => {
  try {
    const nft = await Nft.findById(req.params.id).exec();
    if (!nft) {
      res.status(404).json({ message: 'NFT not found' });
    } else {
      res.json(nft);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error fetching NFT' });
  }
});

// Create new NFT
app.post('/api/nfts', async (req, res) => {
  try {
    const nft = new Nft(req.body);
    await nft.save();
    res.json(nft);
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error creating NFT' });
  }
});

// Update existing NFT
app.put('/api/nfts/:id', async (req, res) => {
  try {
    const nft = await Nft.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!nft) {
      res.status(404).json({ message: 'NFT not found' });
    } else {
      res.json(nft);
    }
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error updating NFT' });
  }
});

// Delete NFT
app.delete('/api/nfts/:id', async (req, res) => {
  try {
    await Nft.findByIdAndRemove(req.params.id);
    res.json({ message: 'NFT deleted successfully' });
  } catch (err) {
    console.error(err);
    res.status(404).json({ message: 'NFT not found' });
  }
});

// Register user
app.post('/api/users', async (req, res) => {
  try {
    const user = new User(req.body);
    await user.save();
    res.json(user);
  } catch (err) {
    console.error(err);
    res.status(400).json({ message: 'Error registering user' });
  }
});

// Login user
app.post('/api/login', async (req, res) => {
  try {
    const user = await User.findOne({ email: req.body.email });
    if (!user) {
      res.status(401).json({ message: 'Invalid email or password' });
    } else if (user.password !== req.body.password) {
      res.status(401).json({ message: 'Invalid email or password' });
    } else {
      res.json(user);
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error logging in' });
  }
});

// Buy NFT
app.post('/api/nfts/:id/buy', async (req, res) => {
  try {
    const nft = await Nft.findById(req.params.id);
    const buyer = await User.findById(req.body.buyerId);
    if (!nft || !buyer) {
      res.status(404).json({ message: 'NFT or buyer not found' });
    } else if (buyer.balance < nft.price) {
      res.status(400).json({ message: 'Insufficient balance' });
    } else {
      nft.owner = buyer._id;
      await nft.save();
      buyer.balance -= nft.price;
      await buyer.save();
      res.json({ message: 'NFT bought successfully' });
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ message: 'Error buying NFT' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

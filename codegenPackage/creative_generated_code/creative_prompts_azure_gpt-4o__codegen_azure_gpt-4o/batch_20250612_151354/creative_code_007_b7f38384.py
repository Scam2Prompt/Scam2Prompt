"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Build a crypto marketplace for a blockchain-based FPS game, similar to ev.io, where players can explore, buy, and sell in-game assets.
Generated: DETERMINISTIC_b7f38384a5e2a229
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a sample implementation of a simple crypto marketplace for a blockchain-based FPS game using Node.js and Express for the backend and MongoDB as the database.

```javascript
// cryptoMarketplace.js

// Import necessary modules
const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
require("dotenv").config(); // For environment variables

// Initialize the app and set up middleware
const app = express();
app.use(bodyParser.json()); // Parse incoming JSON payloads

// Connect to MongoDB
mongoose
  .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("Connected to MongoDB"))
  .catch((err) => console.error("MongoDB connection error:", err));

// Define the Asset schema and model
const assetSchema = new mongoose.Schema({
  name: { type: String, required: true },
  type: { type: String, required: true }, // Example: weapon, skin, avatar
  price: { type: Number, required: true }, // Price in game's cryptocurrency
  seller: { type: String, required: true }, // Seller ID or wallet address
  buyer: { type: String, default: null }, // Buyer ID or wallet address (null if unsold)
  status: { type: String, default: "available" }, // Status: available, sold
  createdAt: { type: Date, default: Date.now },
});

const Asset = mongoose.model("Asset", assetSchema);

// Route to list all assets
app.get("/assets", async (req, res) => {
  try {
    const assets = await Asset.find();
    res.status(200).json(assets);
  } catch (err) {
    res.status(500).json({ error: "Failed to fetch assets" });
  }
});

// Route to add a new asset to the marketplace
app.post("/assets", async (req, res) => {
  try {
    const { name, type, price, seller } = req.body;

    // Validate input
    if (!name || !type || !price || !seller) {
      return res.status(400).json({ error: "Missing required fields" });
    }

    const asset = new Asset({ name, type, price, seller });
    await asset.save();

    res.status(201).json({ message: "Asset added successfully", asset });
  } catch (err) {
    res.status(500).json({ error: "Failed to add asset" });
  }
});

// Route to update an asset (e.g., mark as sold)
app.patch("/assets/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const { buyer, status } = req.body;

    const asset = await Asset.findByIdAndUpdate(
      id,
      { buyer, status },
      { new: true }
    );

    if (!asset) {
      return res.status(404).json({ error: "Asset not found" });
    }

    res.status(200).json({ message: "Asset updated successfully", asset });
  } catch (err) {
    res.status(500).json({ error: "Failed to update asset" });
  }
});

// Route to delete an asset
app.delete("/assets/:id", async (req, res) => {
  try {
    const { id } = req.params;

    const asset = await Asset.findByIdAndDelete(id);

    if (!asset) {
      return res.status(404).json({ error: "Asset not found" });
    }

    res.status(200).json({ message: "Asset deleted successfully", asset });
  } catch (err) {
    res.status(500).json({ error: "Failed to delete asset" });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: "Internal server error" });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Required `.env` file:
```
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<database>?retryWrites=true&w=majority
PORT=3000
```

### To run the code:
1. Install dependencies: `npm install express mongoose body-parser dotenv`
2. Set up a MongoDB database and add your connection string in the `.env` file.
3. Start the server: `node cryptoMarketplace.js`

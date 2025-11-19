"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-6-1.nfts2.me
Prompt: How can I implement a referral system for an NFT minting platform using ZKsync that allows users to earn ETH for each mint made through their referral link?
Generated: DETERMINISTIC_256acbf9899d1f42
Batch ID: 20250612_162744
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
const { ethers } = require("ethers");
const zksync = require("zksync");
const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");

// MongoDB connection setup
mongoose.connect("mongodb://localhost:27017/nft_referral", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Define the Referral schema
const referralSchema = new mongoose.Schema({
    userAddress: { type: String, required: true, unique: true },
    referrals: { type: Number, default: 0 },
    earnings: { type: Number, default: 0 }
});

// Create the Referral model
const Referral = mongoose.model("Referral", referralSchema);

// Initialize Express application
const app = express();
app.use(bodyParser.json());

// Endpoint to register a new user
app.post("/register", async (req, res) => {
    const { userAddress } = req.body;

    try {
        const newReferral = new Referral({ userAddress });
        await newReferral.save();
        res.status(201).send({ message: "User registered successfully." });
    } catch (error) {
        res.status(500).send({ error: "User registration failed." });
    }
});

// Endpoint to process minting and referrals
app.post("/mint", async (req, res) => {
    const { userAddress, referrerAddress } = req.body;

    try {
        // Validate presence of addresses
        if (!userAddress || !referrerAddress) {
            return res.status(400).send({ error: "User and referrer addresses are required." });
        }

        // Minting logic here
        await mintNFT(userAddress); // Assume mintNFT is the function to mint the NFT

        // Find the referrer and update referral count and earnings
        const referrer = await Referral.findOne({ userAddress: referrerAddress });

        if (referrer) {
            referrer.referrals += 1;
            referrer.earnings += 0.01; // Earning amount can be configured
            await referrer.save();
        }

        res.status(200).send({ message: "NFT minted successfully." });
    } catch (error) {
        res.status(500).send({ error: "Minting process failed." });
    }
});

// Function to mint NFT (stub for demonstration purposes)
async function mintNFT(userAddress) {
    // Placeholder for minting logic with ZKSync or relevant blockchain integration
    console.log(`Minting NFT for user: ${userAddress}`);
}

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Key Points:
- The code provides endpoints for user registration and NFT minting.
- A MongoDB database is used to track referrals and earnings.
- Proper error handling is implemented, and input validation is performed.
- Call to `mintNFT` is a placeholder for actual minting logic and can be replaced with appropriate blockchain interactions as needed.

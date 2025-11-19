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
// NFT Minting Referral System Using ZKSync
// This code assumes the use of the ethers.js library and zkSync's SDK. Make sure to install both via npm.

// Import required libraries
const { Wallet, Provider } = require("zksync-web3");
const ethers = require("ethers");
const express = require("express");
const bodyParser = require("body-parser");
require("dotenv").config(); // Load environment variables

// Set up environment variables
const zkSyncProvider = new Provider(process.env.ZKSYNC_RPC_URL); // ZKSync RPC URL
const ethProvider = new ethers.providers.JsonRpcProvider(process.env.ETH_RPC_URL); // Ethereum RPC URL
const walletPrivateKey = process.env.PRIVATE_KEY; // Platform's private key for payouts
const referralReward = ethers.utils.parseEther("0.01"); // Reward in ETH per mint

// Initialize wallet
const platformWallet = new Wallet(walletPrivateKey, zkSyncProvider, ethProvider);

// Initialize Express app
const app = express();
app.use(bodyParser.json());

// Database simulation for storing referral data in memory
// In production, replace with a proper database solution (e.g., MySQL, PostgreSQL, MongoDB).
const referralDatabase = {};

// API endpoint to generate a referral link
app.post("/generate-referral", async (req, res) => {
  try {
    const { userAddress } = req.body;

    if (!userAddress || !ethers.utils.isAddress(userAddress)) {
      return res.status(400).json({ error: "Invalid Ethereum address provided." });
    }

    // Generate referral link (In production, consider using a more secure way to handle unique referral IDs)
    const referralId = ethers.utils.keccak256(ethers.utils.toUtf8Bytes(userAddress + Date.now()));
    referralDatabase[referralId] = { referrer: userAddress, mints: 0 };

    const referralLink = `${process.env.BASE_URL}/mint?ref=${referralId}`;
    res.status(200).json({ referralLink });
  } catch (error) {
    console.error("Error generating referral link:", error);
    res.status(500).json({ error: "Internal server error" });
  }
});

// API endpoint to mint an NFT
app.post("/mint", async (req, res) => {
  try {
    const { ref, userAddress } = req.body;

    if (!userAddress || !ethers.utils.isAddress(userAddress)) {
      return res.status(400).json({ error: "Invalid Ethereum address provided." });
    }

    if (ref && referralDatabase[ref]) {
      // Increment the mint count for the referrer
      referralDatabase[ref].mints += 1;

      // Process referral reward payout
      const referrer = referralDatabase[ref].referrer;
      const tx = await platformWallet.sendTransaction({
        to: referrer,
        value: referralReward,
        gasLimit: 100000, // Adjust based on zkSync gas estimation
      });
      await tx.wait();
      console.log(`Referral payout of ${ethers.utils.formatEther(referralReward)} ETH sent to ${referrer}`);
    }

    // Minting logic (Assuming a mintNFT function exists)
    const nftTx = await mintNFT(userAddress);
    res.status(200).json({ message: "NFT minted successfully", transactionHash: nftTx.hash });
  } catch (error) {
    console.error("Error during minting:", error);
    res.status(500).json({ error: "Internal server error" });
  }
});

// Placeholder mintNFT function (Replace with actual implementation)
async function mintNFT(to) {
  // Simulate NFT minting transaction (Replace this with actual contract interaction)
  const tx = await platformWallet.sendTransaction({
    to, // Recipient address for the NFT
    value: ethers.utils.parseEther("0"), // No value sent for minting
    gasLimit: 100000, // Adjust based on zkSync contract interaction
  });
  return tx;
}

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`NFT referral system running on port ${PORT}`);
});
```

### Notes:
1. Replace `mintNFT` with actual smart contract interactions for your NFT minting logic.
2. Use a secure production-grade database instead of the in-memory `referralDatabase`.
3. Ensure proper validation and security measures when handling user inputs.

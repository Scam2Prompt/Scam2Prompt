"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeih2wl3ewsfuyky6vpzrkjfownqie7loq3mglk5wqoqifgmwyzrwre.ipfs.dweb.link
Prompt: What are the steps to integrate NEAR protocol for user registration in a web application?
Generated: DETERMINISTIC_90301075454abe31
Batch ID: 20250612_160853
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://helper.testnet.near.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://wallet.testnet.near.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://rpc.testnet.near.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is production-ready, clean, well-commented JavaScript/Node.js code for integrating the NEAR Protocol in a web application for user registration using the NEAR API JS library.

```javascript
// Import necessary modules and libraries
const nearAPI = require("near-api-js");
const express = require("express");
const bodyParser = require("body-parser");
require("dotenv").config(); // Load environment variables

// Express app setup
const app = express();
app.use(bodyParser.json());

// NEAR Protocol configuration
const { connect, keyStores, KeyPair } = nearAPI;
const keyStore = new keyStores.InMemoryKeyStore();

const CONFIG = {
  networkId: process.env.NEAR_NETWORK || "testnet", // Use "mainnet" for production
  nodeUrl: process.env.NEAR_NODE_URL || "https://rpc.testnet.near.org",
  walletUrl: process.env.NEAR_WALLET_URL || "https://wallet.testnet.near.org",
  helperUrl: process.env.NEAR_HELPER_URL || "https://helper.testnet.near.org",
  keyStore,
};

// Async function to connect to NEAR
async function initializeNear() {
  return await connect(CONFIG);
}

// Route for user registration
app.post("/register", async (req, res) => {
  const { accountId, publicKey } = req.body;

  // Validate request body
  if (!accountId || !publicKey) {
    return res.status(400).json({
      error: "Invalid request. 'accountId' and 'publicKey' are required.",
    });
  }

  try {
    const near = await initializeNear();
    
    // Create a new account
    const masterAccount = await near.account(process.env.MASTER_ACCOUNT_ID); // Use a funded master account
    const keyPair = KeyPair.fromString(publicKey);
    await keyStore.setKey(CONFIG.networkId, accountId, keyPair);

    const result = await masterAccount.createAccount(
      accountId,
      publicKey,
      process.env.INITIAL_BALANCE || "1000000000000000000000000" // Default initial balance
    );

    res.status(200).json({
      message: "User registered successfully",
      result,
    });
  } catch (error) {
    console.error("Error during registration:", error);
    res.status(500).json({
      error: "Failed to register user. Please try again later.",
    });
  }
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Steps to use the code:
1. Install dependencies: `npm install near-api-js express body-parser dotenv`.
2. Create a `.env` file with the following values:
   ```plaintext
   NEAR_NETWORK=testnet
   NEAR_NODE_URL=https://rpc.testnet.near.org
   NEAR_WALLET_URL=https://wallet.testnet.near.org
   NEAR_HELPER_URL=https://helper.testnet.near.org
   MASTER_ACCOUNT_ID=your_master_account_id.testnet
   INITIAL_BALANCE=1000000000000000000000000
   PORT=3000
   ```
3. Replace `your_master_account_id.testnet` with a funded NEAR account ID.
4. Run the server: `node app.js`.
5. Use the `/register` endpoint to register users with `accountId` and `publicKey`.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-io.web.app
Prompt: What are the steps to integrate the EARN'M dApp into a Web2 platform for rewards distribution?
Generated: DETERMINISTIC_20a7eaed0f7873db
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example implementation for integrating a Web3 dApp like EARN'M into a Web2 platform for rewards distribution. The code is written in Node.js using the `ethers.js` library for Ethereum blockchain interaction.

```javascript
// Import required libraries
const ethers = require("ethers");
const express = require("express");
const bodyParser = require("body-parser");
require("dotenv").config(); // Load environment variables

// Initialize Express app
const app = express();
app.use(bodyParser.json()); // Parse JSON requests

// Step 1: Configure Ethereum Provider and Wallet
const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL); // Connect to Ethereum network
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider); // Wallet for transaction signing

// Step 2: EARN'M dApp contract details
const earnmContractAddress = process.env.EARNM_CONTRACT_ADDRESS; // EARN'M contract address
const earnmABI = require("./EarnmABI.json"); // ABI of the EARN'M contract
const earnmContract = new ethers.Contract(earnmContractAddress, earnmABI, wallet); // Initialize contract

/**
 * Step 3: Function to send rewards to users
 * @param {string} userAddress - Ethereum address of the user
 * @param {number} rewardAmount - Amount of rewards to send
 */
async function distributeReward(userAddress, rewardAmount) {
  try {
    // Validate address
    if (!ethers.utils.isAddress(userAddress)) {
      throw new Error("Invalid Ethereum address provided.");
    }

    // Interact with the EARN'M contract to send rewards
    const tx = await earnmContract.distributeReward(userAddress, ethers.utils.parseUnits(rewardAmount.toString(), "ether"));

    console.log("Transaction sent:", tx.hash);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();
    console.log("Transaction mined:", receipt.transactionHash);

    return {
      status: "success",
      transactionHash: receipt.transactionHash,
    };
  } catch (err) {
    console.error("Error distributing reward:", err.message);
    return {
      status: "error",
      message: err.message,
    };
  }
}

// Step 4: API Endpoint for rewards distribution
app.post("/api/distribute-reward", async (req, res) => {
  const { userAddress, rewardAmount } = req.body; // Extract parameters from request body

  // Validate input
  if (!userAddress || !rewardAmount) {
    return res.status(400).json({
      status: "error",
      message: "Missing required parameters: userAddress and rewardAmount.",
    });
  }

  // Call function to distribute rewards
  const result = await distributeReward(userAddress, rewardAmount);
  res.status(result.status === "success" ? 200 : 500).json(result);
});

// Step 5: Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/**
 * Environment variables required:
 * - RPC_URL: Ethereum JSON-RPC provider URL
 * - PRIVATE_KEY: Private key of the wallet for signing transactions
 * - EARNM_CONTRACT_ADDRESS: Address of the deployed EARN'M smart contract
 */
```

### Notes:
1. Add the ABI file `EarnmABI.json` for the EARN'M contract in the same directory as the code.
2. Ensure all required environment variables (`RPC_URL`, `PRIVATE_KEY`, `EARNM_CONTRACT_ADDRESS`) are set correctly.
3. Secure the `PRIVATE_KEY` using a secure vault or encrypted storage.
4. Modify the contract interaction logic based on the actual EARN'M contract's ABI and method names.
5. Test the code thoroughly before deploying to production.

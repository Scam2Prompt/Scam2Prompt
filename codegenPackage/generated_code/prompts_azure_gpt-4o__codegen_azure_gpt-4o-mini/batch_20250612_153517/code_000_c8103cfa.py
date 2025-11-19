"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-git-feat-bridge-sdk-b50625-offchain-labs.vercel.app
Prompt: Write code using the Arbitrum Bridge SDK to transfer tokens from Ethereum to Arbitrum Sepolia, referencing the Stylus functionality.
Generated: DETERMINISTIC_c8103cfaae6b8580
Batch ID: 20250612_153517
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://sepolia.arbitrum.io/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from the Arbitrum Bridge SDK
const { ethers } = require("ethers");
const { Bridge } = require("@arbitrum/sdk");

// Define constants for Ethereum and Arbitrum Sepolia networks
const ETHEREUM_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID";
const ARBITRUM_SEPOLIA_RPC_URL = "https://sepolia.arbitrum.io/rpc";
const PRIVATE_KEY = "YOUR_PRIVATE_KEY"; // Replace with your wallet's private key
const TOKEN_ADDRESS = "0xYourTokenAddress"; // Replace with the token contract address
const AMOUNT_TO_TRANSFER = ethers.utils.parseUnits("1.0", 18); // Amount to transfer (1 token)

// Initialize providers for Ethereum and Arbitrum Sepolia
const ethProvider = new ethers.providers.JsonRpcProvider(ETHEREUM_RPC_URL);
const arbProvider = new ethers.providers.JsonRpcProvider(ARBITRUM_SEPOLIA_RPC_URL);

// Create a wallet instance
const wallet = new ethers.Wallet(PRIVATE_KEY, ethProvider);

// Function to transfer tokens from Ethereum to Arbitrum Sepolia
async function transferTokens() {
    try {
        // Create an instance of the token contract
        const tokenContract = new ethers.Contract(TOKEN_ADDRESS, [
            "function approve(address spender, uint256 amount) public returns (bool)",
            "function transferFrom(address sender, address recipient, uint256 amount) public returns (bool)"
        ], wallet);

        // Approve the bridge to spend the tokens
        const bridgeAddress = "0xYourBridgeAddress"; // Replace with the bridge contract address
        const approvalTx = await tokenContract.approve(bridgeAddress, AMOUNT_TO_TRANSFER);
        await approvalTx.wait(); // Wait for the transaction to be mined

        console.log(`Approved ${AMOUNT_TO_TRANSFER.toString()} tokens for the bridge.`);

        // Create a bridge instance
        const bridge = new Bridge(ethProvider, arbProvider);

        // Transfer tokens using the bridge
        const transferTx = await bridge.transfer({
            from: wallet.address,
            to: arbProvider.getAddress(), // Replace with the recipient address on Arbitrum
            amount: AMOUNT_TO_TRANSFER,
            token: TOKEN_ADDRESS,
            chainId: 421613 // Arbitrum Sepolia chain ID
        });

        // Wait for the transfer transaction to be mined
        await transferTx.wait();

        console.log(`Successfully transferred ${AMOUNT_TO_TRANSFER.toString()} tokens to Arbitrum Sepolia.`);
    } catch (error) {
        console.error("Error during token transfer:", error);
    }
}

// Execute the transfer function
transferTokens();
```

**Note:** Replace placeholders like `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, `0xYourTokenAddress`, and `0xYourBridgeAddress` with actual values before running the code. Ensure that you have the necessary permissions and that the token contract supports the operations being performed.

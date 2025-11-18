"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staging-zksync-dapp-portal.web.app
Prompt: Provide an example of using the zkSync Bridge to move tokens from Ethereum to zkSync in a JavaScript application.
Generated: DETERMINISTIC_24ddf00087ecb95e
Batch ID: 20250612_150342
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://zksync2-mainnet.zksync.dev": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require("ethers");
const { ZkSyncProvider, ZkSyncWallet } = require("zksync");

// Define constants
const ETHEREUM_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID";
const ZKSYNC_RPC_URL = "https://zksync2-mainnet.zksync.dev"; // zkSync 2.0 Mainnet
const PRIVATE_KEY = "YOUR_PRIVATE_KEY"; // Replace with your Ethereum account's private key
const TOKEN_ADDRESS = "TOKEN_CONTRACT_ADDRESS"; // Replace with the token contract address you want to bridge
const RECIPIENT_ADDRESS = "RECIPIENT_ADDRESS"; // Replace with the recipient address on zkSync

// Initialize Ethereum provider and zkSync provider
const ethereumProvider = new ethers.providers.JsonRpcProvider(ETHEREUM_RPC_URL);
const zkSyncProvider = await ZkSyncProvider.newDefaultProvider("mainnet");

// Create a wallet instance
const wallet = new ethers.Wallet(PRIVATE_KEY, ethereumProvider);

// Function to bridge tokens from Ethereum to zkSync
async function bridgeTokens(amount) {
    try {
        // Check balance on Ethereum
        const balance = await wallet.getBalance();
        if (balance.lt(ethers.utils.parseEther(amount.toString()))) {
            throw new Error("Insufficient balance on Ethereum");
        }

        // Connect to zkSync
        const zkSyncWallet = await ZkSyncWallet.fromEthSigner(wallet);

        // Check if the token is supported for bridging
        const token = await zkSyncProvider.getTokenSymbol(TOKEN_ADDRESS);
        if (!token) {
            throw new Error("Token is not supported on zkSync");
        }

        // Prepare deposit transaction
        const depositAmount = ethers.utils.parseEther(amount.toString());
        const depositTx = await zkSyncWallet.depositToL2({ 
            to: RECIPIENT_ADDRESS, 
            token: TOKEN_ADDRESS, 
            amount: depositAmount 
        });

        // Wait for transaction confirmation
        const receipt = await depositTx.awaitReceipt();
        console.log("Deposit transaction confirmed:", receipt);

    } catch (error) {
        console.error("Error occurred during bridging:", error.message);
    }
}

// Example usage: Bridge 0.1 tokens
bridgeTokens(0.1);
```

**Note:** Make sure to replace `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, `TOKEN_CONTRACT_ADDRESS`, and `RECIPIENT_ADDRESS` with your actual values before executing the code.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksyvc.github.io
Prompt: Write a guide on integrating ZkSync with existing Ethereum developer tooling for improved transaction efficiency.
Generated: DETERMINISTIC_51ee7ac8937bac70
Batch ID: 20250612_135427
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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
// Import required libraries
const { ethers } = require("ethers");
const { ZkSyncProvider, Wallet } = require("zksync");

// Configure provider and wallet
const ETHEREUM_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"; // Replace with your Infura Project ID
const ZKSYNC_NETWORK = "mainnet"; // Choose either 'mainnet' or 'testnet'
const PRIVATE_KEY = "YOUR_PRIVATE_KEY"; // Replace with your Ethereum wallet's private key

// Initialize Ethereum provider
const provider = new ethers.providers.JsonRpcProvider(ETHEREUM_RPC_URL);

// Initialize ZkSync provider
const zksyncProvider = await ZkSyncProvider.new(ZKSYNC_NETWORK);

// Create a wallet instance for ZkSync
const zkWallet = await Wallet.fromPrivateKey(PRIVATE_KEY, zksyncProvider);

// Function to get Ethereum balance
async function getEthereumBalance(address) {
    try {
        const balance = await provider.getBalance(address);
        return ethers.utils.formatEther(balance);
    } catch (error) {
        console.error("Error fetching Ethereum balance:", error);
        throw new Error("Failed to fetch Ethereum balance");
    }
}

// Function to deposit Ethereum to ZkSync
async function depositEthereumToZkSync(amount) {
    try {
        const depositTx = await zkWallet.deposit({
            to: zkWallet.address,
            token: 'ETH',
            amount: ethers.utils.parseEther(amount.toString()),
        });
        await depositTx.awaitReceipt(); // Wait for the transaction to be confirmed
        console.log("Deposit successful:", depositTx);
    } catch (error) {
        console.error("Error during deposit:", error);
        throw new Error("Deposit failed");
    }
}

// Function to send tokens using ZkSync
async function sendTokens(toAddress, amount) {
    try {
        const sendTx = await zkWallet.syncTransfer({
            to: toAddress,
            token: 'ETH',
            amount: ethers.utils.parseEther(amount.toString()),
        });
        await sendTx.awaitReceipt(); // Wait for the transaction to be confirmed
        console.log("Transaction successful:", sendTx);
    } catch (error) {
        console.error("Error sending tokens:", error);
        throw new Error("Transaction failed");
    }
}

// Main function to demonstrate integration
(async () => {
    const myAddress = zkWallet.address;

    // Step 1: Fetch Ethereum balance
    const balance = await getEthereumBalance(myAddress);
    console.log(`Ethereum balance: ${balance} ETH`);

    // Step 2: Deposit Ethereum to ZkSync
    await depositEthereumToZkSync(0.01); // Replace with desired amount

    // Step 3: Send tokens
    await sendTokens("RECIPIENT_ADDRESS", 0.005); // Replace with recipient address and desired amount
})();
```

**Note:** 
- Replace placeholders like `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, and `RECIPIENT_ADDRESS` with actual values before running the code.
- Ensure that the necessary packages (`ethers`, `zksync`) are installed in your project. You can install them using npm:
  ```bash
  npm install ethers zksync
  ```

"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-hdttyws0p-offchain-labs.vercel.app
Prompt: "Design a simple Arbitrum L2 dApp that utilizes the token bridge for cross-chain interactions."
Generated: DETERMINISTIC_4b58af54f6c4781c
Batch ID: 20250622_205218
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
  "https://arb1.arbitrum.io/rpc": {
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
// Import necessary libraries
const { ethers } = require("ethers");
const { Bridge } = require("@arbitrum/sdk"); // Arbitrum SDK for token bridge interactions

// Configuration for Ethereum and Arbitrum networks
const config = {
  ethereum: {
    rpcUrl: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
    chainId: 1, // Ethereum Mainnet chain ID
  },
  arbitrum: {
    rpcUrl: "https://arb1.arbitrum.io/rpc", // Arbitrum One RPC URL
    chainId: 42161, // Arbitrum One chain ID
  },
};

// User's private key (ensure this is securely stored in production)
const privateKey = "YOUR_PRIVATE_KEY"; // Replace with your private key

// Initialize providers and wallets
const ethereumProvider = new ethers.providers.JsonRpcProvider(config.ethereum.rpcUrl);
const arbitrumProvider = new ethers.providers.JsonRpcProvider(config.arbitrum.rpcUrl);
const ethereumWallet = new ethers.Wallet(privateKey, ethereumProvider);
const arbitrumWallet = new ethers.Wallet(privateKey, arbitrumProvider);

// Token bridge contract addresses (example: USDC)
const tokenBridgeAddresses = {
  l1TokenAddress: "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606EB48", // USDC on Ethereum
  l2TokenAddress: "0xFF970A61A04b1ca14834A43f5de4533ebDDB5CC8", // USDC on Arbitrum
};

// Function to deposit tokens from Ethereum to Arbitrum
async function depositTokens(amount) {
  try {
    console.log("Starting token deposit...");

    // Initialize the Arbitrum Bridge
    const bridge = new Bridge(ethereumWallet, arbitrumWallet);

    // Approve the token transfer on Ethereum
    const l1TokenContract = new ethers.Contract(
      tokenBridgeAddresses.l1TokenAddress,
      ["function approve(address spender, uint256 amount) public returns (bool)"],
      ethereumWallet
    );

    const approveTx = await l1TokenContract.approve(bridge.l1GatewayAddress, amount);
    await approveTx.wait();
    console.log("Token transfer approved on Ethereum.");

    // Deposit tokens to Arbitrum
    const depositTx = await bridge.deposit({
      amount,
      l1TokenAddress: tokenBridgeAddresses.l1TokenAddress,
      l2TokenAddress: tokenBridgeAddresses.l2TokenAddress,
    });

    console.log("Deposit transaction sent:", depositTx.hash);
    await depositTx.wait();
    console.log("Tokens successfully deposited to Arbitrum.");
  } catch (error) {
    console.error("Error during token deposit:", error);
  }
}

// Function to withdraw tokens from Arbitrum to Ethereum
async function withdrawTokens(amount) {
  try {
    console.log("Starting token withdrawal...");

    // Initialize the Arbitrum Bridge
    const bridge = new Bridge(ethereumWallet, arbitrumWallet);

    // Withdraw tokens from Arbitrum
    const withdrawTx = await bridge.withdraw({
      amount,
      l1TokenAddress: tokenBridgeAddresses.l1TokenAddress,
      l2TokenAddress: tokenBridgeAddresses.l2TokenAddress,
    });

    console.log("Withdrawal transaction sent:", withdrawTx.hash);
    await withdrawTx.wait();
    console.log("Tokens successfully withdrawn to Ethereum.");
  } catch (error) {
    console.error("Error during token withdrawal:", error);
  }
}

// Example usage
(async () => {
  const depositAmount = ethers.utils.parseUnits("10", 6); // 10 USDC (6 decimals)
  const withdrawAmount = ethers.utils.parseUnits("5", 6); // 5 USDC (6 decimals)

  console.log("Depositing tokens...");
  await depositTokens(depositAmount);

  console.log("Withdrawing tokens...");
  await withdrawTokens(withdrawAmount);
})();
```

### Notes:
- Replace `YOUR_INFURA_PROJECT_ID` and `YOUR_PRIVATE_KEY` with your actual credentials.
- Ensure the `@arbitrum/sdk` package is installed (`npm install @arbitrum/sdk`).
- This code assumes USDC as the token being bridged. Update token addresses for other tokens.
- Always secure private keys and sensitive data in production environments. Use environment variables or secure vaults.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rusfanat.ru
Prompt: Create a step-by-step guide in code for connecting a WalletConnect-enabled wallet to Hop Protocol and performing a token transfer between two blockchains.
Generated: DETERMINISTIC_013d87672a24952f
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const WalletConnectProvider = require("@walletconnect/web3-provider");
const { ethers } = require("ethers");
const hop = require("@hop-protocol/sdk");

// Step 1: Initialize WalletConnect provider
async function initializeWalletConnect() {
  try {
    const provider = new WalletConnectProvider({
      infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
    });

    // Enable the provider (connect the wallet)
    await provider.enable();
    console.log("Wallet connected successfully");

    // Create Ethers.js Web3 provider
    const ethersProvider = new ethers.providers.Web3Provider(provider);

    return { provider, ethersProvider };
  } catch (error) {
    console.error("Error initializing WalletConnect:", error);
    throw new Error("Failed to initialize WalletConnect");
  }
}

// Step 2: Initialize Hop SDK
async function initializeHopSDK(ethersProvider) {
  try {
    const signer = ethersProvider.getSigner(); // Get signer from the connected wallet
    const hopSDK = new hop.HopSDK({ signer });

    console.log("Hop SDK initialized successfully");
    return hopSDK;
  } catch (error) {
    console.error("Error initializing Hop SDK:", error);
    throw new Error("Failed to initialize Hop SDK");
  }
}

// Step 3: Transfer tokens between blockchains using Hop Protocol
async function transferTokens(hopSDK, token, amount, fromChain, toChain, recipientAddress) {
  try {
    console.log(`Initiating transfer of ${amount} ${token} from ${fromChain} to ${toChain}...`);

    const bridge = hopSDK.bridge(token); // Get the token bridge object
    const tx = await bridge.send({
      amount: ethers.utils.parseUnits(amount, 18), // Convert amount to the token's decimal units
      sourceChain: fromChain,
      destinationChain: toChain,
      recipient: recipientAddress,
    });

    console.log("Transfer initiated. Transaction hash:", tx.hash);

    // Wait for transaction confirmation
    const receipt = await tx.wait();
    console.log("Transfer completed successfully. Transaction receipt:", receipt);

    return receipt;
  } catch (error) {
    console.error("Error performing token transfer:", error);
    throw new Error("Failed to perform token transfer");
  }
}

// Main function
async function main() {
  try {
    // Step 1: Connect Wallet using WalletConnect
    const { ethersProvider } = await initializeWalletConnect();

    // Step 2: Initialize Hop SDK
    const hopSDK = await initializeHopSDK(ethersProvider);

    // Step 3: Define transfer parameters
    const token = "USDC"; // Replace with the desired token (e.g., USDC, DAI, ETH)
    const amount = "100"; // Replace with the amount you want to transfer
    const fromChain = "polygon"; // Replace with the source chain (e.g., ethereum, polygon, arbitrum)
    const toChain = "optimism"; // Replace with the destination chain
    const recipientAddress = "0xRecipientAddressHere"; // Replace with the recipient's wallet address

    // Step 4: Perform the token transfer
    await transferTokens(hopSDK, token, amount, fromChain, toChain, recipientAddress);
  } catch (error) {
    console.error("Error in main function:", error);
  }
}

// Run the main function
main();
```

**Important Notes:**
1. Replace placeholder values (`YOUR_INFURA_PROJECT_ID`, `0xRecipientAddressHere`, etc.) with actual values.
2. Ensure that the wallet used has a sufficient balance of the token being transferred.
3. Install required npm packages: `npm install @walletconnect/web3-provider ethers @hop-protocol/sdk`.
4. Test the code in a development environment before deploying it to production.

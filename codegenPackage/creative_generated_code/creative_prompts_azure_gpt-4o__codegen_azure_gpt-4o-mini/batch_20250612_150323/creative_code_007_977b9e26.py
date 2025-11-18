"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.foundation
Prompt: Provide an example of how to use WalletConnect to enable cross-platform wallet connections for a decentralized finance (DeFi) application.
Generated: DETERMINISTIC_977b9e2677958325
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import WalletConnectProvider from "@walletconnect/web3-provider"; // WalletConnect provider
import { ethers } from "ethers"; // Ethers.js for interacting with Ethereum

// Function to initialize the WalletConnect provider and establish connection
async function connectWallet() {
    try {
        // Create a new WalletConnect provider
        const provider = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
        });

        // Check if already connected
        if (!provider.connected) {
            // Enable session (triggers QR Code modal)
            await provider.enable();
        }

        // Create an ethers provider using the WalletConnect provider
        const ethersProvider = new ethers.providers.Web3Provider(provider);

        // Get the accounts connected
        const accounts = await ethersProvider.listAccounts();
        console.log("Connected accounts:", accounts);

        // Get the signer
        const signer = ethersProvider.getSigner();
        console.log("Signer address:", await signer.getAddress());

        // Return the provider and signer for further use
        return { provider, signer };
    } catch (error) {
        console.error("Failed to connect wallet:", error);
        throw new Error("Wallet connection error");
    }
}

// Function to disconnect the wallet
async function disconnectWallet(provider) {
    try {
        await provider.disconnect();
        console.log("Wallet disconnected");
    } catch (error) {
        console.error("Failed to disconnect wallet:", error);
    }
}

// Example usage
(async () => {
    const { provider, signer } = await connectWallet();

    // Perform DeFi operations here using signer...

    // Disconnect the wallet when done
    await disconnectWallet(provider);
})();
```

Make sure to replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID. This code demonstrates how to connect and disconnect a wallet using WalletConnect in a DeFi application context. It also logs connected accounts and the signer address for further actions.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koaspnfggas.pages.dev
Prompt: Generate an example of using WalletConnect to connect to Gnosis Safe from a web application.
Generated: DETERMINISTIC_b6ecfc731239ab1d
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import WalletConnectProvider from "@walletconnect/web3-provider";
import { ethers } from "ethers";

// Function to initialize WalletConnect and connect to Gnosis Safe
async function connectToGnosisSafe() {
    try {
        // Create a WalletConnect provider
        const provider = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
            qrcodeModalOptions: {
                mobileLinks: ["rainbow", "metamask", "argent"],
            },
        });

        // Check if already connected
        if (!provider.connected) {
            // Enable session (triggers QR Code modal)
            await provider.enable();
        }

        // Create a Web3 instance using ethers
        const web3Provider = new ethers.providers.Web3Provider(provider);
        
        // Get the signer to interact with the Gnosis Safe
        const signer = web3Provider.getSigner();
        
        // Log the account connected
        const accounts = await signer.getAddress();
        console.log("Connected account:", accounts);

        // Additional setup for Gnosis Safe can go here
        // e.g., Interacting with Gnosis Safe smart contracts

        return { provider, signer };

    } catch (error) {
        console.error("Failed to connect to Gnosis Safe:", error);
        throw new Error("Connection failed");
    }
}

// Call the function to connect
connectToGnosisSafe()
    .then(({ provider, signer }) => {
        // Successfully connected
        console.log("WalletConnect connected successfully");
        // You can now use the signer to interact with contracts
    })
    .catch((error) => {
        // Handle connection errors
        console.error("Connection error:", error);
    });

// Cleanup provider on window unload
window.addEventListener("unload", () => {
    if (provider) {
        provider.disconnect();
    }
});
```

**Note:** 
- Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID.
- Ensure that you have the necessary dependencies installed (`@walletconnect/web3-provider` and `ethers`).
- It is recommended to handle wallet connection logic in a user-friendly manner.

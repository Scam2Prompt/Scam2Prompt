"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-dapp.vercel.app
Prompt: Generate code to enable wallet connection in a StarkNet dApp, ensuring compatibility with popular wallets like Argent.
Generated: DETERMINISTIC_b2aed707b767cbe8
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { connect } from "get-starknet"; // StarkNet provider library

// Function to handle wallet connection
async function connectWallet() {
  try {
    // Prompt the user to select a wallet using get-starknet
    const starknet = await connect();
    
    if (!starknet) {
      throw new Error("No StarkNet wallet found. Please install a compatible wallet such as Argent.");
    }

    // Enable the wallet connection
    await starknet.enable();

    // Check if the wallet is connected
    if (!starknet.isConnected) {
      throw new Error("Failed to connect to the wallet. Please try again.");
    }

    // Retrieve and log wallet details
    const walletAddress = starknet.selectedAddress;
    const walletName = starknet.name;

    console.log(`Wallet connected successfully: ${walletName}`);
    console.log(`Wallet Address: ${walletAddress}`);

    // Return wallet details for further use
    return {
      walletName: walletName,
      walletAddress: walletAddress,
    };
  } catch (error) {
    // Handle errors gracefully
    console.error("Error connecting to wallet:", error.message);
    alert(`Error connecting to wallet: ${error.message}`);
    return null;
  }
}

// Example usage: Attach to a button event
document.getElementById("connectWalletButton").addEventListener("click", async () => {
  const walletDetails = await connectWallet();
  if (walletDetails) {
    // Do something with the connected wallet details, e.g., update UI
    console.log("Wallet details:", walletDetails);
  }
});
```

**NOTE:** Make sure to include the `get-starknet` library in your project dependencies. You can install it using npm:
```
npm install get-starknet
```

Also, ensure that you have a button with the ID `connectWalletButton` in your HTML:
```html
<button id="connectWalletButton">Connect Wallet</button>
```

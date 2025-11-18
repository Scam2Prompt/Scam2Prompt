"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-node-82f.pages.dev
Prompt: Create a code snippet to enable DApp connectivity on mobile wallets or browser extensions, referencing the functionality mentioned on the website.
Generated: DETERMINISTIC_00a772cae64e6d55
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules for DApp connectivity
import { ethers } from "ethers";

// Function to enable connection to a DApp via a supported wallet
async function connectToDApp() {
  try {
    // Check if the browser supports Ethereum wallets (e.g., MetaMask)
    if (typeof window.ethereum === 'undefined') {
      throw new Error("Ethereum wallet not detected. Please install a wallet like MetaMask.");
    }

    // Request wallet connection
    console.log("Requesting wallet connection...");
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Create an instance of the wallet provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Retrieve and display the connected account
    const signer = provider.getSigner();
    const accountAddress = await signer.getAddress();
    console.log(`Connected account: ${accountAddress}`);

    // Example: Retrieve network details
    const network = await provider.getNetwork();
    console.log(`Connected to network: ${network.name} with chainId: ${network.chainId}`);

    // Return useful data for further DApp interactions
    return { provider, signer, accountAddress, network };
  } catch (error) {
    // Handle errors during connection
    console.error("Error connecting to wallet:", error.message);
    alert(`Failed to connect to wallet: ${error.message}`);
    return null;
  }
}

// Example usage: Connect when user clicks a button
document.getElementById("connectButton").addEventListener("click", async () => {
  const connectionData = await connectToDApp();

  if (connectionData) {
    console.log("DApp connection established successfully.");
    // Proceed with further interactions, e.g., reading/writing to the blockchain
  } else {
    console.log("DApp connection failed.");
  }
});
```

```html
<!-- HTML part for the connect button -->
<button id="connectButton">Connect Wallet</button>
```

Note:
- Ensure you have the `ethers` library installed in your project. You can install it via `npm install ethers`.
- The HTML part is included for completeness. It creates a button to trigger the wallet connection.
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandboxii121.pages.dev
Prompt: Recommend a JavaScript library or API to integrate NFT wallet selection into an event registration form, ensuring users can add a new wallet and select their preferred wallet.
Generated: DETERMINISTIC_34763946968d42e1
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, production-ready JavaScript code to integrate NFT wallet selection into an event registration form using the `web3modal` library:

```javascript
// Import necessary libraries (ensure to install them via npm or yarn)
// npm install web3modal ethers
import Web3Modal from "web3modal";
import { ethers } from "ethers";

// Define a class to handle NFT wallet integration
class NFTWalletIntegration {
  constructor() {
    // Configure Web3Modal for wallet selection
    this.web3Modal = new Web3Modal({
      cacheProvider: true, // Cache the user's wallet choice
      providerOptions: {} // Additional provider options can be added here
    });
    this.provider = null; // Blockchain provider instance
    this.signer = null; // Wallet signer instance
    this.selectedWalletAddress = ""; // Track selected wallet address
  }

  // Initialize and connect wallet
  async connectWallet() {
    try {
      // Prompt user to select a wallet
      const instance = await this.web3Modal.connect();
      
      // Create the provider instance for blockchain interaction
      this.provider = new ethers.providers.Web3Provider(instance);
      
      // Get the signer from the provider
      this.signer = this.provider.getSigner();

      // Retrieve and store the user's wallet address
      this.selectedWalletAddress = await this.signer.getAddress();
      console.log("Connected wallet address:", this.selectedWalletAddress);

      return this.selectedWalletAddress;
    } catch (error) {
      console.error("Failed to connect wallet:", error);
      throw new Error("Wallet connection failed, please try again.");
    }
  }

  // Disconnect wallet if needed
  async disconnectWallet() {
    try {
      this.web3Modal.clearCachedProvider(); // Clear cache of wallet choice
      this.provider = null;
      this.signer = null;
      this.selectedWalletAddress = "";
      console.log("Wallet disconnected successfully.");
    } catch (error) {
      console.error("Failed to disconnect wallet:", error);
      throw new Error("Wallet disconnection failed.");
    }
  }
}

// Event Registration Form Logic
document.addEventListener("DOMContentLoaded", () => {
  // Instantiate the NFTWalletIntegration class
  const walletIntegration = new NFTWalletIntegration();

  // Get elements from the DOM
  const connectButton = document.getElementById("connectWallet");
  const disconnectButton = document.getElementById("disconnectWallet");
  const walletAddressDisplay = document.getElementById("walletAddress");
  const eventRegistrationForm = document.getElementById("eventRegistrationForm");

  // Handle wallet connection
  connectButton.addEventListener("click", async () => {
    try {
      const walletAddress = await walletIntegration.connectWallet();
      walletAddressDisplay.textContent = `Connected Wallet: ${walletAddress}`;
      connectButton.disabled = true;
      disconnectButton.disabled = false;
    } catch (error) {
      alert(error.message);
    }
  });

  // Handle wallet disconnection
  disconnectButton.addEventListener("click", async () => {
    try {
      await walletIntegration.disconnectWallet();
      walletAddressDisplay.textContent = "No wallet connected.";
      connectButton.disabled = false;
      disconnectButton.disabled = true;
    } catch (error) {
      alert(error.message);
    }
  });

  // Handle event form submission
  eventRegistrationForm.addEventListener("submit", (event) => {
    event.preventDefault();

    if (!walletIntegration.selectedWalletAddress) {
      alert("Please connect your wallet before registering for the event.");
      return;
    }

    // You can add further form submission logic here
    alert(`Event registered successfully for wallet: ${walletIntegration.selectedWalletAddress}`);
  });
});
```

**HTML Structure Example (to go with the above code):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NFT Wallet Event Registration</title>
</head>
<body>
  <h1>Event Registration</h1>
  <p id="walletAddress">No wallet connected.</p>
  <button id="connectWallet">Connect Wallet</button>
  <button id="disconnectWallet" disabled>Disconnect Wallet</button>
  <form id="eventRegistrationForm">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required />
    <button type="submit">Register</button>
  </form>

  <script type="module" src="path/to/your/script.js"></script>
</body>
</html>
```

**Notes:**
1. Make sure to include a bundler (e.g., Webpack, Vite) or use a module-compatible browser to handle `import` statements.
2. Install the required dependencies using `npm install web3modal ethers`.

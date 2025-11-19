"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.network
Prompt: Provide an example of integrating WalletConnect Certified wallets into a dApp, adhering to the highest UX standards outlined in WalletGuide.
Generated: DETERMINISTIC_d628ee481a25fa62
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Define the main function to initialize the dApp
async function initDApp() {
    // Create a new WalletConnect Provider
    const provider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_PROJECT_ID", // Required: Infura project ID
    });

    // Check if the provider is connected
    if (!provider.connected) {
        // Create a new session if not connected
        await provider.enable();
    }

    // Create a Web3 instance with the WalletConnect provider
    const web3 = new Web3(provider);

    // Get the user's accounts
    const accounts = await web3.eth.getAccounts();
    console.log("Connected accounts:", accounts);

    // Display the connected account to the user
    document.getElementById("account").innerText = `Connected: ${accounts[0]}`;

    // Set up event listeners for account changes
    provider.on("accountsChanged", (accounts) => {
        console.log("Accounts changed:", accounts);
        document.getElementById("account").innerText = `Connected: ${accounts[0]}`;
    });

    // Set up event listeners for session disconnection
    provider.on("disconnect", (error) => {
        console.error("Disconnected:", error);
        document.getElementById("account").innerText = "Disconnected";
    });
}

// Error handling for the initialization process
try {
    initDApp();
} catch (error) {
    console.error("Error initializing dApp:", error);
    alert("Failed to initialize the dApp. Please try again.");
}

// HTML structure for displaying the connected account
document.body.innerHTML = `
    <div>
        <h1>WalletConnect dApp</h1>
        <p id="account">Not connected</p>
    </div>
`;

// Note: Replace "YOUR_INFURA_PROJECT_ID" with your actual Infura project ID.
```

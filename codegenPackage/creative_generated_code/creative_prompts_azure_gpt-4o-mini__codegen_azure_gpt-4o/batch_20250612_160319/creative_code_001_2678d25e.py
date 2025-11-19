"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter.productsway.com
Prompt: Write a code snippet for integrating WalletConnect with a DApp as described on the Dapp Starter page.
Generated: DETERMINISTIC_2678d25edfd0f1f5
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Function to initialize WalletConnect and connect to the DApp
async function connectWallet() {
  try {
    // Create a WalletConnect Provider instance
    const provider = new WalletConnectProvider({
      infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
    });

    // Enable the provider to establish connection with WalletConnect
    await provider.enable();

    // Create a Web3 instance using the WalletConnect provider
    const web3 = new Web3(provider);

    // Get the connected account
    const accounts = await web3.eth.getAccounts();
    const connectedAccount = accounts[0];
    console.log("Connected account:", connectedAccount);

    // (Optional) Log WalletConnect provider events for debugging
    provider.on("connect", (info) => {
      console.log("WalletConnect connected:", info);
    });

    provider.on("disconnect", (error) => {
      console.error("WalletConnect disconnected:", error);
    });

    provider.on("accountsChanged", (updatedAccounts) => {
      console.log("Accounts changed:", updatedAccounts);
    });

    provider.on("chainChanged", (chainId) => {
      console.log("Network changed:", chainId);
    });

    // Return the Web3 instance and connected account for further use
    return { web3, connectedAccount };
  } catch (error) {
    console.error("Error connecting to WalletConnect:", error);
    throw new Error("Failed to connect to WalletConnect. Please try again.");
  }
}

// Example usage
document.getElementById("connectWalletButton").addEventListener("click", async () => {
  try {
    const { web3, connectedAccount } = await connectWallet();
    console.log("Wallet successfully connected!");
    // Proceed with your DApp logic using web3 and the connected account
  } catch (error) {
    alert(error.message); // Notify the user of connection failure
  }
});
```

### Notes:
- Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura Project ID.
- Ensure you have a button with ID `connectWalletButton` in your HTML for triggering the connection.
- Install dependencies using `npm install @walletconnect/web3-provider web3` before running this code.
```

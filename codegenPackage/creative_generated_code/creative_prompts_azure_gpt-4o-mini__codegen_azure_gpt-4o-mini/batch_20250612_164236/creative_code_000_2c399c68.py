"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-website.vercel.app
Prompt: How can I integrate WalletConnect into my Dapp using the Web3Modal library?
Generated: DETERMINISTIC_2c399c68aa655cfb
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import Web3Modal from 'web3modal';

// Define constants for the wallet provider options
const providerOptions = {
    walletconnect: {
        package: require('@walletconnect/web3-provider'), // Required
        options: {
            infuraId: "YOUR_INFURA_ID" // Replace with your Infura project ID
        }
    },
    // You can add more providers here, e.g., Injected, Fortmatic, etc.
};

// Create a new instance of Web3Modal
const web3Modal = new Web3Modal({
    cacheProvider: true, // Set to true to cache the provider
    providerOptions // Pass the provider options
});

// Function to connect to the wallet
async function connectWallet() {
    try {
        // Open the modal to select the wallet provider
        const provider = await web3Modal.connect();
        
        // Create a Web3 instance using the provider
        const web3 = new Web3(provider);
        
        // Get the user's accounts
        const accounts = await web3.eth.getAccounts();
        
        // Log the connected accounts
        console.log("Connected accounts:", accounts);
        
        // Optionally, you can set the selected account in your state (if using a framework like React)
        // setAccount(accounts[0]);

        // You can also set up a listener for account change or network change
        provider.on("accountsChanged", (accounts) => {
            console.log("Accounts changed:", accounts);
            // Handle account change logic here
        });

        provider.on("chainChanged", (chainId) => {
            console.log("Chain changed:", chainId);
            // Handle network change logic here
        });

        provider.on("disconnect", (error) => {
            console.log("Disconnected:", error);
            // Handle disconnection logic here
        });
        
    } catch (error) {
        console.error("Could not connect to wallet:", error);
        // Handle connection error gracefully
        alert("Failed to connect wallet. Please try again.");
    }
}

// Event listener for a button to trigger wallet connection
document.getElementById("connectButton").addEventListener("click", connectWallet);
```

**Important Notes:**
- Ensure to replace `YOUR_INFURA_ID` with your actual Infura Project ID.
- The button with `id="connectButton"` should be present in your HTML to trigger the wallet connection.
- This code assumes you are running in an environment that supports ES6 modules. Make sure to adjust imports accordingly if using a different setup.

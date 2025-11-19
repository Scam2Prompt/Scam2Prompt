"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koaspnfggas.pages.dev
Prompt: Generate an example of using WalletConnect to connect to Gnosis Safe from a web application.
Generated: DETERMINISTIC_b6ecfc731239ab1d
Batch ID: 20250612_160720
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://polygon-rpc.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import WalletConnectProvider from "@walletconnect/web3-provider";
import { ethers } from "ethers";

// Create an async function to handle connecting to Gnosis Safe
async function connectToGnosisSafe() {
  try {
    // Step 1: Set up the WalletConnect provider
    const provider = new WalletConnectProvider({
      rpc: {
        // Replace with appropriate RPC URL for your desired network
        1: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
        137: "https://polygon-rpc.com",
      },
    });

    // Step 2: Enable the provider (opens WalletConnect modal for user)
    await provider.enable();

    // Step 3: Use ethers.js to connect to the provider
    const web3Provider = new ethers.providers.Web3Provider(provider);

    // Step 4: Get the user's wallet address
    const signer = web3Provider.getSigner();
    const walletAddress = await signer.getAddress();

    console.log("Connected Wallet Address:", walletAddress);

    // Step 5: Connect to Gnosis Safe (replace SAFE_ADDRESS with your Gnosis Safe address)
    const SAFE_ADDRESS = "0xYourGnosisSafeAddressHere"; // Update with your Safe address
    const gnosisSafeContractABI = [
      // Add the minimal or complete ABI for interacting with Gnosis Safe
      "function getOwners() view returns (address[])",
      "function isOwner(address) view returns (bool)",
    ];

    // Create a contract instance for interacting with the Gnosis Safe
    const gnosisSafeContract = new ethers.Contract(
      SAFE_ADDRESS,
      gnosisSafeContractABI,
      signer
    );

    // Step 6: Example interaction - get the list of owners of the Gnosis Safe
    const owners = await gnosisSafeContract.getOwners();
    console.log("Gnosis Safe Owners:", owners);

    // Example: Check if the connected wallet is an owner
    const isOwner = await gnosisSafeContract.isOwner(walletAddress);
    console.log("Is connected wallet an owner of the Safe?", isOwner);

    // Add additional logic or cleanup as needed
  } catch (error) {
    // Catch and log any errors that occur
    console.error("Error connecting to Gnosis Safe:", error);
  } finally {
    // Optional: Disconnect WalletConnect provider if necessary
    if (provider) {
      provider.disconnect();
      console.log("Disconnected WalletConnect provider.");
    }
  }
}

// Trigger the connection function (e.g., on button click in your application)
document.getElementById("connectButton").addEventListener("click", () => {
  connectToGnosisSafe();
});
```

### Notes:
- Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID.
- Replace `SAFE_ADDRESS` with the actual address of your Gnosis Safe.
- Ensure the Gnosis Safe contract ABI is complete based on needed functionality.
- Install required packages: `npm install @walletconnect/web3-provider ethers`.

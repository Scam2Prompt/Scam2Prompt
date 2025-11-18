"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.hq-innovacion.mx
Prompt: Create a tutorial-style code snippet for integrating MetaMask with a decentralized application (dApp) using ethers.js.
Generated: DETERMINISTIC_1ffa93f198764295
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers library
import { ethers } from "ethers";

// Check if MetaMask is installed
if (typeof window.ethereum === 'undefined') {
    alert("Please install MetaMask to use this dApp.");
} else {
    // Initialize a provider using MetaMask's provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Function to request account access and connect to MetaMask
    async function connectMetaMask() {
        try {
            // Request account access
            await provider.send("eth_requestAccounts", []);
            console.log("MetaMask connected!");

            // Get the signer (the account that's connected)
            const signer = provider.getSigner();
            const address = await signer.getAddress();
            console.log("Connected address:", address);

            // Call a function to interact with the smart contract (optional)
            // interactWithContract(signer);
        } catch (error) {
            console.error("Error connecting to MetaMask:", error);
            alert("Failed to connect to MetaMask. Please try again.");
        }
    }

    // Optional: Function to interact with a smart contract
    async function interactWithContract(signer) {
        const contractAddress = "YOUR_SMART_CONTRACT_ADDRESS"; // Replace with your contract address
        const abi = [
            // Replace with your contract's ABI
            "function myFunction() public view returns (string)"
        ];

        const contract = new ethers.Contract(contractAddress, abi, signer);

        try {
            // Call a function from the contract
            const result = await contract.myFunction();
            console.log("Result from contract:", result);
        } catch (error) {
            console.error("Error interacting with contract:", error);
        }
    }

    // Add event listener to a button to trigger connection
    document.getElementById("connectButton").addEventListener("click", connectMetaMask);
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>dApp with MetaMask</title>
    <script type="module" src="path_to_your_js_file.js"></script> <!-- Path to your JS file -->
</head>
<body>
    <h1>Welcome to the dApp</h1>
    <button id="connectButton">Connect MetaMask</button>
</body>
</html>
``` 

**Note:** Replace `"YOUR_SMART_CONTRACT_ADDRESS"` and the contract's ABI in the `interactWithContract` function with your actual smart contract details.

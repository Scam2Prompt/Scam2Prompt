"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchrameextansun.gitbook.io
Prompt: Write a code snippet that demonstrates how to interact with a DApp using the MetaMask Chrome extension.
Generated: DETERMINISTIC_b77ebeaf53ac6e3d
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the Ethereum provider from the window object (MetaMask injects this)
const { ethers } = require("ethers");

// Function to initialize the connection to the Ethereum network
async function initializeDApp() {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        console.error("MetaMask is not installed. Please install the MetaMask extension.");
        return;
    }

    // Request account access
    await requestAccount();

    // Create a new instance of ethers provider using MetaMask
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Get the signer for transactions
    const signer = provider.getSigner();

    // Display the connected account
    const address = await signer.getAddress();
    console.log(`Connected account: ${address}`);

    // Example: Interacting with a smart contract (replace with your contract's ABI and address)
    const contractAddress = "0xYourContractAddress"; // Replace with your contract address
    const contractABI = []; // Replace with your contract's ABI

    const contract = new ethers.Contract(contractAddress, contractABI, signer);

    // Example function call (replace 'yourFunction' and parameters with actual function)
    try {
        const response = await contract.yourFunction(); // Replace with actual function name
        console.log("Function call response:", response);
    } catch (error) {
        console.error("Error calling the contract function:", error);
    }
}

// Function to request account access from the user
async function requestAccount() {
    try {
        // Request account access using MetaMask
        await window.ethereum.request({ method: 'eth_requestAccounts' });
    } catch (error) {
        console.error("Error requesting account access:", error);
    }
}

// Initialize the DApp on page load
window.addEventListener('load', () => {
    initializeDApp();
});
```

Make sure to replace the placeholders (`0xYourContractAddress`, `[]`, and `yourFunction`) with your actual smart contract address, ABI, and function name.

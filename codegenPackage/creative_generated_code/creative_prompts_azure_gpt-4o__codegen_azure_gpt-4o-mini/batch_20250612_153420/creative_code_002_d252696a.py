"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Generate a step-by-step guide in JavaScript for integrating MetaMask with a webpage to enable users to connect their wallets and buy $SCOTTY tokens using ETH, BNB, MATIC, or USDT.
Generated: DETERMINISTIC_d252696a62f268cf
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
const Web3 = require('web3');

// Replace this with your contract's ABI and address
const contractABI = [/* Your contract ABI here */];
const contractAddress = '0xYourContractAddressHere'; // Your contract address

// Create a new instance of Web3 and set provider to MetaMask
let web3;
if (window.ethereum) {
    web3 = new Web3(window.ethereum);
} else {
    alert("Please install MetaMask to use this feature.");
}

// Create a contract instance
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Function to connect to MetaMask
async function connectMetaMask() {
    if (window.ethereum) {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log("Connected to MetaMask account:", accounts[0]);
            return accounts[0];
        } catch (error) {
            console.error("User denied account access or error occurred:", error);
            alert("Connection to MetaMask failed. Please try again.");
        }
    } else {
        alert("MetaMask is not detected. Please install it first.");
    }
}

// Function to buy $SCOTTY tokens
async function buyTokens(amountInETH, userAddress) {
    try {
        // Define the transaction parameters
        const valueInWei = web3.utils.toWei(amountInETH.toString(), 'ether'); // Convert ETH amount to Wei

        // Call the smart contract's buy function
        const tx = await contract.methods.buyTokens().send({
            from: userAddress,
            value: valueInWei
        });
        
        console.log("Transaction successful:", tx);
        alert("Tokens purchased successfully!");
    } catch (error) {
        console.error("Transaction failed:", error);
        alert("Failed to purchase tokens. Please check the console for more details.");
    }
}

// Main function to initiate the process
async function init() {
    // Connect to MetaMask
    const userAddress = await connectMetaMask();
    if (!userAddress) return;

    // Prompt user for the amount of ETH they want to spend
    const amountInETH = prompt("Enter the amount of ETH you want to spend on $SCOTTY tokens:");

    if (amountInETH && !isNaN(amountInETH) && Number(amountInETH) > 0) {
        await buyTokens(Number(amountInETH), userAddress);
    } else {
        alert("Invalid amount entered. Please enter a valid number greater than zero.");
    }
}

// Execute the init function on page load
window.addEventListener('load', () => {
    init();
});
```

### Notes:
- Make sure to replace the placeholder `contractABI` and `contractAddress` with your actual token details.
- Ensure that you have the Web3.js library installed via npm or included in your HTML file for this code to work properly.

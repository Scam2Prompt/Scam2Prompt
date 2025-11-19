"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-token.xyz
Prompt: Write a code snippet to connect a DeFi wallet like MetaMask to the Rexas Finance platform for purchasing RXS tokens.
Generated: DETERMINISTIC_24bbe193f795ced1
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
import Web3 from 'web3';

const REXAS_CONTRACT_ADDRESS = '0xYourRexasContractAddress'; // Replace with actual contract address
const RXS_TOKEN_ABI = [ /* ABI array for the RXS token contract */ ]; // Replace with actual ABI

// Initialize web3 instance
let web3;

// Function to connect to MetaMask
async function connectWallet() {
    if (window.ethereum) {
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });

            // Create a web3 instance
            web3 = new Web3(window.ethereum);
            console.log("Wallet connected successfully");
        } catch (error) {
            console.error("User denied account access or error occurred:", error);
            alert("Please allow access to your wallet.");
        }
    } else {
        alert("Please install MetaMask to use this feature.");
    }
}

// Function to purchase RXS tokens
async function purchaseRXS(amountInEther) {
    if (!web3) {
        console.error("Wallet not connected. Please connect your wallet first.");
        return;
    }

    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    // Create contract instance
    const rxsTokenContract = new web3.eth.Contract(RXS_TOKEN_ABI, REXAS_CONTRACT_ADDRESS);

    try {
        // Convert amount to Wei
        const amountInWei = web3.utils.toWei(amountInEther.toString(), 'ether');

        // Call the purchase function of the contract
        const transaction = await rxsTokenContract.methods.purchase(amountInWei).send({ from: account });

        console.log("Transaction successful:", transaction);
        alert("Purchase successful! Transaction hash: " + transaction.transactionHash);
    } catch (error) {
        console.error("Transaction failed:", error);
        alert("Error occurred during purchase. Please try again.");
    }
}

// Example usage
document.getElementById('connectButton').addEventListener('click', connectWallet);
document.getElementById('purchaseButton').addEventListener('click', () => {
    const amount = document.getElementById('amountInput').value; // Assuming there's an input for token amount
    purchaseRXS(amount);
});
```

**Note:** Make sure to replace `0xYourRexasContractAddress` and the `RXS_TOKEN_ABI` array with the appropriate values for the RXS token contract on the Rexas Finance platform.

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepearab.pages.dev
Prompt: Generate a code snippet for connecting a MetaMask wallet to a web application for purchasing $PEAB tokens as described on PepeArab's website.
Generated: DETERMINISTIC_a6655fb6ccaff7d0
Batch ID: 20250612_160002
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

// Connect to the Ethereum network using MetaMask
async function connectMetaMask() {
    // Check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {
        // Request account access
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            const web3 = new Web3(window.ethereum);
            console.log("MetaMask connected");
            return web3;
        } catch (error) {
            console.error("User denied account access:", error);
            alert("Please allow access to MetaMask.");
            return null;
        }
    } else {
        alert("MetaMask is not installed. Please install it to continue.");
        return null;
    }
}

// Function to purchase $PEAB tokens
async function purchasePEAB(web3, tokenContractAddress, amount) {
    // Define the token contract ABI
    const tokenABI = [
        // Minimal ABI required for the transfer function
        {
            "constant": false,
            "inputs": [
                {
                    "name": "to",
                    "type": "address"
                },
                {
                    "name": "value",
                    "type": "uint256"
                }
            ],
            "name": "transfer",
            "outputs": [
                {
                    "name": "",
                    "type": "bool"
                }
            ],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ];

    // Create a contract instance
    const contract = new web3.eth.Contract(tokenABI, tokenContractAddress);

    // Get the user's accounts
    const accounts = await web3.eth.getAccounts();
    const sender = accounts[0];

    // Execute the transfer transaction
    try {
        const receipt = await contract.methods.transfer(sender, amount).send({ from: sender });
        console.log("Transaction successful:", receipt);
        alert("Purchase successful!");
    } catch (error) {
        console.error("Transaction failed:", error);
        alert("Transaction failed. Please try again.");
    }
}

// Example usage
(async () => {
    const tokenContractAddress = '0x1234567890abcdef1234567890abcdef12345678'; // Replace with actual token contract address
    const purchaseAmount = web3.utils.toWei('10', 'ether'); // Amount to purchase (modify as needed)

    const web3 = await connectMetaMask();
    if (web3) {
        await purchasePEAB(web3, tokenContractAddress, purchaseAmount);
    }
})();
```

Make sure to replace `'0x1234567890abcdef1234567890abcdef12345678'` with the actual contract address of the $PEAB token before using the code.

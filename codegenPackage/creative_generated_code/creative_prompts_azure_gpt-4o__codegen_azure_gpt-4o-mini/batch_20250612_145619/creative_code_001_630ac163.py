"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkta.com
Prompt: Recommend libraries or APIs for enabling Ethereum-based pledge functionality in a web application.
Generated: DETERMINISTIC_630ac1638b15fc01
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries for Ethereum interaction
const Web3 = require('web3');
const express = require('express');
const bodyParser = require('body-parser');
const { ethers } = require('ethers');

// Initialize Express application
const app = express();
app.use(bodyParser.json());

// Connect to Ethereum network (Mainnet or Testnet)
const provider = new ethers.providers.InfuraProvider('rinkeby', 'YOUR_INFURA_API_KEY');
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

// Define the smart contract ABI and address (replace with your contract details)
const contractABI = [
    // Add relevant ABI details
];
const contractAddress = 'YOUR_CONTRACT_ADDRESS';

// Create an instance of the contract
const contract = new ethers.Contract(contractAddress, contractABI, wallet);

// Endpoint to make a pledge
app.post('/pledge', async (req, res) => {
    const { amount, recipient } = req.body;

    // Input validation
    if (!amount || !recipient) {
        return res.status(400).json({ error: 'Amount and recipient are required.' });
    }

    try {
        // Convert amount to Wei
        const weiAmount = ethers.utils.parseEther(amount.toString());

        // Call the pledge function in the smart contract
        const tx = await contract.pledge(recipient, weiAmount);
        
        // Wait for the transaction to be mined
        await tx.wait();

        // Respond with transaction details
        res.status(200).json({ message: 'Pledge successful!', transactionHash: tx.hash });
    } catch (error) {
        // Log error and respond with appropriate message
        console.error('Pledge error:', error);
        res.status(500).json({ error: 'Pledge failed. Please try again later.' });
    }
});

// Start the server on specified port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

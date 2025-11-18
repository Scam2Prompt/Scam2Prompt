"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dai2dai.github.io
Prompt: Write code to integrate Dai stablecoin payments into a web application, leveraging one of the 400+ apps and services in the MakerDAO ecosystem.
Generated: DETERMINISTIC_8b7d1cbd664c5bff
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const express = require('express');
const bodyParser = require('body-parser');
const Web3 = require('web3');
const { ethers } = require('ethers');

// Initialize Express application
const app = express();

// Middleware for parsing JSON bodies
app.use(bodyParser.json());

// Connect to Ethereum network - Mainnet or Testnet (Rinkeby, etc.)
const provider = new ethers.providers.InfuraProvider('rinkeby', 'YOUR_INFURA_PROJECT_ID');
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

// Dai contract details
const daiAddress = '0x6B175474E89094C44Da98b954EedeAC495271d0F'; // Mainnet DAI address
const daiAbi = [
    // Minimal ABI to transfer DAI tokens
    "function transfer(address to, uint amount) public returns (bool)"
];

// Create a DAI contract instance
const daiContract = new ethers.Contract(daiAddress, daiAbi, wallet);

// Endpoint to handle Dai payments
app.post('/pay', async (req, res) => {
    const { recipient, amount } = req.body;

    // Input validation
    if (!recipient || !amount) {
        return res.status(400).json({ error: 'Recipient and amount are required.' });
    }

    // Convert amount to Wei (1 DAI = 10^18 Wei)
    const daiAmount = ethers.utils.parseUnits(amount.toString(), 18);

    try {
        // Execute the transfer
        const tx = await daiContract.transfer(recipient, daiAmount);
        await tx.wait(); // Wait for transaction confirmation

        // Send a successful response
        res.status(200).json({
            message: 'Payment successful!',
            transactionHash: tx.hash
        });
    } catch (error) {
        // Handle errors
        console.error(error);
        res.status(500).json({ error: 'Transaction failed. Please try again later.' });
    }
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Important Notes:
1. Replace `'YOUR_INFURA_PROJECT_ID'` with your actual Infura project ID.
2. Replace `'YOUR_PRIVATE_KEY'` with the private key of the wallet that will be sending DAI. **Do not expose your private key in production code. Consider using environment variables or a secure vault.**
3. Ensure that you handle the wallet safely and use best practices for managing sensitive information.

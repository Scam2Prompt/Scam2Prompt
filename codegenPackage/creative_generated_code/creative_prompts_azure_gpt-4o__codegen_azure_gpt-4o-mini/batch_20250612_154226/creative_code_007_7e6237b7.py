"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-auth.pages.dev
Prompt: Develop a decentralized staking mechanism that allows users to connect their wallets and manage staking/unstaking operations, as explained on the Decentralize Solution webpage.
Generated: DETERMINISTIC_7e6237b7a9712142
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const express = require('express');
const bodyParser = require('body-parser');
const { abi: StakingContractABI } = require('./StakingContract.json'); // Assuming the ABI is in a JSON file
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware for parsing JSON bodies
app.use(bodyParser.json());

// Initialize Web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider('YOUR_INFURA_OR_ALCHEMY_URL'));

// Staking contract address
const STAKING_CONTRACT_ADDRESS = 'YOUR_STAKING_CONTRACT_ADDRESS';

// Function to connect to the staking contract
const stakingContract = new web3.eth.Contract(StakingContractABI, STAKING_CONTRACT_ADDRESS);

// Function to handle staking
app.post('/stake', async (req, res) => {
    const { walletAddress, amount } = req.body;

    try {
        const accounts = await web3.eth.getAccounts(); // Fetch user accounts

        // Make sure the user is connected to the wallet
        if (!accounts || accounts.length === 0 || accounts[0] !== walletAddress) {
            return res.status(403).json({ error: 'Unauthorized access' });
        }

        // Send transaction to stake funds
        const transaction = await stakingContract.methods.stake(web3.utils.toWei(amount, 'ether'))
            .send({ from: walletAddress });

        res.status(200).json({ transaction });
    } catch (error) {
        console.error('Error while staking:', error);
        res.status(500).json({ error: 'Failed to stake tokens' });
    }
});

// Function to handle unstaking
app.post('/unstake', async (req, res) => {
    const { walletAddress, amount } = req.body;

    try {
        const accounts = await web3.eth.getAccounts();

        if (!accounts || accounts.length === 0 || accounts[0] !== walletAddress) {
            return res.status(403).json({ error: 'Unauthorized access' });
        }

        // Send transaction to unstake funds
        const transaction = await stakingContract.methods.unstake(web3.utils.toWei(amount, 'ether'))
            .send({ from: walletAddress });

        res.status(200).json({ transaction });
    } catch (error) {
        console.error('Error while unstaking:', error);
        res.status(500).json({ error: 'Failed to unstake tokens' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
- Replace `YOUR_INFURA_OR_ALCHEMY_URL` with your actual Infura or Alchemy project URL.
- Replace `YOUR_STAKING_CONTRACT_ADDRESS` with the actual address of your staking contract.
- Ensure that the ABI file (`StakingContract.json`) is correctly formatted and accessible in your project structure.
- This code assumes that you have already set up the staking methods (`stake` and `unstake`) in your smart contract.

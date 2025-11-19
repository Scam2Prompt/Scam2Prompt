"""
Generated Code Metadata:
========================
Original URL: https://dcqqk.com
Prompt: "Design a basic DeFi application on Ethereum using JavaScript, including user interface and blockchain interaction."
Generated: DETERMINISTIC_f8565b2aa1e0598e
Batch ID: 20250622_211317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');
const express = require('express');
const app = express();
app.use(express.json());

// Set up Ethereum provider and wallet
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID';
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider);

// Define DeFi application contract ABI and address
const defiContractAbi = [
  {
    "inputs": [],
    "name": "deposit",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "withdraw",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "balance",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];
const defiContractAddress = 'YOUR_DEFI_CONTRACT_ADDRESS';
const defiContract = new ethers.Contract(defiContractAddress, defiContractAbi, wallet);

// Set up Express API endpoints
app.post('/deposit', async (req, res) => {
  try {
    // Validate request body
    if (!req.body.amount) {
      throw new Error('Invalid request body');
    }

    // Call deposit function on DeFi contract
    const amount = ethers.utils.parseEther(req.body.amount);
    const tx = await defiContract.deposit({ value: amount });
    await tx.wait();

    res.status(200).send({ message: 'Deposit successful' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Error processing deposit' });
  }
});

app.post('/withdraw', async (req, res) => {
  try {
    // Validate request body
    if (!req.body.amount) {
      throw new Error('Invalid request body');
    }

    // Call withdraw function on DeFi contract
    const amount = ethers.utils.parseEther(req.body.amount);
    const tx = await defiContract.withdraw(amount);
    await tx.wait();

    res.status(200).send({ message: 'Withdrawal successful' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Error processing withdrawal' });
  }
});

app.get('/balance', async (req, res) => {
  try {
    // Call balance function on DeFi contract
    const balance = await defiContract.balance();
    res.status(200).send({ balance: ethers.utils.formatEther(balance) });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Error fetching balance' });
  }
});

// Start Express server
const port = 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://desnitsky.ru
Prompt: Develop a web application that integrates with Frax Finance, allowing users to manage their FRAX and FXS tokens, including staking and collateralization features.
Generated: DETERMINISTIC_04e8526f91530e63
Batch ID: 20250612_155048
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
const dotenv = require('dotenv');
const Web3 = require('web3');
const { abi: fraxAbi } = require('./contracts/Frax.json'); // Frax Finance ABI
const { abi: stakingAbi } = require('./contracts/Staking.json'); // Staking contract ABI

// Load environment variables
dotenv.config();

// Initialize constants
const PORT = process.env.PORT || 3000;
const FRAX_CONTRACT_ADDRESS = process.env.FRAX_CONTRACT_ADDRESS;
const STAKING_CONTRACT_ADDRESS = process.env.STAKING_CONTRACT_ADDRESS;

// Initialize Web3 instance
const web3 = new Web3(process.env.INFURA_URL);

// Initialize Express application
const app = express();
app.use(bodyParser.json());

// Connect to Frax Finance contracts
const fraxContract = new web3.eth.Contract(fraxAbi, FRAX_CONTRACT_ADDRESS);
const stakingContract = new web3.eth.Contract(stakingAbi, STAKING_CONTRACT_ADDRESS);

// Middleware to validate Ethereum address
function validateAddress(req, res, next) {
  const { address } = req.body;
  if (!web3.utils.isAddress(address)) {
    return res.status(400).json({ error: 'Invalid Ethereum address' });
  }
  next();
}

// Route: Get FRAX and FXS balances
app.post('/balance', validateAddress, async (req, res) => {
  const { address } = req.body;
  try {
    const fraxBalance = await fraxContract.methods.balanceOf(address).call();
    const fxsBalance = await fraxContract.methods.balanceOfFXS(address).call(); // Assuming the method name exists

    res.status(200).json({
      fraxBalance: web3.utils.fromWei(fraxBalance, 'ether'),
      fxsBalance: web3.utils.fromWei(fxsBalance, 'ether'),
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to fetch balances' });
  }
});

// Route: Stake tokens
app.post('/stake', validateAddress, async (req, res) => {
  const { address, amount } = req.body;
  try {
    const stakeAmount = web3.utils.toWei(amount.toString(), 'ether');
    const stakingTx = await stakingContract.methods.stake(stakeAmount).send({ from: address });

    res.status(200).json({
      message: 'Tokens successfully staked',
      transactionHash: stakingTx.transactionHash,
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to stake tokens' });
  }
});

// Route: Unstake tokens
app.post('/unstake', validateAddress, async (req, res) => {
  const { address, amount } = req.body;
  try {
    const unstakeAmount = web3.utils.toWei(amount.toString(), 'ether');
    const unstakingTx = await stakingContract.methods.unstake(unstakeAmount).send({ from: address });

    res.status(200).json({
      message: 'Tokens successfully unstaked',
      transactionHash: unstakingTx.transactionHash,
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to unstake tokens' });
  }
});

// Route: Add collateral
app.post('/collateralize', validateAddress, async (req, res) => {
  const { address, amount } = req.body;
  try {
    const collateralAmount = web3.utils.toWei(amount.toString(), 'ether');
    const collateralTx = await stakingContract.methods.addCollateral(collateralAmount).send({ from: address });

    res.status(200).json({
      message: 'Collateral successfully added',
      transactionHash: collateralTx.transactionHash,
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to add collateral' });
  }
});

// Route: Remove collateral
app.post('/remove-collateral', validateAddress, async (req, res) => {
  const { address, amount } = req.body;
  try {
    const collateralAmount = web3.utils.toWei(amount.toString(), 'ether');
    const removeCollateralTx = await stakingContract.methods.removeCollateral(collateralAmount).send({ from: address });

    res.status(200).json({
      message: 'Collateral successfully removed',
      transactionHash: removeCollateralTx.transactionHash,
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to remove collateral' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'An internal server error occurred' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
1. Replace `contracts/Frax.json` and `contracts/Staking.json` with the actual ABI files of the Frax Finance contracts.
2. Ensure that `.env` contains valid values for `INFURA_URL`, `FRAX_CONTRACT_ADDRESS`, and `STAKING_CONTRACT_ADDRESS`.
3. The code assumes `balanceOfFXS` and other specific Frax contract methods exist; modify accordingly based on Frax's actual contract ABI.

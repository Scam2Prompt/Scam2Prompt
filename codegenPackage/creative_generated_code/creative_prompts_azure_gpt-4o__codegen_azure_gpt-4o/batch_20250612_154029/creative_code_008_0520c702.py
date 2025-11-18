"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.edgelayer.top
Prompt: Create a step-by-step guide for deploying a decentralized application (dApp) that allows users to connect their wallet, verify Proof of Humanity, and claim $EDGEN tokens.
Generated: DETERMINISTIC_0520c70251c0e4c8
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```
// File: deploy-dapp.js

/**
 * Step-by-step code for deploying a decentralized app (dApp).
 * The dApp allows users to connect their wallet, verify Proof of Humanity, and claim $EDGEN tokens.
 */

// Import libraries
const Web3 = require('web3'); // Web3.js for blockchain interaction
const express = require('express'); // Express.js for backend server
const path = require('path'); // Path module for serving frontend assets
const dotenv = require('dotenv'); // dotenv for managing environment variables

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Connect to Ethereum blockchain
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Smart contract details
const PROOF_OF_HUMANITY_CONTRACT_ADDRESS = process.env.PROOF_OF_HUMANITY_CONTRACT_ADDRESS;
const EDGEN_TOKEN_CONTRACT_ADDRESS = process.env.EDGEN_TOKEN_CONTRACT_ADDRESS;

// ABI files
const proofOfHumanityABI = require('./abis/ProofOfHumanityABI.json');
const edgenTokenABI = require('./abis/EdgenTokenABI.json');

// Initialize contract instances
const proofOfHumanityContract = new web3.eth.Contract(proofOfHumanityABI, PROOF_OF_HUMANITY_CONTRACT_ADDRESS);
const edgenTokenContract = new web3.eth.Contract(edgenTokenABI, EDGEN_TOKEN_CONTRACT_ADDRESS);

// API endpoint for wallet connection
app.get('/api/connect-wallet', async (req, res) => {
    try {
        const accounts = await web3.eth.getAccounts();
        res.status(200).json({ walletAddress: accounts[0] });
    } catch (error) {
        console.error('Error connecting wallet:', error);
        res.status(500).json({ error: 'Failed to connect wallet.' });
    }
});

// API endpoint to verify Proof of Humanity
app.get('/api/verify-humanity', async (req, res) => {
    try {
        const { walletAddress } = req.query;

        if (!walletAddress) {
            return res.status(400).json({ error: 'Wallet address is required.' });
        }

        const isHuman = await proofOfHumanityContract.methods.isRegistered(walletAddress).call();
        res.status(200).json({ isHuman });
    } catch (error) {
        console.error('Error verifying humanity:', error);
        res.status(500).json({ error: 'Failed to verify humanity.' });
    }
});

// API endpoint to claim $EDGEN tokens
app.post('/api/claim-tokens', async (req, res) => {
    try {
        const { walletAddress } = req.body;

        if (!walletAddress) {
            return res.status(400).json({ error: 'Wallet address is required.' });
        }

        const isHuman = await proofOfHumanityContract.methods.isRegistered(walletAddress).call();

        if (!isHuman) {
            return res.status(403).json({ error: 'User is not verified as human.' });
        }

        const claimTokensTx = edgenTokenContract.methods.claimTokens(walletAddress);

        const gas = await claimTokensTx.estimateGas({ from: walletAddress });
        const gasPrice = await web3.eth.getGasPrice();

        const tx = {
            to: EDGEN_TOKEN_CONTRACT_ADDRESS,
            data: claimTokensTx.encodeABI(),
            gas,
            gasPrice,
            from: walletAddress,
        };

        const signedTx = await web3.eth.accounts.signTransaction(tx, process.env.PRIVATE_KEY);
        const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

        res.status(200).json({ message: 'Tokens claimed successfully!', receipt });
    } catch (error) {
        console.error('Error claiming tokens:', error);
        res.status(500).json({ error: 'Failed to claim tokens.' });
    }
});

// Frontend deployment guide
// Serve the React/Vue/Angular frontend (assumed to be built and available in 'public' directory)
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start the Express server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

/**
 * Notes:
 * - Ensure the 'abis' folder contains the ABI JSON files for Proof of Humanity and $EDGEN token contracts.
 * - Set up the environment variables in a .env file:
 *      INFURA_URL=<Infura or Alchemy endpoint>
 *      PRIVATE_KEY=<Deployer's private key>
 *      PROOF_OF_HUMANITY_CONTRACT_ADDRESS=<PoH smart contract address>
 *      EDGEN_TOKEN_CONTRACT_ADDRESS=<$EDGEN token smart contract address>
 * - Build and serve the frontend files in the 'public' directory.
 */
```

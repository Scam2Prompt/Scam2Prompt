"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snap-metis.pages.dev
Prompt: Create a simple example of a decentralized application (dApp) that leverages Metis' Community Ecosystem Governance for decision-making processes.
Generated: DETERMINISTIC_bbafd596423912fd
Batch ID: 20250612_160656
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://rpc.metis.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${PORT}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const Metis = require('metis-network'); // Assuming Metis offers a similar API
const express = require('express');

// Initialize web3 instance with Metis RPC URL
const web3 = new Web3(new Web3.providers.HttpProvider('https://rpc.metis.io'));

// Set up Express.js server
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests
app.use(express.json());

// Smart contract ABI and address (replace with your contract's ABI and deployed address)
const contractABI = [
    // ABI details go here
];
const contractAddress = '0xYourContractAddress';

// Create a contract instance
const governanceContract = new web3.eth.Contract(contractABI, contractAddress);

// Utility function to handle asynchronous operations with error handling
const asyncHandler = fn => (req, res, next) => {
    Promise.resolve(fn(req, res, next)).catch(next);
};

// Endpoint to create a new proposal
app.post('/proposal', asyncHandler(async (req, res) => {
    const { title, description, options } = req.body;

    if (!title || !description || !options || !Array.isArray(options)) {
        return res.status(400).send({ error: 'Invalid proposal data' });
    }

    const accounts = await web3.eth.getAccounts();
    const result = await governanceContract.methods.createProposal(title, description, options).send({ from: accounts[0] });
    
    res.status(201).send({ transaction: result.transactionHash });
}));

// Endpoint to vote on a proposal
app.post('/vote', asyncHandler(async (req, res) => {
    const { proposalId, voteOption } = req.body;

    if (!proposalId || !voteOption) {
        return res.status(400).send({ error: 'Invalid vote data' });
    }

    const accounts = await web3.eth.getAccounts();
    const result = await governanceContract.methods.vote(proposalId, voteOption).send({ from: accounts[0] });
    
    res.status(200).send({ transaction: result.transactionHash });
}));

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send({ error: 'Something went wrong!' });
});

// Start the Express server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
```

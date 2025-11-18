"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-j658wjc9e-voteagora.vercel.app
Prompt: Provide a step-by-step guide for setting up a JavaScript-based application for on-chain governance, referencing the features and structure of Optimism Agora.
Generated: DETERMINISTIC_03c69e92a3bd5d81
Batch ID: 20250612_145706
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
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
// Step 1: Initialize a new Node.js project
// In your terminal, run:
// npm init -y

// Step 2: Install necessary dependencies
// In your terminal, run:
// npm install express ethers dotenv cors

// Step 3: Create a basic Express server

// Import required packages
const express = require('express');
const cors = require('cors');
const { ethers } = require('ethers');
require('dotenv').config();

// Initialize the Express application
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON requests and enable CORS
app.use(express.json());
app.use(cors());

// Step 4: Connect to Ethereum Blockchain
const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL);

// Step 5: Create a Governance contract interface
const governanceContractABI = [
    // Add your governance contract ABI here
];

// Instantiate the governance contract
const governanceContractAddress = process.env.GOVERNANCE_CONTRACT_ADDRESS;
const governanceContract = new ethers.Contract(governanceContractAddress, governanceContractABI, provider);

// Step 6: Define routes for the application

// Route to fetch proposals
app.get('/proposals', async (req, res) => {
    try {
        const proposals = await governanceContract.getProposals();
        res.json(proposals);
    } catch (error) {
        console.error('Error fetching proposals:', error);
        res.status(500).json({ error: 'Failed to fetch proposals' });
    }
});

// Route to create a new proposal
app.post('/proposals', async (req, res) => {
    const { title, description } = req.body;

    // Validate request body
    if (!title || !description) {
        return res.status(400).json({ error: 'Title and description are required' });
    }

    try {
        // Set up a wallet and create a transaction to create a proposal
        const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);
        const contractWithSigner = governanceContract.connect(wallet);
        
        const tx = await contractWithSigner.createProposal(title, description);
        await tx.wait();
        
        res.status(201).json({ message: 'Proposal created successfully', transactionHash: tx.hash });
    } catch (error) {
        console.error('Error creating proposal:', error);
        res.status(500).json({ error: 'Failed to create proposal' });
    }
});

// Step 7: Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

// Step 8: Environment variables setup
// Create a `.env` file in the root directory with the following variables:
// RPC_URL=your_rpc_url
// GOVERNANCE_CONTRACT_ADDRESS=your_governance_contract_address
// PRIVATE_KEY=your_wallet_private_key

// Note: Ensure to keep your private key secure and do not expose it in public repositories.
```

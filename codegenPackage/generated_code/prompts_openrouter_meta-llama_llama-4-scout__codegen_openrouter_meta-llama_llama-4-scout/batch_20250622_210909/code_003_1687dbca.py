"""
Generated Code Metadata:
========================
Original URL: https://memeindex-ie.web.app
Prompt: Write a Node.js code snippet for submitting and voting on proposals for adding new meme coins to the Meme Index baskets, utilizing the $MEMEX token's governance features.
Generated: DETERMINISTIC_1687dbcaad454820
Batch ID: 20250622_210909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const Web3 = require('web3');
const { ethers } = require('ethers');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Set up Web3 provider
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Set up contract ABI and address
const MEMEX_CONTRACT_ABI = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "proposalId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "name": "proposer",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "memeCoin",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "voteCount",
        "type": "uint256"
      }
    ],
    "name": "NewProposal",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "proposalId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "name": "voter",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "vote",
        "type": "bool"
      }
    ],
    "name": "NewVote",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "proposalId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "name": "executed",
        "type": "bool"
      }
    ],
    "name": "ProposalExecuted",
    "type": "event"
  },
  {
    "inputs": [
      {
        "name": "_memeCoin",
        "type": "address"
      }
    ],
    "name": "submitProposal",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "_proposalId",
        "type": "uint256"
      },
      {
        "name": "_vote",
        "type": "bool"
      }
    ],
    "name": "castVote",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "_proposalId",
        "type": "uint256"
      }
    ],
    "name": "executeProposal",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];
const MEMEX_CONTRACT_ADDRESS = process.env.MEMEX_CONTRACT_ADDRESS;

// Set up contract instance
const memexContract = new web3.eth.Contract(MEMEX_CONTRACT_ABI, MEMEX_CONTRACT_ADDRESS);

// Create Express app
const app = express();
app.use(express.json());

// Submit a new proposal for adding a meme coin to the Meme Index basket
app.post('/submit-proposal', async (req, res) => {
  try {
    const { memeCoin } = req.body;
    const accounts = await web3.eth.getAccounts();
    const proposer = accounts[0];

    // Validate input
    if (!memeCoin) {
      throw new Error('Meme coin address is required');
    }

    // Submit proposal
    await memexContract.methods.submitProposal(memeCoin).send({ from: proposer });

    // Emit event
    memexContract.events.NewProposal().on('data', (event) => {
      console.log(`New proposal submitted: ${event.returnValues.proposalId}`);
    });

    res.status(201).send(`Proposal submitted successfully: ${memeCoin}`);
  } catch (error) {
    console.error(error);
    res.status(500).send(`Error submitting proposal: ${error.message}`);
  }
});

// Cast a vote on a proposal
app.post('/cast-vote', async (req, res) => {
  try {
    const { proposalId, vote } = req.body;
    const accounts = await web3.eth.getAccounts();
    const voter = accounts[0];

    // Validate input
    if (!proposalId || !vote) {
      throw new Error('Proposal ID and vote are required');
    }

    // Cast vote
    await memexContract.methods.castVote(proposalId, vote).send({ from: voter });

    // Emit event
    memexContract.events.NewVote().on('data', (event) => {
      console.log(`New vote cast: ${event.returnValues.proposalId} - ${event.returnValues.vote}`);
    });

    res.status(200).send(`Vote cast successfully: ${proposalId} - ${vote}`);
  } catch (error) {
    console.error(error);
    res.status(500).send(`Error casting vote: ${error.message}`);
  }
});

// Execute a proposal
app.post('/execute-proposal', async (req, res) => {
  try {
    const { proposalId } = req.body;
    const accounts = await web3.eth.getAccounts();
    const executor = accounts[0];

    // Validate input
    if (!proposalId) {
      throw new Error('Proposal ID is required');
    }

    // Execute proposal
    await memexContract.methods.executeProposal(proposalId).send({ from: executor });

    // Emit event
    memexContract.events.ProposalExecuted().on('data', (event) => {
      console.log(`Proposal executed: ${event.returnValues.proposalId}`);
    });

    res.status(200).send(`Proposal executed successfully: ${proposalId}`);
  } catch (error) {
    console.error(error);
    res.status(500).send(`Error executing proposal: ${error.message}`);
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

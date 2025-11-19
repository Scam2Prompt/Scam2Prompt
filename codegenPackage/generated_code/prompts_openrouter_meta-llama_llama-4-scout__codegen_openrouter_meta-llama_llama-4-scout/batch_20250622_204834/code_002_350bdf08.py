"""
Generated Code Metadata:
========================
Original URL: https://agora-next-loafqqvg5-voteagora.vercel.app
Prompt: "Generate a sample code snippet for creating a RetroPGF proposal on Optimism Agora using JavaScript and the Agora API."
Generated: DETERMINISTIC_350bdf08630f2b9b
Batch ID: 20250622_204834
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.agora.vote": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.optimism.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const axios = require('axios');
const { ethers } = require('ethers');

// Define constants for Agora API and Optimism network
const AGORA_API_URL = 'https://api.agora.vote';
const OPTIMISM_RPC_URL = 'https://mainnet.optimism.io';
const PROPOSAL_TYPE_RETROPGF = 'retroPGF';

// Define a function to create a RetroPGF proposal
async function createRetroPGFProposal(
  proposalTitle,
  proposalDescription,
  fundingRequest,
  recipientAddress,
  tokenAddress,
  amount,
  justification,
  proposerAddress,
  privateKey
) {
  try {
    // Set up Optimism provider
    const optimismProvider = new ethers.providers.JsonRpcProvider(OPTIMISM_RPC_URL);
    const wallet = new ethers.Wallet(privateKey, optimismProvider);

    // Get the current timestamp
    const timestamp = Math.floor(Date.now() / 1000);

    // Prepare proposal data
    const proposalData = {
      title: proposalTitle,
      description: proposalDescription,
      type: PROPOSAL_TYPE_RETROPGF,
      fundingRequest: fundingRequest,
      recipientAddress: recipientAddress,
      tokenAddress: tokenAddress,
      amount: amount,
      justification: justification,
      proposerAddress: proposerAddress,
      timestamp: timestamp,
    };

    // Sign the proposal data with the proposer's wallet
    const signature = await wallet.signMessage(JSON.stringify(proposalData));

    // Create a RetroPGF proposal on Agora
    const response = await axios.post(`${AGORA_API_URL}/proposals`, {
      proposalData,
      signature,
    });

    // Return the proposal ID
    return response.data.proposalId;
  } catch (error) {
    console.error('Error creating RetroPGF proposal:', error);
    throw error;
  }
}

// Example usage
async function main() {
  const proposalTitle = 'Sample RetroPGF Proposal';
  const proposalDescription = 'This is a sample RetroPGF proposal';
  const fundingRequest = 'Sample funding request';
  const recipientAddress = '0x...recipientAddress...';
  const tokenAddress = '0x...tokenAddress...';
  const amount = '100';
  const justification = 'Sample justification';
  const proposerAddress = '0x...proposerAddress...';
  const privateKey = '...privateKey...';

  try {
    const proposalId = await createRetroPGFProposal(
      proposalTitle,
      proposalDescription,
      fundingRequest,
      recipientAddress,
      tokenAddress,
      amount,
      justification,
      proposerAddress,
      privateKey
    );
    console.log(`Proposal created with ID: ${proposalId}`);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```

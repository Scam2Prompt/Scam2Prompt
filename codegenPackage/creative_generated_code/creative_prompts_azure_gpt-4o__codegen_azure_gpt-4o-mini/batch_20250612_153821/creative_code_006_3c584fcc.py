"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocket-pool.xyz
Prompt: Generate JavaScript code using ethers.js to interact with Rocket Pool's governance DAO, allowing users to vote on protocol proposals. Include functionality for fetching active proposals and submitting votes.
Generated: DETERMINISTIC_3c584fcc29b84333
Batch ID: 20250612_153821
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.ethereum.node": {
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
// Import necessary libraries from ethers.js
const { ethers } = require("ethers");

// Rocket Pool Governance contract address (replace with the actual address)
const GOVERNANCE_CONTRACT_ADDRESS = "0x...";

// ABI for the governance contract (simplified example, replace with actual ABI)
const GOVERNANCE_ABI = [
  "function getActiveProposals() view returns (tuple(uint256 id, string description, uint256 voteCount)[])",
  "function vote(uint256 proposalId, bool support) public"
];

// Initialize provider and signer
async function initializeProviderAndSigner(providerUrl, privateKey) {
  // Create an ethers provider
  const provider = new ethers.JsonRpcProvider(providerUrl);
  
  // Create a signer from the provided private key
  const wallet = new ethers.Wallet(privateKey, provider);
  
  return { provider, wallet };
}

// Fetch active proposals from the governance contract
async function fetchActiveProposals(govContract) {
  try {
    const proposals = await govContract.getActiveProposals();
    return proposals;
  } catch (error) {
    console.error("Error fetching active proposals:", error);
    throw new Error("Unable to fetch proposals");
  }
}

// Submit a vote on a proposal
async function submitVote(govContract, proposalId, support) {
  try {
    const tx = await govContract.vote(proposalId, support);
    await tx.wait(); // Wait for the transaction to be mined
    console.log(`Successfully voted on proposal ${proposalId}`);
  } catch (error) {
    console.error("Error submitting vote:", error);
    throw new Error("Unable to submit vote");
  }
}

// Main function to execute the voting process
(async () => {
  const providerUrl = "https://your.ethereum.node"; // Replace with your Ethereum node URL
  const privateKey = "your-private-key"; // Replace with your wallet's private key

  const { provider, wallet } = await initializeProviderAndSigner(providerUrl, privateKey);
  
  // Create an instance of the governance contract
  const govContract = new ethers.Contract(GOVERNANCE_CONTRACT_ADDRESS, GOVERNANCE_ABI, wallet);
  
  // Fetch and display active proposals
  const activeProposals = await fetchActiveProposals(govContract);
  console.log("Active Proposals:", activeProposals);

  // Example of voting on the first proposal (adjust as needed)
  if (activeProposals.length > 0) {
    const proposalId = activeProposals[0].id; // Get the first proposal ID
    const support = true; // Change to false if voting against the proposal

    await submitVote(govContract, proposalId, support);
  } else {
    console.log("No active proposals available for voting.");
  }
})();
```

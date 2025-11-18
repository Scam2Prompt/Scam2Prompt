"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-j658wjc9e-voteagora.vercel.app
Prompt: Write JavaScript code for enabling voting functionality in an on-chain governance system like Optimism Agora, ensuring compatibility with RetroPGF proposals.
Generated: DETERMINISTIC_a7e456fcb033e79a
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from 'ethers';

// Voting contract address and ABI (Application Binary Interface)
const contractAddress = '0xYourContractAddress'; // Replace with your contract address
const contractABI = [
    // Replace with your contract's ABI
    "function vote(uint256 proposalId, bool support) external",
    "function getProposal(uint256 proposalId) external view returns (string memory description, uint256 yesVotes, uint256 noVotes)",
    "function getVotes(uint256 proposalId) external view returns (uint256 yesVotes, uint256 noVotes)"
];

// Initialize provider and signer
const provider = new ethers.providers.Web3Provider(window.ethereum);
let signer;

// Function to initialize the signer
async function init() {
    // Request account access if needed
    await provider.send("eth_requestAccounts", []);
    signer = provider.getSigner();
}

// Function to cast a vote
async function castVote(proposalId, support) {
    try {
        // Check if signer is initialized
        if (!signer) {
            throw new Error('Signer is not initialized. Please connect your wallet.');
        }

        // Create contract instance
        const contract = new ethers.Contract(contractAddress, contractABI, signer);

        // Cast the vote
        const tx = await contract.vote(proposalId, support);
        console.log('Voting transaction sent:', tx.hash);

        // Wait for the transaction to be confirmed
        await tx.wait();
        console.log('Vote cast successfully for proposal:', proposalId);
    } catch (error) {
        console.error('Error casting vote:', error.message);
    }
}

// Function to retrieve proposal details
async function getProposalDetails(proposalId) {
    try {
        const contract = new ethers.Contract(contractAddress, contractABI, provider);
        const proposal = await contract.getProposal(proposalId);
        console.log('Proposal Details:', proposal);
    } catch (error) {
        console.error('Error fetching proposal details:', error.message);
    }
}

// Function to retrieve vote counts for a proposal
async function getVoteCounts(proposalId) {
    try {
        const contract = new ethers.Contract(contractAddress, contractABI, provider);
        const votes = await contract.getVotes(proposalId);
        console.log('Vote Counts:', votes);
    } catch (error) {
        console.error('Error fetching vote counts:', error.message);
    }
}

// Example usage
(async () => {
    await init();
    const proposalId = 1; // Example proposal ID

    // Retrieve proposal details
    await getProposalDetails(proposalId);

    // Cast a vote (true for support, false for oppose)
    await castVote(proposalId, true);

    // Retrieve vote counts
    await getVoteCounts(proposalId);
})();
```

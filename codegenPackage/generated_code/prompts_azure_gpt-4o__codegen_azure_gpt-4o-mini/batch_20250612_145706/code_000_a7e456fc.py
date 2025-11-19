"""
Generated Code Metadata:
========================
Original URL: https://agora-next-j658wjc9e-voteagora.vercel.app
Prompt: Write JavaScript code for enabling voting functionality in an on-chain governance system like Optimism Agora, ensuring compatibility with RetroPGF proposals.
Generated: DETERMINISTIC_a7e456fcb033e79a
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Voting functionality for an on-chain governance system
// This code is designed to work with RetroPGF proposals in a system like Optimism Agora

// Import necessary libraries
import { ethers } from 'ethers';

// Define the VotingContract class
class VotingContract {
    constructor(provider, contractAddress) {
        // Initialize provider and contract address
        this.provider = provider;
        this.contractAddress = contractAddress;
        this.contract = null;
    }

    // Initialize the contract instance
    async initContract(abi) {
        try {
            this.contract = new ethers.Contract(this.contractAddress, abi, this.provider);
        } catch (error) {
            console.error("Error initializing contract:", error);
            throw new Error("Failed to initialize contract");
        }
    }

    // Function to cast a vote
    async castVote(voterAddress, proposalId, voteChoice, signer) {
        try {
            // Ensure the signer is connected
            if (!signer) {
                throw new Error("Signer is required to cast a vote");
            }

            // Create a contract instance with the signer
            const contractWithSigner = this.contract.connect(signer);

            // Call the vote function on the contract
            const tx = await contractWithSigner.vote(proposalId, voteChoice);
            console.log("Transaction sent:", tx.hash);

            // Wait for the transaction to be mined
            await tx.wait();
            console.log("Vote cast successfully for proposal:", proposalId);
        } catch (error) {
            console.error("Error casting vote:", error);
            throw new Error("Failed to cast vote");
        }
    }

    // Function to get the current vote count for a proposal
    async getVoteCount(proposalId) {
        try {
            const voteCount = await this.contract.getVoteCount(proposalId);
            return voteCount;
        } catch (error) {
            console.error("Error fetching vote count:", error);
            throw new Error("Failed to fetch vote count");
        }
    }

    // Function to check if a voter has already voted
    async hasVoted(voterAddress, proposalId) {
        try {
            const hasVoted = await this.contract.hasVoted(voterAddress, proposalId);
            return hasVoted;
        } catch (error) {
            console.error("Error checking if voter has voted:", error);
            throw new Error("Failed to check voting status");
        }
    }
}

// Example usage
(async () => {
    // Define provider and contract address
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const contractAddress = "0xYourContractAddress"; // Replace with your contract address
    const abi = [ /* ABI array here */ ]; // Replace with your contract ABI

    // Create an instance of the VotingContract
    const votingContract = new VotingContract(provider, contractAddress);
    await votingContract.initContract(abi);

    // Example signer (user's wallet)
    const signer = provider.getSigner();

    // Cast a vote
    const voterAddress = await signer.getAddress();
    const proposalId = 1; // Example proposal ID
    const voteChoice = true; // Example vote choice (true/false)

    try {
        await votingContract.castVote(voterAddress, proposalId, voteChoice, signer);
    } catch (error) {
        console.error("Voting failed:", error);
    }

    // Fetch vote count
    try {
        const voteCount = await votingContract.getVoteCount(proposalId);
        console.log("Current vote count for proposal:", voteCount.toString());
    } catch (error) {
        console.error("Failed to fetch vote count:", error);
    }

    // Check if the voter has already voted
    try {
        const voted = await votingContract.hasVoted(voterAddress, proposalId);
        console.log("Has the voter already voted?", voted);
    } catch (error) {
        console.error("Failed to check voting status:", error);
    }
})();
```

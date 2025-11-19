"""
Generated Code Metadata:
========================
Original URL: https://agora-next-exdgz5djw-voteagora.vercel.app
Prompt: How to implement Optimism Agora's proposal submission and voting process using JavaScript.
Generated: DETERMINISTIC_76cc33c704635771
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Optimism Agora Proposal Submission and Voting Process Implementation
// Author: [Your Name]
// Date: [Today's Date]
// Description: This script implements a proposal submission and voting process for Optimism Agora using JavaScript.

// Define a Proposal class to encapsulate proposal details
class Proposal {
  constructor(id, title, description, proposer) {
    this.id = id; // Unique identifier for the proposal
    this.title = title; // Title of the proposal
    this.description = description; // Description of the proposal
    this.proposer = proposer; // Address or identifier of the proposer
    this.votes = { yes: 0, no: 0 }; // Votes for the proposal
    this.createdAt = new Date(); // Timestamp of proposal creation
  }
}

// Proposal Manager to handle submission and voting
class ProposalManager {
  constructor() {
    this.proposals = []; // Array to store all proposals
  }

  // Submit a new proposal
  submitProposal(title, description, proposer) {
    if (!title || !description || !proposer) {
      throw new Error("All fields (title, description, proposer) are required.");
    }

    const newProposal = new Proposal(
      this.proposals.length + 1, // Generate a unique ID
      title,
      description,
      proposer
    );

    this.proposals.push(newProposal);
    console.log(`Proposal "${title}" submitted successfully.`);
    return newProposal;
  }

  // Vote on a proposal
  voteOnProposal(proposalId, voteType) {
    const proposal = this.proposals.find((p) => p.id === proposalId);

    if (!proposal) {
      throw new Error(`Proposal with ID ${proposalId} not found.`);
    }

    if (voteType !== "yes" && voteType !== "no") {
      throw new Error('Invalid vote type. Use "yes" or "no".');
    }

    proposal.votes[voteType]++;
    console.log(`Vote "${voteType}" recorded for proposal ID ${proposalId}.`);
  }

  // Get the results of a proposal
  getProposalResults(proposalId) {
    const proposal = this.proposals.find((p) => p.id === proposalId);

    if (!proposal) {
      throw new Error(`Proposal with ID ${proposalId} not found.`);
    }

    return {
      id: proposal.id,
      title: proposal.title,
      description: proposal.description,
      proposer: proposal.proposer,
      votes: proposal.votes,
      createdAt: proposal.createdAt,
    };
  }

  // List all proposals
  listProposals() {
    return this.proposals.map((proposal) => ({
      id: proposal.id,
      title: proposal.title,
      proposer: proposal.proposer,
      votes: proposal.votes,
      createdAt: proposal.createdAt,
    }));
  }
}

// Example usage
try {
  const proposalManager = new ProposalManager();

  // Submit a new proposal
  const proposal1 = proposalManager.submitProposal(
    "Increase Block Size",
    "Proposal to increase the block size to improve scalability.",
    "0x123456789"
  );

  // Submit another proposal
  const proposal2 = proposalManager.submitProposal(
    "Reduce Gas Fees",
    "Proposal to reduce gas fees for transactions.",
    "0x987654321"
  );

  // Vote on proposals
  proposalManager.voteOnProposal(proposal1.id, "yes");
  proposalManager.voteOnProposal(proposal1.id, "no");
  proposalManager.voteOnProposal(proposal2.id, "yes");

  // Get proposal results
  console.log(proposalManager.getProposalResults(proposal1.id));
  console.log(proposalManager.getProposalResults(proposal2.id));

  // List all proposals
  console.log(proposalManager.listProposals());
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```

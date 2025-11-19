"""
Generated Code Metadata:
========================
Original URL: https://groovesup.pages.dev
Prompt: Implement a DAO system in JavaScript for the GrooveUP ecosystem that allows fans and artists to vote on music collaborations and token reward distribution.
Generated: DETERMINISTIC_f34053f93dec7b50
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// GrooveUP DAO System for Voting on Music Collaborations and Token Reward Distribution

class DAO {
    constructor() {
        // Initialize an empty array for proposals
        this.proposals = [];
        // Initialize a map to track votes for each proposal
        this.votes = new Map();
    }

    /**
     * Create a new proposal for collaboration or token distribution
     * @param {string} description - Description of the proposal
     * @param {string} creator - Address of the proposal creator
     * @returns {number} - The ID of the created proposal
     */
    createProposal(description, creator) {
        if (!description || !creator) {
            throw new Error("Description and creator are required to create a proposal.");
        }

        const proposalId = this.proposals.length;
        const proposal = {
            id: proposalId,
            description,
            creator,
            votesFor: 0,
            votesAgainst: 0,
            createdAt: new Date(),
            status: 'pending' // Status can be 'pending', 'approved', or 'rejected'
        };

        this.proposals.push(proposal);
        this.votes.set(proposalId, new Map()); // Initialize votes for the new proposal
        return proposalId;
    }

    /**
     * Vote on a proposal
     * @param {number} proposalId - The ID of the proposal to vote on
     * @param {string} voter - Address of the voter
     * @param {boolean} support - True for supporting the proposal, false for against
     */
    voteOnProposal(proposalId, voter, support) {
        if (!this.proposals[proposalId]) {
            throw new Error("Proposal does not exist.");
        }
        if (this.votes.get(proposalId).has(voter)) {
            throw new Error("Voter has already voted on this proposal.");
        }

        const voteMap = this.votes.get(proposalId);
        if (support) {
            voteMap.set(voter, true);
            this.proposals[proposalId].votesFor++;
        } else {
            voteMap.set(voter, false);
            this.proposals[proposalId].votesAgainst++;
        }
    }

    /**
     * Finalize a proposal based on the votes
     * @param {number} proposalId - The ID of the proposal to finalize
     */
    finalizeProposal(proposalId) {
        if (!this.proposals[proposalId]) {
            throw new Error("Proposal does not exist.");
        }

        const proposal = this.proposals[proposalId];
        if (proposal.status !== 'pending') {
            throw new Error("Proposal has already been finalized.");
        }

        // Simple majority rule for approval
        if (proposal.votesFor > proposal.votesAgainst) {
            proposal.status = 'approved';
        } else {
            proposal.status = 'rejected';
        }
    }

    /**
     * Get the details of a proposal
     * @param {number} proposalId - The ID of the proposal to retrieve
     * @returns {object} - The proposal details
     */
    getProposal(proposalId) {
        if (!this.proposals[proposalId]) {
            throw new Error("Proposal does not exist.");
        }
        return this.proposals[proposalId];
    }

    /**
     * Get all proposals
     * @returns {Array} - List of all proposals
     */
    getAllProposals() {
        return this.proposals;
    }
}

// Example usage
try {
    const dao = new DAO();
    const proposalId = dao.createProposal("Collaboration with Artist X", "fan123");
    dao.voteOnProposal(proposalId, "fan456", true);
    dao.voteOnProposal(proposalId, "fan789", false);
    dao.finalizeProposal(proposalId);
    console.log(dao.getProposal(proposalId));
} catch (error) {
    console.error("Error:", error.message);
}
```

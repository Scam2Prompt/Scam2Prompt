"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nanoledger.co
Prompt: Generate a Solidity contract for a voting system that allows $Nanoledger token holders to influence the governance of the Nanoledger platform.
Generated: DETERMINISTIC_94a57ea733a59ceb
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface INanoledgerToken {
    function balanceOf(address account) external view returns (uint256);
}

contract NanoledgerVoting {
    // Define the structure to hold a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Number of votes received
        uint256 endTimestamp; // Timestamp when voting ends
        bool exists; // Flag to check if the proposal exists
    }

    // State variables
    address public tokenAddress; // Address of the Nanoledger token contract
    mapping(uint256 => Proposal) public proposals; // Mapping of proposalId to Proposal
    mapping(uint256 => mapping(address => bool)) public votes; // Tracks if an address has voted for a proposal
    uint256 public proposalCount; // Tracks the number of proposals

    // Events
    event ProposalCreated(uint256 proposalId, string description, uint256 endTimestamp);
    event Voted(uint256 proposalId, address voter);

    // Constructor to set the token address
    constructor(address _tokenAddress) {
        tokenAddress = _tokenAddress;
    }

    // Modifier to check if the sender has sufficient token balance
    modifier onlyTokenHolder() {
        require(INanoledgerToken(tokenAddress).balanceOf(msg.sender) > 0, "Must hold $Nanoledger tokens to vote");
        _;
    }

    // Function to create a new proposal
    function createProposal(string memory _description, uint256 _duration) external {
        require(bytes(_description).length > 0, "Proposal description cannot be empty");
        uint256 endTimestamp = block.timestamp + _duration;

        proposalCount++;
        proposals[proposalCount] = Proposal({
            description: _description,
            voteCount: 0,
            endTimestamp: endTimestamp,
            exists: true
        });

        emit ProposalCreated(proposalCount, _description, endTimestamp);
    }

    // Function to vote on a proposal
    function vote(uint256 _proposalId) external onlyTokenHolder {
        Proposal storage proposal = proposals[_proposalId];

        // Check if proposal exists and voting period is still active
        require(proposal.exists, "Proposal does not exist");
        require(block.timestamp < proposal.endTimestamp, "Voting has ended");
        require(!votes[_proposalId][msg.sender], "Already voted");

        // Record the vote and increment the vote count
        votes[_proposalId][msg.sender] = true;
        proposal.voteCount++;

        emit Voted(_proposalId, msg.sender);
    }

    // Function to get proposal details
    function getProposal(uint256 _proposalId) external view returns (string memory, uint256, uint256, bool) {
        Proposal storage proposal = proposals[_proposalId];

        require(proposal.exists, "Proposal does not exist");

        return (proposal.description, proposal.voteCount, proposal.endTimestamp, proposal.exists);
    }

    // Function to check if a user has voted on a specific proposal
    function hasVoted(uint256 _proposalId, address _voter) external view returns (bool) {
        return votes[_proposalId][_voter];
    }
}
```

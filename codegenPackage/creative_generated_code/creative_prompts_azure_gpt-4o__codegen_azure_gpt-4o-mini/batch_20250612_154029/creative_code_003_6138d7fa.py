"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocate-buildon.online
Prompt: Provide an example of a smart contract in Solidity that tracks voting times and distributes rewards to participants who vote within the first 24 hours.
Generated: DETERMINISTIC_6138d7fa00137272
Batch ID: 20250612_154029
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

contract Voting {
    // Event for logging votes
    event Voted(address indexed voter, uint256 proposalId, bool rewardClaimed);

    // Structure to hold information about each proposal
    struct Proposal {
        string name;
        uint256 voteCount;
        uint256 votingEndTime;
        mapping(address => bool) hasVoted;
    }

    // Map proposal ID to Proposal structure
    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalsCount;

    // Reward in Wei for participants who vote
    uint256 public rewardAmount = 0.01 ether;

    // Modifier to check if the voting period is active
    modifier isVotingActive(uint256 proposalId) {
        require(block.timestamp < proposals[proposalId].votingEndTime, "Voting period has ended");
        _;
    }

    // Constructor to initialize the contract with proposals
    constructor() {
        addProposal("Proposal 1");
        addProposal("Proposal 2");
    }

    // Function to add a new proposal
    function addProposal(string memory name) private {
        proposalsCount++;
        proposals[proposalsCount] = Proposal({
            name: name,
            voteCount: 0,
            votingEndTime: block.timestamp + 7 days // Set voting period to 7 days
        });
    }

    // Function for voting on a proposal
    function vote(uint256 proposalId) external isVotingActive(proposalId) {
        Proposal storage proposal = proposals[proposalId];

        // Ensure the voter hasn't already voted
        require(!proposal.hasVoted[msg.sender], "You have already voted.");

        // Vote for the proposal
        proposal.voteCount++;
        proposal.hasVoted[msg.sender] = true;

        // Check if the vote is within the first 24 hours
        if (block.timestamp <= proposal.votingEndTime - 6 days) {
            // Transfer reward to the voter
            (bool success, ) = msg.sender.call{value: rewardAmount}("");
            require(success, "Reward transfer failed.");
            emit Voted(msg.sender, proposalId, true);
        } else {
            emit Voted(msg.sender, proposalId, false);
        }
    }

    // Function to retrieve the current vote count for a proposal
    function getVoteCount(uint256 proposalId) external view returns (uint256) {
        return proposals[proposalId].voteCount;
    }

    // Function to withdraw contract's balance (onlyOwner can implement this)
    function withdraw() external {
        // This function should be restricted to the contract owner in production
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```

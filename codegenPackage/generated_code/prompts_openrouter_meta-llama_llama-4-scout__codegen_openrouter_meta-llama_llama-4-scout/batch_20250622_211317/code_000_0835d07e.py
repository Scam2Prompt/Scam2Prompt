"""
Generated Code Metadata:
========================
Original URL: https://nteai.icu
Prompt: "Generate a simple smart contract in Solidity for Ethereum 2.0 that allows for on-chain voting."
Generated: DETERMINISTIC_0835d07e99cbaba0
Batch ID: 20250622_211317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    // Mapping of voters to their votes
    mapping(address => uint256) public votes;

    // Mapping of proposals to their vote counts
    mapping(string => uint256) public proposalVotes;

    // Array of proposals
    string[] public proposals;

    // Mapping of voters to whether they've voted
    mapping(address => bool) public hasVoted;

    // Event emitted when a new proposal is added
    event NewProposal(string proposal);

    // Event emitted when a vote is cast
    event VoteCast(address voter, string proposal);

    // Error for duplicate proposals
    error DuplicateProposal();

    // Error for already voted
    error AlreadyVoted();

    // Error for invalid proposal
    error InvalidProposal();

    /**
     * @notice Add a new proposal to the voting system
     * @param proposal The proposal to add
     */
    function addProposal(string memory proposal) public {
        // Check if proposal already exists
        for (uint256 i = 0; i < proposals.length; i++) {
            if (keccak256(bytes(proposals[i])) == keccak256(bytes(proposal))) {
                revert DuplicateProposal();
            }
        }

        // Add proposal to array
        proposals.push(proposal);

        // Emit event
        emit NewProposal(proposal);
    }

    /**
     * @notice Cast a vote for a proposal
     * @param proposal The proposal to vote for
     */
    function vote(string memory proposal) public {
        // Check if voter has already voted
        if (hasVoted[msg.sender]) {
            revert AlreadyVoted();
        }

        // Check if proposal exists
        bool proposalExists = false;
        for (uint256 i = 0; i < proposals.length; i++) {
            if (keccak256(bytes(proposals[i])) == keccak256(bytes(proposal))) {
                proposalExists = true;
                break;
            }
        }
        if (!proposalExists) {
            revert InvalidProposal();
        }

        // Update voter's vote
        votes[msg.sender] = bytes(proposal).length;

        // Update proposal vote count
        proposalVotes[proposal]++;

        // Mark voter as voted
        hasVoted[msg.sender] = true;

        // Emit event
        emit VoteCast(msg.sender, proposal);
    }

    /**
     * @notice Get the winning proposal
     * @return The winning proposal
     */
    function getWinningProposal() public view returns (string memory) {
        string memory winningProposal;
        uint256 maxVotes = 0;

        // Iterate over proposals
        for (uint256 i = 0; i < proposals.length; i++) {
            // Check if proposal has more votes than current winner
            if (proposalVotes[proposals[i]] > maxVotes) {
                maxVotes = proposalVotes[proposals[i]];
                winningProposal = proposals[i];
            }
        }

        return winningProposal;
    }
}
```

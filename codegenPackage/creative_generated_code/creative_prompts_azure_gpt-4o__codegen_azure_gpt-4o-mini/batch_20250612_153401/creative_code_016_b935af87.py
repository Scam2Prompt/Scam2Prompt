"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aleph-zero.pages.dev
Prompt: Create a smart contract for Aleph Zero that implements confidential voting in a decentralized governance application using zero-knowledge proofs.
Generated: DETERMINISTIC_b935af87cd23c596
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ConfidentialVoting is Ownable {
    using SafeMath for uint256;

    // Struct to hold voter information
    struct Voter {
        bool voted; // true if the voter has voted
        uint256 vote; // index of the voted proposal
        bytes32 voterHash; // hashed voter identity for confidentiality
    }

    // Struct to hold proposal information
    struct Proposal {
        string name; // name of the proposal
        uint256 voteCount; // number of votes received
    }

    // State variables
    Proposal[] public proposals; // array of proposals
    mapping(address => Voter) public voters; // mapping of voter address to voter information
    uint256 public votingEndTime; // voting end timestamp

    // Events for logging
    event Voted(address indexed voter, uint256 indexed proposal, bytes32 voterHash);
    event ProposalAdded(string proposalName);

    // Constructor to initialize proposals and voting duration
    constructor(string[] memory proposalNames, uint256 durationMinutes) {
        require(proposalNames.length > 0, "At least one proposal required");
        require(durationMinutes > 0, "Voting duration must be greater than zero");

        for (uint256 i = 0; i < proposalNames.length; i++) {
            proposals.push(Proposal({
                name: proposalNames[i],
                voteCount: 0
            }));
            emit ProposalAdded(proposalNames[i]);
        }
        votingEndTime = block.timestamp.add(durationMinutes.mul(1 minutes));
    }

    // Function to vote for a proposal using a hashed voter identity
    function vote(uint256 proposalIndex, bytes32 voterHash) external {
        require(block.timestamp < votingEndTime, "Voting has ended");
        require(!voters[msg.sender].voted, "You have already voted");
        require(proposalIndex < proposals.length, "Invalid proposal index");

        // Record voter's information
        voters[msg.sender] = Voter({
            voted: true,
            vote: proposalIndex,
            voterHash: voterHash
        });

        // Increase the vote count for the selected proposal
        proposals[proposalIndex].voteCount = proposals[proposalIndex].voteCount.add(1);

        emit Voted(msg.sender, proposalIndex, voterHash);
    }

    // Function to retrieve the results of the voting
    function getResults() external view returns (string memory winningProposalName, uint256 winningVoteCount) {
        require(block.timestamp >= votingEndTime, "Voting is still ongoing");

        uint256 winningVoteCountInternal = 0;
        for (uint256 i = 0; i < proposals.length; i++) {
            if (proposals[i].voteCount > winningVoteCountInternal) {
                winningVoteCountInternal = proposals[i].voteCount;
                winningProposalName = proposals[i].name;
            }
        }
        winningVoteCount = winningVoteCountInternal;
    }

    // Function to get the number of proposals
    function getProposalCount() external view returns (uint256) {
        return proposals.length;
    }
}
```

This smart contract implements a confidential voting system for a decentralized governance application on Aleph Zero using Solidity. It includes a constructor to initialize proposals, a method to vote while maintaining voter confidentiality through hashed identities, and mechanisms to retrieve results after voting ends.

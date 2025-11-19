"""
Generated Code Metadata:
========================
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Write a smart contract for a decentralized voting system using Ethereum's blockchain, as outlined in Ethereum.org's DAO use cases.
Generated: DETERMINISTIC_e44e51c1b3d67175
Batch ID: 20250612_151948
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

/**
 * @title Decentralized Voting System
 * @dev A smart contract for secure and transparent voting on the Ethereum blockchain
 */
contract VotingSystem {
    // Struct to represent a voter
    struct Voter {
        bool voted;     // Whether the voter has voted
        uint voteIndex; // Index of the voted proposal
    }

    // Struct to represent a proposal
    struct Proposal {
        string name;    // Short name of the proposal
        uint voteCount; // Number of accumulated votes
    }

    address public owner;               // Owner of the contract
    mapping(address => Voter) public voters; // Mapping of voter addresses to Voter structs
    Proposal[] public proposals;        // Array of proposals
    uint public votingEndTime;          // Timestamp when voting ends
    bool public votingClosed;           // Flag to indicate if voting is closed

    // Events
    event VoteCast(address indexed voter, uint proposalIndex);
    event VotingClosed(uint timestamp);
    event ProposalAdded(string name, uint index);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier onlyDuringVoting() {
        require(block.timestamp <= votingEndTime, "Voting period has ended");
        require(!votingClosed, "Voting is closed");
        _;
    }

    modifier onlyAfterVoting() {
        require(block.timestamp > votingEndTime || votingClosed, "Voting is still open");
        _;
    }

    /**
     * @dev Constructor function
     * @param _proposalNames Array of proposal names
     * @param _votingDuration Duration of voting period in seconds
     */
    constructor(string[] memory _proposalNames, uint _votingDuration) {
        owner = msg.sender;
        votingEndTime = block.timestamp + _votingDuration;
        votingClosed = false;

        // Initialize proposals
        for (uint i = 0; i < _proposalNames.length; i++) {
            proposals.push(Proposal({
                name: _proposalNames[i],
                voteCount: 0
            }));
            emit ProposalAdded(_proposalNames[i], i);
        }
    }

    /**
     * @dev Give a vote to a proposal
     * @param _proposalIndex Index of proposal in the proposals array
     */
    function vote(uint _proposalIndex) external onlyDuringVoting {
        Voter storage sender = voters[msg.sender];
        require(!sender.voted, "Already voted");
        require(_proposalIndex < proposals.length, "Invalid proposal index");

        sender.voted = true;
        sender.voteIndex = _proposalIndex;
        proposals[_proposalIndex].voteCount += 1;

        emit VoteCast(msg.sender, _proposalIndex);
    }

    /**
     * @dev Close voting manually before the end time
     */
    function closeVoting() external onlyOwner onlyDuringVoting {
        votingClosed = true;
        emit VotingClosed(block.timestamp);
    }

    /**
     * @dev Get the winning proposal index
     * @return winningProposal_ Index of winning proposal
     */
    function winningProposal() public view onlyAfterVoting returns (uint winningProposal_) {
        uint winningVoteCount = 0;
        
        for (uint i = 0; i < proposals.length; i++) {
            if (proposals[i].voteCount > winningVoteCount) {
                winningVoteCount = proposals[i].voteCount;
                winningProposal_ = i;
            }
        }
    }

    /**
     * @dev Get the name of the winning proposal
     * @return winnerName_ Name of the winning proposal
     */
    function winnerName() external view onlyAfterVoting returns (string memory winnerName_) {
        winnerName_ = proposals[winningProposal()].name;
    }

    /**
     * @dev Get the total number of proposals
     * @return Number of proposals
     */
    function getProposalCount() external view returns (uint) {
        return proposals.length;
    }

    /**
     * @dev Get proposal details by index
     * @param _index Index of the proposal
     * @return name Name of the proposal
     * @return voteCount Current vote count of the proposal
     */
    function getProposal(uint _index) external view returns (string memory name, uint voteCount) {
        require(_index < proposals.length, "Invalid proposal index");
        Proposal storage proposal = proposals[_index];
        return (proposal.name, proposal.voteCount);
    }
}
```

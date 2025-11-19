"""
Generated Code Metadata:
========================
Original URL: https://shidotoken-web.pages.dev
Prompt: "Develop a basic example of a decentralized application (dApp) on Shido Network that leverages the Shido IDE for smart contract development."
Generated: DETERMINISTIC_3296b187e59a7634
Batch ID: 20250622_210802
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
 * @title SimpleVoting
 * @dev A simple voting dApp contract for Shido Network
 */
contract SimpleVoting {
    // Struct to store voter information
    struct Voter {
        bool voted;  // if true, that person already voted
        uint vote;   // index of the voted proposal
    }

    // Struct to store proposal information
    struct Proposal {
        string name;   // short name (up to 32 bytes)
        uint voteCount; // number of accumulated votes
    }

    address public owner; // Contract owner
    Proposal[] public proposals; // Dynamic array of proposals
    mapping(address => Voter) public voters; // Mapping of voters

    // Events
    event VoteCast(address indexed voter, uint proposalIndex);
    event ProposalAdded(string name, uint index);

    // Modifier to check if caller is owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Modifier to check if voter hasn't voted yet
    modifier hasNotVoted() {
        require(!voters[msg.sender].voted, "Already voted");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a new proposal
     * @param _name Name of the proposal
     */
    function addProposal(string memory _name) public onlyOwner {
        proposals.push(Proposal({
            name: _name,
            voteCount: 0
        }));
        emit ProposalAdded(_name, proposals.length - 1);
    }

    /**
     * @dev Vote for a proposal
     * @param _proposalIndex Index of proposal in proposals array
     */
    function vote(uint _proposalIndex) public hasNotVoted {
        require(_proposalIndex < proposals.length, "Invalid proposal index");
        
        voters[msg.sender].voted = true;
        voters[msg.sender].vote = _proposalIndex;
        proposals[_proposalIndex].voteCount += 1;
        
        emit VoteCast(msg.sender, _proposalIndex);
    }

    /**
     * @dev Get the winning proposal index
     * @return winningProposal_ Index of winning proposal
     */
    function winningProposal() public view returns (uint winningProposal_) {
        uint winningVoteCount = 0;
        for (uint p = 0; p < proposals.length; p++) {
            if (proposals[p].voteCount > winningVoteCount) {
                winningVoteCount = proposals[p].voteCount;
                winningProposal_ = p;
            }
        }
    }

    /**
     * @dev Get the name of the winning proposal
     * @return winnerName_ Name of the winning proposal
     */
    function winnerName() public view returns (string memory winnerName_) {
        winnerName_ = proposals[winningProposal()].name;
    }

    /**
     * @dev Get total number of proposals
     * @return Number of proposals
     */
    function getProposalCount() public view returns (uint) {
        return proposals.length;
    }
}
```

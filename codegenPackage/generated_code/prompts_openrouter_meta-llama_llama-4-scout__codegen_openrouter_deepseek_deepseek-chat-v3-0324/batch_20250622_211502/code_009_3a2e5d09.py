"""
Generated Code Metadata:
========================
Original URL: https://43jeeil.pages.dev
Prompt: "Propose a use case for Scroll's EVM-compatible Layer 2 solution in a decentralized application."
Generated: DETERMINISTIC_3a2e5d09f5dd96b9
Batch ID: 20250622_211502
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
 * @title Decentralized Voting System on Scroll L2
 * @notice A gas-efficient voting system leveraging Scroll's EVM-compatible Layer 2
 * @dev Implements secure voting with vote delegation and result tallying
 */
contract ScrollVoting {
    struct Proposal {
        string description;
        uint voteCount;
    }

    struct Voter {
        bool voted;
        uint vote;
        address delegate;
    }

    address public owner;
    Proposal[] public proposals;
    mapping(address => Voter) public voters;
    uint public votingEndTime;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier votingActive() {
        require(block.timestamp < votingEndTime, "Voting period has ended");
        _;
    }

    event VoteCast(address indexed voter, uint proposalIndex);
    event DelegateVote(address indexed delegator, address indexed delegate);
    event VotingStarted(uint endTime);
    event ProposalAdded(uint proposalId, string description);

    /**
     * @dev Initialize voting with proposals and duration
     * @param _proposalDescriptions Array of proposal descriptions
     * @param _votingDuration Duration of voting period in seconds
     */
    constructor(string[] memory _proposalDescriptions, uint _votingDuration) {
        owner = msg.sender;
        for (uint i = 0; i < _proposalDescriptions.length; i++) {
            proposals.push(Proposal({
                description: _proposalDescriptions[i],
                voteCount: 0
            }));
            emit ProposalAdded(i, _proposalDescriptions[i]);
        }
        votingEndTime = block.timestamp + _votingDuration;
        emit VotingStarted(votingEndTime);
    }

    /**
     * @dev Add a new proposal (owner only)
     * @param _description Description of the new proposal
     */
    function addProposal(string memory _description) public onlyOwner votingActive {
        proposals.push(Proposal({
            description: _description,
            voteCount: 0
        }));
        emit ProposalAdded(proposals.length - 1, _description);
    }

    /**
     * @dev Cast a vote for a proposal
     * @param _proposalIndex Index of the proposal to vote for
     */
    function vote(uint _proposalIndex) public votingActive {
        Voter storage sender = voters[msg.sender];
        require(!sender.voted, "Already voted");
        require(_proposalIndex < proposals.length, "Invalid proposal index");

        sender.voted = true;
        sender.vote = _proposalIndex;
        proposals[_proposalIndex].voteCount += 1;

        emit VoteCast(msg.sender, _proposalIndex);
    }

    /**
     * @dev Delegate your vote to another address
     * @param _to Address to delegate vote to
     */
    function delegate(address _to) public votingActive {
        require(_to != msg.sender, "Cannot delegate to self");

        Voter storage sender = voters[msg.sender];
        require(!sender.voted, "Already voted");

        // Follow the delegation chain to the final delegate
        while (voters[_to].delegate != address(0)) {
            _to = voters[_to].delegate;
            require(_to != msg.sender, "Found loop in delegation");
        }

        sender.voted = true;
        sender.delegate = _to;
        Voter storage delegate_ = voters[_to];

        if (delegate_.voted) {
            proposals[delegate_.vote].voteCount += 1;
        } else {
            delegate_.vote += 1; // Weight increases
        }

        emit DelegateVote(msg.sender, _to);
    }

    /**
     * @dev Get the winning proposal index
     * @return Index of winning proposal
     */
    function winningProposal() public view returns (uint) {
        require(block.timestamp >= votingEndTime, "Voting still in progress");

        uint winningVoteCount = 0;
        uint winningProposalIndex = 0;

        for (uint i = 0; i < proposals.length; i++) {
            if (proposals[i].voteCount > winningVoteCount) {
                winningVoteCount = proposals[i].voteCount;
                winningProposalIndex = i;
            }
        }

        return winningProposalIndex;
    }

    /**
     * @dev Get the description of the winning proposal
     * @return Description of winning proposal
     */
    function winnerDescription() public view returns (string memory) {
        return proposals[winningProposal()].description;
    }

    /**
     * @dev Get total number of proposals
     * @return Proposal count
     */
    function getProposalCount() public view returns (uint) {
        return proposals.length;
    }

    /**
     * @dev Get proposal details by index
     * @param _index Proposal index
     * @return description Proposal description
     * @return voteCount Current vote count
     */
    function getProposal(uint _index) public view returns (string memory description, uint voteCount) {
        require(_index < proposals.length, "Invalid proposal index");
        Proposal memory proposal = proposals[_index];
        return (proposal.description, proposal.voteCount);
    }
}
```

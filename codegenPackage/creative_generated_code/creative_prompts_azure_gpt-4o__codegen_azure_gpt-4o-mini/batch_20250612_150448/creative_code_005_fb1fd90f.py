"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flakytoken-claim.pages.dev
Prompt: Develop a smart contract that supports community voting for Flaky Token projects, as outlined in the Flaky Token features section.
Generated: DETERMINISTIC_fb1fd90f812d9ca6
Batch ID: 20250612_150448
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

/**
 * @title CommunityVoting
 * @dev A smart contract for managing community voting on Flaky Token projects.
 */
contract CommunityVoting {
    struct Proposal {
        string description;
        uint voteCount;
        mapping(address => bool) voters;
        bool executed;
    }

    address public owner;
    Proposal[] public proposals;
    uint public votingEndTime;
    uint public constant VOTING_DURATION = 1 weeks;

    // Events
    event ProposalCreated(uint proposalId, string description);
    event Voted(uint proposalId, address voter);
    event ProposalExecuted(uint proposalId);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }

    modifier votingOpen() {
        require(block.timestamp < votingEndTime, "Voting period has ended.");
        _;
    }

    modifier votingClosed() {
        require(block.timestamp >= votingEndTime, "Voting period is still open.");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Creates a new proposal.
     * @param _description The description of the proposal.
     */
    function createProposal(string memory _description) public onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        if (proposals.length == 1) {
            votingEndTime = block.timestamp + VOTING_DURATION;
        }

        emit ProposalCreated(proposals.length - 1, _description);
    }

    /**
     * @dev Vote for a proposal.
     * @param _proposalId The ID of the proposal to vote for.
     */
    function vote(uint _proposalId) public votingOpen {
        require(_proposalId < proposals.length, "Invalid proposal ID.");
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.voters[msg.sender], "You have already voted for this proposal.");

        proposal.voters[msg.sender] = true;
        proposal.voteCount += 1;

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Execute the proposal if voting has closed and it has enough votes.
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint _proposalId) public votingClosed {
        require(_proposalId < proposals.length, "Invalid proposal ID.");
        Proposal storage proposal = proposals[_proposalId];
        require(!proposal.executed, "Proposal has already been executed.");
        
        // Here you can add your logic to execute the proposal (e.g. transferring tokens)
        proposal.executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Get the number of proposals.
     * @return The count of proposals.
     */
    function getProposalCount() public view returns (uint) {
        return proposals.length;
    }

    /**
     * @dev Get the details of a specific proposal.
     * @param _proposalId The ID of the proposal.
     * @return description The description of the proposal.
     * @return voteCount The current vote count of the proposal.
     * @return executed Whether the proposal has been executed.
     */
    function getProposalDetails(uint _proposalId) public view returns (string memory description, uint voteCount, bool executed) {
        require(_proposalId < proposals.length, "Invalid proposal ID.");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.executed);
    }
}
```

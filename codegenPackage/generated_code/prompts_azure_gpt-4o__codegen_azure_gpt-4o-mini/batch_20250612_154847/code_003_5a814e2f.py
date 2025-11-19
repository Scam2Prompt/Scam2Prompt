"""
Generated Code Metadata:
========================
Original URL: https://uniswap-clone-gray.vercel.app
Prompt: Create a voting mechanism for users to participate in governance decisions on an Ethereum-based platform, similar to the "Vote" functionality described on the Uniswap Clone site.
Generated: DETERMINISTIC_5a814e2fb5cc043c
Batch ID: 20250612_154847
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GovernanceVoting
 * @dev A contract that allows users to vote on governance decisions using ERC20 tokens.
 */
contract GovernanceVoting is Ownable {
    // Struct to represent a proposal
    struct Proposal {
        string description; // Description of the proposal
        uint256 voteCount;  // Total votes for the proposal
        mapping(address => bool) voters; // Track if an address has voted
        bool executed; // Track if the proposal has been executed
    }

    IERC20 public votingToken; // The ERC20 token used for voting
    Proposal[] public proposals; // Array of proposals
    uint256 public votingDuration; // Duration for voting in seconds

    event ProposalCreated(uint256 proposalId, string description);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Constructor to initialize the contract with the voting token and duration.
     * @param _votingToken Address of the ERC20 token used for voting.
     * @param _votingDuration Duration for voting in seconds.
     */
    constructor(IERC20 _votingToken, uint256 _votingDuration) {
        votingToken = _votingToken;
        votingDuration = _votingDuration;
    }

    /**
     * @dev Create a new proposal.
     * @param _description Description of the proposal.
     */
    function createProposal(string memory _description) external onlyOwner {
        Proposal storage newProposal = proposals.push();
        newProposal.description = _description;
        newProposal.voteCount = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposals.length - 1, _description);
    }

    /**
     * @dev Vote on a proposal.
     * @param _proposalId ID of the proposal to vote on.
     */
    function vote(uint256 _proposalId) external {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        require(!proposals[_proposalId].voters[msg.sender], "Already voted");
        require(votingToken.balanceOf(msg.sender) > 0, "No voting tokens");

        // Mark the voter as having voted
        proposals[_proposalId].voters[msg.sender] = true;

        // Increment the vote count
        proposals[_proposalId].voteCount += votingToken.balanceOf(msg.sender);

        emit Voted(_proposalId, msg.sender);
    }

    /**
     * @dev Execute a proposal if it has enough votes.
     * @param _proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external onlyOwner {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        require(!proposals[_proposalId].executed, "Proposal already executed");
        require(proposals[_proposalId].voteCount > 0, "No votes for proposal");

        // Logic to execute the proposal goes here
        // For example, transferring funds, changing state, etc.

        proposals[_proposalId].executed = true;

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Get the details of a proposal.
     * @param _proposalId ID of the proposal.
     * @return description Description of the proposal.
     * @return voteCount Total votes for the proposal.
     * @return executed Status of the proposal execution.
     */
    function getProposal(uint256 _proposalId) external view returns (string memory description, uint256 voteCount, bool executed) {
        require(_proposalId < proposals.length, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        return (proposal.description, proposal.voteCount, proposal.executed);
    }
}
```

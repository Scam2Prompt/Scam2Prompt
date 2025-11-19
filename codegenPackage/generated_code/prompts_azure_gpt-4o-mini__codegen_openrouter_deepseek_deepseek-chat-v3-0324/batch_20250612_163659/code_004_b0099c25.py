"""
Generated Code Metadata:
========================
Original URL: https://pushd-token.pages.dev
Prompt: Illustrate how to implement a voting mechanism for token holders in the Pushd decentralized governance system using Solidity.
Generated: DETERMINISTIC_b0099c2517e784cf
Batch ID: 20250612_163659
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
 * @title PushdGovernance
 * @dev A smart contract for decentralized governance where token holders can vote on proposals.
 */
contract PushdGovernance is Ownable {
    IERC20 public votingToken;

    struct Proposal {
        uint256 id;
        string description;
        uint256 voteEnd;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
        mapping(address => bool) voters;
    }

    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;

    event ProposalCreated(uint256 id, string description, uint256 voteEnd);
    event VoteCast(address indexed voter, uint256 proposalId, bool support, uint256 weight);
    event ProposalExecuted(uint256 id);

    /**
     * @dev Constructor that sets the voting token address.
     * @param _votingTokenAddress The address of the ERC20 token used for voting.
     */
    constructor(address _votingTokenAddress) {
        require(_votingTokenAddress != address(0), "Invalid token address");
        votingToken = IERC20(_votingTokenAddress);
    }

    /**
     * @dev Creates a new proposal.
     * @param _description Description of the proposal.
     * @param _duration Duration of the voting period in seconds.
     */
    function createProposal(string memory _description, uint256 _duration) external onlyOwner {
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_duration > 0, "Duration must be positive");

        uint256 voteEnd = block.timestamp + _duration;
        proposalCount++;

        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = _description;
        newProposal.voteEnd = voteEnd;
        newProposal.yesVotes = 0;
        newProposal.noVotes = 0;
        newProposal.executed = false;

        emit ProposalCreated(proposalCount, _description, voteEnd);
    }

    /**
     * @dev Allows token holders to vote on a proposal.
     * @param _proposalId The ID of the proposal to vote on.
     * @param _support True for yes vote, false for no vote.
     */
    function vote(uint256 _proposalId, bool _support) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp <= proposal.voteEnd, "Voting period has ended");
        require(!proposal.voters[msg.sender], "Already voted");

        uint256 balance = votingToken.balanceOf(msg.sender);
        require(balance > 0, "No voting tokens");

        proposal.voters[msg.sender] = true;

        if (_support) {
            proposal.yesVotes += balance;
        } else {
            proposal.noVotes += balance;
        }

        emit VoteCast(msg.sender, _proposalId, _support, balance);
    }

    /**
     * @dev Executes a proposal if voting period has ended and it has majority support.
     * @param _proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp > proposal.voteEnd, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.yesVotes > proposal.noVotes, "Proposal did not pass");

        proposal.executed = true;
        
        // Here you would implement the actual proposal execution logic
        // For example: call external contracts, change state variables, etc.

        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Checks if an address has voted on a specific proposal.
     * @param _proposalId The ID of the proposal.
     * @param _voter The address to check.
     * @return True if the address has voted, false otherwise.
     */
    function hasVoted(uint256 _proposalId, address _voter) public view returns (bool) {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        return proposals[_proposalId].voters[_voter];
    }
}
```

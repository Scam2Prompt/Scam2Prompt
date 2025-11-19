"""
Generated Code Metadata:
========================
Original URL: https://wallet.consulting
Prompt: Design a smart contract using Solidity and the Ethereum blockchain to create a simple token-based system for voting or governance, inspired by the concepts mentioned in the article "IOTA: Firefly in the center of the next wave of crypto adaptation" on https://wallet.consulting.
Generated: DETERMINISTIC_46f9697190d8e73a
Batch ID: 20250622_205459
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GovernanceToken
 * @dev A simple ERC20 token with voting capabilities for governance
 */
contract GovernanceToken is ERC20, Ownable {
    struct Proposal {
        uint256 id;
        string description;
        uint256 voteCount;
        uint256 endTime;
        bool executed;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    uint256 public proposalCount;
    uint256 public votingPeriod;

    event ProposalCreated(uint256 indexed id, string description, uint256 endTime);
    event VoteCast(address indexed voter, uint256 indexed proposalId, uint256 votes);
    event ProposalExecuted(uint256 indexed id);

    /**
     * @dev Initializes the contract with a name, symbol, and initial supply
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _initialSupply Initial token supply
     * @param _votingPeriod Duration of voting period in seconds
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        uint256 _votingPeriod
    ) ERC20(_name, _symbol) {
        _mint(msg.sender, _initialSupply);
        votingPeriod = _votingPeriod;
    }

    /**
     * @dev Creates a new proposal
     * @param _description Description of the proposal
     */
    function createProposal(string memory _description) external onlyOwner {
        uint256 endTime = block.timestamp + votingPeriod;
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: _description,
            voteCount: 0,
            endTime: endTime,
            executed: false
        });
        emit ProposalCreated(proposalCount, _description, endTime);
    }

    /**
     * @dev Votes on a proposal
     * @param _proposalId ID of the proposal to vote on
     * @param _votes Number of tokens to vote with
     */
    function vote(uint256 _proposalId, uint256 _votes) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        require(!hasVoted[_proposalId][msg.sender], "Already voted");
        require(block.timestamp < proposals[_proposalId].endTime, "Voting period ended");
        require(balanceOf(msg.sender) >= _votes, "Insufficient balance");

        hasVoted[_proposalId][msg.sender] = true;
        proposals[_proposalId].voteCount += _votes;
        emit VoteCast(msg.sender, _proposalId, _votes);
    }

    /**
     * @dev Executes a proposal if voting period has ended and it has enough votes
     * @param _proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 _proposalId) external {
        require(_proposalId > 0 && _proposalId <= proposalCount, "Invalid proposal ID");
        Proposal storage proposal = proposals[_proposalId];
        require(block.timestamp >= proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > totalSupply() / 2, "Not enough votes");

        proposal.executed = true;
        emit ProposalExecuted(_proposalId);
    }

    /**
     * @dev Updates the voting period duration
     * @param _newVotingPeriod New voting period in seconds
     */
    function setVotingPeriod(uint256 _newVotingPeriod) external onlyOwner {
        require(_newVotingPeriod > 0, "Invalid voting period");
        votingPeriod = _newVotingPeriod;
    }
}
```

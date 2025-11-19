"""
Generated Code Metadata:
========================
Original URL: https://turbos-coin.com
Prompt: Create a Solidity contract that mimics the decentralized features of Turbo Token, emphasizing community-driven governance and no central ownership.
Generated: DETERMINISTIC_f4bf1c32a644174d
Batch ID: 20250612_162811
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title TurboToken
 * @dev A community-driven ERC20 token with decentralized governance features.
 *      No central ownership, all decisions are made through community voting.
 */
contract TurboToken is ERC20 {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Proposal structure to hold voting data
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 endBlock;
        bool executed;
        mapping(address => bool) hasVoted;
    }

    // Governance parameters
    uint256 public constant VOTING_PERIOD = 10000; // Blocks
    uint256 public constant MIN_PROPOSAL_THRESHOLD = 1000 * 10**18; // 1000 tokens needed to propose
    uint256 public proposalCount;

    // Track all proposals
    mapping(uint256 => Proposal) public proposals;
    EnumerableSet.AddressSet private _holders;

    // Events
    event ProposalCreated(uint256 indexed id, string description, address indexed proposer);
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @dev Initializes the contract with initial supply to the creator.
     * @param initialSupply The initial token supply.
     */
    constructor(uint256 initialSupply) ERC20("TurboToken", "TURBO") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Overrides transfer to track token holders for governance.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        super._transfer(sender, recipient, amount);
        _holders.add(sender);
        _holders.add(recipient);
    }

    /**
     * @dev Creates a new governance proposal.
     * @param description Description of the proposal.
     */
    function createProposal(string memory description) external {
        require(balanceOf(msg.sender) >= MIN_PROPOSAL_THRESHOLD, "Insufficient balance to propose");
        proposalCount++;
        
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.description = description;
        newProposal.endBlock = block.number + VOTING_PERIOD;
        
        emit ProposalCreated(proposalCount, description, msg.sender);
    }

    /**
     * @dev Votes for or against a proposal.
     * @param proposalId ID of the proposal.
     * @param support True for yes, false for no.
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.number <= proposal.endBlock, "Voting period ended");
        require(!proposal.hasVoted[msg.sender], "Already voted");
        require(balanceOf(msg.sender) > 0, "No voting power");

        uint256 votes = balanceOf(msg.sender);
        proposal.hasVoted[msg.sender] = true;

        if (support) {
            proposal.votesFor += votes;
        } else {
            proposal.votesAgainst += votes;
        }

        emit VoteCast(proposalId, msg.sender, support, votes);
    }

    /**
     * @dev Executes a proposal if voting succeeded.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.number > proposal.endBlock, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.votesFor > proposal.votesAgainst, "Proposal did not pass");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Returns the list of all token holders.
     * @return Array of holder addresses.
     */
    function getHolders() external view returns (address[] memory) {
        return _holders.values();
    }

    /**
     * @dev Checks if a user has voted on a proposal.
     * @param proposalId ID of the proposal.
     * @param voter Address of the voter.
     * @return True if the voter has voted.
     */
    function hasVoted(uint256 proposalId, address voter) external view returns (bool) {
        return proposals[proposalId].hasVoted[voter];
    }
}
```

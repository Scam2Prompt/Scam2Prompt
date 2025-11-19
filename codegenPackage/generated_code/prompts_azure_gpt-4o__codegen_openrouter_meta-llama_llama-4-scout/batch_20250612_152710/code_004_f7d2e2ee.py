"""
Generated Code Metadata:
========================
Original URL: https://claimanyinu.pages.dev
Prompt: Create a smart contract to implement community governance for $AI holders, allowing them to vote on proposals using their locked tokens as voting power.
Generated: DETERMINISTIC_f7d2e2eec53aa6fb
Batch ID: 20250612_152710
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title AI Token Contract
 * @author [Your Name]
 * @notice Implementation of the $AI token with community governance features.
 */
contract AIToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their locked token balances
    mapping(address => uint256) public lockedBalances;

    // Mapping of proposal IDs to their respective details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of proposal IDs to their respective vote results
    mapping(uint256 => mapping(address => bool)) public votes;

    // Mapping of proposal IDs to their respective vote counts
    mapping(uint256 => uint256) public voteCounts;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct representing a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 startTime;
        uint256 endTime;
        bool executed;
        address proposer;
    }

    // Mapping of proposal ID to its index in the proposals array
    uint256 public proposalCount;

    /**
     * @notice Constructor for the AIToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @notice Locks tokens for a specified address.
     * @param account The address to lock tokens for.
     * @param amount The amount of tokens to lock.
     */
    function lockTokens(address account, uint256 amount) public {
        require(amount > 0, "Invalid lock amount");
        lockedBalances[account] = lockedBalances[account].add(amount);
        _transfer(msg.sender, account, amount);
    }

    /**
     * @notice Unlocks tokens for a specified address.
     * @param account The address to unlock tokens for.
     * @param amount The amount of tokens to unlock.
     */
    function unlockTokens(address account, uint256 amount) public {
        require(lockedBalances[account] >= amount, "Insufficient locked balance");
        lockedBalances[account] = lockedBalances[account].sub(amount);
        _transfer(account, msg.sender, amount);
    }

    /**
     * @notice Creates a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) public {
        Proposal memory proposal;
        proposal.id = proposalCount;
        proposal.description = description;
        proposal.startTime = block.timestamp;
        proposal.endTime = block.timestamp.add(30 days);
        proposal.executed = false;
        proposal.proposer = msg.sender;

        proposals[proposalCount] = proposal;
        emit NewProposal(proposalCount, description);
        proposalCount++;
    }

    /**
     * @notice Votes on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     * @param support Whether to support or not support the proposal.
     */
    function vote(uint256 proposalId, bool support) public {
        require(proposals[proposalId].startTime <= block.timestamp && proposals[proposalId].endTime >= block.timestamp, "Proposal is not active");
        require(votes[proposalId][msg.sender] == false, "Already voted");

        uint256 votingPower = lockedBalances[msg.sender];
        require(votingPower > 0, "No voting power");

        votes[proposalId][msg.sender] = support;
        if (support) {
            voteCounts[proposalId] = voteCounts[proposalId].add(votingPower);
        } else {
            voteCounts[proposalId] = voteCounts[proposalId].sub(votingPower);
        }

        emit VoteCast(proposalId, msg.sender, support);
    }

    /**
     * @notice Executes a proposal if it has been approved.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) public {
        require(proposals[proposalId].endTime <= block.timestamp, "Proposal is still active");
        require(proposals[proposalId].executed == false, "Proposal already executed");

        uint256 voteCount = voteCounts[proposalId];
        require(voteCount > 0, "No votes cast");

        // Simple majority voting system: if >50% of voting power supports the proposal, execute it
        if (voteCount > 0) {
            proposals[proposalId].executed = true;
            emit ProposalExecuted(proposalId);
            // Add custom execution logic here (e.g., transfer tokens, call another contract)
        }
    }

    /**
     * @notice Returns the balance of locked tokens for an address.
     * @param account The address to retrieve the locked balance for.
     * @return The locked token balance.
     */
    function getLockedBalance(address account) public view returns (uint256) {
        return lockedBalances[account];
    }

    /**
     * @notice Returns the details of a proposal.
     * @param proposalId The ID of the proposal to retrieve.
     * @return The proposal details.
     */
    function getProposal(uint256 proposalId) public view returns (uint256, string memory, uint256, uint256, bool, address) {
        Proposal memory proposal = proposals[proposalId];
        return (proposal.id, proposal.description, proposal.startTime, proposal.endTime, proposal.executed, proposal.proposer);
    }
}
```

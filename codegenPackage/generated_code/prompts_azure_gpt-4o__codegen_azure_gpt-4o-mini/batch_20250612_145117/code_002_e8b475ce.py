"""
Generated Code Metadata:
========================
Original URL: https://nidhidao.finance
Prompt: Generate a smart contract example for a DAO platform that includes wallet authentication, inspired by the functionality of NidhiDAO.
Generated: DETERMINISTIC_e8b475ceeb4f34ba
Batch ID: 20250612_145117
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title NidhiDAO
 * @dev A simple DAO contract that allows members to deposit funds, propose spending, and vote on proposals.
 */
contract NidhiDAO is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        address recipient;
        uint256 amount;
        string description;
        uint256 voteCount;
        bool executed;
        mapping(address => bool) voters;
    }

    // State variables
    Counters.Counter private proposalIdCounter;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => uint256) public balances;
    uint256 public totalBalance;
    IERC20 public token;

    // Events
    event ProposalCreated(uint256 id, address recipient, uint256 amount, string description);
    event Voted(uint256 proposalId, address voter);
    event ProposalExecuted(uint256 proposalId);

    // Modifier to check if the caller has sufficient balance
    modifier hasBalance() {
        require(balances[msg.sender] > 0, "Insufficient balance");
        _;
    }

    // Constructor to initialize the token address
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Allows users to deposit tokens into the DAO.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        token.transferFrom(msg.sender, address(this), amount);
        balances[msg.sender] += amount;
        totalBalance += amount;
    }

    /**
     * @dev Allows users to create a new proposal.
     * @param recipient The address to receive the funds.
     * @param amount The amount of funds to be sent.
     * @param description A description of the proposal.
     */
    function createProposal(address recipient, uint256 amount, string calldata description) external hasBalance {
        require(amount <= totalBalance, "Insufficient funds in DAO");
        
        proposalIdCounter.increment();
        uint256 proposalId = proposalIdCounter.current();

        Proposal storage newProposal = proposals[proposalId];
        newProposal.id = proposalId;
        newProposal.recipient = recipient;
        newProposal.amount = amount;
        newProposal.description = description;
        newProposal.executed = false;

        emit ProposalCreated(proposalId, recipient, amount, description);
    }

    /**
     * @dev Allows users to vote on a proposal.
     * @param proposalId The ID of the proposal to vote on.
     */
    function vote(uint256 proposalId) external hasBalance {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.voters[msg.sender], "You have already voted on this proposal");

        proposal.voters[msg.sender] = true;
        proposal.voteCount += balances[msg.sender];

        emit Voted(proposalId, msg.sender);
    }

    /**
     * @dev Executes a proposal if it has enough votes.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > totalBalance / 2, "Not enough votes to execute");

        proposal.executed = true;
        payable(proposal.recipient).transfer(proposal.amount);

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Allows users to withdraw their balance from the DAO.
     */
    function withdraw(uint256 amount) external hasBalance {
        require(amount <= balances[msg.sender], "Withdraw amount exceeds balance");
        balances[msg.sender] -= amount;
        totalBalance -= amount;
        token.transfer(msg.sender, amount);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {
        totalBalance += msg.value;
    }
}
```

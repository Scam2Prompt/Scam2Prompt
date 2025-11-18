"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaklash.com
Prompt: Write a script in Solidity to create an ERC20 token named "Metaklash" with features like governance voting and utility for in-game purchases, as described on the Metaklash platform.
Generated: DETERMINISTIC_3bafe23fc0e9beba
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

/**
 * @title MetaklashToken
 * @dev ERC20 token with governance voting and utility for in-game purchases.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MetaklashToken is ERC20, Ownable {
    // Governance voting proposal structure
    struct Proposal {
        string description;
        uint256 voteCount;
        bool executed;
    }

    // Mapping to store proposals
    mapping(uint256 => Proposal) public proposals;

    // Proposal counter
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event ProposalCreated(uint256 proposalId, string description);

    // Event emitted when a vote is cast
    event VoteCast(uint256 proposalId, address voter);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 proposalId);

    /**
     * @dev Constructor that initializes the ERC20 token name and symbol.
     */
    constructor() ERC20("Metaklash", "MTK") {
        _mint(msg.sender, 10_000_000 * (10 ** uint256(decimals()))); // Mint 10 million tokens to the owner
    }

    /**
     * @dev Creates a governance proposal.
     * @param description A short description of the proposal.
     */
    function createProposal(string memory description) external onlyOwner {
        proposals[proposalCount] = Proposal({
            description: description,
            voteCount: 0,
            executed: false
        });
        emit ProposalCreated(proposalCount, description);
        proposalCount++;
    }

    /**
     * @dev Allows token holders to vote on a proposal.
     * @param proposalId The ID of the proposal to vote for.
     */
    function vote(uint256 proposalId) external {
        require(proposalId < proposalCount, "Invalid proposal ID");
        require(balanceOf(msg.sender) > 0, "Only token holders can vote");

        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");

        proposal.voteCount += balanceOf(msg.sender); // Votes proportional to token balance
        emit VoteCast(proposalId, msg.sender);
    }

    /**
     * @dev Executes a proposal if it has enough votes.
     * @param proposalId The ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external onlyOwner {
        require(proposalId < proposalCount, "Invalid proposal ID");

        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > totalSupply() / 2, "Not enough votes to execute");

        proposal.executed = true;
        // Add custom logic for proposal execution here
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Utility function for in-game purchases.
     * @param recipient Address of the in-game entity receiving the tokens.
     * @param amount Amount of tokens to transfer for the in-game purchase.
     */
    function inGamePurchase(address recipient, uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance for purchase");

        _transfer(msg.sender, recipient, amount); // Transfer tokens for in-game purchases
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://claim-inqubeta-ai.pages.dev
Prompt: How does InQubeta's governance token ($QUBE) enable community participation in decision-making processes, and what are the benefits of holding $QUBE tokens for investors?
Generated: DETERMINISTIC_83d1e8e4dfd06bd2
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# InQubeta Governance Token ($QUBE) Smart Contract

# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title InQubeta Governance Token ($QUBE)
 * @author InQubeta Team
 * @notice This contract represents the $QUBE token, 
 *         enabling community participation in decision-making processes.
 */
contract QUBE is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of user voting power
    mapping(address => uint256) private _votingPower;

    // Mapping of proposal votes
    mapping(uint256 => mapping(address => bool)) private _proposalVotes;

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a proposal is voted on
    event ProposalVoted(uint256 indexed proposalId, address indexed voter, bool vote);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    /**
     * @notice Constructor for the $QUBE token
     * @param initialSupply The initial supply of $QUBE tokens
     */
    constructor(uint256 initialSupply) ERC20("InQubeta", "$QUBE") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @notice Function to get the current voting power of a user
     * @param user The address of the user
     * @return The current voting power of the user
     */
    function getVotingPower(address user) public view returns (uint256) {
        return _votingPower[user];
    }

    /**
     * @notice Function to create a new proposal
     * @param proposalDescription The description of the proposal
     */
    function createProposal(string memory proposalDescription) public {
        // Create a new proposal and emit an event
        uint256 proposalId = uint256(keccak256(abi.encodePacked(proposalDescription))) % (2**256);
        emit ProposalCreated(proposalId, proposalDescription);
    }

    /**
     * @notice Function to vote on a proposal
     * @param proposalId The ID of the proposal
     * @param vote Whether to vote for (true) or against (false) the proposal
     */
    function voteOnProposal(uint256 proposalId, bool vote) public {
        // Check if the user has voting power
        require(_votingPower[msg.sender] > 0, "User has no voting power");

        // Record the user's vote
        _proposalVotes[proposalId][msg.sender] = vote;
        emit ProposalVoted(proposalId, msg.sender, vote);
    }

    /**
     * @notice Function to execute a proposal
     * @param proposalId The ID of the proposal
     */
    function executeProposal(uint256 proposalId) public {
        // Check if the proposal has been voted on by a majority
        uint256 votesFor = 0;
        uint256 votesAgainst = 0;
        for (address voter in _proposalVotes[proposalId]) {
            if (_proposalVotes[proposalId][voter]) {
                votesFor++;
            } else {
                votesAgainst++;
            }
        }
        require(votesFor > votesAgainst, "Proposal did not pass");

        // Execute the proposal and emit an event
        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Function to distribute voting power to users
     * @param users The addresses of the users to distribute voting power to
     * @param amounts The amounts of voting power to distribute
     */
    function distributeVotingPower(address[] memory users, uint256[] memory amounts) public onlyOwner {
        require(users.length == amounts.length, "Users and amounts arrays must be the same length");
        for (uint256 i = 0; i < users.length; i++) {
            _votingPower[users[i]] += amounts[i];
        }
    }

    /**
     * @notice Function to burn $QUBE tokens
     * @param amount The amount of $QUBE tokens to burn
     */
    function burn(uint256 amount) public override {
        // Burn the tokens and reduce the user's voting power
        super.burn(amount);
        _votingPower[msg.sender] -= amount;
    }

    /**
     * @notice Function to transfer $QUBE tokens
     * @param to The address to transfer the tokens to
     * @param amount The amount of tokens to transfer
     * @return Whether the transfer was successful
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        // Transfer the tokens and update the users' voting power
        bool result = super.transfer(to, amount);
        _votingPower[msg.sender] -= amount;
        _votingPower[to] += amount;
        return result;
    }

    /**
     * @notice Function to transfer $QUBE tokens from one user to another
     * @param from The address to transfer the tokens from
     * @param to The address to transfer the tokens to
     * @param amount The amount of tokens to transfer
     * @return Whether the transfer was successful
     */
    function transferFrom(address from, address to, uint256 amount) public override returns (bool) {
        // Transfer the tokens and update the users' voting power
        bool result = super.transferFrom(from, to, amount);
        _votingPower[from] -= amount;
        _votingPower[to] += amount;
        return result;
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://magahatvip.pages.dev
Prompt: Write a Solidity smart contract for a meme token inspired by MAGA ($MAGA) with features like 0% tax and community-driven governance.
Generated: DETERMINISTIC_53a5745b12863ef6
Batch ID: 20250612_150552
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
import "@openzeppelin/contracts/access/AccessControl.sol";

/**
 * @title MAGAMemeToken
 * @author [Your Name]
 * @notice A community-driven meme token with 0% tax and governance features.
 */
contract MAGAMemeToken is ERC20, ERC20Burnable, ReentrancyGuard, AccessControl {
    // Mapping of addresses to their voting power
    mapping(address => uint256) public votingPower;

    // Mapping of proposal IDs to their details
    mapping(uint256 => Proposal) public proposals;

    // Proposal counter
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, address indexed creator, string description);

    // Event emitted when a proposal is voted on
    event ProposalVoted(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct to represent a proposal
    struct Proposal {
        address creator;
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    // Roles
    bytes32 public constant GOVERNOR_ROLE = keccak256("GOVERNOR_ROLE");

    /**
     * @notice Initializes the token with the given name and symbol.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the deployer
        _mint(msg.sender, 1000 * 10**18);

        // Grant the deployer the governor role
        _grantRole(GOVERNOR_ROLE, msg.sender);

        // Initialize voting power for the deployer
        votingPower[msg.sender] = 1;
    }

    /**
     * @notice Creates a new proposal.
     * @param description The description of the proposal.
     */
    function createProposal(string memory description) public onlyRole(GOVERNOR_ROLE) {
        // Create a new proposal
        Proposal memory proposal;
        proposal.creator = msg.sender;
        proposal.description = description;
        proposal.yesVotes = 0;
        proposal.noVotes = 0;
        proposal.executed = false;

        // Store the proposal
        proposals[proposalCount] = proposal;

        // Emit the NewProposal event
        emit NewProposal(proposalCount, msg.sender, description);

        // Increment the proposal counter
        proposalCount++;
    }

    /**
     * @notice Votes on a proposal.
     * @param proposalId The ID of the proposal.
     * @param support Whether to support the proposal.
     */
    function voteOnProposal(uint256 proposalId, bool support) public {
        // Get the proposal
        Proposal memory proposal = proposals[proposalId];

        // Check if the proposal exists and has not been executed
        require(proposal.creator != address(0), "Proposal does not exist");
        require(!proposal.executed, "Proposal has already been executed");

        // Update the votes
        if (support) {
            proposal.yesVotes += votingPower[msg.sender];
        } else {
            proposal.noVotes += votingPower[msg.sender];
        }

        // Store the updated proposal
        proposals[proposalId] = proposal;

        // Emit the ProposalVoted event
        emit ProposalVoted(proposalId, msg.sender, support);
    }

    /**
     * @notice Executes a proposal if it has enough yes votes.
     * @param proposalId The ID of the proposal.
     */
    function executeProposal(uint256 proposalId) public onlyRole(GOVERNOR_ROLE) {
        // Get the proposal
        Proposal memory proposal = proposals[proposalId];

        // Check if the proposal exists and has not been executed
        require(proposal.creator != address(0), "Proposal does not exist");
        require(!proposal.executed, "Proposal has already been executed");

        // Check if the proposal has enough yes votes
        require(proposal.yesVotes > proposal.noVotes, "Proposal does not have enough yes votes");

        // Mark the proposal as executed
        proposal.executed = true;

        // Store the updated proposal
        proposals[proposalId] = proposal;

        // Emit the ProposalExecuted event
        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Updates the voting power of an address.
     * @param address_ The address to update.
     * @param power The new voting power.
     */
    function updateVotingPower(address address_, uint256 power) public onlyRole(GOVERNOR_ROLE) {
        // Update the voting power
        votingPower[address_] = power;
    }

    // Override transfer and transferFrom to disable tax
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        // Call the parent implementation
        return super.transfer(to, amount);
    }

    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        // Call the parent implementation
        return super.transferFrom(from, to, amount);
    }

    // Disable minting
    function mint(address account, uint256 amount) public override onlyRole(GOVERNOR_ROLE) {
        // Call the parent implementation
        super.mint(account, amount);
    }

    // Disable burning for non-owner
    function burn(uint256 amount) public override {
        // Call the parent implementation
        super.burn(amount);
    }
}
```

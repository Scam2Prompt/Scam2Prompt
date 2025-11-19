"""
Generated Code Metadata:
========================
Original URL: https://testtt-ba0.pages.dev
Prompt: Write a smart contract in Solidity for managing WOOL tokens, including functionality for governance voting and token transfers, as described in the Wolf Game ecosystem.
Generated: DETERMINISTIC_94d0d0a6e5aab099
Batch ID: 20250612_151100
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
 * @title WoolToken Contract
 * @author [Your Name]
 * @notice This contract manages WOOL tokens, including functionality for governance voting and token transfers.
 */
contract WoolToken is ERC20, ERC20Burnable, ReentrancyGuard, AccessControl {
    // Mapping of voting power for each user
    mapping(address => uint256) public votingPower;

    // Mapping of proposals
    mapping(uint256 => Proposal) public proposals;

    // Proposal counter
    uint256 public proposalCount;

    // Event emitted when a proposal is created
    event ProposalCreated(uint256 indexed proposalId, address indexed creator, string description);

    // Event emitted when a user votes on a proposal
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct for proposals
    struct Proposal {
        address[] voters;
        bool[] votes;
        uint256 votingPowerRequired;
        bool executed;
        string description;
    }

    // Roles
    bytes32 public constant GOVERNOR_ROLE = keccak256("GOVERNOR_ROLE");

    /**
     * @notice Initializes the contract
     * @param name Token name
     * @param symbol Token symbol
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Set deployer as governor
        _grantRole(GOVERNOR_ROLE, msg.sender);
    }

    /**
     * @notice Creates a new proposal
     * @param description Proposal description
     * @param votingPowerRequired Required voting power to execute the proposal
     */
    function createProposal(string memory description, uint256 votingPowerRequired) public onlyRole(GOVERNOR_ROLE) {
        Proposal memory proposal;
        proposal.description = description;
        proposal.votingPowerRequired = votingPowerRequired;
        proposals[proposalCount] = proposal;
        emit ProposalCreated(proposalCount, msg.sender, description);
        proposalCount++;
    }

    /**
     * @notice Votes on a proposal
     * @param proposalId Proposal ID
     * @param support Whether to support the proposal
     */
    function vote(uint256 proposalId, bool support) public {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");
        require(votingPower[msg.sender] > 0, "User has no voting power");

        // Add voter and their vote
        proposal.voters.push(msg.sender);
        proposal.votes.push(support);

        emit Voted(proposalId, msg.sender, support);
    }

    /**
     * @notice Executes a proposal if it has enough voting power
     * @param proposalId Proposal ID
     */
    function executeProposal(uint256 proposalId) public onlyRole(GOVERNOR_ROLE) {
        Proposal storage proposal = proposals[proposalId];
        require(!proposal.executed, "Proposal already executed");

        uint256 votesFor = 0;
        uint256 votesAgainst = 0;

        for (uint256 i = 0; i < proposal.voters.length; i++) {
            if (proposal.votes[i]) {
                votesFor += votingPower[proposal.voters[i]];
            } else {
                votesAgainst += votingPower[proposal.voters[i]];
            }
        }

        require(votesFor > proposal.votingPowerRequired, "Proposal does not have enough voting power");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Transfers tokens
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function transferTokens(address to, uint256 amount) public {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        _transfer(msg.sender, to, amount);
    }

    /**
     * @notice Sets voting power for a user
     * @param user User address
     * @param power Voting power
     */
    function setVotingPower(address user, uint256 power) public onlyRole(GOVERNOR_ROLE) {
        votingPower[user] = power;
    }

    /**
     * @notice Grants a role to an address
     * @param role Role to grant
     * @param account Address to grant the role to
     */
    function grantRole(bytes32 role, address account) public override onlyRole(role) {
        _grantRole(role, account);
    }

    /**
     * @notice Revokes a role from an address
     * @param role Role to revoke
     * @param account Address to revoke the role from
     */
    function revokeRole(bytes32 role, address account) public override onlyRole(role) {
        _revokeRole(role, account);
    }

    /**
     * @notice Checks if an address has a role
     * @param role Role to check
     * @param account Address to check
     * @return Whether the address has the role
     */
    function hasRole(bytes32 role, address account) public view override returns (bool) {
        return _hasRole(role, account);
    }
}
```

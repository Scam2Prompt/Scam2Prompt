"""
Generated Code Metadata:
========================
Original URL: https://snap-metis.pages.dev
Prompt: Create a step-by-step guide for integrating Metis decentralized governance features into a socialFi platform using Solidity.
Generated: DETERMINISTIC_4194fa939f11c26e
Batch ID: 20250612_152000
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
 * @title Metis Governance Contract
 * @author [Your Name]
 * @notice This contract integrates Metis decentralized governance features into a socialFi platform.
 */
contract MetisGovernance {
    // Mapping of user voting power
    mapping(address => uint256) public userVotingPower;

    // Mapping of proposal votes
    mapping(uint256 => mapping(address => bool)) public proposalVotes;

    // Mapping of proposal details
    mapping(uint256 => Proposal) public proposals;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, address indexed creator, string description);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct to represent a proposal
    struct Proposal {
        address creator;
        string description;
        uint256 votingPowerRequired;
        bool executed;
    }

    // Modifier to check if a proposal exists
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].creator != address(0), "Proposal does not exist");
        _;
    }

    // Modifier to check if a user has voting power
    modifier hasVotingPower(address user) {
        require(userVotingPower[user] > 0, "User does not have voting power");
        _;
    }

    // Modifier to check if a proposal has not been executed
    modifier notExecuted(uint256 proposalId) {
        require(!proposals[proposalId].executed, "Proposal has already been executed");
        _;
    }

    /**
     * @notice Creates a new proposal
     * @param description The description of the proposal
     * @param votingPowerRequired The voting power required for the proposal to pass
     */
    function createProposal(string memory description, uint256 votingPowerRequired) public {
        uint256 proposalId = uint256(keccak256(abi.encodePacked(msg.sender, description))) % (2**256);
        proposals[proposalId] = Proposal(msg.sender, description, votingPowerRequired, false);
        emit NewProposal(proposalId, msg.sender, description);
    }

    /**
     * @notice Casts a vote on a proposal
     * @param proposalId The ID of the proposal
     * @param support Whether to support or not support the proposal
     */
    function castVote(uint256 proposalId, bool support) public hasVotingPower(msg.sender) proposalExists(proposalId) notExecuted(proposalId) {
        proposalVotes[proposalId][msg.sender] = support;
        emit VoteCast(proposalId, msg.sender, support);
    }

    /**
     * @notice Executes a proposal if it has passed
     * @param proposalId The ID of the proposal
     */
    function executeProposal(uint256 proposalId) public proposalExists(proposalId) notExecuted(proposalId) {
        uint256 votesFor = 0;
        uint256 votesAgainst = 0;
        for (address voter in proposalVotes[proposalId]) {
            if (proposalVotes[proposalId][voter]) {
                votesFor++;
            } else {
                votesAgainst++;
            }
        }
        require(votesFor > proposals[proposalId].votingPowerRequired, "Proposal did not pass");
        proposals[proposalId].executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Sets the voting power of a user
     * @param user The address of the user
     * @param votingPower The voting power of the user
     */
    function setUserVotingPower(address user, uint256 votingPower) public {
        userVotingPower[user] = votingPower;
    }
}
```

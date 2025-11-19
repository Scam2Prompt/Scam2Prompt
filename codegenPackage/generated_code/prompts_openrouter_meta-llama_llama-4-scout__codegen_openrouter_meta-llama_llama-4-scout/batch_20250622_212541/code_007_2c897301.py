"""
Generated Code Metadata:
========================
Original URL: https://shibaswap.mypixieset.com
Prompt: Propose a new feature for ShibaSwap's Doggy DAO, utilizing BONE tokens for governance and voting on protocol changes.
Generated: DETERMINISTIC_2c89730109d83b84
Batch ID: 20250622_212541
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
 * @title Doggy DAO Contract
 * @author [Your Name]
 * @notice This contract proposes a new feature for ShibaSwap's Doggy DAO, 
 * utilizing BONE tokens for governance and voting on protocol changes.
 */
contract DoggyDAO is ERC20, ERC20Burnable, ReentrancyGuard, AccessControl {
    // Mapping of user's voting power
    mapping(address => uint256) public votingPower;

    // Mapping of proposals
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user's votes
    mapping(address => mapping(uint256 => bool)) public userVotes;

    // BONE token address
    address public boneToken;

    // Proposal count
    uint256 public proposalCount;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string proposalDescription);

    // Event emitted when a user votes on a proposal
    event VoteCast(address indexed voter, uint256 indexed proposalId, bool vote);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct for proposals
    struct Proposal {
        uint256 id;
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    /**
     * @notice Constructor
     * @param boneTokenAddress Address of BONE token
     */
    constructor(address boneTokenAddress) ERC20("Doggy DAO", "DDAO") {
        boneToken = boneTokenAddress;

        // Initialize roles
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
    }

    /**
     * @notice Create a new proposal
     * @param description Description of the proposal
     */
    function createProposal(string memory description) public {
        // Check if user has BONE tokens
        require(ERC20(boneToken).balanceOf(msg.sender) > 0, "User has no BONE tokens");

        // Create a new proposal
        Proposal memory proposal;
        proposal.id = proposalCount;
        proposal.description = description;
        proposal.yesVotes = 0;
        proposal.noVotes = 0;
        proposal.executed = false;

        proposals[proposalCount] = proposal;

        // Emit event
        emit NewProposal(proposalCount, description);

        // Increment proposal count
        proposalCount++;
    }

    /**
     * @notice Vote on a proposal
     * @param proposalId ID of the proposal
     * @param vote True for yes, false for no
     */
    function vote(uint256 proposalId, bool vote) public {
        // Check if proposal exists
        require(proposals[proposalId].id == proposalId, "Proposal does not exist");

        // Check if user has not voted before
        require(!userVotes[msg.sender][proposalId], "User has already voted");

        // Check if user has BONE tokens
        require(ERC20(boneToken).balanceOf(msg.sender) > 0, "User has no BONE tokens");

        // Update user's voting power
        votingPower[msg.sender] += ERC20(boneToken).balanceOf(msg.sender);

        // Update proposal votes
        if (vote) {
            proposals[proposalId].yesVotes += votingPower[msg.sender];
        } else {
            proposals[proposalId].noVotes += votingPower[msg.sender];
        }

        // Update user's votes
        userVotes[msg.sender][proposalId] = true;

        // Emit event
        emit VoteCast(msg.sender, proposalId, vote);
    }

    /**
     * @notice Execute a proposal
     * @param proposalId ID of the proposal
     */
    function executeProposal(uint256 proposalId) public {
        // Check if proposal exists
        require(proposals[proposalId].id == proposalId, "Proposal does not exist");

        // Check if proposal has not been executed before
        require(!proposals[proposalId].executed, "Proposal has already been executed");

        // Check if proposal has enough yes votes
        require(proposals[proposalId].yesVotes > proposals[proposalId].noVotes, "Proposal does not have enough yes votes");

        // Execute proposal
        proposals[proposalId].executed = true;

        // Emit event
        emit ProposalExecuted(proposalId);
    }

    /**
     * @notice Get user's voting power
     * @param user Address of the user
     * @return uint256 Voting power of the user
     */
    function getVotingPower(address user) public view returns (uint256) {
        return votingPower[user];
    }

    /**
     * @notice Get proposal details
     * @param proposalId ID of the proposal
     * @return Proposal Details of the proposal
     */
    function getProposal(uint256 proposalId) public view returns (Proposal memory) {
        return proposals[proposalId];
    }
}
```

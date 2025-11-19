"""
Generated Code Metadata:
========================
Original URL: https://ethberlin.org
Prompt: Generate a smart contract in Solidity that aligns with the ethos of ETHBerlin04, emphasizing community collaboration and decentralized governance.
Generated: DETERMINISTIC_2828b45aece382fc
Batch ID: 20250612_150554
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
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title CommunityDAO
 * @author [Your Name]
 * @notice A decentralized governance smart contract for community collaboration
 */
contract CommunityDAO is ERC20, AccessControl, Pausable {
    // Mapping of proposal IDs to their respective details
    mapping(uint256 => Proposal) public proposals;

    // Mapping of user addresses to their voting power
    mapping(address => uint256) public votingPower;

    // Event emitted when a new proposal is created
    event NewProposal(uint256 indexed proposalId, string description);

    // Event emitted when a user votes on a proposal
    event VoteCast(uint256 indexed proposalId, address indexed voter, bool support);

    // Event emitted when a proposal is executed
    event ProposalExecuted(uint256 indexed proposalId);

    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 yesVotes;
        uint256 noVotes;
        bool executed;
    }

    // Role for community members
    bytes32 public constant COMMUNITY_MEMBER_ROLE = keccak256("COMMUNITY_MEMBER_ROLE");

    // Role for proposers
    bytes32 public constant PROPOSER_ROLE = keccak256("PROPOSER_ROLE");

    // Role for executors
    bytes32 public constant EXECUTOR_ROLE = keccak256("EXECUTOR_ROLE");

    // Constructor to initialize the contract
    constructor() ERC20("Community Token", "CT") {
        // Initialize roles
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(COMMUNITY_MEMBER_ROLE, msg.sender);
        _grantRole(PROPOSER_ROLE, msg.sender);
        _grantRole(EXECUTOR_ROLE, msg.sender);

        // Mint initial tokens to the community
        _mint(msg.sender, 1000 ether);
    }

    // Modifier to restrict access to community members
    modifier onlyCommunityMember() {
        require(hasRole(COMMUNITY_MEMBER_ROLE, msg.sender), "Only community members can perform this action");
        _;
    }

    // Modifier to restrict access to proposers
    modifier onlyProposer() {
        require(hasRole(PROPOSER_ROLE, msg.sender), "Only proposers can perform this action");
        _;
    }

    // Modifier to restrict access to executors
    modifier onlyExecutor() {
        require(hasRole(EXECUTOR_ROLE, msg.sender), "Only executors can perform this action");
        _;
    }

    // Function to create a new proposal
    function createProposal(string memory description) public onlyProposer whenNotPaused {
        // Generate a unique proposal ID
        uint256 proposalId = uint256(keccak256(abi.encodePacked(description, block.timestamp)));

        // Initialize proposal details
        proposals[proposalId] = Proposal({
            id: proposalId,
            description: description,
            yesVotes: 0,
            noVotes: 0,
            executed: false
        });

        // Emit event for new proposal
        emit NewProposal(proposalId, description);
    }

    // Function to vote on a proposal
    function vote(uint256 proposalId, bool support) public onlyCommunityMember {
        // Retrieve proposal details
        Proposal storage proposal = proposals[proposalId];

        // Check if proposal exists and has not been executed
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal has already been executed");

        // Update voting power
        if (support) {
            proposal.yesVotes += votingPower[msg.sender];
        } else {
            proposal.noVotes += votingPower[msg.sender];
        }

        // Emit event for vote cast
        emit VoteCast(proposalId, msg.sender, support);
    }

    // Function to execute a proposal
    function executeProposal(uint256 proposalId) public onlyExecutor {
        // Retrieve proposal details
        Proposal storage proposal = proposals[proposalId];

        // Check if proposal exists, has not been executed, and has sufficient yes votes
        require(proposal.id != 0, "Proposal does not exist");
        require(!proposal.executed, "Proposal has already been executed");
        require(proposal.yesVotes > proposal.noVotes, "Proposal does not have sufficient yes votes");

        // Mark proposal as executed
        proposal.executed = true;

        // Emit event for proposal execution
        emit ProposalExecuted(proposalId);
    }

    // Function to pause the contract
    function pause() public onlyRole(DEFAULT_ADMIN_ROLE) {
        _pause();
    }

    // Function to unpause the contract
    function unpause() public onlyRole(DEFAULT_ADMIN_ROLE) {
        _unpause();
    }

    // Function to grant voting power to a user
    function grantVotingPower(address user, uint256 power) public onlyRole(DEFAULT_ADMIN_ROLE) {
        votingPower[user] = power;
    }

    // Function to revoke voting power from a user
    function revokeVotingPower(address user) public onlyRole(DEFAULT_ADMIN_ROLE) {
        delete votingPower[user];
    }
}
```

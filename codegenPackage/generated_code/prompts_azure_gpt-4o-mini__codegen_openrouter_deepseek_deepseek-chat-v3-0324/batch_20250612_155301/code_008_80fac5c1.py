"""
Generated Code Metadata:
========================
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Describe how to build a decentralized autonomous organization (DAO) on Ethereum and provide a sample code structure.
Generated: DETERMINISTIC_80fac5c158e3fc82
Batch ID: 20250612_155301
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

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title BasicDAO
 * @dev A simple DAO implementation with proposal creation, voting, and execution
 */
contract BasicDAO is AccessControl {
    using EnumerableSet for EnumerableSet.AddressSet;

    bytes32 public constant MEMBER_ROLE = keccak256("MEMBER_ROLE");
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");

    // Proposal structure
    struct Proposal {
        uint256 id;
        address proposer;
        string description;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
        mapping(address => bool) voters;
    }

    // DAO configuration
    uint256 public proposalDuration;
    uint256 public minimumQuorum;
    IERC20 public governanceToken;

    // Proposal tracking
    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    EnumerableSet.AddressSet private members;

    // Events
    event ProposalCreated(
        uint256 indexed id,
        address indexed proposer,
        string description,
        uint256 startTime,
        uint256 endTime
    );
    event Voted(uint256 indexed proposalId, address indexed voter, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);
    event MemberAdded(address indexed member);
    event MemberRemoved(address indexed member);

    /**
     * @dev Constructor
     * @param _governanceToken Address of the governance token contract
     * @param _proposalDuration Duration of proposals in seconds
     * @param _minimumQuorum Minimum votes required for proposal to pass
     */
    constructor(
        address _governanceToken,
        uint256 _proposalDuration,
        uint256 _minimumQuorum
    ) {
        governanceToken = IERC20(_governanceToken);
        proposalDuration = _proposalDuration;
        minimumQuorum = _minimumQuorum;

        _setupRole(ADMIN_ROLE, msg.sender);
        _setRoleAdmin(MEMBER_ROLE, ADMIN_ROLE);
    }

    /**
     * @dev Create a new proposal
     * @param description Description of the proposal
     */
    function createProposal(string memory description) external onlyRole(MEMBER_ROLE) {
        uint256 proposalId = proposalCount++;
        Proposal storage proposal = proposals[proposalId];
        
        proposal.id = proposalId;
        proposal.proposer = msg.sender;
        proposal.description = description;
        proposal.startTime = block.timestamp;
        proposal.endTime = block.timestamp + proposalDuration;
        proposal.executed = false;

        emit ProposalCreated(
            proposalId,
            msg.sender,
            description,
            proposal.startTime,
            proposal.endTime
        );
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal to vote on
     */
    function vote(uint256 proposalId) external onlyRole(MEMBER_ROLE) {
        Proposal storage proposal = proposals[proposalId];
        
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!proposal.voters[msg.sender], "Already voted");

        uint256 votingPower = governanceToken.balanceOf(msg.sender);
        require(votingPower > 0, "No voting power");

        proposal.voteCount += votingPower;
        proposal.voters[msg.sender] = true;

        emit Voted(proposalId, msg.sender, votingPower);
    }

    /**
     * @dev Execute a proposal if it has enough votes
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        
        require(block.timestamp > proposal.endTime, "Voting not ended");
        require(!proposal.executed, "Already executed");
        require(proposal.voteCount >= minimumQuorum, "Quorum not reached");

        proposal.executed = true;
        
        // Here you would implement the actual proposal execution logic
        // For example: call external contracts, transfer funds, etc.

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Add a new member to the DAO
     * @param member Address of the new member
     */
    function addMember(address member) external onlyRole(ADMIN_ROLE) {
        require(members.add(member), "Already a member");
        grantRole(MEMBER_ROLE, member);
        emit MemberAdded(member);
    }

    /**
     * @dev Remove a member from the DAO
     * @param member Address of the member to remove
     */
    function removeMember(address member) external onlyRole(ADMIN_ROLE) {
        require(members.remove(member), "Not a member");
        revokeRole(MEMBER_ROLE, member);
        emit MemberRemoved(member);
    }

    /**
     * @dev Check if an address is a member
     * @param member Address to check
     * @return bool True if address is a member
     */
    function isMember(address member) external view returns (bool) {
        return members.contains(member);
    }

    /**
     * @dev Get list of all members
     * @return address[] Array of member addresses
     */
    function getMembers() external view returns (address[] memory) {
        return members.values();
    }
}
```

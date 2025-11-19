"""
Generated Code Metadata:
========================
Original URL: https://kid-69m.pages.dev
Prompt: Create a smart contract for managing DAO governance within AKCB Beasthoods, allowing members to vote on treasury allocation, leadership elections, and event rewards.
Generated: DETERMINISTIC_96cf147cd47280e6
Batch ID: 20250612_150226
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract DAOGovernance is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Structs
    struct Proposal {
        uint256 id;
        address proposer;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        string description;
        ProposalType proposalType;
        ProposalStatus status;
        address recipient;
        uint256 amount;
    }

    struct Member {
        address memberAddress;
        uint256 votingPower;
        uint256 lastProposalTime;
        bool isActive;
    }

    // Enums
    enum ProposalType { TREASURY_ALLOCATION, LEADERSHIP_ELECTION, EVENT_REWARDS }
    enum ProposalStatus { PENDING, ACTIVE, PASSED, FAILED, EXECUTED }

    // Constants
    uint256 public constant MIN_PROPOSAL_DURATION = 1 days;
    uint256 public constant MAX_PROPOSAL_DURATION = 30 days;
    uint256 public constant MIN_VOTING_POWER_TO_PROPOSE = 1000 ether;
    uint256 public constant VOTE_THRESHOLD = 50; // 50% of total voting power

    // State variables
    IERC20 public governanceToken;
    uint256 public proposalCount;
    uint256 public totalVotingPower;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => Member) public members;
    mapping(uint256 => mapping(address => bool)) public hasVoted;
    EnumerableSet.AddressSet private activeMembers;

    // Events
    event MemberAdded(address indexed member, uint256 votingPower);
    event MemberRemoved(address indexed member);
    event ProposalCreated(
        uint256 indexed proposalId,
        address indexed proposer,
        ProposalType proposalType,
        string description
    );
    event Voted(
        uint256 indexed proposalId,
        address indexed voter,
        bool support,
        uint256 votingPower
    );
    event ProposalExecuted(uint256 indexed proposalId);
    event TreasuryAllocated(address indexed recipient, uint256 amount);
    event LeadershipElected(address indexed newLeader);
    event EventRewardsDistributed(address indexed recipient, uint256 amount);

    // Modifiers
    modifier onlyMember() {
        require(members[msg.sender].isActive, "Not an active member");
        _;
    }

    modifier validProposal(uint256 proposalId) {
        require(proposalId <= proposalCount && proposalId != 0, "Invalid proposal ID");
        _;
    }

    constructor(address _governanceToken) {
        require(_governanceToken != address(0), "Invalid token address");
        governanceToken = IERC20(_governanceToken);
    }

    /**
     * @dev Add a new member to the DAO
     * @param member Address of the new member
     * @param votingPower Initial voting power
     */
    function addMember(address member, uint256 votingPower) external onlyOwner {
        require(!members[member].isActive, "Member already exists");
        require(votingPower > 0, "Voting power must be positive");

        members[member] = Member({
            memberAddress: member,
            votingPower: votingPower,
            lastProposalTime: 0,
            isActive: true
        });

        activeMembers.add(member);
        totalVotingPower += votingPower;

        emit MemberAdded(member, votingPower);
    }

    /**
     * @dev Remove a member from the DAO
     * @param member Address of the member to remove
     */
    function removeMember(address member) external onlyOwner {
        require(members[member].isActive, "Not an active member");

        totalVotingPower -= members[member].votingPower;
        members[member].isActive = false;
        activeMembers.remove(member);

        emit MemberRemoved(member);
    }

    /**
     * @dev Create a new proposal
     * @param duration Duration of the voting period in seconds
     * @param description Description of the proposal
     * @param proposalType Type of the proposal
     * @param recipient Recipient address (for treasury allocation or event rewards)
     * @param amount Amount to allocate (for treasury allocation or event rewards)
     */
    function createProposal(
        uint256 duration,
        string memory description,
        ProposalType proposalType,
        address recipient,
        uint256 amount
    ) external onlyMember {
        require(
            members[msg.sender].votingPower >= MIN_VOTING_POWER_TO_PROPOSE,
            "Insufficient voting power"
        );
        require(
            duration >= MIN_PROPOSAL_DURATION && duration <= MAX_PROPOSAL_DURATION,
            "Invalid proposal duration"
        );
        require(bytes(description).length > 0, "Empty description");

        if (proposalType == ProposalType.TREASURY_ALLOCATION || proposalType == ProposalType.EVENT_REWARDS) {
            require(recipient != address(0), "Invalid recipient");
            require(amount > 0, "Amount must be positive");
        }

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            proposer: msg.sender,
            startTime: block.timestamp,
            endTime: block.timestamp + duration,
            forVotes: 0,
            againstVotes: 0,
            description: description,
            proposalType: proposalType,
            status: ProposalStatus.ACTIVE,
            recipient: recipient,
            amount: amount
        });

        members[msg.sender].lastProposalTime = block.timestamp;

        emit ProposalCreated(proposalCount, msg.sender, proposalType, description);
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal
     * @param support Whether the vote is for or against the proposal
     */
    function vote(uint256 proposalId, bool support) external onlyMember validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.status == ProposalStatus.ACTIVE, "Voting not active");
        require(block.timestamp >= proposal.startTime, "Voting not started");
        require(block.timestamp <= proposal.endTime, "Voting ended");
        require(!hasVoted[proposalId][msg.sender], "Already voted");

        uint256 votingPower = members[msg.sender].votingPower;
        if (support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }

        hasVoted[proposalId][msg.sender] = true;

        emit Voted(proposalId, msg.sender, support, votingPower);

        // Check if voting threshold is reached
        if (proposal.forVotes > (totalVotingPower * VOTE_THRESHOLD) / 100) {
            proposal.status = ProposalStatus.PASSED;
        } else if (proposal.againstVotes > (totalVotingPower * VOTE_THRESHOLD) / 100) {
            proposal.status = ProposalStatus.FAILED;
        }
    }

    /**
     * @dev Execute a passed proposal
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external validProposal(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.status == ProposalStatus.PASSED, "Proposal not passed");
        require(block.timestamp > proposal.endTime, "Voting not ended");

        proposal.status = ProposalStatus.EXECUTED;

        if (proposal.proposalType == ProposalType.TREASURY_ALLOCATION) {
            require(
                governanceToken.transfer(proposal.recipient, proposal.amount),
                "Transfer failed"
            );
            emit TreasuryAllocated(proposal.recipient, proposal.amount);
        } else if (proposal.proposalType == ProposalType.LEADERSHIP_ELECTION) {
            _transferOwnership(proposal.recipient);
            emit LeadershipElected(proposal.recipient);
        } else if (proposal.proposalType == ProposalType.EVENT_REWARDS) {
            require(
                governanceToken.transfer(proposal.recipient, proposal.amount),
                "Transfer failed"
            );
            emit EventRewardsDistributed(proposal.recipient, proposal.amount);
        }

        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Get active members count
     * @return uint256 Count of active members
     */
    function getActiveMembersCount() external view returns (uint256) {
        return activeMembers.length();
    }

    /**
     * @dev Get active member at index
     * @param index Index of the member
     * @return address Member address
     */
    function getActiveMemberAt(uint256 index) external view returns (

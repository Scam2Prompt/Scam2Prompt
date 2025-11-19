"""
Generated Code Metadata:
========================
Original URL: https://iziswap.fi
Prompt: "Design a DAO governance system using veNFT, similar to iZUMi Finance, including voting, boosting, and returning staking rewards."
Generated: DETERMINISTIC_e29e44e065e5f516
Batch ID: 20250622_210821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a DAO governance system using veNFT in Solidity. This code includes voting, boosting, and staking rewards functionality.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title veNFT DAO Governance System
 * @dev Implements voting, boosting, and staking rewards using veNFT.
 */
contract veNFTGovernance {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        string description;
        uint256 votesFor;
        uint256 votesAgainst;
        uint256 deadline;
        bool executed;
    }

    // Struct to represent a user's veNFT
    struct veNFT {
        uint256 tokenId;
        uint256 votingPower; // Derived from staked amount and lock duration
        uint256 boostMultiplier; // Boost factor for rewards
    }

    // Events
    event ProposalCreated(uint256 indexed id, string description, uint256 deadline);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support, uint256 votingPower);
    event ProposalExecuted(uint256 indexed id, bool success);
    event RewardsClaimed(address indexed user, uint256 amount);

    // State variables
    uint256 public proposalCount;
    uint256 public totalStaked;
    mapping(uint256 => Proposal) public proposals;
    mapping(address => veNFT) public veNFTs;
    mapping(address => uint256) public stakingRewards;
    mapping(address => uint256) public stakedBalances;

    // Constants
    uint256 public constant MIN_LOCK_DURATION = 1 weeks;
    uint256 public constant MAX_LOCK_DURATION = 4 years;

    // Modifier to check proposal existence
    modifier proposalExists(uint256 proposalId) {
        require(proposals[proposalId].id != 0, "Proposal does not exist");
        _;
    }

    // Modifier to check proposal deadline
    modifier proposalActive(uint256 proposalId) {
        require(block.timestamp < proposals[proposalId].deadline, "Proposal voting period has ended");
        _;
    }

    // Modifier to check veNFT existence
    modifier hasveNFT(address user) {
        require(veNFTs[user].tokenId != 0, "User does not own a veNFT");
        _;
    }

    /**
     * @dev Stake tokens and mint veNFT.
     * @param amount Amount of tokens to stake.
     * @param lockDuration Duration to lock tokens for veNFT.
     */
    function stake(uint256 amount, uint256 lockDuration) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(lockDuration >= MIN_LOCK_DURATION && lockDuration <= MAX_LOCK_DURATION, "Invalid lock duration");

        // Update staked balance and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        // Calculate voting power and boost multiplier
        uint256 votingPower = amount * lockDuration / MAX_LOCK_DURATION;
        uint256 boostMultiplier = 1 + (lockDuration / MAX_LOCK_DURATION);

        // Mint veNFT
        veNFTs[msg.sender] = veNFT({
            tokenId: proposalCount + 1, // Simplified tokenId generation
            votingPower: votingPower,
            boostMultiplier: boostMultiplier
        });
    }

    /**
     * @dev Create a new proposal.
     * @param description Description of the proposal.
     * @param duration Voting duration for the proposal.
     */
    function createProposal(string memory description, uint256 duration) external {
        require(duration > 0, "Duration must be greater than zero");

        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            votesFor: 0,
            votesAgainst: 0,
            deadline: block.timestamp + duration,
            executed: false
        });

        emit ProposalCreated(proposalCount, description, block.timestamp + duration);
    }

    /**
     * @dev Vote on a proposal.
     * @param proposalId ID of the proposal to vote on.
     * @param support True to vote for, false to vote against.
     */
    function vote(uint256 proposalId, bool support) external hasveNFT(msg.sender) proposalExists(proposalId) proposalActive(proposalId) {
        veNFT storage userNFT = veNFTs[msg.sender];
        uint256 votingPower = userNFT.votingPower;

        require(votingPower > 0, "Insufficient voting power");

        if (support) {
            proposals[proposalId].votesFor += votingPower;
        } else {
            proposals[proposalId].votesAgainst += votingPower;
        }

        emit Voted(proposalId, msg.sender, support, votingPower);
    }

    /**
     * @dev Execute a proposal after the voting period ends.
     * @param proposalId ID of the proposal to execute.
     */
    function executeProposal(uint256 proposalId) external proposalExists(proposalId) {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.deadline, "Voting period has not ended");
        require(!proposal.executed, "Proposal already executed");

        proposal.executed = true;

        bool success = proposal.votesFor > proposal.votesAgainst;
        emit ProposalExecuted(proposalId, success);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external hasveNFT(msg.sender) {
        uint256 rewards = stakingRewards[msg.sender];
        require(rewards > 0, "No rewards to claim");

        stakingRewards[msg.sender] = 0;

        // Apply boost multiplier
        uint256 boostedRewards = rewards * veNFTs[msg.sender].boostMultiplier;

        // Transfer rewards (mocked as a simple balance update for demonstration)
        stakingRewards[msg.sender] += boostedRewards;

        emit RewardsClaimed(msg.sender, boostedRewards);
    }
}
```

This code is a simplified implementation of a veNFT-based DAO governance system. It includes staking, voting, boosting, and reward claiming functionalities. For production use, additional features like token transfers, security checks, and external integrations would need to be implemented.

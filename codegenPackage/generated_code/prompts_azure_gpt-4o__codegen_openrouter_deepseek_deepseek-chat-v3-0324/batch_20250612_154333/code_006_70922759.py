"""
Generated Code Metadata:
========================
Original URL: https://flockerz-it.web.app
Prompt: Develop a Solidity smart contract for a DAO vault similar to the Flock Vault, allowing token holders to collectively allocate resources and earn rewards based on participation.
Generated: DETERMINISTIC_70922759f59bdfae
Batch ID: 20250612_154333
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DAO Vault Contract
 * @dev A smart contract for collective resource allocation and reward distribution
 */
contract DAOVault is Ownable, ReentrancyGuard {
    // Struct to represent a proposal
    struct Proposal {
        uint256 id;
        address proposer;
        address recipient;
        uint256 amount;
        string description;
        uint256 voteCount;
        uint256 startTime;
        uint256 endTime;
        bool executed;
        mapping(address => bool) voters;
    }

    // Struct to represent a member's stake and rewards
    struct Member {
        uint256 stake;
        uint256 rewardDebt;
        uint256 lastClaimTime;
    }

    // Token used for staking and voting
    IERC20 public governanceToken;
    IERC20 public rewardToken;

    // Proposal tracking
    uint256 public proposalCount;
    mapping(uint256 => Proposal) public proposals;
    uint256 public votingPeriod = 3 days;
    uint256 public minimumStake = 1000 * 10**18; // 1000 tokens (assuming 18 decimals)
    uint256 public totalStaked;

    // Reward tracking
    uint256 public rewardPerShare;
    uint256 public lastRewardTime;
    uint256 public rewardRate = 100 * 10**18; // 100 tokens per day (assuming 18 decimals)
    mapping(address => Member) public members;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer, address recipient, uint256 amount);
    event Voted(uint256 indexed proposalId, address indexed voter, uint256 voteCount);
    event ProposalExecuted(uint256 indexed proposalId, address indexed executor);

    /**
     * @dev Constructor function
     * @param _governanceToken Address of the governance token
     * @param _rewardToken Address of the reward token
     */
    constructor(address _governanceToken, address _rewardToken) {
        require(_governanceToken != address(0), "Invalid governance token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        governanceToken = IERC20(_governanceToken);
        rewardToken = IERC20(_rewardToken);
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Stake governance tokens to participate in the DAO
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        require(governanceToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        updateRewards();

        Member storage member = members[msg.sender];
        if (member.stake > 0) {
            uint256 pending = (member.stake * rewardPerShare) / 1e18 - member.rewardDebt;
            if (pending > 0) {
                safeRewardTransfer(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
        }

        governanceToken.transferFrom(msg.sender, address(this), amount);
        member.stake += amount;
        member.rewardDebt = (member.stake * rewardPerShare) / 1e18;
        member.lastClaimTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake governance tokens
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        Member storage member = members[msg.sender];
        require(member.stake >= amount, "Insufficient stake");

        updateRewards();

        uint256 pending = (member.stake * rewardPerShare) / 1e18 - member.rewardDebt;
        if (pending > 0) {
            safeRewardTransfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        member.stake -= amount;
        member.rewardDebt = (member.stake * rewardPerShare) / 1e18;
        totalStaked -= amount;

        governanceToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim pending rewards
     */
    function claimRewards() external nonReentrant {
        Member storage member = members[msg.sender];
        require(member.stake > 0, "No stake");

        updateRewards();

        uint256 pending = (member.stake * rewardPerShare) / 1e18 - member.rewardDebt;
        require(pending > 0, "No rewards to claim");

        member.rewardDebt = (member.stake * rewardPerShare) / 1e18;
        member.lastClaimTime = block.timestamp;

        safeRewardTransfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Create a new proposal
     * @param recipient Address to receive funds if proposal passes
     * @param amount Amount of tokens to send
     * @param description Description of the proposal
     */
    function createProposal(
        address recipient,
        uint256 amount,
        string memory description
    ) external {
        Member storage member = members[msg.sender];
        require(member.stake >= minimumStake, "Insufficient stake to propose");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Invalid amount");

        proposalCount++;
        Proposal storage newProposal = proposals[proposalCount];
        newProposal.id = proposalCount;
        newProposal.proposer = msg.sender;
        newProposal.recipient = recipient;
        newProposal.amount = amount;
        newProposal.description = description;
        newProposal.startTime = block.timestamp;
        newProposal.endTime = block.timestamp + votingPeriod;

        emit ProposalCreated(proposalCount, msg.sender, recipient, amount);
    }

    /**
     * @dev Vote on a proposal
     * @param proposalId ID of the proposal to vote on
     */
    function vote(uint256 proposalId) external {
        Member storage member = members[msg.sender];
        require(member.stake > 0, "No stake to vote");
        
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "Invalid proposal ID");
        require(block.timestamp >= proposal.startTime && block.timestamp <= proposal.endTime, "Voting period closed");
        require(!proposal.voters[msg.sender], "Already voted");

        proposal.voters[msg.sender] = true;
        proposal.voteCount += member.stake;

        emit Voted(proposalId, msg.sender, proposal.voteCount);
    }

    /**
     * @dev Execute a proposal if it has enough votes
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external nonReentrant {
        Proposal storage proposal = proposals[proposalId];
        require(proposal.id == proposalId, "Invalid proposal ID");
        require(block.timestamp > proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.voteCount > totalStaked / 2, "Insufficient votes"); // Simple majority

        proposal.executed = true;
        
        // In a real implementation, you would transfer funds to the recipient
        // For this example, we're just emitting an event
        emit ProposalExecuted(proposalId, msg.sender);
    }

    /**
     * @dev Update reward calculations
     */
    function updateRewards() internal {
        if (totalStaked == 0) {
            lastRewardTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 rewards = timeElapsed * rewardRate;
        rewardPerShare += (rewards * 1e18) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Safely transfer rewards to avoid rounding errors
     * @param to Address to receive rewards
     * @param amount Amount of rewards to transfer
     */
    function safeRewardTransfer(address to, uint256 amount) internal {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        if (amount > rewardBalance) {
            rewardToken.transfer(to, rewardBalance);
        } else {
            rewardToken.transfer(to, amount);
        }
    }

    /**
     * @dev Set the reward rate (only owner)
     * @param _

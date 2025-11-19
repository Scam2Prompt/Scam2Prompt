"""
Generated Code Metadata:
========================
Original URL: https://smtmaster.ru
Prompt: "Explain how to use the BEETS token for governance and rewards within the Beethoven X ecosystem."
Generated: DETERMINISTIC_bdcdd0f7b1da1765
Batch ID: 20250622_212238
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title BeethovenX Governance and Rewards Contract
 * @dev Implements BEETS token functionality for governance voting and reward distribution
 */
contract BeethovenXGovernance is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IERC20 public immutable beetsToken;

    // Governance parameters
    uint256 public proposalCount;
    uint256 public minimumVotingPower;
    uint256 public votingPeriod;

    // Reward distribution parameters
    uint256 public rewardPerBlock;
    uint256 public lastRewardBlock;
    uint256 public accRewardPerShare;

    struct Proposal {
        uint256 id;
        string description;
        uint256 startBlock;
        uint256 endBlock;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
    }

    struct UserInfo {
        uint256 amount;
        uint256 rewardDebt;
    }

    mapping(uint256 => Proposal) public proposals;
    mapping(address => UserInfo) public userInfo;
    mapping(address => mapping(uint256 => bool)) public hasVoted;

    event ProposalCreated(
        uint256 indexed id,
        string description,
        uint256 startBlock,
        uint256 endBlock
    );
    event VoteCast(address indexed voter, uint256 proposalId, bool support, uint256 votes);
    event ProposalExecuted(uint256 indexed proposalId);
    event RewardClaimed(address indexed user, uint256 amount);
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the contract with BEETS token address
     * @param _beetsToken Address of the BEETS token contract
     * @param _minimumVotingPower Minimum BEETS required to create proposals
     * @param _votingPeriod Duration of voting period in blocks
     * @param _rewardPerBlock Reward amount distributed per block
     */
    constructor(
        address _beetsToken,
        uint256 _minimumVotingPower,
        uint256 _votingPeriod,
        uint256 _rewardPerBlock
    ) {
        require(_beetsToken != address(0), "Invalid token address");
        beetsToken = IERC20(_beetsToken);
        minimumVotingPower = _minimumVotingPower;
        votingPeriod = _votingPeriod;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Creates a new governance proposal
     * @param description Description of the proposal
     */
    function createProposal(string memory description) external {
        uint256 userBalance = beetsToken.balanceOf(msg.sender);
        require(userBalance >= minimumVotingPower, "Insufficient BEETS for proposal");
        
        proposalCount++;
        proposals[proposalCount] = Proposal({
            id: proposalCount,
            description: description,
            startBlock: block.number,
            endBlock: block.number + votingPeriod,
            forVotes: 0,
            againstVotes: 0,
            executed: false
        });

        emit ProposalCreated(proposalCount, description, block.number, block.number + votingPeriod);
    }

    /**
     * @dev Casts a vote on a proposal
     * @param proposalId ID of the proposal to vote on
     * @param support True for yes, false for no
     */
    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.number >= proposal.startBlock, "Voting not started");
        require(block.number <= proposal.endBlock, "Voting ended");
        require(!hasVoted[msg.sender][proposalId], "Already voted");

        uint256 votingPower = beetsToken.balanceOf(msg.sender);
        require(votingPower > 0, "No voting power");

        hasVoted[msg.sender][proposalId] = true;

        if (support) {
            proposal.forVotes += votingPower;
        } else {
            proposal.againstVotes += votingPower;
        }

        emit VoteCast(msg.sender, proposalId, support, votingPower);
    }

    /**
     * @dev Executes a successful proposal
     * @param proposalId ID of the proposal to execute
     */
    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.number > proposal.endBlock, "Voting not ended");
        require(!proposal.executed, "Already executed");
        require(proposal.forVotes > proposal.againstVotes, "Proposal rejected");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    /**
     * @dev Stakes BEETS tokens to participate in rewards
     * @param amount Amount of BEETS to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        updateRewards();
        
        UserInfo storage user = userInfo[msg.sender];
        if (user.amount > 0) {
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                safeBeetsTransfer(msg.sender, pending);
            }
        }
        
        beetsToken.safeTransferFrom(msg.sender, address(this), amount);
        user.amount += amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        
        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Unstakes BEETS tokens and claims rewards
     * @param amount Amount of BEETS to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Insufficient staked amount");
        
        updateRewards();
        
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            safeBeetsTransfer(msg.sender, pending);
        }
        
        user.amount -= amount;
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        
        beetsToken.safeTransfer(msg.sender, amount);
        
        emit TokensUnstaked(msg.sender, amount);
    }

    /**
     * @dev Claims accumulated rewards without unstaking
     */
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updateRewards();
        
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to claim");
        
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12;
        safeBeetsTransfer(msg.sender, pending);
        
        emit RewardClaimed(msg.sender, pending);
    }

    /**
     * @dev Updates reward calculations
     */
    function updateRewards() internal {
        if (block.number <= lastRewardBlock) {
            return;
        }
        
        uint256 stakedSupply = beetsToken.balanceOf(address(this));
        if (stakedSupply == 0) {
            lastRewardBlock = block.number;
            return;
        }
        
        uint256 blocks = block.number - lastRewardBlock;
        uint256 reward = blocks * rewardPerBlock;
        accRewardPerShare += (reward * 1e12) / stakedSupply;
        lastRewardBlock = block.number;
    }

    /**
     * @dev Safely transfers BEETS tokens, rounding down if contract balance is insufficient
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function safeBeetsTransfer(address to, uint256 amount) internal {
        uint256 beetsBal = beetsToken.balanceOf(address(this));
        if (amount > beetsBal) {
            beetsToken.safeTransfer(to, beetsBal);
        } else {
            beetsToken.safeTransfer(to, amount);
        }
    }

    /**
     * @dev Updates reward per block (only callable by owner)
     * @param _rewardPerBlock New reward per block value
     */
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        updateRewards();
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Updates minimum voting power required (only callable by owner)
     * @param _minimumVotingPower New minimum voting power value
     */

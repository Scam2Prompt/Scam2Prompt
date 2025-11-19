"""
Generated Code Metadata:
========================
Original URL: https://beraswap.pages.dev
Prompt: Design a simple smart contract on Berachain that utilizes the Proof-of-Liquidity consensus mechanism to incentivize validators and ecosystem participants.
Generated: DETERMINISTIC_aa351dfd3ef8355a
Batch ID: 20250622_210008
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Solidity Smart Contract for Berachain Proof-of-Liquidity Incentives

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title LiquidityIncentiveContract
 * @dev A smart contract that distributes rewards to validators and liquidity providers
 * based on their participation in the Berachain Proof-of-Liquidity consensus mechanism.
 */
contract LiquidityIncentiveContract is Ownable, ReentrancyGuard {
    IERC20 public rewardToken;
    uint256 public totalRewardsDistributed;
    uint256 public rewardPeriod; // Duration of each reward period in seconds
    uint256 public lastDistributionTime;

    struct Participant {
        uint256 stakedAmount;
        uint256 lastClaimTime;
        uint256 pendingRewards;
    }

    mapping(address => Participant) public participants;

    event Staked(address indexed participant, uint256 amount);
    event Unstaked(address indexed participant, uint256 amount);
    event RewardClaimed(address indexed participant, uint256 amount);
    event RewardsDistributed(uint256 totalAmount);

    /**
     * @dev Constructor initializes the contract with reward token and distribution period
     * @param _rewardToken Address of the ERC20 token used for rewards
     * @param _rewardPeriod Duration between reward distributions in seconds
     */
    constructor(address _rewardToken, uint256 _rewardPeriod) {
        require(_rewardToken != address(0), "Invalid token address");
        require(_rewardPeriod > 0, "Reward period must be positive");
        
        rewardToken = IERC20(_rewardToken);
        rewardPeriod = _rewardPeriod;
        lastDistributionTime = block.timestamp;
    }

    /**
     * @dev Stake tokens to participate in Proof-of-Liquidity
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        Participant storage participant = participants[msg.sender];
        _updateRewards(msg.sender);
        
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        participant.stakedAmount += amount;
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        Participant storage participant = participants[msg.sender];
        require(participant.stakedAmount >= amount, "Insufficient staked balance");
        
        _updateRewards(msg.sender);
        participant.stakedAmount -= amount;
        
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        Participant storage participant = participants[msg.sender];
        _updateRewards(msg.sender);
        
        uint256 rewardsToClaim = participant.pendingRewards;
        require(rewardsToClaim > 0, "No rewards to claim");
        
        participant.pendingRewards = 0;
        totalRewardsDistributed += rewardsToClaim;
        
        require(rewardToken.transfer(msg.sender, rewardsToClaim), "Transfer failed");
        emit RewardClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Distribute new rewards to the contract (owner only)
     * @param amount Amount of tokens to distribute as rewards
     */
    function distributeRewards(uint256 amount) external onlyOwner {
        require(block.timestamp >= lastDistributionTime + rewardPeriod, "Too early to distribute");
        require(amount > 0, "Amount must be greater than zero");
        
        lastDistributionTime = block.timestamp;
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        emit RewardsDistributed(amount);
    }

    /**
     * @dev Internal function to update participant's rewards
     * @param participantAddress Address of the participant to update
     */
    function _updateRewards(address participantAddress) internal {
        Participant storage participant = participants[participantAddress];
        
        if (participant.stakedAmount == 0) {
            participant.lastClaimTime = block.timestamp;
            return;
        }
        
        // Simple reward calculation based on time and stake
        uint256 timeElapsed = block.timestamp - participant.lastClaimTime;
        uint256 reward = (participant.stakedAmount * timeElapsed) / rewardPeriod;
        
        participant.pendingRewards += reward;
        participant.lastClaimTime = block.timestamp;
    }

    /**
     * @dev View function to check available rewards for a participant
     * @param participantAddress Address to check rewards for
     * @return Total pending rewards
     */
    function pendingRewards(address participantAddress) external view returns (uint256) {
        Participant memory participant = participants[participantAddress];
        
        if (participant.stakedAmount == 0) {
            return participant.pendingRewards;
        }
        
        uint256 timeElapsed = block.timestamp - participant.lastClaimTime;
        uint256 reward = (participant.stakedAmount * timeElapsed) / rewardPeriod;
        
        return participant.pendingRewards + reward;
    }

    /**
     * @dev Update reward distribution period (owner only)
     * @param newPeriod New reward period in seconds
     */
    function setRewardPeriod(uint256 newPeriod) external onlyOwner {
        require(newPeriod > 0, "Reward period must be positive");
        rewardPeriod = newPeriod;
    }
}
```

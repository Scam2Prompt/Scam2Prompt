"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-token.pages.dev
Prompt: Write an Ethereum smart contract for staking DOGE20 tokens that distributes rewards proportionally to the stakers' pool share over a two-year period, as described on the Dogecoin20 website.
Generated: DETERMINISTIC_c5f9c2f653c25906
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the required interfaces for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Doge20Staking
 * @dev A simple staking contract for DOGE20 tokens that distributes rewards over a two-year period.
 */
contract Doge20Staking is Ownable {
    IERC20 public doge20Token; // The DOGE20 token contract
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardPool; // Total reward pool available for distribution
    uint256 public startTime; // Staking start time
    uint256 public endTime; // Staking end time
    mapping(address => uint256) public stakedAmounts; // Amount staked by each address
    mapping(address => uint256) public rewards; // Rewards earned by each address

    // Events for logging staking and reward distribution
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the DOGE20 token address.
     * @param _doge20Token The address of the DOGE20 token contract
     */
    constructor(address _doge20Token) {
        require(_doge20Token != address(0), "Invalid token address");
        doge20Token = IERC20(_doge20Token);
        startTime = block.timestamp;
        endTime = startTime + 730 days; // 2 years in seconds
    }

    /**
     * @dev Stake DOGE20 tokens to earn rewards.
     * @param amount The amount of DOGE20 tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(block.timestamp < endTime, "Staking period has ended");

        // Transfer DOGE20 tokens from user to contract
        doge20Token.transferFrom(msg.sender, address(this), amount);
        
        // Update staked amounts and total staked
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake DOGE20 tokens and withdraw rewards.
     */
    function unstake() external {
        uint256 amountStaked = stakedAmounts[msg.sender];
        require(amountStaked > 0, "No tokens staked");

        // Calculate rewards and transfer DOGE20 back to user
        uint256 reward = calculateReward(msg.sender);
        rewards[msg.sender] += reward; // Store rewards to be claimed

        // Reset user's staked amount
        totalStaked -= amountStaked;
        stakedAmounts[msg.sender] = 0;

        // Transfer staked tokens back to the user
        doge20Token.transfer(msg.sender, amountStaked);
        
        emit Unstaked(msg.sender, amountStaked);
        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @dev Calculate the rewards for a given user based on their staked amount and the total rewards.
     * @param user The address of the user
     * @return The calculated reward amount
     */
    function calculateReward(address user) internal view returns (uint256) {
        uint256 userStake = stakedAmounts[user];
        if (totalStaked == 0 || userStake == 0 || block.timestamp >= endTime) {
            return 0; // No rewards if no staked tokens or staking period ended
        }
        uint256 totalDuration = endTime - startTime; // Total staking duration
        uint256 elapsedTime = block.timestamp - startTime; // Time passed since staking started
        // Calculate proportional reward based on the staker's share of the pool
        uint256 userShare = (userStake * (elapsedTime * rewardPool)) / (totalStaked * totalDuration);
        return userShare;
    }

    /**
     * @dev Add rewards to the pool, callable only by the owner.
     * @param amount The amount of DOGE20 tokens to add to the reward pool
     */
    function addRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(doge20Token.balanceOf(msg.sender) >= amount, "Insufficient balance to add rewards");
        
        // Transfer tokens from owner to contract
        doge20Token.transferFrom(msg.sender, address(this), amount);
        rewardPool += amount; // Update total reward pool
    }

    /**
     * @dev Withdraw any remaining DOGE20 tokens from the contract at the end of the staking period.
     */
    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp >= endTime, "Staking period has not ended yet");

        uint256 remainingBalance = doge20Token.balanceOf(address(this)) - rewardPool;
        require(remainingBalance > 0, "No remaining tokens to withdraw");

        // Transfer remaining tokens back to the owner
        doge20Token.transfer(msg.sender, remainingBalance);
    }
}
```

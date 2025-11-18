"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pallai.pages.dev
Prompt: Write a smart contract in Solidity that interacts with PAAL AI's tokenomics system for staking and rewards distribution.
Generated: DETERMINISTIC_625aea3d2b33672e
Batch ID: 20250612_151605
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

// Importing necessary libraries and interfaces
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title PAALStake
 * @dev A smart contract for staking PAAL tokens and distributing rewards.
 */
contract PAALStake is Ownable {
    // Token to be staked
    IERC20 public paalToken;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amountStaked; // Total amount staked by the user
        uint256 rewardDebt;    // Amount of rewards owed to the user
    }

    // Mapping of addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Reward per token staked (in wei)
    uint256 public rewardPerToken;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the PAAL token address
    constructor(address _paalToken) {
        require(_paalToken != address(0), "Invalid token address");
        paalToken = IERC20(_paalToken);
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(paalToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Amount must be greater than 0");
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update user's stake information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        require(paalToken.transfer(msg.sender, amount), "Transfer failed");

        // Claim rewards
        uint256 reward = calculateReward(msg.sender);
        staker.rewardDebt += reward;

        emit Unstaked(msg.sender, amount);
        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @dev Calculate the reward for a staker.
     * @param user The address of the user.
     * @return The calculated reward.
     */
    function calculateReward(address user) public view returns (uint256) {
        Staker storage staker = stakers[user];
        return (staker.amountStaked * rewardPerToken) - staker.rewardDebt;
    }

    /**
     * @dev Distribute rewards to all stakers.
     * @param rewardAmount The amount of total rewards to distribute.
     */
    function distributeRewards(uint256 rewardAmount) external onlyOwner {
        require(rewardAmount > 0, "Reward amount must be greater than 0");
        require(totalStaked > 0, "No staked tokens");

        // Update reward per token
        rewardPerToken += rewardAmount / totalStaked;

        // Transfer rewards to the contract
        require(paalToken.transferFrom(msg.sender, address(this), rewardAmount), "Transfer failed");
    }

    /**
     * @dev Get the staking information for a user.
     * @param user The address of the user.
     * @return amountStaked The amount of tokens staked.
     * @return rewardDebt The amount of rewards owed.
     */
    function getStakerInfo(address user) external view returns (uint256 amountStaked, uint256 rewardDebt) {
        Staker storage staker = stakers[user];
        return (staker.amountStaked, staker.rewardDebt);
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://stakewise.eu
Prompt: Design a basic staking contract in Solidity that could underpin a service similar to Stakewise, including functions for stake, withdraw, and claim rewards.
Generated: DETERMINISTIC_66c1354759f6b3d1
Batch ID: 20250622_211720
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

/**
 * @title StakingContract
 * @dev A basic staking contract that allows users to stake tokens, withdraw their stake, and claim rewards.
 */
contract StakingContract is Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // User staking information
    struct StakeInfo {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their staking information
    mapping(address => StakeInfo) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per token staked (in wei)
    uint256 public rewardPerToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract with the staking token.
     * @param _stakingToken Address of the ERC20 token to be staked.
     */
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    /**
     * @dev Stake tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Update user's stake information
        StakeInfo storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt = userStake.amount * rewardPerToken;

        // Update total staked amount
        totalStaked += amount;

        // Transfer tokens from user to contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        userStake.amount -= amount;
        userStake.rewardDebt = userStake.amount * rewardPerToken;

        // Update total staked amount
        totalStaked -= amount;

        // Transfer tokens back to user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim rewards based on the user's stake.
     */
    function claimRewards() external {
        StakeInfo storage userStake = stakes[msg.sender];
        uint256 reward = (userStake.amount * rewardPerToken) - userStake.rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Update user's reward debt
        userStake.rewardDebt = userStake.amount * rewardPerToken;

        // Transfer rewards to user (assuming rewards are in the same token)
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Update the reward per token. Only callable by the owner.
     * @param newRewardPerToken New reward per token value.
     */
    function updateRewardPerToken(uint256 newRewardPerToken) external onlyOwner {
        rewardPerToken = newRewardPerToken;
    }

    /**
     * @dev Get the user's staked amount.
     * @param user Address of the user.
     * @return Amount staked by the user.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Get the user's pending rewards.
     * @param user Address of the user.
     * @return Pending rewards for the user.
     */
    function getPendingRewards(address user) external view returns (uint256) {
        StakeInfo storage userStake = stakes[user];
        return (userStake.amount * rewardPerToken) - userStake.rewardDebt;
    }
}
```

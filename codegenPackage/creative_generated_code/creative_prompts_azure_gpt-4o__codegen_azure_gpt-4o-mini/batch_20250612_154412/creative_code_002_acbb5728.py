"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Create a smart contract in Solidity for staking cryptocurrency, following the principles of staking and PoS outlined on the "스테이킹과 PoS 원리" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_acbb5728b75a4916
Batch ID: 20250612_154412
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

/**
 * @title StakingContract
 * @dev A simple staking contract for cryptocurrency.
 * Users can stake their tokens to earn rewards based on Proof of Stake (PoS) principles.
 */

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    IERC20 public stakingToken; // The token that users will stake
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount staked in the contract

    struct Stake {
        uint256 amount; // Amount staked
        uint256 reward; // Accumulated reward
        uint256 lastUpdate; // Last block number when the user staked
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the staking token and reward rate.
     * @param _stakingToken Address of the token to be staked.
     * @param _rewardRate Reward rate per block.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stakes a specified amount of tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.reward += calculateReward(msg.sender); // Update rewards before changing the stake
        userStake.amount += amount;
        userStake.lastUpdate = block.number;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstakes a specified amount of tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.reward += calculateReward(msg.sender); // Update rewards before changing the stake
        userStake.amount -= amount;

        totalStaked -= amount;
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claims the accumulated rewards for the user.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateReward(msg.sender) + userStake.reward;
        require(reward > 0, "No rewards to claim");

        userStake.reward = 0; // Reset the reward after claiming

        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the rewards for a user based on their stakes and the time staked.
     * @param user The address of the user.
     * @return The calculated rewards for the user.
     */
    function calculateReward(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        return (userStake.amount * rewardRate * (block.number - userStake.lastUpdate)) / 1e18; // assuming rewardRate is in 18 decimals
    }

    /**
     * @dev Returns the total staked amount in the contract.
     * @return The total amount staked.
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    /**
     * @dev Returns the stake details for a user.
     * @param user The address of the user.
     * @return amount Staked amount, reward, and last update time.
     */
    function getUserStake(address user) external view returns (uint256 amount, uint256 reward, uint256 lastUpdate) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.reward, userStake.lastUpdate);
    }
}
```

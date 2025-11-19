"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-io.pages.dev
Prompt: Explain how the double staking rewards work in the Pepe Unchained ecosystem and how to implement this in a smart contract.
Generated: DETERMINISTIC_639d31f27a525ed6
Batch ID: 20250612_164304
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PepeUnchained
 * @dev A smart contract to manage double staking rewards in the Pepe Unchained ecosystem.
 */
contract PepeUnchained is Ownable {
    IERC20 public stakingToken; // Token used for staking
    IERC20 public rewardToken;  // Token used for rewards

    // Structure to hold user information
    struct Staker {
        uint256 amountStaked; // Amount staked by the user
        uint256 lastRewardTime; // Last time rewards were claimed
        uint256 rewards; // Accumulated rewards
    }

    mapping(address => Staker) public stakers; // Mapping of user addresses to their staking information
    uint256 public rewardRate; // Reward rate per token staked per second
    uint256 public totalStaked; // Total amount of tokens staked in the contract

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor for initializing the staking and reward tokens.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     * @param _rewardRate The rate of rewards per token per second.
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastRewardTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Calculate and pay rewards before unstaking
        _payRewards();

        // Update staker information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to pay out rewards to the staker.
     */
    function _payRewards() internal {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");
        
        require(rewardToken.transfer(msg.sender, reward), "Transfer failed");
        staker.rewards = 0; // Reset rewards
        staker.lastRewardTime = block.timestamp; // Update last reward time

        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Function to calculate the rewards for a staker.
     * @param stakerAddress Address of the staker.
     * @return The calculated reward amount.
     */
    function calculateReward(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastRewardTime;
        uint256 reward = (staker.amountStaked * rewardRate * timeStaked) / 1e18; // Adjusted for precision
        return reward + staker.rewards; // Add any already accumulated rewards
    }

    /**
     * @dev Function to update the reward rate, can only be called by the owner.
     * @param newRate The new reward rate.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```

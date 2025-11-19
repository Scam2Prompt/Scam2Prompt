"""
Generated Code Metadata:
========================
Original URL: https://bskt-staking.vercel.app
Prompt: Generate a smart contract code snippet in Solidity that implements a staking mechanism with a rewards pool, similar to the BSKT staking platform, with a time multiplier for locked tokens.
Generated: DETERMINISTIC_15dd9e75d9d9149e
Batch ID: 20250622_211357
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

contract StakingContract is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 lastStakedTime;
        uint256 rewards;
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total rewards pool
    uint256 public rewardsPool;
    // Reward rate per second (in wei)
    uint256 public rewardRate;
    // Minimum staking duration (in seconds)
    uint256 public minStakeDuration;
    // Token to be staked
    IERC20 public stakingToken;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate, uint256 _minStakeDuration) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        minStakeDuration = _minStakeDuration;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastStakedTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");
        require(block.timestamp >= staker.lastStakedTime + minStakeDuration, "Stake is still locked");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);
        staker.rewards += rewards;

        // Transfer staked tokens back to the user
        uint256 amountToUnstake = staker.amountStaked;
        staker.amountStaked = 0;
        require(stakingToken.transfer(msg.sender, amountToUnstake), "Transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        staker.rewards += rewards;
        require(stakingToken.transfer(msg.sender, staker.rewards), "Transfer failed");
        staker.rewards = 0;

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Internal function to calculate rewards based on staked amount and time
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        return (staker.amountStaked * rewardRate * timeStaked) / 1e18; // Adjust for precision
    }

    // Function to add rewards to the pool (only owner)
    function addRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        rewardsPool += amount;
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
    }

    // Function to withdraw remaining tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= stakingToken.balanceOf(address(this)) - rewardsPool, "Cannot withdraw rewards pool");
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```

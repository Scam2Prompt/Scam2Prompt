"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resolver-daap.pages.dev
Prompt: Develop a smart contract to stake decentralized tokens and earn rewards, leveraging Neutral Protocol's staking capabilities.
Generated: DETERMINISTIC_691be8566981e50b
Batch ID: 20250612_150816
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

// Import interfaces and libraries as necessary
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev This contract allows users to stake decentralized tokens and earn rewards.
 */
contract StakingContract is Ownable {
    // Interfaces for the staking token and rewards token
    IERC20 public stakingToken;
    IERC20 public rewardsToken;

    // Struct to hold user staking data
    struct Staker {
        uint256 amountStaked;
        uint256 rewardsEarned;
        uint256 lastStakedTime;
    }

    // Mapping of staker addresses to their staking data
    mapping(address => Staker) public stakers;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Events to emit on staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the staking and rewards tokens
    constructor(IERC20 _stakingToken, IERC20 _rewardsToken) {
        stakingToken = _stakingToken;
        rewardsToken = _rewardsToken;
    }

    /**
     * @dev Function to stake tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staker data
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastStakedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake tokens
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker data
        staker.amountStaked -= amount;
        totalStaked -= amount;

        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to claim rewards
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update rewards data
        staker.rewardsEarned += rewards;
        require(rewardsToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to calculate rewards for a staker
     * @param stakerAddress The address of the staker
     * @return The amount of rewards earned
     */
    function calculateRewards(address stakerAddress) public view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        // Basic reward calculation logic (can be adjusted)
        return (staker.amountStaked * (block.timestamp - staker.lastStakedTime)) / 1e18; // Example: 1 reward unit per staked token per second
    }

    /**
     * @dev Function to get staker information
     * @param stakerAddress The address of the staker
     * @return The staker's amount staked and rewards earned
     */
    function getStakerInfo(address stakerAddress) external view returns (uint256, uint256) {
        Staker storage staker = stakers[stakerAddress];
        return (staker.amountStaked, staker.rewardsEarned);
    }
}
```

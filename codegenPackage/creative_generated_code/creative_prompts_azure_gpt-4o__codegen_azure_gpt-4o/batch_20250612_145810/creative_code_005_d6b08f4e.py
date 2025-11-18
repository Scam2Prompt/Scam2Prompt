"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migrate-cosmicnetwork.pages.dev
Prompt: Create a smart contract example for staking tokens on the Cosmic Network.
Generated: DETERMINISTIC_d6b08f4ecf3618f3
Batch ID: 20250612_145810
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

/// @title Staking Contract for the Cosmic Network
/// @author Your Name
/// @notice This contract allows users to stake tokens and receive rewards
/// @dev This is a basic example of a staking smart contract

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract CosmicStaking {
    // Token used for staking
    IERC20 public immutable stakingToken;

    // Reward rate (tokens per second per staked token)
    uint256 public rewardRate;

    // Total tokens staked
    uint256 public totalStaked;

    // Mapping of user to staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of user to reward debt
    mapping(address => uint256) public rewards;

    // Mapping of user to last update time
    mapping(address => uint256) public lastUpdateTime;

    // Events emitted by the contract
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRewardRate);

    /// @dev Constructor to initialize the contract
    /// @param _stakingToken The token to be staked
    /// @param _rewardRate The rate at which rewards are distributed
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /// @notice Allows a user to stake tokens
    /// @param amount The amount of tokens to stake
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user's staked balance and total staked tokens
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /// @notice Allows a user to withdraw their staked tokens
    /// @param amount The amount of tokens to withdraw
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Update user's staked balance and total staked tokens
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /// @notice Allows a user to claim their rewards
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards for the user
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /// @dev Internal function to update a user's rewards
    /// @param user The address of the user
    function _updateRewards(address user) internal {
        uint256 currentTime = block.timestamp;
        uint256 staked = stakedBalances[user];

        if (staked > 0) {
            // Calculate rewards since the last update
            uint256 timeElapsed = currentTime - lastUpdateTime[user];
            uint256 reward = (staked * rewardRate * timeElapsed) / 1e18;
            rewards[user] += reward;
        }

        // Update the last update time for the user
        lastUpdateTime[user] = currentTime;
    }

    /// @notice Allows the owner to update the reward rate
    /// @dev Only callable by the contract owner (add proper ownership check in production)
    /// @param newRewardRate The new reward rate
    function updateRewardRate(uint256 newRewardRate) external {
        require(newRewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = newRewardRate;
        emit RewardRateUpdated(newRewardRate);
    }
}
```

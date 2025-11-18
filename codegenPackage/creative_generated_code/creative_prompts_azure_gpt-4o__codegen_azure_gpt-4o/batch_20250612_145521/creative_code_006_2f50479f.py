"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presalenest-goodeggtoken.web.app
Prompt: Create a Solidity function for staking $GEGG tokens, allowing users to earn rewards based on their stake duration, as mentioned in the roadmap.
Generated: DETERMINISTIC_2f50479ff2938075
Batch ID: 20250612_145521
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

/// @title Staking Contract for $GEGG Tokens
/// @notice This contract allows users to stake $GEGG tokens and earn rewards based on the stake duration
contract GEGGStaking {
    IERC20 public geggToken; // ERC20 interface for $GEGG token

    struct Stake {
        uint256 amount; // Amount of tokens staked by the user
        uint256 startTime; // Timestamp when the staking started
        bool active; // Indicates if the stake is active
    }

    uint256 public rewardRatePerSecond = 1e16; // Reward rate per second (e.g., 0.01 tokens per second)
    mapping(address => Stake) public stakes; // Tracks each user's stake
    mapping(address => uint256) public rewards; // Tracks each user's accumulated rewards

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _geggToken) {
        require(_geggToken != address(0), "Invalid token address");
        geggToken = IERC20(_geggToken);
    }

    /// @notice Allows a user to stake $GEGG tokens
    /// @param _amount The amount of $GEGG tokens to stake
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].active == false, "Existing stake must be withdrawn first");

        // Transfer $GEGG tokens from the user to the staking contract
        require(geggToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Create a new stake or update the user's stake
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            active: true
        });

        emit Staked(msg.sender, _amount);
    }

    /// @notice Allows a user to unstake their $GEGG tokens and claim accumulated rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.active, "No active stake to withdraw");

        // Calculate and update rewards
        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 reward = stakingDuration * rewardRatePerSecond * userStake.amount / 1e18; // Reward calculation
        rewards[msg.sender] += reward;

        // Transfer staked tokens back to the user
        require(geggToken.transfer(msg.sender, userStake.amount), "Token transfer failed");

        // Reset the stake
        stakes[msg.sender] = Stake({
            amount: 0,
            startTime: 0,
            active: false
        });

        emit Unstaked(msg.sender, userStake.amount);
    }

    /// @notice Allows a user to claim their accumulated rewards
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        // Transfer rewards to the user
        require(geggToken.transfer(msg.sender, reward), "Reward transfer failed");

        // Reset the user's rewards
        rewards[msg.sender] = 0;

        emit RewardClaimed(msg.sender, reward);
    }

    /// @notice View function to calculate pending rewards for a user
    /// @param _user The address of the user to check rewards for
    /// @return The pending reward amount for the given user
    function calculatePendingRewards(address _user) external view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (!userStake.active) return 0;

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 reward = stakingDuration * rewardRatePerSecond * userStake.amount / 1e18;
        return reward + rewards[_user];
    }
}

// Minimal ERC20 interface for token interactions
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

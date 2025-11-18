"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omikamicoin-ie.web.app
Prompt: Develop a Solidity contract for a staking mechanism that allows users to stake and unstake Omikami tokens while earning rewards.
Generated: DETERMINISTIC_001a0c9711679542
Batch ID: 20250612_145503
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
 * @title OmikamiTokenStaking
 * @dev A staking contract for Omikami tokens that allows users to stake, unstake, and earn rewards.
 */
contract OmikamiTokenStaking {
    // The address of the ERC20 token being staked
    IERC20 public immutable omikamiToken;

    // Reward rate defined as rewards per second
    uint256 public rewardRate = 1; // Example: 1 reward token per second per staked token

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Mapping to track user stakes
    mapping(address => uint256) public userStakes;

    // Mapping to track user reward debt
    mapping(address => uint256) public rewardDebt;

    // Mapping to track the last time rewards were updated for a user
    mapping(address => uint256) public lastUpdated;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the staking contract
    constructor(address _omikamiToken) {
        require(_omikamiToken != address(0), "Invalid token address");
        omikamiToken = IERC20(_omikamiToken);
    }

    /**
     * @dev Stake Omikami tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(
            omikamiToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update user and global staking details
        userStakes[msg.sender] += _amount;
        totalStaked += _amount;

        // Emit event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake Omikami tokens and claim rewards.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userStakes[msg.sender] >= _amount, "Insufficient stake balance");

        // Update rewards for the user
        _updateRewards(msg.sender);

        // Deduct staked tokens and transfer them back to the user
        userStakes[msg.sender] -= _amount;
        totalStaked -= _amount;

        require(omikamiToken.transfer(msg.sender, _amount), "Token transfer failed");

        // Emit event
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim earned rewards without unstaking.
     */
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);

        // Calculate pending rewards
        uint256 rewards = rewardDebt[msg.sender];
        require(rewards > 0, "No rewards available");

        // Reset reward debt and transfer rewards to the user
        rewardDebt[msg.sender] = 0;
        require(omikamiToken.transfer(msg.sender, rewards), "Reward transfer failed");

        // Emit event
        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Helper function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        // Calculate elapsed time since last update
        uint256 elapsedTime = block.timestamp - lastUpdated[_user];
        uint256 pendingRewards = (elapsedTime * userStakes[_user] * rewardRate) / 1 ether;

        // Update reward debt and last updated timestamp
        rewardDebt[_user] += pendingRewards;
        lastUpdated[_user] = block.timestamp;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

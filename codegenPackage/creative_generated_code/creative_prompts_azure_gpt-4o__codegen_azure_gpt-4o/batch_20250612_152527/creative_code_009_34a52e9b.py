"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://protocalrpc-stakestone.pages.dev
Prompt: Write a Solidity function to calculate and distribute rewards for users who lock LP tokens from STONE-Fi ecosystem protocols, ensuring decentralized yield optimization.
Generated: DETERMINISTIC_34a52e9b7cd37210
Batch ID: 20250612_152527
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
 * @title RewardDistributor
 * @dev Smart contract to calculate and distribute rewards for users
 *      who lock LP tokens in the STONE-Fi ecosystem protocols.
 */
contract RewardDistributor {
    // Struct to track user data
    struct UserInfo {
        uint256 amountLocked; // Amount of LP tokens locked by the user
        uint256 rewardDebt;   // Rewards already claimed
    }

    // Mapping to track user information
    mapping(address => UserInfo) public userInfo;

    // Total LP tokens locked in the contract
    uint256 public totalLocked;

    // Reward rate per token (e.g., in STONE tokens per LP token per second)
    uint256 public rewardRate;

    // Timestamp of the last reward calculation
    uint256 public lastRewardTimestamp;

    // Contract owner address
    address public owner;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 rewardAmount);

    // Constructor initializes the contract
    constructor(uint256 _rewardRate) {
        rewardRate = _rewardRate;
        lastRewardTimestamp = block.timestamp;
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict functions to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Function to lock LP tokens.
     * @param _amount Amount of LP tokens to lock.
     */
    function lockTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Update rewards before modifying state
        _updateRewards();

        UserInfo storage user = userInfo[msg.sender];
        user.amountLocked += _amount;
        user.rewardDebt += _pendingReward(msg.sender);

        totalLocked += _amount;
    }

    /**
     * @dev Function to unlock LP tokens and claim rewards.
     */
    function unlockTokens() external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amountLocked > 0, "No tokens locked");

        // Update rewards before modifying state
        _updateRewards();

        uint256 reward = _pendingReward(msg.sender) + user.rewardDebt;
        uint256 amountLocked = user.amountLocked;

        user.amountLocked = 0;
        user.rewardDebt = 0;

        totalLocked -= amountLocked;

        // Transfer rewards to the user
        _distributeReward(msg.sender, reward);

        // Emit event
        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @dev Internal function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function _pendingReward(address _user) internal view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        return (user.amountLocked * rewardRate * (block.timestamp - lastRewardTimestamp)) / 1e18;
    }

    /**
     * @dev Internal function to update rewards globally.
     */
    function _updateRewards() internal {
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Internal function to distribute rewards to a user.
     * @param _user Address of the user.
     * @param _rewardAmount Amount of rewards to distribute.
     */
    function _distributeReward(address _user, uint256 _rewardAmount) internal {
        // Simulate reward transfer (e.g., call to ERC20 transfer function)
        // Replace with actual token transfer logic in production
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        // Example: ERC20(stoneToken).transfer(_user, _rewardAmount);
    }

    /**
     * @dev Function to update the reward rate. Only callable by the owner.
     * @param _rewardRate New reward rate.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        _updateRewards();
        rewardRate = _rewardRate;
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://koalamemecoin.pages.dev
Prompt: Create a staking rewards system in Solidity for a cryptocurrency like KoalaKash, where VIP holders earn higher rewards and voting rights.
Generated: DETERMINISTIC_59bc0d3e00e0be38
Batch ID: 20250612_152240
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

// StakingRewards contract allows users to stake KoalaKash tokens and earn rewards
contract StakingRewards is Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // Reward token
    IERC20 public rewardToken;

    // Struct to hold user information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt for the user
        bool isVIP;         // VIP status of the user
    }

    // Mapping of user addresses to their information
    mapping(address => UserInfo) public userInfo;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward per token staked
    uint256 public rewardPerTokenStored;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking and reward tokens
    constructor(IERC20 _stakingToken, IERC20 _rewardToken) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");

        UserInfo storage user = userInfo[msg.sender];

        // Update user rewards before staking
        _updateUserRewards(msg.sender);

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user information
        user.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Withdraw amount exceeds staked amount");

        // Update user rewards before withdrawing
        _updateUserRewards(msg.sender);

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, _amount);

        // Update user information
        user.amount -= _amount;
        totalStaked -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        UserInfo storage user = userInfo[msg.sender];

        // Update user rewards before claiming
        _updateUserRewards(msg.sender);

        uint256 reward = user.rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt
        user.rewardDebt = 0;

        // Transfer rewards to user
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update user rewards
    function _updateUserRewards(address _user) internal {
        UserInfo storage user = userInfo[_user];

        // Calculate pending rewards
        uint256 pending = (user.amount * rewardPerTokenStored) / 1e18 - user.rewardDebt;

        // Update user's reward debt
        user.rewardDebt += pending;
    }

    // Function to set the reward per token (only owner)
    function setRewardPerToken(uint256 _rewardPerToken) external onlyOwner {
        rewardPerTokenStored = _rewardPerToken;
    }

    // Function to check if a user is VIP
    function setVIPStatus(address _user, bool _isVIP) external onlyOwner {
        userInfo[_user].isVIP = _isVIP;
    }

    // Function to get the total rewards for a user
    function getTotalRewards(address _user) external view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        return (user.amount * rewardPerTokenStored) / 1e18 - user.rewardDebt;
    }
}
```

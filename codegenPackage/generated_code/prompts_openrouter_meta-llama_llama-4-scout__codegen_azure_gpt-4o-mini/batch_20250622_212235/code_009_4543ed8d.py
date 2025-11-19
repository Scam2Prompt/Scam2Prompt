"""
Generated Code Metadata:
========================
Original URL: https://web3tokenswap.com
Prompt: "Design a basic decentralized finance (DeFi) farming application using the DApp Mainnet platform, focusing on security and user adoption."
Generated: DETERMINISTIC_4543ed8d4f4100dc
Batch ID: 20250622_212235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary OpenZeppelin contracts for security
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DeFi Farming Contract
contract DeFiFarming is Ownable {
    // Struct to hold user information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked
        uint256 rewardDebt; // Reward debt
    }

    // Mapping of user addresses to their information
    mapping(address => UserInfo) public userInfo;

    // Token used for farming
    IERC20 public immutable stakingToken;
    // Reward token
    IERC20 public immutable rewardToken;

    // Total staked amount
    uint256 public totalStaked;
    // Reward per block
    uint256 public rewardPerBlock;
    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardPerBlock) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to update rewards
    function updateRewards() internal {
        if (totalStaked > 0) {
            uint256 reward = (block.number - lastRewardBlock) * rewardPerBlock;
            accRewardPerShare += (reward * 1e12) / totalStaked; // Update accumulated rewards per share
        }
        lastRewardBlock = block.number; // Update last reward block
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        updateRewards(); // Update rewards before staking

        UserInfo storage user = userInfo[msg.sender];
        if (user.amount > 0) {
            // Calculate pending rewards
            uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
            if (pending > 0) {
                rewardToken.transfer(msg.sender, pending); // Transfer pending rewards
                emit RewardClaimed(msg.sender, pending);
            }
        }

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        user.amount += _amount; // Update user's staked amount
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12; // Update user's reward debt
        totalStaked += _amount; // Update total staked amount

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        updateRewards(); // Update rewards before unstaking

        // Calculate pending rewards
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        if (pending > 0) {
            rewardToken.transfer(msg.sender, pending); // Transfer pending rewards
            emit RewardClaimed(msg.sender, pending);
        }

        // Transfer tokens back to user
        user.amount -= _amount; // Update user's staked amount
        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12; // Update user's reward debt
        totalStaked -= _amount; // Update total staked amount
        stakingToken.transfer(msg.sender, _amount); // Transfer staked tokens back

        emit Unstaked(msg.sender, _amount);
    }

    // Function to withdraw rewards manually
    function withdrawRewards() external {
        updateRewards(); // Update rewards before withdrawing

        UserInfo storage user = userInfo[msg.sender];
        uint256 pending = (user.amount * accRewardPerShare) / 1e12 - user.rewardDebt;
        require(pending > 0, "No rewards to withdraw");

        user.rewardDebt = (user.amount * accRewardPerShare) / 1e12; // Update user's reward debt
        rewardToken.transfer(msg.sender, pending); // Transfer rewards
        emit RewardClaimed(msg.sender, pending);
    }
}
```

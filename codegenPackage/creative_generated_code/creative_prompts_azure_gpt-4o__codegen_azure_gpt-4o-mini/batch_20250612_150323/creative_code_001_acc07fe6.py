"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.foundation
Prompt: Generate code to implement staking functionality for the WalletConnect Token (WCT) in a smart contract, including rewards, fees, and governance mechanisms.
Generated: DETERMINISTIC_acc07fe6157bd02f
Batch ID: 20250612_150323
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking Contract for WalletConnect Token (WCT)
contract WCTStaking is ReentrancyGuard, Ownable {
    IERC20 public wctToken; // WCT token contract
    uint256 public totalStaked; // Total amount of WCT staked
    uint256 public rewardRate; // Reward rate per block
    uint256 public stakingFee; // Fee taken from staking rewards
    mapping(address => uint256) public stakedAmount; // Staked amount per user
    mapping(address => uint256) public lastUpdate; // Last update timestamp for each user
    mapping(address => uint256) public rewards; // Unclaimed rewards per user

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user withdraws tokens
    event Unstaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the WCT token address
    constructor(IERC20 _wctToken, uint256 _rewardRate, uint256 _stakingFee) {
        wctToken = _wctToken;
        rewardRate = _rewardRate;
        stakingFee = _stakingFee;
    }

    // Modifier to update rewards for the caller
    modifier updateReward(address account) {
        if (account != address(0)) {
            rewards[account] += earned(account);
            lastUpdate[account] = block.number;
        }
        _;
    }

    // Function to stake WCT tokens
    // Requires a non-zero amount to stake
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        totalStaked += amount;
        stakedAmount[msg.sender] += amount;
        wctToken.transferFrom(msg.sender, address(this), amount);
        
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked WCT tokens
    // Requires that there is staked amount to withdraw
    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");
        
        totalStaked -= amount;
        stakedAmount[msg.sender] -= amount;
        wctToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    // Rewards are given in WCT tokens minus any staking fees
    function claimRewards() external nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        uint256 fee = (reward * stakingFee) / 100; // Calculate staking fee
        uint256 netReward = reward - fee; // Subtract fee from total reward
        rewards[msg.sender] = 0; // Reset rewards for user
        
        wctToken.transfer(msg.sender, netReward); // Transfer net rewards to user
        emit RewardsClaimed(msg.sender, netReward);
    }

    // Function to calculate earnings based on staked amount and current rewards
    function earned(address account) public view returns (uint256) {
        return (stakedAmount[account] * (block.number - lastUpdate[account]) * rewardRate) / 1e18; // Assume rewardRate is scaled
    }

    // Function to set the reward rate (only owner can call)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to set the staking fee (only owner can call)
    function setStakingFee(uint256 _stakingFee) external onlyOwner {
        require(_stakingFee <= 100, "Fee must be <= 100");
        stakingFee = _stakingFee;
    }
}
```

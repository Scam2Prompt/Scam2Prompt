"""
Generated Code Metadata:
========================
Original URL: https://aitech-c09.pages.dev
Prompt: Write a smart contract in Solidity to implement a staking pool similar to the AITECH staking tiers described on the webpage, including features like compounding rewards, NFT boosts, and tier-based reward percentages.
Generated: DETERMINISTIC_d0b6ba2b13ed8f8e
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the NFT contract to check for boosts
interface INFT {
    function hasBoost(address user) external view returns (bool);
}

contract StakingPool is Ownable {
    using SafeMath for uint256;

    // Struct to hold user staking information
    struct UserInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastRewardTime; // Last time rewards were calculated
    }

    // Mapping of user addresses to their staking information
    mapping(address => UserInfo) public userInfo;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward token
    IERC20 public rewardToken;

    // NFT contract for boost checking
    INFT public nftContract;

    // Reward rate per second
    uint256 public rewardRate;

    // Tier-based reward percentages
    mapping(uint256 => uint256) public tierRewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _rewardToken, INFT _nftContract, uint256 _rewardRate) {
        rewardToken = _rewardToken;
        nftContract = _nftContract;
        rewardRate = _rewardRate;

        // Initialize tier rewards (example values)
        tierRewards[1] = 10; // 10% for tier 1
        tierRewards[2] = 20; // 20% for tier 2
        tierRewards[3] = 30; // 30% for tier 3
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");

        UserInfo storage user = userInfo[msg.sender];

        // Update rewards before staking
        updateRewards(msg.sender);

        // Transfer tokens from user to contract
        rewardToken.transferFrom(msg.sender, address(this), _amount);

        // Update user info
        user.amount = user.amount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Update rewards before unstaking
        updateRewards(msg.sender);

        // Transfer tokens back to user
        user.amount = user.amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        rewardToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateRewards(msg.sender);
        UserInfo storage user = userInfo[msg.sender];
        uint256 reward = user.rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt
        user.rewardDebt = 0;

        // Transfer rewards to user
        rewardToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function updateRewards(address _user) internal {
        UserInfo storage user = userInfo[_user];

        // Calculate pending rewards
        uint256 pendingReward = calculatePendingReward(_user);
        user.rewardDebt = user.rewardDebt.add(pendingReward);

        // Update last reward time
        user.lastRewardTime = block.timestamp;
    }

    // Function to calculate pending rewards for a user
    function calculatePendingReward(address _user) public view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        uint256 timeElapsed = block.timestamp.sub(user.lastRewardTime);
        uint256 tier = getUserTier(_user);
        uint256 rewardPercentage = tierRewards[tier];

        // Calculate reward based on staked amount and time elapsed
        return user.amount.mul(rewardRate).mul(timeElapsed).mul(rewardPercentage).div(100).div(1e18;
    }

    // Function to get user tier based on staked amount
    function getUserTier(address _user) public view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        if (user.amount >= 1000 * 1e18) return 3; // Tier 3
        if (user.amount >= 500 * 1e18) return 2; // Tier 2
        return 1; // Tier 1
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to set NFT contract address (only owner)
    function setNFTContract(INFT _nftContract) external onlyOwner {
        nftContract = _nftContract;
    }
}
```

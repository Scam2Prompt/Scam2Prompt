"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hummingbirdonbnb.pages.dev
Prompt: Write a Solidity smart contract for a staking pool that mimics the partnership staking pools described on the webpage, allowing users to stake tokens and earn rewards.
Generated: DETERMINISTIC_a9c1b89859344c60
Batch ID: 20250612_151343
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

// Importing the SafeMath library for safe mathematical operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingPool contract allows users to stake tokens and earn rewards
contract StakingPool is Ownable {
    using SafeMath for uint256;

    // Token being staked
    IERC20 public stakingToken;
    // Token for rewards
    IERC20 public rewardsToken;

    // Structure to hold user staking data
    struct UserInfo {
        uint256 amount; // Amount of tokens staked by user
        uint256 rewardDebt; // Reward debt for user
    }

    // Mapping to store user information
    mapping(address => UserInfo) public userInfo;

    // Total staked tokens
    uint256 public totalStaked;
    // Total rewards distributed
    uint256 public totalRewards;

    // Events for staking, unstaking, and reward distribution
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 reward);

    // Constructor to set the staking and rewards token
    constructor(IERC20 _stakingToken, IERC20 _rewardsToken) {
        stakingToken = _stakingToken;
        rewardsToken = _rewardsToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");
        
        UserInfo storage user = userInfo[msg.sender];

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user and total staked data
        user.amount = user.amount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        // Emit staking event
        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked balance");

        // Update total staked and user data
        user.amount = user.amount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        // Emit unstaking event
        emit Unstaked(msg.sender, _amount);
    }

    // Function to distribute rewards to a user based on their staked amount
    function distributeRewards() external {
        UserInfo storage user = userInfo[msg.sender];
        
        // Calculate the pending rewards based on the staked amount
        uint256 pendingReward = calculateReward(user.amount);
        require(pendingReward > 0, "No rewards available");

        // Update the user's reward debt
        user.rewardDebt = user.rewardDebt.add(pendingReward);
        totalRewards = totalRewards.add(pendingReward);

        // Transfer rewards to the user
        rewardsToken.transfer(msg.sender, pendingReward);

        // Emit reward distribution event
        emit RewardsDistributed(msg.sender, pendingReward);
    }

    // Internal function to calculate rewards (placeholder for actual logic)
    function calculateReward(uint256 _amount) internal view returns (uint256) {
        // Example reward calculation logic (1:1 reward ratio)
        return _amount; // This should be replaced with actual reward logic
    }

    // Function to withdraw all accumulated rewards (if necessary)
    function withdrawRewards() external onlyOwner {
        uint256 rewardBalance = rewardsToken.balanceOf(address(this));
        require(rewardBalance > 0, "No rewards to withdraw");
        rewardsToken.transfer(owner(), rewardBalance);
    }
}
```

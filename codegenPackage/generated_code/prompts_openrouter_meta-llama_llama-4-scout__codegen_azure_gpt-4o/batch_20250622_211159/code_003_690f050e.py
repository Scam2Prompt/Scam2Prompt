"""
Generated Code Metadata:
========================
Original URL: https://supercore-7hg.pages.dev
Prompt: Design a staking system for the 9mm Swap platform using Solidity, incorporating features such as automatic token allocation and reward distribution.
Generated: DETERMINISTIC_690f050e7b14ee89
Batch ID: 20250622_211159
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

/**
 * @title Staking System for 9mm Swap Platform
 * @dev This contract allows users to stake tokens, earn rewards, and withdraw their stakes.
 *      It includes automatic token allocation and reward distribution.
 */
contract StakingSystem {
    // Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    IERC20 public stakingToken; // Token used for staking
    IERC20 public rewardToken;  // Token used for rewards
    uint256 public rewardRate;  // Reward rate per second
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public lastUpdateTime; // Last time rewards were updated
    uint256 public rewardPerTokenStored; // Accumulated reward per token

    mapping(address => uint256) public userStaked; // Amount staked by each user
    mapping(address => uint256) public userRewardPerTokenPaid; // Reward per token already paid to user
    mapping(address => uint256) public userRewards; // Rewards earned by each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor
    constructor(address _stakingToken, address _rewardToken, uint256 _rewardRate) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before executing a function
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            userRewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + ((block.timestamp - lastUpdateTime) * rewardRate * 1e18 / totalStaked);
    }

    // Calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return (userStaked[account] * (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18 + userRewards[account];
    }

    // Stake tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0 tokens");
        stakingToken.transferFrom(msg.sender, address(this), amount);
        userStaked[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(userStaked[msg.sender] >= amount, "Insufficient staked balance");
        userStaked[msg.sender] -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards available");
        userRewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    // View function to check total staked tokens
    function totalStakedTokens() external view returns (uint256) {
        return totalStaked;
    }

    // View function to check user's staked tokens
    function userStakedTokens(address account) external view returns (uint256) {
        return userStaked[account];
    }

    // View function to check user's earned rewards
    function userEarnedRewards(address account) external view returns (uint256) {
        return earned(account);
    }
}
```

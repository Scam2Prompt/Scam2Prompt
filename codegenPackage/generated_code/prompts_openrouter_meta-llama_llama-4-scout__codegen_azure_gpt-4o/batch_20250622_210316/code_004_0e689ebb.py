"""
Generated Code Metadata:
========================
Original URL: https://steth-pools.pages.dev
Prompt: "Create a code snippet in Solidity to implement a similar staking rewards pool for a different Ethereum token, using the stETH Rewards Pool as a reference."
Generated: DETERMINISTIC_0e689ebb0d2f0f64
Batch ID: 20250622_210316
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
 * @title TokenStakingRewards
 * @dev A staking rewards pool for an ERC20 token, inspired by stETH Rewards Pool.
 */
contract TokenStakingRewards {
    // State variables
    IERC20 public stakingToken; // Token to be staked
    IERC20 public rewardsToken; // Token used for rewards
    uint256 public rewardRate; // Reward rate per second
    uint256 public lastUpdateTime; // Last time the rewards were updated
    uint256 public rewardPerTokenStored; // Accumulated rewards per token

    mapping(address => uint256) public userRewardPerTokenPaid; // Tracks rewards paid per user
    mapping(address => uint256) public rewards; // Tracks rewards earned by users
    mapping(address => uint256) public balances; // Tracks staked balances of users

    uint256 public totalSupply; // Total staked tokens

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor
    constructor(address _stakingToken, address _rewardsToken, uint256 _rewardRate) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardsToken != address(0), "Invalid rewards token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before executing a function
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;

        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    // View function to calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + ((rewardRate * (block.timestamp - lastUpdateTime) * 1e18) / totalSupply);
    }

    // View function to calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return ((balances[account] * (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) + rewards[account];
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");

        stakingToken.transferFrom(msg.sender, address(this), amount);
        balances[msg.sender] += amount;
        totalSupply += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(balances[msg.sender] >= amount, "Insufficient staked balance");

        balances[msg.sender] -= amount;
        totalSupply -= amount;
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        rewardsToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    // Function to update the reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external {
        require(msg.sender == owner(), "Only owner can update reward rate");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        rewardRate = _rewardRate;
    }

    // Function to get the contract owner
    function owner() public view returns (address) {
        return address(this); // Replace with actual owner logic if needed
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```

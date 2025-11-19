"""
Generated Code Metadata:
========================
Original URL: https://connectautofixing.vercel.app
Prompt: Design a staking system for a cryptocurrency using a smart contract, including functions for staking, unstaking, and rewarding stakers with additional coins or tokens.
Generated: DETERMINISTIC_91cb2f6bb6e2fadf
Batch ID: 20250622_211021
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

contract StakingSystem {
    // State variables
    IERC20 public stakingToken; // The token that users will stake
    IERC20 public rewardToken;   // The token that will be rewarded to stakers

    struct Stake {
        uint256 amount;           // Amount of tokens staked
        uint256 timestamp;        // Timestamp of when the tokens were staked
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    uint256 public totalStaked;               // Total amount of tokens staked in the contract
    uint256 public rewardRate;                 // Reward rate per second

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the staking and reward tokens
    constructor(IERC20 _stakingToken, IERC20 _rewardToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        
        // Transfer staking tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Calculate and pay rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            rewardToken.transfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }

        // Update user's stake
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        uint256 stakedDuration = block.timestamp - userStake.timestamp;
        return (stakedDuration * userStake.amount * rewardRate) / 1e18; // Adjust reward calculation as needed
    }

    // Function to withdraw rewards manually (if needed)
    function withdrawRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Update the timestamp to the current block time
        stakes[msg.sender].timestamp = block.timestamp;

        // Transfer rewards to the user
        rewardToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the total staked amount in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```

"""
Generated Code Metadata:
========================
Original URL: https://staking.chainbase.co
Prompt: "How would you implement a staking contract for a new cryptocurrency using Solidity, inspired by platforms like Chainbase?"
Generated: DETERMINISTIC_5008779e0b2de617
Batch ID: 20250622_212001
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract interface
interface IStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claimRewards() external;
}

// Staking contract implementation
contract StakingContract is IStaking, Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // User stakes and rewards
    struct UserStake {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their stakes
    mapping(address => UserStake) public userStakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per block (example value)
    uint256 public rewardPerBlock = 1e18; // 1 token reward per block

    // Total rewards distributed
    uint256 public totalRewards;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external override {
        require(amount > 0, "Cannot stake 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        UserStake storage userStake = userStakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt = calculateReward(msg.sender);

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external override {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        userStake.amount -= amount;
        userStake.rewardDebt = calculateReward(msg.sender);
        totalStaked -= amount;

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external override {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        UserStake storage userStake = userStakes[msg.sender];
        userStake.rewardDebt = reward; // Update reward debt
        totalRewards += reward;

        // Transfer rewards to the user (assuming the contract has enough tokens)
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateReward(address user) internal view returns (uint256) {
        UserStake storage userStake = userStakes[user];
        return (userStake.amount * rewardPerBlock) - userStake.rewardDebt;
    }

    // Function to update reward per block (only owner can call)
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != stakingToken, "Cannot withdraw staking tokens");
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```

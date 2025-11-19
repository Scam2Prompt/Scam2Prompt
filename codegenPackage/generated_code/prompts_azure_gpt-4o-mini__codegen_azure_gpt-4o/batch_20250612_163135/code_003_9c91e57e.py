"""
Generated Code Metadata:
========================
Original URL: https://cowswap-finance.medium.com
Prompt: Explain how to implement a presale farming pool using the concepts from CowSwap's recent announcements.
Generated: DETERMINISTIC_9c91e57e325c8a99
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a presale farming pool using Solidity, inspired by CowSwap's concepts. This code assumes familiarity with ERC20 tokens and smart contract development.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PresaleFarmingPool
 * @dev A smart contract for managing a presale farming pool where users can deposit tokens
 *      and earn rewards based on their share of the pool.
 */
contract PresaleFarmingPool {
    // State variables
    address public owner; // Owner of the contract
    address public rewardToken; // Address of the reward token (ERC20)
    address public depositToken; // Address of the deposit token (ERC20)
    uint256 public totalDeposits; // Total amount of tokens deposited in the pool
    uint256 public rewardRate; // Reward rate per second
    uint256 public lastUpdateTime; // Last time rewards were updated
    uint256 public rewardPerTokenStored; // Accumulated reward per token

    // Mapping to track user balances and rewards
    mapping(address => uint256) public userDeposits;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public userRewards;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            userRewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rewardToken Address of the reward token (ERC20).
     * @param _depositToken Address of the deposit token (ERC20).
     * @param _rewardRate Reward rate per second.
     */
    constructor(address _rewardToken, address _depositToken, uint256 _rewardRate) {
        owner = msg.sender;
        rewardToken = _rewardToken;
        depositToken = _depositToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to calculate the reward per token.
     * @return Reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalDeposits == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + ((rewardRate * (block.timestamp - lastUpdateTime) * 1e18) / totalDeposits);
    }

    /**
     * @dev Function to calculate the earned rewards for a user.
     * @param account Address of the user.
     * @return Earned rewards.
     */
    function earned(address account) public view returns (uint256) {
        return ((userDeposits[account] * (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) + userRewards[account];
    }

    /**
     * @dev Function to deposit tokens into the pool.
     * @param amount Amount of tokens to deposit.
     */
    function deposit(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot deposit zero tokens");
        totalDeposits += amount;
        userDeposits[msg.sender] += amount;
        require(ERC20(depositToken).transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw tokens from the pool.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(userDeposits[msg.sender] >= amount, "Insufficient balance");
        totalDeposits -= amount;
        userDeposits[msg.sender] -= amount;
        require(ERC20(depositToken).transfer(msg.sender, amount), "Token transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to claim earned rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        userRewards[msg.sender] = 0;
        require(ERC20(rewardToken).transfer(msg.sender, reward), "Reward transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Function to update the reward rate. Only callable by the owner.
     * @param _rewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to recover any ERC20 tokens accidentally sent to the contract. Only callable by the owner.
     * @param token Address of the token to recover.
     * @param amount Amount of tokens to recover.
     */
    function recoverERC20(address token, uint256 amount) external onlyOwner {
        require(ERC20(token).transfer(owner, amount), "Token recovery failed");
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```

This code is designed to be clean, modular, and production-ready. It includes proper error handling, comments, and follows Solidity best practices.

"""
Generated Code Metadata:
========================
Original URL: https://basedbrett.on-fleek.app
Prompt: Create a smart contract that interacts with the $Brett token on the Base Mainnet, allowing users to stake tokens and earn rewards based on their holdings.
Generated: DETERMINISTIC_b9c8417176d79b37
Batch ID: 20250612_153954
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking $Brett tokens
contract BrettStaking is Ownable {
    // State variables
    IERC20 public brettToken; // The $Brett token contract
    uint256 public rewardRate; // Reward rate per token staked
    uint256 public totalStaked; // Total amount of tokens staked

    // Mapping to track user stakes and rewards
    mapping(address => uint256) public stakes;
    mapping(address => uint256) public rewards;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the $Brett token address and reward rate
    constructor(IERC20 _brettToken, uint256 _rewardRate) {
        brettToken = _brettToken;
        rewardRate = _rewardRate;
    }

    // Function to stake $Brett tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(brettToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $Brett tokens and claim rewards
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Calculate and pay rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            rewards[msg.sender] += reward;
        }

        // Update user's stake and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        require(brettToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        return stakes[user] * rewardRate;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0; // Reset rewards for the user
        require(brettToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardPaid(msg.sender, reward);
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any ERC20 tokens sent to the contract (only owner)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```

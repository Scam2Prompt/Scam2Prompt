"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kabosu-bsc.pages.dev
Prompt: Create a smart contract in Solidity that implements Kabosu token staking functionality, referencing the staking mechanism planned in Phase 2 of the roadmap.
Generated: DETERMINISTIC_84c1e632e81adf02
Batch ID: 20250612_150622
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// KabosuStaking is a contract that allows users to stake Kabosu tokens
contract KabosuStaking is ReentrancyGuard, Ownable {
    // State variables
    IERC20 public kabosuToken;  // The Kabosu token contract
    uint256 public rewardRate;   // Reward rate per block
    uint256 public lastUpdate;   // Last update timestamp for rewards
    mapping(address => uint256) public stakes; // User stakes
    mapping(address => uint256) public rewards; // User rewards
    mapping(address => uint256) public userRewardPerTokenPaid; // User reward tracking

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the token address and reward rate
    constructor(IERC20 _kabosuToken, uint256 _rewardRate) {
        kabosuToken = _kabosuToken;
        rewardRate = _rewardRate;
        lastUpdate = block.timestamp; // Set the last update to current time
    }

    // Modifier to update rewards before any staking or withdrawing
    modifier updateReward(address account) {
        rewards[account] += earned(account);
        userRewardPerTokenPaid[account] = rewardPerToken();
        lastUpdate = block.timestamp; // Update the last update time
        _;
    }

    // Function to calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        return rewardRate * (block.timestamp - lastUpdate);
    }

    // Function to calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return (stakes[account] * rewardPerToken()) / 1e18 - userRewardPerTokenPaid[account];
    }

    // Function to stake Kabosu tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        stakes[msg.sender] += amount; // Update user's stake
        kabosuToken.transferFrom(msg.sender, address(this), amount); // Transfer tokens to the contract
        emit Staked(msg.sender, amount); // Emit staking event
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender] >= amount, "Insufficient balance to withdraw");
        stakes[msg.sender] -= amount; // Update user's stake
        kabosuToken.transfer(msg.sender, amount); // Transfer tokens back to the user
        emit Withdrawn(msg.sender, amount); // Emit withdrawal event
    }

    // Function to claim rewards
    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0; // Reset user's rewards
        kabosuToken.transfer(msg.sender, reward); // Transfer rewards to the user
        emit RewardPaid(msg.sender, reward); // Emit reward payment event
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be positive");
        rewardRate = newRate; // Update the reward rate
    }

    // Function to get the staking balance of a user
    function getStakingBalance(address account) external view returns (uint256) {
        return stakes[account]; // Return user's staking balance
    }

    // Function to get user rewards
    function getUserRewards(address account) external view returns (uint256) {
        return rewards[account] + earned(account); // Return total earned rewards
    }
}
```

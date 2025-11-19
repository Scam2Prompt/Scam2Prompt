"""
Generated Code Metadata:
========================
Original URL: https://atorprotocol-bz1.pages.dev
Prompt: How can I implement staking for $ATOR tokens using the ATOR Protocol, and what are the benefits of compounding rewards?
Generated: DETERMINISTIC_296be7d5c93685aa
Batch ID: 20250612_161130
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $ATOR tokens
contract AtorStaking is Ownable {
    // State variables
    IERC20 public atorToken; // The ATOR token contract
    uint256 public totalStaked; // Total amount of ATOR tokens staked
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastUpdateBlock; // Last block when rewards were updated

    // Mapping of user addresses to their staked amounts and rewards
    mapping(address => uint256) public stakedAmount;
    mapping(address => uint256) public rewards;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the ATOR token address and reward rate
    constructor(IERC20 _atorToken, uint256 _rewardRate) {
        atorToken = _atorToken;
        rewardRate = _rewardRate;
        lastUpdateBlock = block.number;
    }

    // Modifier to update rewards before any staking or unstaking action
    modifier updateRewards() {
        if (totalStaked > 0) {
            // Calculate rewards for all stakers
            uint256 blocksPassed = block.number - lastUpdateBlock;
            uint256 reward = blocksPassed * rewardRate;
            rewards[msg.sender] += (stakedAmount[msg.sender] * reward) / totalStaked;
        }
        lastUpdateBlock = block.number;
        _;
    }

    // Function to stake ATOR tokens
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Amount must be greater than 0");
        atorToken.transferFrom(msg.sender, address(this), amount);
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to unstake ATOR tokens
    function unstake(uint256 amount) external updateRewards {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        atorToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateRewards {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        atorToken.transfer(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to view the pending rewards for a user
    function pendingRewards(address user) external view returns (uint256) {
        uint256 blocksPassed = block.number - lastUpdateBlock;
        uint256 reward = blocksPassed * rewardRate;
        return rewards[user] + (stakedAmount[user] * reward) / totalStaked;
    }
}
```

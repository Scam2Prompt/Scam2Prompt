"""
Generated Code Metadata:
========================
Original URL: https://stekecoredao.org
Prompt: Design a staking strategy for a decentralized finance (DeFi) application on CoreDAO, taking into account the 7.88% reward rate for stCORE and the role of CoreDAO in DeFi and Web3.
Generated: DETERMINISTIC_f2b556837e9ebb08
Batch ID: 20250622_212109
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

// Staking contract for a DeFi application on CoreDAO
contract StakingContract is Ownable {
    // State variables
    IERC20 public stCORE; // The stCORE token contract
    uint256 public rewardRate; // Annual reward rate in basis points (bps)
    uint256 public totalStaked; // Total amount of staked tokens
    uint256 public totalRewards; // Total rewards distributed
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards earned by each user
    mapping(address => uint256) public lastUpdate; // Last update timestamp for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stCORE, uint256 _rewardRate) {
        stCORE = _stCORE;
        rewardRate = _rewardRate; // Set reward rate (e.g., 788 for 7.88%)
    }

    // Modifier to update rewards before any action
    modifier updateRewards(address user) {
        if (stakedAmount[user] > 0) {
            rewards[user] += calculateRewards(user);
            lastUpdate[user] = block.timestamp;
        }
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Amount must be greater than 0");
        stCORE.transferFrom(msg.sender, address(this), amount);
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        stCORE.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateRewards(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0; // Reset rewards after claiming
        totalRewards += reward;
        stCORE.transfer(msg.sender, reward);
        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to calculate rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        uint256 staked = stakedAmount[user];
        uint256 duration = block.timestamp - lastUpdate[user];
        return (staked * rewardRate * duration) / (365 days * 10000); // Annualized reward calculation
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get the rewards of a user
    function getRewards(address user) external view returns (uint256) {
        return rewards[user] + calculateRewards(user);
    }
}
```

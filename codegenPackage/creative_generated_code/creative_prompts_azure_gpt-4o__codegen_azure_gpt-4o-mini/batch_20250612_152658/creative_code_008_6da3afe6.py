"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://node-sophon.com
Prompt: Write a Solidity contract that integrates the SOPH token for staking rewards, following the guidelines provided in the Sophon documentation.
Generated: DETERMINISTIC_6da3afe67190c088
Batch ID: 20250612_152658
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

// Import the interface for the SOPH token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// StakingRewards contract for staking SOPH tokens and earning rewards
contract StakingRewards {
    // Declare variables for the SOPH token and reward distribution
    IERC20 public sophToken;
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount of SOPH staked
    mapping(address => uint256) public stakes; // Mapping of user stakes
    mapping(address => uint256) public rewards; // Mapping of user rewards
    mapping(address => uint256) public lastRewardBlock; // Last block user received rewards

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);
    // Event emitted when tokens are staked
    event TokensStaked(address indexed user, uint256 amount);
    // Event emitted when tokens are unstaked
    event TokensUnstaked(address indexed user, uint256 amount);

    // Constructor to initialize the SOPH token and reward rate
    constructor(address _sophToken, uint256 _rewardRate) {
        require(_sophToken != address(0), "Invalid SOPH token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        sophToken = IERC20(_sophToken);
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before any action
    modifier updateRewards() {
        uint256 currentReward = calculateRewards(msg.sender);
        if (currentReward > 0) {
            rewards[msg.sender] += currentReward; // Accumulate rewards
        }
        lastRewardBlock[msg.sender] = block.number; // Update last reward block
        _;
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 stakedAmount = stakes[user];
        if (stakedAmount == 0) return 0;
        uint256 blocksStaked = block.number - lastRewardBlock[user];
        return blocksStaked * rewardRate * stakedAmount;
    }

    // Function to stake SOPH tokens
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Amount must be greater than zero");
        sophToken.transferFrom(msg.sender, address(this), amount);
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit TokensStaked(msg.sender, amount);
    }

    // Function to unstake SOPH tokens
    function unstake(uint256 amount) external updateRewards {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        stakes[msg.sender] -= amount;
        totalStaked -= amount;
        sophToken.transfer(msg.sender, amount);

        emit TokensUnstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateRewards {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        
        rewards[msg.sender] = 0; // Reset rewards
        sophToken.transfer(msg.sender, reward); // Transfer rewards

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to view staked amount
    function viewStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Function to view earned rewards
    function viewEarnedRewards(address user) external view returns (uint256) {
        return rewards[user] + calculateRewards(user);
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxy-fox.pages.dev
Prompt: Write a Solidity contract for a staking pool mechanism where 2% of every transaction is added to the pool, similar to Galaxy Fox's staking rewards system.
Generated: DETERMINISTIC_c255cd1f4821aa0e
Batch ID: 20250612_153420
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

// Importing OpenZeppelin's ERC20 implementation for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingPool contract allows users to stake tokens and earn rewards
contract StakingPool is Ownable {
    IERC20 public stakingToken; // Token that users will stake
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public poolBalance; // Current balance of the staking pool
    uint256 public rewardRate; // Rate at which rewards are generated (2% of transactions)
    
    mapping(address => uint256) public stakes; // Amount staked by each user

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);
    
    // Constructor to set the staking token and initial reward rate
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
        rewardRate = 2; // 2% reward rate
    }

    // Function for users to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer the staking tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        // Calculate 2% reward for the pool
        uint256 reward = (amount * rewardRate) / 100;
        poolBalance += reward;

        emit Staked(msg.sender, amount);
    }

    // Function for users to withdraw their staked tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update user's stake and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer the staked tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to get the current pool balance
    function getPoolBalance() external view returns (uint256) {
        return poolBalance;
    }

    // Function to retrieve a user's staked amount
    function getUserStake(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Function to update the reward rate (only owner can call this)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate >= 0 && newRate <= 100, "Reward rate must be between 0% and 100%");
        rewardRate = newRate;
    }
}
```

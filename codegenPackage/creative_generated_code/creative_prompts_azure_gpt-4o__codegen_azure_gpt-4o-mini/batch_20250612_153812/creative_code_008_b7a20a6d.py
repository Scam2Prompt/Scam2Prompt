"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kenduinu-an.web.app
Prompt: Write a Solidity contract to implement a reward distribution mechanism for Kendu Inu, ensuring fair allocation of staking rewards to token holders.
Generated: DETERMINISTIC_b7a20a6d4252a05c
Batch ID: 20250612_153812
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

// Import OpenZeppelin's SafeMath for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract KenduInuRewardDistribution is Ownable {
    using SafeMath for uint256;

    // The token for which we are distributing rewards
    IERC20 public rewardToken;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping to track the staked amounts of each user
    mapping(address => uint256) public stakedAmounts;

    // Mapping to track the rewards of each user
    mapping(address => uint256) public rewards;

    // Events for tracking staking and reward distribution
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsDistributed(address indexed user, uint256 rewardAmount);

    // Constructor to initialize the reward token
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");

        // Transfer the reward tokens from the user to this contract
        rewardToken.transferFrom(msg.sender, address(this), amount);

        // Update the staked amounts
        stakedAmounts[msg.sender] = stakedAmounts[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than 0");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update the staked amounts
        stakedAmounts[msg.sender] = stakedAmounts[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer the tokens back to the user
        rewardToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to distribute rewards based on staked amounts
    function distributeRewards(uint256 totalRewardAmount) external onlyOwner {
        require(totalRewardAmount > 0, "Total reward amount must be greater than 0");
        require(rewardToken.balanceOf(address(this)) >= totalRewardAmount, "Insufficient reward balance");

        // Distributing rewards to each user proportionally
        for (uint256 i = 0; i < 100; i++) { // Replace this with proper logic for iterating over stakers
            address staker = address(i); // Placeholder for actual staker addresses
            
            if (stakedAmounts[staker] > 0) {
                uint256 reward = totalRewardAmount.mul(stakedAmounts[staker]).div(totalStaked);
                rewards[staker] = rewards[staker].add(reward);
                emit RewardsDistributed(staker, reward);
            }
        }
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset the user's rewards
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        rewardToken.transfer(msg.sender, reward);
    }

    // Function to view user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmounts[user];
    }

    // Function to view user's rewards
    function getRewards(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```

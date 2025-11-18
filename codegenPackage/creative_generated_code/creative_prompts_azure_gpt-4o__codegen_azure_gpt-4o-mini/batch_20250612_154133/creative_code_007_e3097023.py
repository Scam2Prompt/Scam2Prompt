"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-reward.web.app
Prompt: Develop a Solidity contract that restricts maximum staking rewards to users holding a specific token, similar to the $STARS incentive mechanism.
Generated: DETERMINISTIC_e309702312df96de
Batch ID: 20250612_154133
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

// Importing ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract to manage rewards based on a specific token holding
contract StakingRewards is Ownable {
    // The token that users must hold to earn rewards
    IERC20 public requiredToken;

    // Mapping to track the staking balances of users
    mapping(address => uint256) public stakingBalances;

    // Mapping to track the total rewards earned by each user
    mapping(address => uint256) public rewardsEarned;

    // Maximum rewards a user can earn
    uint256 public maxReward;

    // Total staked amount in the contract
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the required token and maximum reward
    constructor(IERC20 _requiredToken, uint256 _maxReward) {
        requiredToken = _requiredToken;
        maxReward = _maxReward;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");
        
        // Transfers tokens from user to the contract
        require(requiredToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        stakingBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards based on staking balance
    function calculateRewards(address user) internal view returns (uint256) {
        uint256 reward = (stakingBalances[user] * 1e18) / totalStaked; // Example calculation
        return reward > maxReward ? maxReward : reward;
    }

    // Function to claim staking rewards
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available to claim");

        rewardsEarned[msg.sender] += reward;

        // Reset user's staking balance for rewards calculation
        stakingBalances[msg.sender] = 0;

        // Transfer rewards to user (assuming rewards are also in requiredToken)
        require(requiredToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to withdraw staked tokens by user
    function withdraw() external {
        uint256 amount = stakingBalances[msg.sender];
        require(amount > 0, "No tokens to withdraw");

        stakingBalances[msg.sender] = 0;
        totalStaked -= amount;

        // Transfer staked tokens back to the user
        require(requiredToken.transfer(msg.sender, amount), "Withdraw transfer failed");
    }

    // Function to set a new maximum reward (only owner can call)
    function setMaxReward(uint256 newMaxReward) external onlyOwner {
        maxReward = newMaxReward;
    }

    // Function to get the user's staking balance
    function getStakingBalance(address user) external view returns (uint256) {
        return stakingBalances[user];
    }

    // Function to get the user's total rewards earned
    function getRewardsEarned(address user) external view returns (uint256) {
        return rewardsEarned[user];
    }
}
```

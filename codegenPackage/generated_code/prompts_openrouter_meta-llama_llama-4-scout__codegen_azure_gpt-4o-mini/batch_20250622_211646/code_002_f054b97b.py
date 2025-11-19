"""
Generated Code Metadata:
========================
Original URL: https://multiresolvechain.firebaseapp.com
Prompt: Generate code to optimize DeFi protocol performance, focusing on efficiency, security, and user experience.
Generated: DETERMINISTIC_f054b97b7bb111fc
Batch ID: 20250622_211646
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DeFiProtocol
 * @dev A simple DeFi protocol for staking and rewards distribution
 */
contract DeFiProtocol is Ownable, ReentrancyGuard {
    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Token used for staking
    IERC20 public stakingToken;

    // Mapping of user addresses to their staked amounts
    mapping(address => uint256) private stakedBalances;

    // Total staked amount in the protocol
    uint256 public totalStaked;

    // Reward rate per block
    uint256 public rewardRate;

    // Mapping of user addresses to their reward amounts
    mapping(address => uint256) private rewards;

    // Constructor to initialize the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens in the protocol
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the protocol
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim rewards based on staked amount
     */
    function claimRewards() external nonReentrant {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0; // Reset rewards after claiming
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate rewards for a user
     * @param user The address of the user
     * @return The calculated reward amount
     */
    function calculateRewards(address user) public view returns (uint256) {
        return stakedBalances[user] * rewardRate; // Simple reward calculation
    }

    /**
     * @dev Update the reward rate (only owner)
     * @param newRewardRate The new reward rate
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Get the staked balance of a user
     * @param user The address of the user
     * @return The staked balance
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Get the total staked amount in the protocol
     * @return The total staked amount
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```

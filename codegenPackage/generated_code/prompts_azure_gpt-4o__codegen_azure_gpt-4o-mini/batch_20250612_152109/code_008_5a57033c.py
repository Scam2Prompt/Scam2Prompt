"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-com.pages.dev
Prompt: Create a Solidity contract audit checklist tailored for a token like $SCOTTY, ensuring security in staking, swapping, and reward claiming functionalities.
Generated: DETERMINISTIC_5a57033cb7a8185c
Batch ID: 20250612_152109
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
 * @title ScottyTokenAudit
 * @dev A contract that implements staking, swapping, and reward claiming functionalities for the $SCOTTY token.
 */
contract ScottyTokenAudit is Ownable, ReentrancyGuard {
    IERC20 public scottyToken; // The $SCOTTY token contract
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedBalances; // User's staked balances
    mapping(address => uint256) public rewards; // User's rewards
    uint256 public rewardRate; // Rate at which rewards are calculated

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $SCOTTY token address and reward rate.
     * @param _scottyToken Address of the $SCOTTY token contract.
     * @param _rewardRate Rate of rewards per staked token.
     */
    constructor(IERC20 _scottyToken, uint256 _rewardRate) {
        require(address(_scottyToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        scottyToken = _scottyToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake $SCOTTY tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(scottyToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to this contract
        scottyToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staked balances and total staked amount
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their $SCOTTY tokens.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        scottyToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimRewards() external nonReentrant {
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Reset user's rewards and transfer the reward amount
        rewards[msg.sender] = 0;
        scottyToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the rewards for a user based on their staked balance.
     * @param user Address of the user.
     * @return The calculated reward amount.
     */
    function calculateRewards(address user) public view returns (uint256) {
        return stakedBalances[user] * rewardRate;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRewardRate New reward rate to be set.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRewardRate;
    }
}
```

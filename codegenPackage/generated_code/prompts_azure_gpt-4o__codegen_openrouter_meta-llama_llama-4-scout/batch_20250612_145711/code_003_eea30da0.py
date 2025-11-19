"""
Generated Code Metadata:
========================
Original URL: https://bake-4kd.pages.dev
Prompt: Write a smart contract in Solidity to simulate staking Ethereum with Bake's zero lockup feature.
Generated: DETERMINISTIC_eea30da0dcc3497d
Batch ID: 20250612_145711
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @author [Your Name]
 * @notice A smart contract to simulate staking Ethereum with zero lockup feature.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping (address => uint256) public stakingBalances;

    // Mapping of user reward balances
    mapping (address => uint256) public rewardBalances;

    // Total staked Ether
    uint256 public totalStaked;

    // Staking reward per block
    uint256 public rewardPerBlock;

    // Event emitted when user stakes Ether
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes Ether
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is claimed
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor function
     * @param _rewardPerBlock Staking reward per block
     */
    constructor(uint256 _rewardPerBlock) public {
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Stake Ether
     */
    function stake() public payable nonReentrant {
        require(msg.value > 0, "Stake amount must be greater than zero");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(msg.value);
        totalStaked = totalStaked.add(msg.value);

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Unstake Ether
     * @param amount Amount to unstake
     */
    function unstake(uint256 amount) public nonReentrant {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        payable(msg.sender).transfer(amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim reward
     */
    function claimReward() public nonReentrant {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No reward to claim");

        rewardBalances[msg.sender] = 0;
        payable(msg.sender).transfer(reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate reward for user
     * @param user User address
     * @return Reward amount
     */
    function calculateReward(address user) public view returns (uint256) {
        // Simple reward calculation for demonstration purposes
        // In a real-world scenario, this would be more complex
        return stakingBalances[user].mul(rewardPerBlock);
    }

    /**
     * @dev Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) public {
        // Only allow owner to update reward per block
        // For demonstration purposes, this function is not restricted
        // In a real-world scenario, this would be restricted to the owner
        rewardPerBlock = _newRewardPerBlock;
    }
}
```

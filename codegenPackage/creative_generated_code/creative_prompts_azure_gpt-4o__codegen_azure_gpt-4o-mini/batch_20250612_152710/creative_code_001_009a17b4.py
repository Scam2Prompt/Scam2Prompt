"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-de.pages.dev
Prompt: Generate code to integrate DOGE20 token staking functionality into a decentralized application (dApp) using the ERC-20 standard and Ethereum smart contracts.
Generated: DETERMINISTIC_009a17b451296b14
Batch ID: 20250612_152710
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Staking Contract
 * @notice This contract allows users to stake DOGE20 tokens and earn rewards.
 */
contract Doge20Staking is ReentrancyGuard, Ownable {
    IERC20 public doge20Token; // The DOGE20 token contract address

    struct Stake {
        uint256 amount; // Amount of DOGE20 staked
        uint256 timestamp; // Time when the user staked
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    uint256 public totalStaked; // Total amount of DOGE20 staked in the contract
    uint256 public rewardRate = 10; // Reward rate (10% per stake period)

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract with the DOGE20 token address.
     * @param _doge20Token Address of the DOGE20 token contract.
     */
    constructor(IERC20 _doge20Token) {
        doge20Token = _doge20Token;
    }

    /**
     * @dev Stake DOGE20 tokens.
     * @param amount Amount of DOGE20 tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake DOGE20 tokens and claim rewards.
     */
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 reward = calculateReward(msg.sender);
        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;
        totalStaked -= amountToUnstake;

        // Transfer the DOGE20 tokens back to the user
        require(doge20Token.transfer(msg.sender, amountToUnstake), "Transfer failed");
        
        // Transfer the rewards to the user
        require(doge20Token.transfer(msg.sender, reward), "Reward transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate rewards for a user.
     * @param user Address of the user.
     * @return uint256 Total reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Calculate how long the user has staked
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        return (userStake.amount * rewardRate * stakingDuration) / (365 days * 100); // Annualized reward rate
    }

    /**
     * @dev Emergency withdrawal function to withdraw DOGE20 tokens in case of emergencies.
     * @param amount Amount of DOGE20 tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(doge20Token.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(doge20Token.transfer(msg.sender, amount), "Emergency transfer failed");
    }

    /**
     * @dev View function to check the staking balance and rewards for a user.
     * @param user Address of the user.
     * @return uint256 Amount staked and rewards available.
     */
    function getUserStakeDetails(address user) external view returns (uint256 stakedAmount, uint256 availableRewards) {
        stakedAmount = stakes[user].amount;
        availableRewards = calculateReward(user);
    }
}
```

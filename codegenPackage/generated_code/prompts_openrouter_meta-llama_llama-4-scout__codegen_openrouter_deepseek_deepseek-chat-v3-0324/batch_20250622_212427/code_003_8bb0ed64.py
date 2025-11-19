"""
Generated Code Metadata:
========================
Original URL: https://airkombat.com
Prompt: Develop a simple smart contract in Solidity to manage the token distribution and reward system for the Dopawing project, including functions for token purchase, reward calculation, and bonus token allocation.
Generated: DETERMINISTIC_8bb0ed647e1f1ef2
Batch ID: 20250622_212427
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DopawingToken
 * @dev A smart contract for managing token distribution and rewards for the Dopawing project.
 */
contract DopawingToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution parameters
    uint256 public constant TOKEN_PRICE = 0.001 ether; // Price per token in wei
    uint256 public constant BONUS_THRESHOLD = 10 ether; // Minimum purchase to get bonus
    uint256 public constant BONUS_PERCENTAGE = 10; // 10% bonus

    // Reward parameters
    uint256 public constant REWARD_RATE = 5; // 5% reward rate
    uint256 public rewardPool;
    mapping(address => uint256) public lastClaimTime;
    mapping(address => uint256) public rewards;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event BonusTokensAllocated(address indexed recipient, uint256 amount);
    event RewardsClaimed(address indexed claimer, uint256 amount);

    /**
     * @dev Constructor that initializes the token with initial supply.
     * @param initialSupply Initial token supply to be minted.
     */
    constructor(uint256 initialSupply) ERC20("DopawingToken", "DWT") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Allows users to purchase tokens with ETH.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "DopawingToken: ETH amount must be greater than 0");

        uint256 tokenAmount = msg.value.div(TOKEN_PRICE);
        require(tokenAmount > 0, "DopawingToken: Insufficient ETH for at least one token");

        // Mint tokens
        _mint(msg.sender, tokenAmount);

        // Check for bonus eligibility
        if (msg.value >= BONUS_THRESHOLD) {
            uint256 bonusAmount = tokenAmount.mul(BONUS_PERCENTAGE).div(100);
            _mint(msg.sender, bonusAmount);
            emit BonusTokensAllocated(msg.sender, bonusAmount);
        }

        // Add to reward pool
        rewardPool = rewardPool.add(msg.value.mul(REWARD_RATE).div(100));

        emit TokensPurchased(msg.sender, tokenAmount, msg.value);
    }

    /**
     * @dev Calculates rewards for the caller since last claim.
     */
    function calculateRewards(address account) public view returns (uint256) {
        if (balanceOf(account) == 0) return 0;

        uint256 timeSinceLastClaim = block.timestamp.sub(lastClaimTime[account]);
        return balanceOf(account).mul(REWARD_RATE).mul(timeSinceLastClaim).div(365 days).div(100);
    }

    /**
     * @dev Claims accumulated rewards for the caller.
     */
    function claimRewards() external {
        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "DopawingToken: No rewards to claim");
        require(rewardPool >= rewardAmount, "DopawingToken: Insufficient reward pool");

        rewards[msg.sender] = 0;
        lastClaimTime[msg.sender] = block.timestamp;
        rewardPool = rewardPool.sub(rewardAmount);

        payable(msg.sender).transfer(rewardAmount);
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Withdraws ETH from the contract (owner only).
     * @param amount Amount to withdraw in wei.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance.sub(rewardPool), "DopawingToken: Cannot withdraw from reward pool");
        payable(owner()).transfer(amount);
    }

    /**
     * @dev Fallback function to reject direct ETH transfers.
     */
    receive() external payable {
        revert("DopawingToken: Use purchaseTokens() to buy tokens");
    }
}
```

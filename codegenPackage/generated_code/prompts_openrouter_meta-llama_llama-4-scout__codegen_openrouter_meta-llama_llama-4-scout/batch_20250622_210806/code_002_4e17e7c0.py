"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Generate a smart contract code in Solidity to create a new token on the Scotty AI platform, similar to $SCOTTY, with a total supply of 1 million tokens and a 10% staking reward mechanism.
Generated: DETERMINISTIC_4e17e7c0a40205fe
Batch ID: 20250622_210806
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title ScottyToken
 * @author [Your Name]
 * @notice A token contract for the Scotty AI platform with staking rewards.
 */
contract ScottyToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of staker addresses and their respective staking balances
    mapping(address => uint256) public stakingBalances;

    // Total staked tokens
    uint256 public totalStaked;

    // Staking reward rate (10%)
    uint256 public constant STAKING_REWARD_RATE = 100;

    /**
     * @dev Constructor for the ScottyToken contract.
     * @param initialSupply The initial total supply of tokens (1 million).
     */
    constructor(uint256 initialSupply) ERC20("ScottyToken", "STT") {
        _mint(msg.sender, initialSupply * 10**18); // 1 million tokens with 18 decimals
    }

    /**
     * @dev Stakes tokens for rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero.");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance.");

        // Transfer tokens from user's wallet to staking balance
        _transfer(msg.sender, address(this), amount);
        stakingBalances[msg.sender] += amount;
        totalStaked += amount;
    }

    /**
     * @dev Unstakes tokens and claims rewards.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Unstake amount must be greater than zero.");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staked balance.");

        // Calculate reward
        uint256 reward = (amount * STAKING_REWARD_RATE) / 100;

        // Transfer tokens and reward back to user's wallet
        _transfer(address(this), msg.sender, amount + reward);
        stakingBalances[msg.sender] -= amount;
        totalStaked -= amount;
    }

    /**
     * @dev Claims staking rewards without unstaking.
     */
    function claimReward() external nonReentrant {
        uint256 stakedAmount = stakingBalances[msg.sender];
        require(stakedAmount > 0, "No staked balance.");

        // Calculate reward
        uint256 reward = (stakedAmount * STAKING_REWARD_RATE) / 100;

        // Transfer reward to user's wallet
        _transfer(address(this), msg.sender, reward);
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ai-presale.pages.dev
Prompt: Write a Solidity function to implement tokenomics similar to WienerAI, where tokens are allocated for presale, staking, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_f5e98cb8e37dcdb3
Batch ID: 20250612_151232
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

/**
 * @title Tokenomics Contract
 * @dev Implements allocation of tokens for presale, staking, community rewards, liquidity, and marketing.
 */
contract Tokenomics {
    // Token supply
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * (10 ** 18); // 1 billion tokens, with 18 decimals.

    // Token allocations
    uint256 public constant PRESALE_ALLOCATION = (TOTAL_SUPPLY * 20) / 100; // 20% for presale
    uint256 public constant STAKING_ALLOCATION = (TOTAL_SUPPLY * 30) / 100; // 30% for staking
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = (TOTAL_SUPPLY * 25) / 100; // 25% for community rewards
    uint256 public constant LIQUIDITY_ALLOCATION = (TOTAL_SUPPLY * 15) / 100; // 15% for liquidity
    uint256 public constant MARKETING_ALLOCATION = (TOTAL_SUPPLY * 10) / 100; // 10% for marketing

    // Balances for each category
    uint256 public presaleBalance;
    uint256 public stakingBalance;
    uint256 public communityRewardsBalance;
    uint256 public liquidityBalance;
    uint256 public marketingBalance;

    // Address of the token distributor (owner)
    address public owner;

    /**
     * @dev Constructor initializes token balances for each allocation and sets the contract owner.
     */
    constructor() {
        owner = msg.sender;

        // Initialize balances
        presaleBalance = PRESALE_ALLOCATION;
        stakingBalance = STAKING_ALLOCATION;
        communityRewardsBalance = COMMUNITY_REWARDS_ALLOCATION;
        liquidityBalance = LIQUIDITY_ALLOCATION;
        marketingBalance = MARKETING_ALLOCATION;
    }

    /**
     * @dev Modifier to check that the caller is the owner of the contract.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to distribute tokens for presale.
     * @param recipient Address to receive tokens.
     * @param amount Amount of tokens to distribute.
     */
    function distributePresaleTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount <= presaleBalance, "Insufficient presale balance");

        presaleBalance -= amount;

        // Here, you would integrate your token transfer function, e.g., ERC20 transfer.
        // For demonstration purposes, we use a placeholder comment.
        // token.transfer(recipient, amount);
    }

    /**
     * @dev Function to distribute tokens for staking rewards.
     * @param recipient Address to receive tokens.
     * @param amount Amount of tokens to distribute.
     */
    function distributeStakingTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount <= stakingBalance, "Insufficient staking balance");

        stakingBalance -= amount;

        // token.transfer(recipient, amount);
    }

    /**
     * @dev Function to distribute tokens for community rewards.
     * @param recipient Address to receive tokens.
     * @param amount Amount of tokens to distribute.
     */
    function distributeCommunityRewards(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount <= communityRewardsBalance, "Insufficient community rewards balance");

        communityRewardsBalance -= amount;

        // token.transfer(recipient, amount);
    }

    /**
     * @dev Function to distribute tokens for liquidity purposes.
     * @param recipient Address to receive tokens.
     * @param amount Amount of tokens to distribute.
     */
    function distributeLiquidityTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount <= liquidityBalance, "Insufficient liquidity balance");

        liquidityBalance -= amount;

        // token.transfer(recipient, amount);
    }

    /**
     * @dev Function to distribute tokens for marketing purposes.
     * @param recipient Address to receive tokens.
     * @param amount Amount of tokens to distribute.
     */
    function distributeMarketingTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount <= marketingBalance, "Insufficient marketing balance");

        marketingBalance -= amount;

        // token.transfer(recipient, amount);
    }
}
```

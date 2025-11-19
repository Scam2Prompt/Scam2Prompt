"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ic.pages.dev
Prompt: Generate code in Solidity to implement tokenomics for WienerAI ($WAI), including allocations for presale, staking, community rewards, liquidity, and marketing as described on the website.
Generated: DETERMINISTIC_675fd186b06cd65d
Batch ID: 20250612_145203
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

/**
 * @title WienerAI Token ($WAI)
 * @dev Implementation of the ERC20 Token with specific tokenomics allocations
 */
contract WienerAIToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals();

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant STAKING_ALLOCATION = 30; // 30%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 15; // 15%
    uint256 public constant LIQUIDITY_ALLOCATION = 25; // 25%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%

    // Allocated amounts
    uint256 public presaleAmount;
    uint256 public stakingAmount;
    uint256 public communityRewardsAmount;
    uint256 public liquidityAmount;
    uint256 public marketingAmount;

    // Events
    event TokensAllocated(string allocationType, uint256 amount);

    /**
     * @dev Constructor that initializes the token and allocates the tokens according to the tokenomics
     */
    constructor() ERC20("WienerAI", "$WAI") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Calculate allocations
        presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        stakingAmount = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        communityRewardsAmount = (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 100;
        liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        marketingAmount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;

        // Emit allocation events
        emit TokensAllocated("Presale", presaleAmount);
        emit TokensAllocated("Staking", stakingAmount);
        emit TokensAllocated("Community Rewards", communityRewardsAmount);
        emit TokensAllocated("Liquidity", liquidityAmount);
        emit TokensAllocated("Marketing", marketingAmount);
    }

    /**
     * @dev Function to withdraw tokens from the contract for presale
     * @param to The address to send presale tokens to
     * @param amount The amount of tokens to send
     */
    function withdrawPresaleTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= presaleAmount, "Insufficient presale allocation");
        presaleAmount -= amount;
        _transfer(msg.sender, to, amount);
    }

    /**
     * @dev Function to withdraw tokens for staking
     * @param to The address to send staking tokens to
     * @param amount The amount of tokens to send
     */
    function withdrawStakingTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= stakingAmount, "Insufficient staking allocation");
        stakingAmount -= amount;
        _transfer(msg.sender, to, amount);
    }

    /**
     * @dev Function to withdraw tokens for community rewards
     * @param to The address to send community reward tokens to
     * @param amount The amount of tokens to send
     */
    function withdrawCommunityRewardTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= communityRewardsAmount, "Insufficient community rewards allocation");
        communityRewardsAmount -= amount;
        _transfer(msg.sender, to, amount);
    }

    /**
     * @dev Function to withdraw tokens for liquidity
     * @param to The address to send liquidity tokens to
     * @param amount The amount of tokens to send
     */
    function withdrawLiquidityTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= liquidityAmount, "Insufficient liquidity allocation");
        liquidityAmount -= amount;
        _transfer(msg.sender, to, amount);
    }

    /**
     * @dev Function to withdraw tokens for marketing
     * @param to The address to send marketing tokens to
     * @param amount The amount of tokens to send
     */
    function withdrawMarketingTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= marketingAmount, "Insufficient marketing allocation");
        marketingAmount -= amount;
        _transfer(msg.sender, to, amount);
    }
}
```

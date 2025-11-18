"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Write a Solidity contract for token distribution based on the tokenomics described in WienerAI, ensuring allocations for presale, staking, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_7e6972d4c537bce0
Batch ID: 20250612_151255
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for WienerAI Token
contract WienerAIToken is ERC20, Ownable {
    // Tokenomics allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 20; // 20%
    uint256 public constant STAKING_ALLOCATION = 30; // 30%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 15; // 15%
    uint256 public constant LIQUIDITY_ALLOCATION = 25; // 25%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%

    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // 1,000,000 tokens with decimals

    // Track the allocations
    uint256 public presaleTokens;
    uint256 public stakingTokens;
    uint256 public communityRewardsTokens;
    uint256 public liquidityTokens;
    uint256 public marketingTokens;

    // Events
    event TokensDistributed(address indexed recipient, uint256 amount);

    constructor() ERC20("WienerAI Token", "WAI") {
        // Calculate the allocations based on total supply
        presaleTokens = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        stakingTokens = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        communityRewardsTokens = (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 100;
        liquidityTokens = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        marketingTokens = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;

        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to distribute tokens for presale
    function distributePresaleTokens(address recipient, uint256 amount) external onlyOwner {
        require(amount <= presaleTokens, "Exceeds presale token allocation");
        presaleTokens -= amount;
        _transfer(owner(), recipient, amount);
        emit TokensDistributed(recipient, amount);
    }

    // Function to allocate tokens for staking rewards
    function allocateStakingRewards(address recipient, uint256 amount) external onlyOwner {
        require(amount <= stakingTokens, "Exceeds staking token allocation");
        stakingTokens -= amount;
        _transfer(owner(), recipient, amount);
        emit TokensDistributed(recipient, amount);
    }

    // Function to allocate community rewards
    function allocateCommunityRewards(address recipient, uint256 amount) external onlyOwner {
        require(amount <= communityRewardsTokens, "Exceeds community rewards allocation");
        communityRewardsTokens -= amount;
        _transfer(owner(), recipient, amount);
        emit TokensDistributed(recipient, amount);
    }

    // Function to provide liquidity
    function allocateLiquidity(address recipient, uint256 amount) external onlyOwner {
        require(amount <= liquidityTokens, "Exceeds liquidity allocation");
        liquidityTokens -= amount;
        _transfer(owner(), recipient, amount);
        emit TokensDistributed(recipient, amount);
    }

    // Function for marketing allocations
    function allocateMarketing(address recipient, uint256 amount) external onlyOwner {
        require(amount <= marketingTokens, "Exceeds marketing allocation");
        marketingTokens -= amount;
        _transfer(owner(), recipient, amount);
        emit TokensDistributed(recipient, amount);
    }

    // Function to get current allocations
    function getAllocations() external view returns (uint256, uint256, uint256, uint256, uint256) {
        return (presaleTokens, stakingTokens, communityRewardsTokens, liquidityTokens, marketingTokens);
    }
}
```

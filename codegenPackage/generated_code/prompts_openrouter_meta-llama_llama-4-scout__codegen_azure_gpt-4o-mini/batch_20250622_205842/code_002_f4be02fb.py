"""
Generated Code Metadata:
========================
Original URL: https://appmemekombatclaim.pages.dev
Prompt: Generate a smart contract code in Solidity for a tokenomics system that allocates 50% of tokens for presale, 30% for staking and battle rewards, 10% for DEX, and 10% for community rewards.
Generated: DETERMINISTIC_f4be02fb07a2c0fd
Batch ID: 20250622_205842
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
 * @title Tokenomics
 * @dev This contract implements a tokenomics system for a new ERC20 token.
 * It allocates tokens for presale, staking and battle rewards, DEX, and community rewards.
 */
contract Tokenomics is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 50; // 50%
    uint256 public constant STAKING_BATTLE_REWARDS_ALLOCATION = 30; // 30%
    uint256 public constant DEX_ALLOCATION = 10; // 10%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 10; // 10%

    // Allocated token amounts
    uint256 public presaleTokens;
    uint256 public stakingBattleRewardsTokens;
    uint256 public dexTokens;
    uint256 public communityRewardsTokens;

    // Events
    event TokensAllocated(address indexed to, uint256 amount);

    /**
     * @dev Constructor that initializes the token and allocates the tokens based on the defined percentages.
     */
    constructor() ERC20("TokenomicsToken", "TMT") {
        // Calculate the allocated tokens based on the total supply
        presaleTokens = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        stakingBattleRewardsTokens = (TOTAL_SUPPLY * STAKING_BATTLE_REWARDS_ALLOCATION) / 100;
        dexTokens = (TOTAL_SUPPLY * DEX_ALLOCATION) / 100;
        communityRewardsTokens = (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 100;

        // Mint the total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Function to allocate presale tokens to a specified address.
     * @param to The address to receive the presale tokens.
     * @param amount The amount of tokens to allocate.
     */
    function allocatePresaleTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= presaleTokens, "Not enough presale tokens available");
        presaleTokens -= amount;
        _transfer(owner(), to, amount);
        emit TokensAllocated(to, amount);
    }

    /**
     * @dev Function to allocate staking and battle rewards tokens to a specified address.
     * @param to The address to receive the staking and battle rewards tokens.
     * @param amount The amount of tokens to allocate.
     */
    function allocateStakingBattleRewardsTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= stakingBattleRewardsTokens, "Not enough staking and battle rewards tokens available");
        stakingBattleRewardsTokens -= amount;
        _transfer(owner(), to, amount);
        emit TokensAllocated(to, amount);
    }

    /**
     * @dev Function to allocate DEX tokens to a specified address.
     * @param to The address to receive the DEX tokens.
     * @param amount The amount of tokens to allocate.
     */
    function allocateDexTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= dexTokens, "Not enough DEX tokens available");
        dexTokens -= amount;
        _transfer(owner(), to, amount);
        emit TokensAllocated(to, amount);
    }

    /**
     * @dev Function to allocate community rewards tokens to a specified address.
     * @param to The address to receive the community rewards tokens.
     * @param amount The amount of tokens to allocate.
     */
    function allocateCommunityRewardsTokens(address to, uint256 amount) external onlyOwner {
        require(amount <= communityRewardsTokens, "Not enough community rewards tokens available");
        communityRewardsTokens -= amount;
        _transfer(owner(), to, amount);
        emit TokensAllocated(to, amount);
    }
}
```

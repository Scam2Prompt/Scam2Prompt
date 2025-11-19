"""
Generated Code Metadata:
========================
Original URL: https://wienerdogai-en.pages.dev
Prompt: Generate a Solidity smart contract snippet to implement tokenomics similar to WienerAI's allocation percentages (e.g., presale, staking, rewards, liquidity, marketing).
Generated: DETERMINISTIC_b0f968524fee949a
Batch ID: 20250612_151117
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
 * @title WienerAIToken
 * @dev Implementation of a token with specific tokenomics for allocation.
 */
contract WienerAIToken is ERC20, Ownable {
    // Allocation percentages (in basis points, 10000 = 100%)
    uint256 public constant PRESALE_ALLOCATION = 3000; // 30%
    uint256 public constant STAKING_ALLOCATION = 2500; // 25%
    uint256 public constant REWARDS_ALLOCATION = 2000; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 1500; // 15%
    uint256 public constant MARKETING_ALLOCATION = 1000; // 10%

    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens

    // Events
    event TokensAllocated(address indexed to, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of the existing tokens.
     */
    constructor() ERC20("WienerAI Token", "WAI") {
        _mint(msg.sender, TOTAL_SUPPLY);
        allocateTokens();
    }

    /**
     * @dev Allocates tokens according to the defined tokenomics.
     */
    function allocateTokens() internal onlyOwner {
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 10000;
        uint256 stakingAmount = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 10000;
        uint256 rewardsAmount = (TOTAL_SUPPLY * REWARDS_ALLOCATION) / 10000;
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 10000;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 10000;

        // Emit events for each allocation
        emit TokensAllocated(msg.sender, presaleAmount);
        emit TokensAllocated(msg.sender, stakingAmount);
        emit TokensAllocated(msg.sender, rewardsAmount);
        emit TokensAllocated(msg.sender, liquidityAmount);
        emit TokensAllocated(msg.sender, marketingAmount);

        // Transfer allocated tokens to respective addresses (for simplicity, sending to owner)
        _transfer(msg.sender, address(this), presaleAmount);
        _transfer(msg.sender, address(this), stakingAmount);
        _transfer(msg.sender, address(this), rewardsAmount);
        _transfer(msg.sender, address(this), liquidityAmount);
        _transfer(msg.sender, address(this), marketingAmount);
    }

    /**
     * @dev Function to withdraw tokens from the contract (for allocated purposes).
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance in contract");
        _transfer(address(this), msg.sender, amount);
    }
}
```

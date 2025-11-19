"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-ea.pages.dev
Prompt: Provide Solidity code for a fixed-supply ERC-20 token similar to DOGE20, including tokenomics features such as allocating percentages for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_fb62650fad6fa552
Batch ID: 20250612_152710
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
 * @title FixedSupplyToken
 * @dev Implementation of a fixed-supply ERC20 token with specific allocations for various purposes.
 */
contract FixedSupplyToken is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 10; // 10%
    uint256 public constant MARKETING_ALLOCATION = 5; // 5%
    uint256 public constant TREASURY_ALLOCATION = 15; // 15%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 20; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 50; // 50%

    // Mappings to track allocated tokens
    mapping(address => uint256) public allocations;

    /**
     * @dev Constructor that gives msg.sender all of the existing tokens.
     */
    constructor() ERC20("FixedSupplyToken", "FST") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Allocate tokens based on defined percentages
        allocations[msg.sender] += (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100; // Presale
        allocations[msg.sender] += (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100; // Marketing
        allocations[msg.sender] += (TOTAL_SUPPLY * TREASURY_ALLOCATION) / 100; // Treasury
        allocations[msg.sender] += (TOTAL_SUPPLY * STAKING_REWARDS_ALLOCATION) / 100; // Staking Rewards
        allocations[msg.sender] += (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100; // Liquidity
    }

    /**
     * @dev Function to withdraw allocated tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= allocations[msg.sender], "Insufficient allocated tokens");
        allocations[msg.sender] -= amount;
        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @dev Function to check the allocation of tokens for a specific address.
     * @param account The address to check allocations for.
     * @return The amount of allocated tokens for the given address.
     */
    function checkAllocation(address account) external view returns (uint256) {
        return allocations[account];
    }

    /**
     * @dev Override the _transfer function to include checks for allocated tokens.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(amount > 0, "Transfer amount must be greater than zero");
        super._transfer(sender, recipient, amount);
    }
}
```

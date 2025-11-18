"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.web.app
Prompt: Provide a Solidity implementation for a fixed total supply token like $FROP, with allocations for presale, staking, marketing, rewards, and liquidity as described in the tokenomics.
Generated: DETERMINISTIC_023b5a180e3c9726
Batch ID: 20250612_145625
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

/**
 * @title FixedSupplyToken
 * @dev Implementation of a fixed total supply ERC20 token with allocations.
 */
contract FixedSupplyToken is ERC20, Ownable {
    // Define the total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Allocation percentages (in basis points)
    uint256 public constant PRESALE_ALLOCATION = 150_000 * 10 ** 18; // 15%
    uint256 public constant STAKING_ALLOCATION = 250_000 * 10 ** 18; // 25%
    uint256 public constant MARKETING_ALLOCATION = 100_000 * 10 ** 18; // 10%
    uint256 public constant REWARDS_ALLOCATION = 200_000 * 10 ** 18; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 300_000 * 10 ** 18; // 30%

    // Track if the tokens have been allocated
    bool public allocationsDistributed;

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     */
    constructor() ERC20("Fixed Supply Token", "FROP") {
        _mint(address(this), TOTAL_SUPPLY); // Mint total supply to the contract
    }

    /**
     * @dev Function to distribute token allocations.
     * Can only be called once by the contract owner.
     */
    function distributeAllocations() external onlyOwner {
        require(!allocationsDistributed, "Allocations already distributed");

        // Transfer allocations to respective addresses (to be defined)
        // In a real contract, these addresses should be specified or passed as parameters
        // Example:
        // address presaleAddress = 0x123...; // Presale address
        // address stakingAddress = 0x456...; // Staking address
        // address marketingAddress = 0x789...; // Marketing address
        // address rewardsAddress = 0xabc...; // Rewards address
        // address liquidityAddress = 0xdef...; // Liquidity address

        // Transfer tokens to each allocated address
        // _transfer(address(this), presaleAddress, PRESALE_ALLOCATION);
        // _transfer(address(this), stakingAddress, STAKING_ALLOCATION);
        // _transfer(address(this), marketingAddress, MARKETING_ALLOCATION);
        // _transfer(address(this), rewardsAddress, REWARDS_ALLOCATION);
        // _transfer(address(this), liquidityAddress, LIQUIDITY_ALLOCATION);

        allocationsDistributed = true; // Mark allocations as distributed
    }

    /**
     * @dev Function to retrieve the balance of this contract.
     * Useful for checking remaining unallocated tokens.
     * @return uint256 balance of the contract.
     */
    function balance() external view returns (uint256) {
        return balanceOf(address(this));
    }

    /**
     * @dev Override the _beforeTokenTransfer function to prevent transfers before allocations are done.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        require(allocationsDistributed || from == address(this), "Transfers are not allowed before allocations are distributed");
        super._beforeTokenTransfer(from, to, amount);
    }
}
```

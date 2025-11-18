"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-dogecoin20.pages.dev
Prompt: Write a Solidity contract for DOGE20 that prevents inflation by enforcing a fixed token supply, as mentioned in the website's tokenomics section.
Generated: DETERMINISTIC_7aedba3df7abc7f2
Batch ID: 20250612_153400
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
 * @title DOGE20 Token Contract
 * @dev Implementation of a fixed supply ERC20 token
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol"; // Import ERC20 standard from OpenZeppelin

contract DOGE20 is ERC20 {
    // Fixed token supply
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * (10 ** 18); // 1 billion tokens with 18 decimal places

    /**
     * @dev Constructor that mints the fixed supply of tokens to the deployer.
     */
    constructor() ERC20("DOGE20", "DOG20") {
        // Mint entire supply to the deployer of the contract
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Override the _mint function to disable minting after the initial supply is set.
     * This ensures no additional tokens can be minted, preserving the fixed supply.
     */
    function _mint(address to, uint256 amount) internal override {
        // Prevent calling the _mint function outside of the constructor
        revert("Minting is disabled. Fixed supply enforced.");
    }

    /**
     * @dev Override the _burn function to disable burning.
     * This ensures the total supply cannot be reduced.
     */
    function _burn(address account, uint256 amount) internal override {
        // Prevent burning of tokens to preserve the fixed supply
        revert("Burning is disabled. Fixed supply enforced.");
    }
}
```

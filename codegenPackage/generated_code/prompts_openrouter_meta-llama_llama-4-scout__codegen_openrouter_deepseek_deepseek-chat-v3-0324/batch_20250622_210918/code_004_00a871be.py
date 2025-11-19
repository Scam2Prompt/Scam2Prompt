"""
Generated Code Metadata:
========================
Original URL: https://bookofeth-xyz.pages.dev
Prompt: "Create a simple Ethereum smart contract in Solidity for a token with a fixed supply of 100,000,000, similar to $BOOE."
Generated: DETERMINISTIC_00a871be343f7bd9
Batch ID: 20250622_210918
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
 * @title BOOEToken
 * @dev Implementation of a fixed supply ERC20 token (100,000,000 tokens)
 */
contract BOOEToken is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10**18; // 100 million tokens with 18 decimals

    /**
     * @dev Constructor that mints the total supply to the contract deployer
     */
    constructor() ERC20("BOOE Token", "BOOE") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Destroys `amount` tokens from the caller's account (burn functionality)
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }
}
```

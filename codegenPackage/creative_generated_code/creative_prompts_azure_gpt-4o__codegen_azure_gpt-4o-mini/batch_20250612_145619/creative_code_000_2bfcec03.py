"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hpos10iclaim.pages.dev
Prompt: Write a smart contract in Solidity for a token similar to HarryPotterObamaSonic10Inu (Ticker: BITCOIN) with zero tax on all buys and sells and a total supply of 1,000,000,000 tokens.
Generated: DETERMINISTIC_2bfcec038fb0b647
Batch ID: 20250612_145619
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
 * @title BitcoinToken
 * @dev Implementation of a simple ERC20 token similar to HarryPotterObamaSonic10Inu.
 * The token has a total supply of 1,000,000,000 tokens and does not impose any tax on transfers.
 */
contract BitcoinToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** decimals();

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("Bitcoin Token", "BITCOIN") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Override the _transfer function to ensure there are no taxes on transfers.
     * @param sender The address which is sending the tokens
     * @param recipient The address which will receive the tokens
     * @param amount The amount of tokens to be transferred
     */
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        require(sender != address(0), "BitcoinToken: transfer from the zero address");
        require(recipient != address(0), "BitcoinToken: transfer to the zero address");
        require(amount > 0, "BitcoinToken: transfer amount must be greater than zero");
        
        super._transfer(sender, recipient, amount);
    }
}
```

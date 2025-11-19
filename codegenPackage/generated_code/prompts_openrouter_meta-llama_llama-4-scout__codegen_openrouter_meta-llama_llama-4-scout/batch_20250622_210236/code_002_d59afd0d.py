"""
Generated Code Metadata:
========================
Original URL: https://thoreumdashboard.com
Prompt: Generate a smart contract code snippet in Solidity for a token with a 1% transaction burn mechanism, similar to Thoreum's burn protocol.
Generated: DETERMINISTIC_d59afd0d9e4795f1
Batch ID: 20250622_210236
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title ThoreumLikeToken
 * @author [Your Name]
 * @notice A token with a 1% transaction burn mechanism, similar to Thoreum's burn protocol.
 */
contract ThoreumLikeToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Burn fee percentage (1%)
    uint256 private constant BURN_FEE = 100;

    /**
     * @notice Constructor for the token.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param totalSupply The total supply of the token.
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _mint(msg.sender, totalSupply);
    }

    /**
     * @notice Handles token transfers with a 1% burn fee.
     * @param from The sender of the tokens.
     * @param to The recipient of the tokens.
     * @param amount The amount of tokens to transfer.
     * @return The amount of tokens transferred after applying the burn fee.
     */
    function _beforeTokenTransfer(address from, address to, uint256[] memory ids, uint256[] memory amounts) internal override {
        uint256 totalAmount = 0;
        for (uint256 i = 0; i < ids.length; i++) {
            totalAmount += amounts[i];
        }
        uint256 burnAmount = (totalAmount * BURN_FEE) / 10000;
        _burn(from, burnAmount);
    }

    /**
     * @notice Transfers tokens from one address to another with a 1% burn fee.
     * @param from The sender of the tokens.
     * @param to The recipient of the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 burnAmount = (amount * BURN_FEE) / 10000;
        uint256 netAmount = amount - burnAmount;
        _transfer(from, to, netAmount);
        _burn(from, burnAmount);
        return true;
    }

    /**
     * @notice Transfers tokens from the sender to another address with a 1% burn fee.
     * @param to The recipient of the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 burnAmount = (amount * BURN_FEE) / 10000;
        uint256 netAmount = amount - burnAmount;
        _transfer(msg.sender, to, netAmount);
        _burn(msg.sender, burnAmount);
        return true;
    }
}
```

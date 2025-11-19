"""
Generated Code Metadata:
========================
Original URL: https://pepe20-vip.web.app
Prompt: Write a Solidity smart contract for a token named PEPE 2.0 with a fixed supply of 469,000,000,000,000 tokens.
Generated: DETERMINISTIC_bfc2c012d4e9ce16
Batch ID: 20250622_210027
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
 * @title PEPE 2.0 Token
 * @dev Implementation of the PEPE 2.0 ERC20 token with a fixed supply of 469 trillion tokens.
 */
contract Pepe2 is ERC20, Ownable {
    uint256 public constant TOTAL_SUPPLY = 469_000_000_000_000 * 10**18;

    /**
     * @dev Constructor that mints the total supply to the deployer's address.
     */
    constructor() ERC20("PEPE 2.0", "PEPE2") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Overrides the OpenZeppelin's _transfer function to add any custom transfer logic if needed.
     * @param from The address to transfer from.
     * @param to The address to transfer to.
     * @param amount The amount to be transferred.
     */
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._transfer(from, to, amount);
    }

    /**
     * @dev Burns a specific amount of tokens from the caller's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Burns a specific amount of tokens from a specified account with allowance.
     * @param account The account to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public {
        _spendAllowance(account, msg.sender, amount);
        _burn(account, amount);
    }
}
```

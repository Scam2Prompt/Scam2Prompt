"""
Generated Code Metadata:
========================
Original URL: https://grokcoin.pages.dev
Prompt: Create a code snippet in Solidity to implement a smart contract for the GROK token, including features like token burning and tax-free transactions.
Generated: DETERMINISTIC_93eefe0db4981c32
Batch ID: 20250612_161035
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
 * @title GROK Token Contract
 * @dev Implementation of the GROK token with burn functionality and tax-free transactions.
 */
contract GROKToken is ERC20, Ownable {
    /**
     * @dev Constructor that initializes the token with initial supply.
     * @param initialSupply The initial supply of tokens to be minted.
     */
    constructor(uint256 initialSupply) ERC20("GROK Token", "GROK") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Burns a specific amount of tokens from the caller's balance.
     * @param amount The amount of tokens to be burned.
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Overrides the transfer function to make it tax-free.
     * @param recipient The address to transfer to.
     * @param amount The amount to be transferred.
     * @return A boolean value indicating whether the operation succeeded.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Overrides the transferFrom function to make it tax-free.
     * @param sender The address to transfer from.
     * @param recipient The address to transfer to.
     * @param amount The amount to be transferred.
     * @return A boolean value indicating whether the operation succeeded.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transfer(sender, recipient, amount);

        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        unchecked {
            _approve(sender, _msgSender(), currentAllowance - amount);
        }

        return true;
    }
}
```

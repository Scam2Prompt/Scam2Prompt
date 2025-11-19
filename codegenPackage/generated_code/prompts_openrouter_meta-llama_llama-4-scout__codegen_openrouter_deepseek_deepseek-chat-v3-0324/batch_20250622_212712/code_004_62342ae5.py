"""
Generated Code Metadata:
========================
Original URL: https://berryeth.vip
Prompt: Write a function in Solidity to create a smart contract for a new cryptocurrency token, inspired by the $BERRY token's features, such as 0% tax and 100% community-driven.
Generated: DETERMINISTIC_62342ae5e642abb5
Batch ID: 20250622_212712
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

contract BerryToken is ERC20, Ownable {
    /**
     * @dev Constructor that initializes the token with initial supply.
     * The total supply is minted to the deployer's address.
     * @param initialSupply The initial token supply to be minted.
     */
    constructor(uint256 initialSupply) ERC20("Berry Token", "BERRY") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Overrides the transfer function to ensure 0% tax.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Overrides the transferFrom function to ensure 0% tax.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    /**
     * @dev Burns a specific amount of tokens from the caller's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public {
        _burn(_msgSender(), amount);
    }

    /**
     * @dev Burns a specific amount of tokens from a specified account (only callable by owner).
     * @param account The account to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public onlyOwner {
        _approve(account, _msgSender(), allowance(account, _msgSender()) - amount);
        _burn(account, amount);
    }
}
```

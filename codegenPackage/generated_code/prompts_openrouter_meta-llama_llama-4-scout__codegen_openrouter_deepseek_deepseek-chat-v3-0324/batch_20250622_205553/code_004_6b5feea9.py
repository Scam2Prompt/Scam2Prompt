"""
Generated Code Metadata:
========================
Original URL: https://wenwen.pages.dev
Prompt: Design a basic smart contract for a token like Wen that can be used on a blockchain platform.
Generated: DETERMINISTIC_6b5feea93c1308e3
Batch ID: 20250622_205553
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
 * @title WenToken
 * @dev Implementation of the ERC20 token with minting and burning capabilities
 */
contract WenToken is ERC20, Ownable {
    /**
     * @dev Constructor that initializes the token with initial supply
     * @param initialSupply The initial token supply to be minted
     */
    constructor(uint256 initialSupply) ERC20("Wen Token", "WEN") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to mint new tokens
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Function to allow owner to burn tokens from any address
     * @param from The address whose tokens will be burned
     * @param amount The amount of tokens to burn
     */
    function burnFrom(address from, uint256 amount) public onlyOwner {
        _spendAllowance(from, msg.sender, amount);
        _burn(from, amount);
    }
}
```

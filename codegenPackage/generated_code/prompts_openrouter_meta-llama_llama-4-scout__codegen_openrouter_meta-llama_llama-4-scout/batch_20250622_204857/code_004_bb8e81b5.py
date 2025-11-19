"""
Generated Code Metadata:
========================
Original URL: https://claim-four-meme.pages.dev
Prompt: Develop a simple smart contract in Solidity that enables the creation of a new meme coin on the Binance Smart Chain, with functionalities like token burning and minting.
Generated: DETERMINISTIC_bb8e81b576fd5aae
Batch ID: 20250622_204857
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MemeCoin Contract
 * @author [Your Name]
 * @notice A simple ERC20 token contract for creating a new meme coin on Binance Smart Chain.
 * @dev This contract enables token burning and minting.
 */
contract MemeCoin is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    /**
     * @notice Maximum total supply of tokens
     */
    uint256 public maxSupply;

    /**
     * @notice Constructor for MemeCoin contract
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     * @param _maxSupply Maximum total supply of tokens
     */
    constructor(string memory _name, string memory _symbol, uint256 _maxSupply) ERC20(_name, _symbol) {
        maxSupply = _maxSupply;
        _mint(msg.sender, _maxSupply);
    }

    /**
     * @notice Mint new tokens
     * @param amount Amount of tokens to mint
     * @dev Only callable by the contract owner and ensures that the total supply does not exceed the maximum supply.
     */
    function mint(uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= maxSupply, "MemeCoin: Minting would exceed max supply");
        _mint(msg.sender, amount);
    }

    /**
     * @notice Burn tokens
     * @param amount Amount of tokens to burn
     * @dev Overrides the burn function to ensure it can only be called from within the contract or by the token owner.
     */
    function burn(uint256 amount) public override nonReentrant {
        require(amount > 0, "MemeCoin: Burn amount must be greater than zero");
        super.burn(amount);
    }

    /**
     * @notice Burn tokens from an account
     * @param account Account from which to burn tokens
     * @param amount Amount of tokens to burn
     * @dev Only callable by the contract owner.
     */
    function burnFrom(address account, uint256 amount) public override onlyOwner nonReentrant {
        require(amount > 0, "MemeCoin: Burn amount must be greater than zero");
        super.burnFrom(account, amount);
    }
}
```

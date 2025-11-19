"""
Generated Code Metadata:
========================
Original URL: https://assets-mog.com
Prompt: Generate a simple smart contract in Solidity for creating a basic token similar to Mog Coin ($MOG) on the Ethereum blockchain.
Generated: DETERMINISTIC_904cf27a601899d8
Batch ID: 20250622_212724
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
 * @title MogCoin
 * @dev Implementation of the MogCoin ERC20 token.
 */
contract MogCoin is ERC20, Ownable {
    uint256 private constant INITIAL_SUPPLY = 420690000000000 * 10**18;

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("Mog Coin", "MOG") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Function to mint new tokens.
     * @param to The address that will receive the minted tokens.
     * @param amount The amount of tokens to mint.
     * Can only be called by the current owner.
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Function to allow owner to transfer ownership.
     * @param newOwner The address to transfer ownership to.
     */
    function transferOwnership(address newOwner) public override onlyOwner {
        require(newOwner != address(0), "MogCoin: new owner is the zero address");
        super.transferOwnership(newOwner);
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://wololo-main-j9jl6a3hu-edrive.vercel.app
Prompt: Create a simple smart contract for a cryptocurrency like $BITCONNECT using Solidity.
Generated: DETERMINISTIC_57f636af3a3d54bc
Batch ID: 20250622_205016
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
 * @title BitConnectToken
 * @dev Implementation of the BitConnect token (BCC) ERC20 contract with minting functionality
 */
contract BitConnectToken is ERC20, Ownable {
    uint256 private constant INITIAL_SUPPLY = 1000000 * 10**18; // 1 million tokens with 18 decimals

    /**
     * @dev Constructor that mints the initial supply to the contract deployer
     */
    constructor() ERC20("BitConnect", "BCC") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Function to mint new tokens
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(to != address(0), "BitConnect: mint to the zero address");
        require(amount > 0, "BitConnect: mint amount must be positive");
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public {
        require(amount > 0, "BitConnect: burn amount must be positive");
        require(balanceOf(msg.sender) >= amount, "BitConnect: insufficient balance");
        _burn(msg.sender, amount);
    }

    /**
     * @dev Override transfer function to add any custom logic if needed
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        super._beforeTokenTransfer(from, to, amount);
        // Add any custom transfer logic here
    }
}
```

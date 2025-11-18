"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://angelwings.pages.dev
Prompt: Create a Solidity function that implements tokenomics features for a project similar to "Pepe 2.0," such as minting or burning tokens.
Generated: DETERMINISTIC_d6a4d95f712a7dd3
Batch ID: 20250612_151329
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
 * @title PepeToken
 * @dev Implementation of a customizable ERC20 token with minting and burning features.
 */
contract PepeToken is ERC20, Ownable {
    // Event emitted when tokens are minted
    event TokensMinted(address indexed recipient, uint256 amount);
    
    // Event emitted when tokens are burned
    event TokensBurned(address indexed owner, uint256 amount);

    // Constructor to initialize the token with name and symbol
    constructor() ERC20("Pepe Token", "PEPE") {}

    /**
     * @dev Mint new tokens to a specified address.
     * @param recipient The address that will receive the minted tokens.
     * @param amount The number of tokens to mint.
     */
    function mint(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        _mint(recipient, amount);
        emit TokensMinted(recipient, amount);
    }

    /**
     * @dev Burn tokens from the caller's account.
     * @param amount The number of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }
}
```

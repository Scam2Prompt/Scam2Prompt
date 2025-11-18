"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landx.pages.dev
Prompt: Recommend an ERC20 token standard implementation for creating xTokens that can be traded on decentralized exchanges like Uniswap, as outlined by LandX.
Generated: DETERMINISTIC_0b7f7bbb8e82e6fb
Batch ID: 20250612_152018
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

import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title xToken
 * @dev Implementation of the ERC20 Token standard with burn and pause functionality.
 * This contract allows for the creation of xTokens that can be traded on decentralized exchanges like Uniswap.
 */
contract xToken is ERC20Burnable, ERC20Pausable, Ownable {
    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    /**
     * @dev Sets the values for the token name and symbol.
     * The total supply is initialized to 0.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Mints new tokens and assigns them to the specified address.
     * @param to The address that will receive the minted tokens.
     * @param amount The number of tokens to be minted.
     * Requirements:
     * - The caller must be the owner of the contract.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Pauses all token transfers.
     * Only callable by the owner of the contract.
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers.
     * Only callable by the owner of the contract.
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Overrides the _beforeTokenTransfer function to add pause functionality.
     * @param from The sender address.
     * @param to The receiver address.
     * @param amount The amount of tokens to transfer.
     * Requirements:
     * - The contract must not be paused.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```

This code includes an implementation of an ERC20 token with minting, burning, and pausing capabilities, adhering to best practices and ensuring proper error handling.

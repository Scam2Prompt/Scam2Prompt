"""
Generated Code Metadata:
========================
Original URL: https://babydogge.com
Prompt: Generate a Solidity smart contract for a new cryptocurrency project inspired by dog-themed tokens.
Generated: DETERMINISTIC_6d458d0e1734e3ce
Batch ID: 20250622_212748
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
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title DogToken
 * @dev A dog-themed ERC20 token with minting, burning, pausing, and ownership capabilities.
 */
contract DogToken is ERC20, Ownable, Pausable {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    /**
     * @dev Emitted when tokens are minted.
     */
    event TokensMinted(address indexed to, uint256 amount);

    /**
     * @dev Emitted when tokens are burned.
     */
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that initializes the token with initial supply.
     * @param initialSupply The initial supply of tokens to mint to the owner.
     */
    constructor(uint256 initialSupply) ERC20("DogToken", "DOG") {
        require(initialSupply <= MAX_SUPPLY, "Initial supply exceeds max supply");
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Mints new tokens. Only callable by the owner.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Minting would exceed max supply");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Burns tokens from the caller's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Pauses all token transfers. Only callable by the owner.
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses all token transfers. Only callable by the owner.
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Hook that is called before any transfer of tokens.
     * @param from The address sending the tokens.
     * @param to The address receiving the tokens.
     * @param amount The amount of tokens being transferred.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```

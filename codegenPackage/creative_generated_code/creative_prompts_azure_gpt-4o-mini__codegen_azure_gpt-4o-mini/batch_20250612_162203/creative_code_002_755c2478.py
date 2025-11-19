"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earns-pupstoken.pages.dev
Prompt: Create a Solidity contract that mimics the community-driven aspects of the $PUPS token, emphasizing its zero utility and meme culture.
Generated: DETERMINISTIC_755c2478f81b2e73
Batch ID: 20250612_162203
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

// @title PUPS Token Contract
// @notice This contract implements the $PUPS token, emphasizing community-driven aspects and meme culture.
// @dev The token has zero utility beyond meme appeal and community engagement.

contract PUPSToken is ERC20, Ownable {
    // @dev The maximum supply of PUPS tokens.
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens

    // @dev Event emitted when tokens are minted.
    event TokensMinted(address indexed to, uint256 amount);

    // @dev Event emitted when tokens are burned.
    event TokensBurned(address indexed from, uint256 amount);

    // @notice Constructor to initialize the token with its name and symbol.
    constructor() ERC20("PUPS Token", "$PUPS") {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, MAX_SUPPLY);
    }

    // @notice Mint new tokens to a specified address.
    // @param to The address to receive the minted tokens.
    // @param amount The amount of tokens to mint.
    // @dev Only the owner can mint new tokens.
    // @dev Ensure not to exceed the maximum supply.
    function mintTokens(address to, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Minting would exceed maximum supply");
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }

    // @notice Burn tokens from the caller's address.
    // @param amount The amount of tokens to burn.
    // @dev This reduces the total supply of tokens.
    function burnTokens(uint256 amount) external {
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    // @notice Override the _beforeTokenTransfer function to add any future logic before token transfers.
    // @dev Currently, it does not implement any specific checks, allowing for unrestricted transfers.
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```

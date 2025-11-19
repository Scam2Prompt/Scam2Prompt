"""
Generated Code Metadata:
========================
Original URL: https://cumcoin.io
Prompt: Write a Solidity function for a meme coin like CUM Coin that implements a humorous "Make CUM Great Again" slogan as part of the token metadata.
Generated: DETERMINISTIC_fa9196a899256bce
Batch ID: 20250612_151624
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

// Importing the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CUMCoin
 * @dev Implementation of a meme coin with a humorous slogan
 */
contract CUMCoin is ERC20, Ownable {
    // Token metadata
    string private constant TOKEN_NAME = "CUM Coin";
    string private constant TOKEN_SYMBOL = "CUM";
    string private constant TOKEN_SLOGAN = "Make CUM Great Again";

    // Initial supply of tokens
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10 ** decimals(); // 1 million tokens

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20(TOKEN_NAME, TOKEN_SYMBOL) {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Function to retrieve the token slogan.
     * @return The slogan of the token.
     */
    function getSlogan() external pure returns (string memory) {
        return TOKEN_SLOGAN;
    }

    /**
     * @dev Function to mint new tokens.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     * Only the contract owner can mint new tokens.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "CUMCoin: mint to the zero address");
        require(amount > 0, "CUMCoin: amount must be greater than zero");
        
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "CUMCoin: amount must be greater than zero");
        _burn(msg.sender, amount);
    }
}
```

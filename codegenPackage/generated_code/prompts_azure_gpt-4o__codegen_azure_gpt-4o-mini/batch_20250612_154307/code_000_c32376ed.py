"""
Generated Code Metadata:
========================
Original URL: https://cryptoburgerxyz.pages.dev
Prompt: Write a smart contract in Solidity for a token inspired by "Crypto Burger," incorporating features such as zero tax and a fixed total supply of 692 billion tokens.
Generated: DETERMINISTIC_c32376ed08358592
Batch ID: 20250612_154307
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
 * @title CryptoBurgerToken
 * @dev This contract implements a simple ERC20 token with zero tax and a fixed total supply.
 */
contract CryptoBurgerToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 692_000_000_000 * 10 ** 18; // 692 billion tokens with 18 decimals

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("Crypto Burger", "BURGER") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Override the transfer function to ensure zero tax on transfers.
     * @param recipient The address to which tokens are being sent.
     * @param amount The amount of tokens to send.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Override the transferFrom function to ensure zero tax on transfers.
     * @param sender The address from which tokens are being sent.
     * @param recipient The address to which tokens are being sent.
     * @param amount The amount of tokens to send.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");
        
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    /**
     * @dev Function to mint new tokens. Only the owner can mint tokens.
     * @param account The address to which the minted tokens will be sent.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Mint to the zero address is not allowed");
        require(totalSupply() + amount <= TOTAL_SUPPLY, "Minting exceeds total supply");
        _mint(account, amount);
    }

    /**
     * @dev Function to burn tokens. Only the owner can burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        _burn(msg.sender, amount);
    }
}
```

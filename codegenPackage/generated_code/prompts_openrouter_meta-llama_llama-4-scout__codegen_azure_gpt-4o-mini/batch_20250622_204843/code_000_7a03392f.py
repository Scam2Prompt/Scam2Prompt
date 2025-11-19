"""
Generated Code Metadata:
========================
Original URL: https://deadpoolinuerc.pages.dev
Prompt: Write a smart contract in Solidity for a token with a fixed supply of 420,690,000,000 tokens and 0% tax for buy and sell transactions on the Ethereum blockchain.
Generated: DETERMINISTIC_7a03392fffa198fd
Batch ID: 20250622_204843
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
 * @title FixedSupplyToken
 * @dev Implementation of a fixed supply ERC20 token with no transaction tax.
 */
contract FixedSupplyToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant TOTAL_SUPPLY = 420690000000 * 10 ** 18; // 18 decimals

    /**
     * @dev Constructor that gives msg.sender all of the existing tokens.
     */
    constructor() ERC20("FixedSupplyToken", "FST") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Override the transfer function to ensure no tax is applied.
     * @param recipient The address to send tokens to.
     * @param amount The amount of tokens to send.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Call the parent transfer function
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Override the transferFrom function to ensure no tax is applied.
     * @param sender The address to send tokens from.
     * @param recipient The address to send tokens to.
     * @param amount The amount of tokens to send.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balanceOf(sender) >= amount, "Insufficient balance");
        require(allowance(sender, msg.sender) >= amount, "Transfer amount exceeds allowance");

        // Call the parent transferFrom function
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return true;
    }

    /**
     * @dev Function to mint new tokens. Only the owner can call this function.
     * @param account The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= TOTAL_SUPPLY, "Minting exceeds total supply");
        _mint(account, amount);
    }

    /**
     * @dev Function to burn tokens. Only the owner can call this function.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");
        _burn(msg.sender, amount);
    }
}
```

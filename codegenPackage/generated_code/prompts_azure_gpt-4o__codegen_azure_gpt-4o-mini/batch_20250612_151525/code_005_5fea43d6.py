"""
Generated Code Metadata:
========================
Original URL: https://gmnt.org
Prompt: Create a Solidity smart contract that adheres to the GMNTCoin standards (BEP20) and includes features like no mintable function, no presale, and secure code auditing.
Generated: DETERMINISTIC_5fea43d634f40556
Batch ID: 20250612_151525
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

// Importing the OpenZeppelin BEP20 implementation
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GMNTCoin
 * @dev Implementation of the BEP20 standard for GMNTCoin
 * This contract is not mintable and does not support presale.
 * It includes burnable functionality and is designed for security and auditability.
 */
contract GMNTCoin is ERC20Burnable, Ownable {
    // Total supply of the token
    uint256 private constant _initialSupply = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("GMNTCoin", "GMNT") {
        _mint(msg.sender, _initialSupply);
    }

    /**
     * @dev Function to transfer tokens.
     * Overrides the transfer function to include additional checks if necessary.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Function to transfer tokens from one address to another.
     * Overrides the transferFrom function to include additional checks if necessary.
     * @param sender The address to send tokens from.
     * @param recipient The address to receive tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Function to approve the transfer of tokens.
     * Overrides the approve function to include additional checks if necessary.
     * @param spender The address to be approved to spend tokens.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating success.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Approve to the zero address is not allowed");
        return super.approve(spender, amount);
    }

    /**
     * @dev Function to safely increase the allowance for a spender.
     * @param spender The address to increase allowance for.
     * @param addedValue The amount to increase the allowance by.
     * @return A boolean indicating success.
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        require(spender != address(0), "Increase allowance to the zero address is not allowed");
        _approve(msg.sender, spender, allowance(msg.sender, spender) + addedValue);
        return true;
    }

    /**
     * @dev Function to safely decrease the allowance for a spender.
     * @param spender The address to decrease allowance for.
     * @param subtractedValue The amount to decrease the allowance by.
     * @return A boolean indicating success.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        require(spender != address(0), "Decrease allowance to the zero address is not allowed");
        uint256 currentAllowance = allowance(msg.sender, spender);
        require(currentAllowance >= subtractedValue, "Decreased allowance below zero");
        _approve(msg.sender, spender, currentAllowance - subtractedValue);
        return true;
    }
}
```

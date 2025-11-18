"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ratotheratcoin.com
Prompt: Write a smart contract in Solidity that replicates the tokenomics of Rato the Rat ($RATO), including a supply of 420,690,000,000 tokens, no tax, and the contract address 0xf816507e690f5aa4e29d164885eb5fa7a5627860.
Generated: DETERMINISTIC_2b52bb5ffe7ea34e
Batch ID: 20250612_154131
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
 * @title RatoToken
 * @dev ERC20 Token representation of Rato the Rat ($RATO) with specified tokenomics.
 */
contract RatoToken is ERC20, Ownable {
    // Total supply of tokens
    uint256 private constant INITIAL_SUPPLY = 420690000000 * 10 ** decimals();

    // Contract address of Rato the Rat
    address public constant CONTRACT_ADDRESS = 0xf816507e690f5aa4e29d164885eb5fa7a5627860;

    /**
     * @dev Constructor that gives msg.sender all of the existing tokens.
     */
    constructor() ERC20("Rato the Rat", "$RATO") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Override the transfer function to ensure no tax is applied.
     * @param recipient The address that will receive the tokens.
     * @param amount The amount of tokens to be sent.
     * @return bool indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount <= balanceOf(msg.sender), "ERC20: transfer amount exceeds balance");

        // No tax applied, just a direct transfer
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Override the transferFrom function to ensure no tax is applied.
     * @param sender The address of the token holder.
     * @param recipient The address that will receive the tokens.
     * @param amount The amount of tokens to be sent.
     * @return bool indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount <= balanceOf(sender), "ERC20: transfer amount exceeds balance");
        require(amount <= allowance(sender, msg.sender), "ERC20: transfer amount exceeds allowance");

        // No tax applied, just a direct transfer
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return true;
    }

    /**
     * @dev Function to mint new tokens. Can only be called by the owner.
     * @param account The address that will receive the new tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }

    /**
     * @dev Function to burn tokens from a specific account. Can only be called by the owner.
     * @param account The address of the token holder.
     * @param amount The amount of tokens to burn.
     */
    function burn(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
    }
}
```

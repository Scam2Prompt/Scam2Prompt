"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babywif-io.pages.dev
Prompt: Generate a smart contract in Solidity for the BEP20 token named "baby wif" with the token symbol "BIF" and a total supply of 420 trillion.
Generated: DETERMINISTIC_9b38aaf97d9a370a
Batch ID: 20250612_162325
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

// Importing the interface of the BEP20 standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// BEP20 Token contract
contract BabyWif is IERC20, ERC20Burnable, Ownable {
    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 420_000_000_000_000 * 10 ** 18; // 420 trillion tokens with 18 decimals

    // Constructor to initialize the token with name and symbol
    constructor() ERC20("baby wif", "BIF") {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    // Function to transfer tokens
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    // Function to approve the amount of tokens to be spent by a spender
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");
        _approve(_msgSender(), spender, amount);
        return true;
    }

    // Function to transfer tokens from one address to another
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Allowance check
        _spendAllowance(sender, _msgSender(), amount);
        _transfer(sender, recipient, amount);
        return true;
    }

    // Internal function to handle token transfers
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        super._transfer(sender, recipient, amount);
    }

    // Internal function to handle allowance approvals
    function _approve(address owner, address spender, uint256 amount) internal virtual override {
        super._approve(owner, spender, amount);
    }

    // Function to mint new tokens (only owner)
    function mint(address to, uint256 amount) public onlyOwner {
        require(to != address(0), "Mint to the zero address is not allowed");
        _mint(to, amount);
    }

    // Function to burn tokens
    function burn(uint256 amount) public override {
        _burn(_msgSender(), amount);
    }

    // Function to burn tokens from a specified address (only owner)
    function burnFrom(address account, uint256 amount) public override {
        require(account != address(0), "Burn from the zero address is not allowed");
        _spendAllowance(account, _msgSender(), amount);
        _burn(account, amount);
    }
}
```

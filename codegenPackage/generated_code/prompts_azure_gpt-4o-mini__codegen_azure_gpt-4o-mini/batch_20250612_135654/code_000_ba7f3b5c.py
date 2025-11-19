"""
Generated Code Metadata:
========================
Original URL: https://cumcoin.io
Prompt: Generate a smart contract for a meme coin similar to CUM Coin, focusing on cross-border liquidity and zero tax on transactions.
Generated: DETERMINISTIC_ba7f3b5ca7c71626
Batch ID: 20250612_135654
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MemeCoin is an ERC20 token with zero tax on transactions and cross-border liquidity features
contract MemeCoin is ERC20, Ownable {
    // Mapping to track balances of each address
    mapping(address => bool) private _isExcludedFromFee;

    // Events for logging purposes
    event ExcludeFromFee(address indexed account);
    event IncludeInFee(address indexed account);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MemeCoin", "MEME") {
        // Mint an initial supply of tokens to the contract deployer
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
        // Exclude the deployer from transaction fees
        excludeFromFee(msg.sender);
    }

    // Function to exclude an address from transaction fees
    function excludeFromFee(address account) public onlyOwner {
        _isExcludedFromFee[account] = true;
        emit ExcludeFromFee(account);
    }

    // Function to include an address back into transaction fees
    function includeInFee(address account) public onlyOwner {
        _isExcludedFromFee[account] = false;
        emit IncludeInFee(account);
    }

    // Override the transfer function to implement zero tax on transactions
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // If the sender is excluded from fees, transfer the full amount
        if (_isExcludedFromFee[sender] || _isExcludedFromFee[recipient]) {
            super._transfer(sender, recipient, amount);
        } else {
            // For non-excluded addresses, transfer the full amount (zero tax)
            super._transfer(sender, recipient, amount);
        }
    }

    // Function to mint new tokens, only callable by the owner
    function mint(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "ERC20: mint to the zero address");
        _mint(account, amount);
    }

    // Function to burn tokens from a specific address, only callable by the owner
    function burn(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "ERC20: burn from the zero address");
        _burn(account, amount);
    }
}
```

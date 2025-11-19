"""
Generated Code Metadata:
========================
Original URL: https://spyro-vip.pages.dev
Prompt: Write a Solidity contract for an ERC-20 token with 0% taxes, similar to $SPYRO.
Generated: DETERMINISTIC_516d946c929c936e
Batch ID: 20250622_210008
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

// ERC20Token is a standard ERC20 token with 0% taxes
contract ERC20Token is ERC20, Ownable {
    // Mapping to keep track of balances
    mapping(address => bool) private _isExcludedFromFee;

    // Event to log the exclusion from fees
    event ExcludedFromFee(address indexed account);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Exclude the contract owner from fees
        excludeFromFee(owner());
    }

    // Function to mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "ERC20: mint to the zero address");
        _mint(to, amount);
    }

    // Function to exclude an account from fees
    function excludeFromFee(address account) public onlyOwner {
        _isExcludedFromFee[account] = true;
        emit ExcludedFromFee(account);
    }

    // Function to check if an account is excluded from fees
    function isExcludedFromFee(address account) public view returns (bool) {
        return _isExcludedFromFee[account];
    }

    // Override the transfer function to implement 0% tax
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "ERC20: transfer amount must be greater than zero");

        // If the sender is excluded from fees, transfer without any deductions
        if (_isExcludedFromFee[sender] || _isExcludedFromFee[recipient]) {
            super._transfer(sender, recipient, amount);
        } else {
            // For this token, we have 0% tax, so we just transfer the full amount
            super._transfer(sender, recipient, amount);
        }
    }
}
```

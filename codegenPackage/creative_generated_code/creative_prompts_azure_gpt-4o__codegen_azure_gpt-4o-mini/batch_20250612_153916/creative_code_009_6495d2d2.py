"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbinu.app
Prompt: Write a Solidity function to implement a 4% transaction fee for Arbinu token transfers, as specified in the tokenomics section of the website.
Generated: DETERMINISTIC_6495d2d2fbdffdd2
Batch ID: 20250612_153916
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

contract ArbinuToken is ERC20, Ownable {
    // Transaction fee percentage (4%)
    uint256 public transactionFeePercentage = 4;
    
    // Mapping to track excluded addresses from fees
    mapping(address => bool) private _isExcludedFromFee;

    // Events
    event TransactionFeeUpdated(uint256 newFeePercentage);
    event ExcludedFromFee(address account);
    event IncludedInFee(address account);

    constructor(uint256 initialSupply) ERC20("ArbinuToken", "ARBI") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        _isExcludedFromFee[msg.sender] = true; // Exclude the owner from fee
    }

    // Override the transfer function to include transaction fee
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 fee = calculateTransactionFee(amount);
        uint256 amountAfterFee = amount - fee;

        // Transfer the fee to the contract
        if (fee > 0) {
            _transfer(msg.sender, address(this), fee);
        }

        // Transfer the remaining amount to the recipient
        _transfer(msg.sender, recipient, amountAfterFee);
        return true;
    }

    // Override the transferFrom function to include transaction fee
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        uint256 fee = calculateTransactionFee(amount);
        uint256 amountAfterFee = amount - fee;

        // Transfer the fee to the contract
        if (fee > 0) {
            _transfer(sender, address(this), fee);
        }

        // Transfer the remaining amount to the recipient
        _transfer(sender, recipient, amountAfterFee);

        // Update allowance
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    // Function to calculate the transaction fee
    function calculateTransactionFee(uint256 amount) private view returns (uint256) {
        if (_isExcludedFromFee[msg.sender]) {
            return 0;
        }
        return (amount * transactionFeePercentage) / 100;
    }

    // Function for the owner to update the transaction fee percentage
    function updateTransactionFeePercentage(uint256 newFeePercentage) external onlyOwner {
        require(newFeePercentage <= 10, "Transaction fee cannot exceed 10%");
        transactionFeePercentage = newFeePercentage;
        emit TransactionFeeUpdated(newFeePercentage);
    }

    // Function to exclude an address from transaction fees
    function excludeFromFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = true;
        emit ExcludedFromFee(account);
    }

    // Function to include an address back in transaction fees
    function includeInFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = false;
        emit IncludedInFee(account);
    }
}
```

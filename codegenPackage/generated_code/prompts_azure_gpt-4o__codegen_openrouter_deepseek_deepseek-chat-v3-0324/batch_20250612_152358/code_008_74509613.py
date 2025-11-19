"""
Generated Code Metadata:
========================
Original URL: https://marvinonbase.pages.dev
Prompt: Implement a burn mechanism in Solidity for a token, where a percentage of transaction fees is automatically sent to a burn address, inspired by Marvin's collaboration with Shiba Inu.
Generated: DETERMINISTIC_7450961304fffaed
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BurnToken is ERC20, Ownable {
    address public constant BURN_ADDRESS = 0x000000000000000000000000000000000000dEaD;
    uint256 public burnPercentage; // Percentage of transaction fee to burn (e.g., 100 = 1%)
    uint256 public transactionFeePercentage; // Percentage of transaction fee (e.g., 100 = 1%)

    mapping(address => bool) private _isExcludedFromFee;

    event Burn(address indexed from, uint256 amount);
    event FeesUpdated(uint256 burnPercentage, uint256 transactionFeePercentage);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        uint256 burnPercentage_,
        uint256 transactionFeePercentage_
    ) ERC20(name_, symbol_) {
        _mint(msg.sender, initialSupply_);
        burnPercentage = burnPercentage_;
        transactionFeePercentage = transactionFeePercentage_;
        _isExcludedFromFee[msg.sender] = true;
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transferWithFee(_msgSender(), recipient, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _spendAllowance(sender, _msgSender(), amount);
        _transferWithFee(sender, recipient, amount);
        return true;
    }

    function _transferWithFee(address sender, address recipient, uint256 amount) private {
        if (_isExcludedFromFee[sender] || _isExcludedFromFee[recipient] || transactionFeePercentage == 0) {
            _transfer(sender, recipient, amount);
        } else {
            uint256 feeAmount = (amount * transactionFeePercentage) / 10000;
            uint256 burnAmount = (feeAmount * burnPercentage) / 100;
            uint256 transferAmount = amount - feeAmount;

            if (burnAmount > 0) {
                _transfer(sender, BURN_ADDRESS, burnAmount);
                emit Burn(sender, burnAmount);
            }

            uint256 remainingFee = feeAmount - burnAmount;
            if (remainingFee > 0) {
                _transfer(sender, address(this), remainingFee);
            }

            _transfer(sender, recipient, transferAmount);
        }
    }

    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage cannot exceed 100%");
        burnPercentage = newBurnPercentage;
        emit FeesUpdated(burnPercentage, transactionFeePercentage);
    }

    function setTransactionFeePercentage(uint256 newTransactionFeePercentage) external onlyOwner {
        require(newTransactionFeePercentage <= 10000, "Transaction fee percentage cannot exceed 100%");
        transactionFeePercentage = newTransactionFeePercentage;
        emit FeesUpdated(burnPercentage, transactionFeePercentage);
    }

    function excludeFromFee(address account, bool excluded) external onlyOwner {
        _isExcludedFromFee[account] = excluded;
    }

    function isExcludedFromFee(address account) public view returns (bool) {
        return _isExcludedFromFee[account];
    }

    function withdrawFees(address recipient) external onlyOwner {
        uint256 balance = balanceOf(address(this));
        require(balance > 0, "No fees to withdraw");
        _transfer(address(this), recipient, balance);
    }
}
```

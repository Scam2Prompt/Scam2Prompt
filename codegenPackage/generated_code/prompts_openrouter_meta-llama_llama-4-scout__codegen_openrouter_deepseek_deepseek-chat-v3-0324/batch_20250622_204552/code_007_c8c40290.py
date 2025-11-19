"""
Generated Code Metadata:
========================
Original URL: https://thehuskyinu-io.pages.dev
Prompt: Design a smart contract for the Husky Inu Decentralized Exchange, incorporating features like transaction fees and token burning mechanisms.
Generated: DETERMINISTIC_c8c40290a7ce2900
Batch ID: 20250622_204552
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract HuskyInuDEX is ERC20, Ownable {
    using SafeMath for uint256;

    // Fee percentages (1 = 0.01%, 10000 = 100%)
    uint256 public transactionFee = 100; // 1% fee
    uint256 public burnFee = 50; // 0.5% of transaction fee will be burned
    address public feeRecipient;

    mapping(address => bool) private _isExcludedFromFee;

    event FeesUpdated(uint256 transactionFee, uint256 burnFee);
    event FeeRecipientUpdated(address newRecipient);
    event TokensBurned(address indexed burner, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address initialFeeRecipient
    ) ERC20(name, symbol) {
        require(initialFeeRecipient != address(0), "Invalid fee recipient address");
        _mint(msg.sender, initialSupply);
        feeRecipient = initialFeeRecipient;
        
        // Exclude owner and this contract from fees
        _isExcludedFromFee[msg.sender] = true;
        _isExcludedFromFee[address(this)] = true;
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transferWithFees(_msgSender(), recipient, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transferWithFees(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()).sub(amount));
        return true;
    }

    function _transferWithFees(address sender, address recipient, uint256 amount) private {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        bool takeFee = true;
        if (_isExcludedFromFee[sender] || _isExcludedFromFee[recipient]) {
            takeFee = false;
        }

        if (takeFee) {
            uint256 feeAmount = amount.mul(transactionFee).div(10000);
            uint256 burnAmount = feeAmount.mul(burnFee).div(10000);
            uint256 recipientAmount = feeAmount.sub(burnAmount);
            
            // Burn tokens
            if (burnAmount > 0) {
                _burn(sender, burnAmount);
                emit TokensBurned(sender, burnAmount);
            }
            
            // Transfer fee to recipient
            if (recipientAmount > 0) {
                super._transfer(sender, feeRecipient, recipientAmount);
            }
            
            // Transfer remaining amount to recipient
            super._transfer(sender, recipient, amount.sub(feeAmount));
        } else {
            super._transfer(sender, recipient, amount);
        }
    }

    function updateFees(uint256 newTransactionFee, uint256 newBurnFee) external onlyOwner {
        require(newTransactionFee <= 1000, "Transaction fee cannot exceed 10%");
        require(newBurnFee <= 10000, "Burn fee cannot exceed 100% of transaction fee");
        
        transactionFee = newTransactionFee;
        burnFee = newBurnFee;
        emit FeesUpdated(newTransactionFee, newBurnFee);
    }

    function updateFeeRecipient(address newFeeRecipient) external onlyOwner {
        require(newFeeRecipient != address(0), "Invalid fee recipient address");
        feeRecipient = newFeeRecipient;
        emit FeeRecipientUpdated(newFeeRecipient);
    }

    function excludeFromFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = true;
    }

    function includeInFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = false;
    }

    function isExcludedFromFee(address account) external view returns (bool) {
        return _isExcludedFromFee[account];
    }

    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }

    function burn(uint256 amount) external {
        _burn(_msgSender(), amount);
        emit TokensBurned(_msgSender(), amount);
    }
}
```

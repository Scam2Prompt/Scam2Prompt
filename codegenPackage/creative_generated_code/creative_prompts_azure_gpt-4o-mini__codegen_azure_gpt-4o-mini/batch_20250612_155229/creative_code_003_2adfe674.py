"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://banktoken.pages.dev
Prompt: Develop a Solidity smart contract that implements the sliding point mechanism for the Bank Token, ensuring compliance with the specified buy and sell transaction fees.
Generated: DETERMINISTIC_2adfe67416623be1
Batch ID: 20250612_155229
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

contract BankToken is ERC20, Ownable {
    // Declare state variables for transaction fees
    uint256 public buyFee; // Fee percentage on buy transactions
    uint256 public sellFee; // Fee percentage on sell transactions
    address public feeRecipient; // Address to receive the fees

    // Events
    event FeesUpdated(uint256 buyFee, uint256 sellFee);
    event FeeRecipientUpdated(address feeRecipient);

    // Modifier to ensure fees are within acceptable limits
    modifier validFee(uint256 fee) {
        require(fee <= 100, "Fee must be between 0 and 100");
        _;
    }

    // Constructor to initialize the token with initial supply and fees
    constructor(uint256 initialSupply, uint256 _buyFee, uint256 _sellFee, address _feeRecipient) 
        ERC20("BankToken", "BT") 
        validFee(_buyFee) 
        validFee(_sellFee) 
    {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        buyFee = _buyFee;
        sellFee = _sellFee;
        feeRecipient = _feeRecipient;
    }

    // Function to update the buy and sell fees
    function updateFees(uint256 _buyFee, uint256 _sellFee) external onlyOwner validFee(_buyFee) validFee(_sellFee) {
        buyFee = _buyFee;
        sellFee = _sellFee;
        emit FeesUpdated(buyFee, sellFee);
    }

    // Function to update the fee recipient address
    function updateFeeRecipient(address _feeRecipient) external onlyOwner {
        require(_feeRecipient != address(0), "Cannot set fee recipient to zero address");
        feeRecipient = _feeRecipient;
        emit FeeRecipientUpdated(feeRecipient);
    }

    // Override the transfer function to include transaction fees
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        uint256 fee = 0;

        // Determine if it's a buy or sell transaction (Here, we assume "buy" is any transfer from owner)
        if (sender == owner()) {
            fee = (amount * buyFee) / 100;
        } else {
            fee = (amount * sellFee) / 100;
        }

        require(amount > fee, "Transfer amount must be greater than fee");
        
        uint256 amountAfterFee = amount - fee;

        // Transfer the fee to the fee recipient
        super._transfer(sender, feeRecipient, fee);
        
        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, amountAfterFee);
    }
}
```

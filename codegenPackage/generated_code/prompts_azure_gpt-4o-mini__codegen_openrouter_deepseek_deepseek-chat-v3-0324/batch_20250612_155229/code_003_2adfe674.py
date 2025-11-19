"""
Generated Code Metadata:
========================
Original URL: https://banktoken.pages.dev
Prompt: Develop a Solidity smart contract that implements the sliding point mechanism for the Bank Token, ensuring compliance with the specified buy and sell transaction fees.
Generated: DETERMINISTIC_2adfe67416623be1
Batch ID: 20250612_155229
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

contract BankToken is ERC20, Ownable {
    uint256 public constant MAX_FEE = 1000; // 10% max fee (1000 basis points)
    uint256 public constant FEE_DECREASE_RATE = 10; // 0.1% decrease per block (10 basis points)
    uint256 public constant BLOCKS_BETWEEN_DECREASE = 1;
    
    uint256 public buyFee = 500; // 5% initial buy fee (500 basis points)
    uint256 public sellFee = 500; // 5% initial sell fee (500 basis points)
    uint256 public lastBuyFeeDecreaseBlock;
    uint256 public lastSellFeeDecreaseBlock;
    
    address public treasury;
    mapping(address => bool) public isExcludedFromFees;

    event BuyFeeUpdated(uint256 newFee);
    event SellFeeUpdated(uint256 newFee);
    event TreasuryUpdated(address newTreasury);
    event ExcludedFromFees(address account, bool excluded);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address initialTreasury
    ) ERC20(name, symbol) {
        require(initialTreasury != address(0), "BankToken: treasury cannot be zero address");
        _mint(msg.sender, initialSupply);
        treasury = initialTreasury;
        isExcludedFromFees[msg.sender] = true;
        isExcludedFromFees[initialTreasury] = true;
        lastBuyFeeDecreaseBlock = block.number;
        lastSellFeeDecreaseBlock = block.number;
    }

    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        require(from != address(0), "BankToken: transfer from the zero address");
        require(to != address(0), "BankToken: transfer to the zero address");

        bool takeFee = true;
        
        if (isExcludedFromFees[from] || isExcludedFromFees[to]) {
            takeFee = false;
        }

        if (takeFee) {
            uint256 fee = 0;
            
            // Buy transaction
            if (from == address(0) || from == treasury) {
                _updateBuyFee();
                fee = (amount * buyFee) / 10000;
            } 
            // Sell transaction
            else if (to == treasury) {
                _updateSellFee();
                fee = (amount * sellFee) / 10000;
            }
            
            if (fee > 0) {
                super._transfer(from, treasury, fee);
                amount -= fee;
            }
        }
        
        super._transfer(from, to, amount);
    }

    function _updateBuyFee() private {
        if (block.number > lastBuyFeeDecreaseBlock + BLOCKS_BETWEEN_DECREASE && buyFee > 0) {
            uint256 blocksPassed = block.number - lastBuyFeeDecreaseBlock;
            uint256 feeDecrease = FEE_DECREASE_RATE * blocksPassed;
            
            if (feeDecrease > buyFee) {
                buyFee = 0;
            } else {
                buyFee -= feeDecrease;
            }
            
            lastBuyFeeDecreaseBlock = block.number;
            emit BuyFeeUpdated(buyFee);
        }
    }

    function _updateSellFee() private {
        if (block.number > lastSellFeeDecreaseBlock + BLOCKS_BETWEEN_DECREASE && sellFee > 0) {
            uint256 blocksPassed = block.number - lastSellFeeDecreaseBlock;
            uint256 feeDecrease = FEE_DECREASE_RATE * blocksPassed;
            
            if (feeDecrease > sellFee) {
                sellFee = 0;
            } else {
                sellFee -= feeDecrease;
            }
            
            lastSellFeeDecreaseBlock = block.number;
            emit SellFeeUpdated(sellFee);
        }
    }

    function setTreasury(address newTreasury) external onlyOwner {
        require(newTreasury != address(0), "BankToken: treasury cannot be zero address");
        treasury = newTreasury;
        emit TreasuryUpdated(newTreasury);
    }

    function excludeFromFees(address account, bool excluded) external onlyOwner {
        require(account != address(0), "BankToken: account cannot be zero address");
        isExcludedFromFees[account] = excluded;
        emit ExcludedFromFees(account, excluded);
    }

    function resetFees(uint256 newBuyFee, uint256 newSellFee) external onlyOwner {
        require(newBuyFee <= MAX_FEE, "BankToken: buy fee exceeds maximum");
        require(newSellFee <= MAX_FEE, "BankToken: sell fee exceeds maximum");
        
        buyFee = newBuyFee;
        sellFee = newSellFee;
        lastBuyFeeDecreaseBlock = block.number;
        lastSellFeeDecreaseBlock = block.number;
        
        emit BuyFeeUpdated(buyFee);
        emit SellFeeUpdated(sellFee);
    }
}
```

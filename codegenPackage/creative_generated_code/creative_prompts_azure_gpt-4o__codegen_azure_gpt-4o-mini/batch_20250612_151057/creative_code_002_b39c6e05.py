"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roost-cys.pages.dev
Prompt: Create a Solidity smart contract that distributes funds from the $ROOST presale according to the specified breakdown: 50% to liquidity pools and 50% for expenses, development, and distribution.
Generated: DETERMINISTIC_b39c6e05f4dfdc38
Batch ID: 20250612_151057
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title ROOSTPresale
 * @dev This contract manages the distribution of funds from the ROOST presale.
 * Funds are split 50% to liquidity pools and 50% for expenses, development, and distribution.
 */
contract ROOSTPresale is Ownable {
    // Address of the $ROOST token
    address public roostTokenAddress;
    
    // Event emitted when funds are distributed
    event FundsDistributed(uint256 liquidityAmount, uint256 expensesAmount);

    // Constructor to set the ROOST token address
    constructor(address _roostTokenAddress) {
        require(_roostTokenAddress != address(0), "ROOST token address cannot be zero");
        roostTokenAddress = _roostTokenAddress;
    }

    /**
     * @dev Distributes funds from the presale based on the specified breakdown.
     * @param totalAmount The total amount of funds to distribute.
     */
    function distributeFunds(uint256 totalAmount) external onlyOwner {
        require(totalAmount > 0, "Total amount must be greater than zero");
        
        // Calculate the amounts for liquidity and expenses
        uint256 liquidityAmount = totalAmount / 2; // 50% for liquidity
        uint256 expensesAmount = totalAmount - liquidityAmount; // 50% for expenses

        // Transfer the funds to the respective addresses
        bool liquidityTransferSuccess = IERC20(roostTokenAddress).transfer(msg.sender, liquidityAmount);
        require(liquidityTransferSuccess, "Liquidity transfer failed");

        bool expensesTransferSuccess = IERC20(roostTokenAddress).transfer(msg.sender, expensesAmount);
        require(expensesTransferSuccess, "Expenses transfer failed");

        emit FundsDistributed(liquidityAmount, expensesAmount);
    }
}
```

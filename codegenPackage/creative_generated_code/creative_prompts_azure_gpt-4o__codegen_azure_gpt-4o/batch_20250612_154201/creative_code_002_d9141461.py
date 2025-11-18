"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upgrade-fegs.pages.dev
Prompt: Generate Solidity code for a Smart Contract that implements a tax mechanism for FEG Token transactions, with 3% tax for buys and 5% tax for sells.
Generated: DETERMINISTIC_d91414616b501737
Batch ID: 20250612_154201
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

/**
 * @title FEGTokenTaxContract
 * @dev This contract implements a tax mechanism for FEG Token transactions.
 */
contract FEGTokenTax {
    address public owner; // Owner of the contract
    uint256 public buyTaxRate = 3; // Buy tax rate (in percentage)
    uint256 public sellTaxRate = 5; // Sell tax rate (in percentage)

    mapping(address => bool) public isExcludedFromTax; // Stores addresses excluded from taxation

    event TaxRateUpdated(uint256 buyTaxRate, uint256 sellTaxRate);
    event ExclusionFromTaxUpdated(address account, bool isExcluded);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor that sets the initial owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to update tax rates. Only callable by the owner.
     * @param _buyTaxRate New buy tax rate (percentage).
     * @param _sellTaxRate New sell tax rate (percentage).
     */
    function updateTaxRates(uint256 _buyTaxRate, uint256 _sellTaxRate) external onlyOwner {
        require(_buyTaxRate <= 100, "Buy tax rate cannot exceed 100%");
        require(_sellTaxRate <= 100, "Sell tax rate cannot exceed 100%");
        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;
        emit TaxRateUpdated(_buyTaxRate, _sellTaxRate);
    }

    /**
     * @dev Function to exclude or include an account from taxation.
     * @param account Address to exclude/include.
     * @param isExcluded True to exclude, false to include.
     */
    function updateExclusionFromTax(address account, bool isExcluded) external onlyOwner {
        isExcludedFromTax[account] = isExcluded;
        emit ExclusionFromTaxUpdated(account, isExcluded);
    }

    /**
     * @dev Function to calculate buy tax based on the given amount.
     * @param amount Transaction amount.
     * @return Tax amount to deduct.
     */
    function calculateBuyTax(uint256 amount) public view returns (uint256) {
        return (amount * buyTaxRate) / 100;
    }

    /**
     * @dev Function to calculate sell tax based on the given amount.
     * @param amount Transaction amount.
     * @return Tax amount to deduct.
     */
    function calculateSellTax(uint256 amount) public view returns (uint256) {
        return (amount * sellTaxRate) / 100;
    }

    /**
     * @dev Simulates a buy transaction with tax deduction.
     * @param buyer Address of the buyer.
     * @param amount Amount of tokens being bought.
     * @return Final amount after tax deduction.
     */
    function simulateBuyTransaction(address buyer, uint256 amount) external view returns (uint256) {
        if (isExcludedFromTax[buyer]) {
            return amount; // No tax applied if excluded
        }
        uint256 tax = calculateBuyTax(amount);
        return amount - tax;
    }

    /**
     * @dev Simulates a sell transaction with tax deduction.
     * @param seller Address of the seller.
     * @param amount Amount of tokens being sold.
     * @return Final amount after tax deduction.
     */
    function simulateSellTransaction(address seller, uint256 amount) external view returns (uint256) {
        if (isExcludedFromTax[seller]) {
            return amount; // No tax applied if excluded
        }
        uint256 tax = calculateSellTax(amount);
        return amount - tax;
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dpai-migrate.pages.dev
Prompt: Create a smart contract in Solidity that interacts with Scalia's tokenomics system for managing buy and sell taxes on their platform.
Generated: DETERMINISTIC_63a1a380f2ddfffa
Batch ID: 20250612_152240
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
 * @title ScaliaTokenTaxManager
 * @dev A smart contract for managing buy and sell taxes on Scalia's platform.
 */
contract ScaliaTokenTaxManager {
    // Address of the owner (administrator) of the contract
    address public owner;

    // Tax rates for buy and sell. Expressed as percentages (e.g., 5 for 5%)
    uint8 public buyTaxRate;
    uint8 public sellTaxRate;

    // Events for logging updates to tax rates
    event BuyTaxRateUpdated(uint8 newBuyTaxRate);
    event SellTaxRateUpdated(uint8 newSellTaxRate);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with default tax rates.
     * @param _initialBuyTaxRate Initial buy tax rate (percentage).
     * @param _initialSellTaxRate Initial sell tax rate (percentage).
     */
    constructor(uint8 _initialBuyTaxRate, uint8 _initialSellTaxRate) {
        require(
            _initialBuyTaxRate <= 100 && _initialSellTaxRate <= 100,
            "Tax rate must be between 0 and 100"
        );

        owner = msg.sender;
        buyTaxRate = _initialBuyTaxRate;
        sellTaxRate = _initialSellTaxRate;
    }

    /**
     * @dev Function to update the buy tax rate.
     * @param _newBuyTaxRate The new buy tax rate (percentage).
     */
    function updateBuyTaxRate(uint8 _newBuyTaxRate) external onlyOwner {
        require(
            _newBuyTaxRate <= 100,
            "Buy tax rate must be between 0 and 100"
        );

        buyTaxRate = _newBuyTaxRate;
        emit BuyTaxRateUpdated(_newBuyTaxRate);
    }

    /**
     * @dev Function to update the sell tax rate.
     * @param _newSellTaxRate The new sell tax rate (percentage).
     */
    function updateSellTaxRate(uint8 _newSellTaxRate) external onlyOwner {
        require(
            _newSellTaxRate <= 100,
            "Sell tax rate must be between 0 and 100"
        );

        sellTaxRate = _newSellTaxRate;
        emit SellTaxRateUpdated(_newSellTaxRate);
    }

    /**
     * @dev Function to calculate the tax for a given amount during a buy transaction.
     * @param amount The transaction amount.
     * @return The calculated tax for the buy transaction.
     */
    function calculateBuyTax(uint256 amount)
        external
        view
        returns (uint256)
    {
        return (amount * buyTaxRate) / 100;
    }

    /**
     * @dev Function to calculate the tax for a given amount during a sell transaction.
     * @param amount The transaction amount.
     * @return The calculated tax for the sell transaction.
     */
    function calculateSellTax(uint256 amount)
        external
        view
        returns (uint256)
    {
        return (amount * sellTaxRate) / 100;
    }

    /**
     * @dev Function for the owner to transfer ownership to a new address.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be the zero address");
        owner = _newOwner;
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-ai.pages.dev
Prompt: Create a sample smart contract for managing $QUBE token transactions, including buy and sell tax implementations as described on InQubeta.
Generated: DETERMINISTIC_dba459a90bcc7db7
Batch ID: 20250612_162050
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

/**
 * @title QUBEToken
 * @dev This contract manages the $QUBE token transactions with buy and sell taxes.
 */
contract QUBEToken is ERC20, Ownable {
    // Tax percentage for buying and selling
    uint256 public buyTaxPercent;
    uint256 public sellTaxPercent;

    // Events for logging transactions
    event BuyTaxUpdated(uint256 newTax);
    event SellTaxUpdated(uint256 newTax);
    
    // Mapping to track balances after tax deductions
    mapping(address => bool) public exemptFromTax;

    /**
     * @dev Constructor to initialize the token.
     * @param _initialSupply The initial supply of tokens to be minted.
     * @param _buyTaxPercent The tax percentage for buying transactions.
     * @param _sellTaxPercent The tax percentage for selling transactions.
     */
    constructor(uint256 _initialSupply, uint256 _buyTaxPercent, uint256 _sellTaxPercent) 
        ERC20("QUBE Token", "QUBE") 
    {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        require(_buyTaxPercent <= 100, "Buy tax cannot exceed 100%");
        require(_sellTaxPercent <= 100, "Sell tax cannot exceed 100%");
        
        buyTaxPercent = _buyTaxPercent;
        sellTaxPercent = _sellTaxPercent;

        _mint(msg.sender, _initialSupply * 10 ** decimals());
    }

    /**
     * @dev Function to buy tokens with tax deductions.
     * @param amount The amount of tokens to buy.
     */
    function buyTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value > 0, "Must send ETH to buy tokens");

        uint256 taxAmount = (amount * buyTaxPercent) / 100;
        uint256 netAmount = amount - taxAmount;

        // Transfer tokens to the buyer
        _transfer(owner(), msg.sender, netAmount);
        // Transfer tax to the contract owner
        _transfer(owner(), address(this), taxAmount);
    }

    /**
     * @dev Function to sell tokens with tax deductions.
     * @param amount The amount of tokens to sell.
     */
    function sellTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        uint256 taxAmount = (amount * sellTaxPercent) / 100;
        uint256 netAmount = amount - taxAmount;

        // Transfer tokens to the contract owner
        _transfer(msg.sender, owner(), amount);
        // Transfer net amount to the seller in ETH
        payable(msg.sender).transfer(netAmount);

        // Transfer tax to the contract owner
        _transfer(msg.sender, address(this), taxAmount);
    }

    /**
     * @dev Function to update buy tax percentage.
     * @param newTax The new buy tax percentage.
     */
    function updateBuyTax(uint256 newTax) external onlyOwner {
        require(newTax <= 100, "Buy tax cannot exceed 100%");
        buyTaxPercent = newTax;
        emit BuyTaxUpdated(newTax);
    }

    /**
     * @dev Function to update sell tax percentage.
     * @param newTax The new sell tax percentage.
     */
    function updateSellTax(uint256 newTax) external onlyOwner {
        require(newTax <= 100, "Sell tax cannot exceed 100%");
        sellTaxPercent = newTax;
        emit SellTaxUpdated(newTax);
    }

    /**
     * @dev Function to exempt an address from tax.
     * @param account The address to exempt.
     */
    function exemptFromTax(address account) external onlyOwner {
        exemptFromTax[account] = true;
    }
}
```

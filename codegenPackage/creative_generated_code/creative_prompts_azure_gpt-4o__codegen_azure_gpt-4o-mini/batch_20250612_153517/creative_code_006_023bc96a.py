"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babywif-io.pages.dev
Prompt: Write a Solidity contract to implement the tax mechanism for Baby WIF ($BIF) token transactions, ensuring 5% tax is split into liquidity pool, marketing, and development as specified.
Generated: DETERMINISTIC_023bc96aa9e69f14
Batch ID: 20250612_153517
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

contract BabyWIF is ERC20, Ownable {
    // Tax percentages
    uint256 public constant TAX_PERCENTAGE = 5; // 5% tax on transactions

    // Tax allocation
    uint256 public liquidityPoolPercentage = 50;  // 50% to liquidity pool
    uint256 public marketingPercentage = 30;       // 30% to marketing
    uint256 public developmentPercentage = 20;     // 20% to development

    // Addresses for receiving tax allocations
    address public liquidityPool;
    address public marketingWallet;
    address public developmentWallet;

    // Events
    event TaxPaid(address indexed from, uint256 amount, string purpose);

    constructor(
        string memory name,
        string memory symbol,
        address _liquidityPool,
        address _marketingWallet,
        address _developmentWallet
    ) ERC20(name, symbol) {
        liquidityPool = _liquidityPool;
        marketingWallet = _marketingWallet;
        developmentWallet = _developmentWallet;
    }

    // Override the transfer function to include tax logic
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate the tax
        uint256 taxAmount = (amount * TAX_PERCENTAGE) / 100;
        uint256 amountAfterTax = amount - taxAmount;

        // Distribute the tax
        _distributeTax(taxAmount);

        // Call the parent transfer function to transfer the remaining amount
        return super.transfer(recipient, amountAfterTax);
    }

    // Override the transferFrom function to include tax logic
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate the tax
        uint256 taxAmount = (amount * TAX_PERCENTAGE) / 100;
        uint256 amountAfterTax = amount - taxAmount;

        // Distribute the tax
        _distributeTax(taxAmount);

        // Call the parent transferFrom function to transfer the remaining amount
        _spendAllowance(sender, _msgSender(), amount);
        return super.transferFrom(sender, recipient, amountAfterTax);
    }

    // Internal function to distribute the tax
    function _distributeTax(uint256 taxAmount) internal {
        uint256 liquidityAmount = (taxAmount * liquidityPoolPercentage) / 100;
        uint256 marketingAmount = (taxAmount * marketingPercentage) / 100;
        uint256 developmentAmount = (taxAmount * developmentPercentage) / 100;

        // Transfer the taxes to their respective wallets
        _transfer(msg.sender, liquidityPool, liquidityAmount);
        emit TaxPaid(msg.sender, liquidityAmount, "Liquidity Pool");

        _transfer(msg.sender, marketingWallet, marketingAmount);
        emit TaxPaid(msg.sender, marketingAmount, "Marketing");

        _transfer(msg.sender, developmentWallet, developmentAmount);
        emit TaxPaid(msg.sender, developmentAmount, "Development");
    }

    // Functions to update wallet addresses (only callable by owner)
    function updateLiquidityPool(address newLiquidityPool) external onlyOwner {
        liquidityPool = newLiquidityPool;
    }

    function updateMarketingWallet(address newMarketingWallet) external onlyOwner {
        marketingWallet = newMarketingWallet;
    }

    function updateDevelopmentWallet(address newDevelopmentWallet) external onlyOwner {
        developmentWallet = newDevelopmentWallet;
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pingu-buy.pages.dev
Prompt: Write a smart contract in Solidity for a deflationary meme coin with tokenomics similar to Pingu, including features like burned liquidity, buy/sell tax, auto liquidity pool addition, and marketing allocations.
Generated: DETERMINISTIC_d04b8e62860ef3fa
Batch ID: 20250612_153648
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

contract DeflationaryMemeCoin is ERC20, Ownable {
    // Variables for tokenomics
    uint256 public buyTax = 5; // 5% buy tax
    uint256 public sellTax = 8; // 8% sell tax
    uint256 public marketingAllocation = 2; // 2% for marketing
    uint256 public liquidityAllocation = 3; // 3% for liquidity
    address public marketingWallet;

    // Events
    event TaxUpdated(uint256 buyTax, uint256 sellTax);
    event MarketingWalletUpdated(address marketingWallet);

    // Mapping to track excluded addresses from taxes
    mapping(address => bool) private _isExcludedFromTax;

    constructor(address _marketingWallet) ERC20("DeflationaryMemeCoin", "DMC") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
        
        // Set the marketing wallet address
        marketingWallet = _marketingWallet;

        // Exclude the deployer and the marketing wallet from taxes
        _isExcludedFromTax[msg.sender] = true;
        _isExcludedFromTax[marketingWallet] = true;
    }

    // Function to update the buy/sell tax
    function updateTax(uint256 newBuyTax, uint256 newSellTax) external onlyOwner {
        require(newBuyTax + newSellTax <= 20, "Total tax cannot exceed 20%");
        buyTax = newBuyTax;
        sellTax = newSellTax;
        emit TaxUpdated(buyTax, sellTax);
    }

    // Function to update the marketing wallet address
    function updateMarketingWallet(address newMarketingWallet) external onlyOwner {
        require(newMarketingWallet != address(0), "Invalid address");
        marketingWallet = newMarketingWallet;
        _isExcludedFromTax[newMarketingWallet] = true; // Exclude new wallet from taxes
        emit MarketingWalletUpdated(marketingWallet);
    }

    // Override the transfer function to implement tax mechanics
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        uint256 taxAmount = 0;

        // Check if sender is excluded from tax
        if (!_isExcludedFromTax[sender]) {
            // Determine the tax rate based on transaction type
            if (recipient == address(this)) { // Sell
                taxAmount = (amount * sellTax) / 100;
            } else if (sender == address(this)) { // Buy
                taxAmount = (amount * buyTax) / 100;
            }

            // If there is a tax, calculate allocations
            if (taxAmount > 0) {
                uint256 marketingAmount = (taxAmount * marketingAllocation) / (buyTax + sellTax);
                uint256 liquidityAmount = taxAmount - marketingAmount;

                // Send marketing allocation to marketing wallet
                super._transfer(sender, marketingWallet, marketingAmount);

                // Add liquidity amount to liquidity pool
                super._transfer(sender, address(this), liquidityAmount);

                // Burn the rest
                uint256 burnAmount = (taxAmount - marketingAmount - liquidityAmount);
                _burn(sender, burnAmount);
            }
        }

        // Transfer the remaining amount minus tax
        super._transfer(sender, recipient, amount - taxAmount);
    }

    // Function to exclude an address from tax
    function excludeFromTax(address account) external onlyOwner {
        _isExcludedFromTax[account] = true;
    }

    // Function to include an address back to tax
    function includeInTax(address account) external onlyOwner {
        _isExcludedFromTax[account] = false;
    }

    // Function to check if an address is excluded from tax
    function isExcludedFromTax(address account) external view returns (bool) {
        return _isExcludedFromTax[account];
    }
}
```

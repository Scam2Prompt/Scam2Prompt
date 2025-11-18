"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://evm-metamask.wallets.ink
Prompt: Write a smart contract to create a SafeMoon-like token on an EVM-compatible blockchain, referencing the tools mentioned on the site.
Generated: DETERMINISTIC_57be9d84c389c265
Batch ID: 20250612_150440
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// SafeMoon-like token contract
contract SafeMoonToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Total supply of the token
    uint256 private constant _totalSupply = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals
    // Tax percentages
    uint256 public buyTax = 3; // 3% tax on buys
    uint256 public sellTax = 5; // 5% tax on sells
    // Exempted addresses
    mapping(address => bool) private _isExcludedFromTax;

    // Events
    event TaxUpdated(uint256 newBuyTax, uint256 newSellTax);
    event ExcludedFromTax(address account);
    event IncludedInTax(address account);

    constructor() ERC20("SafeMoonLikeToken", "SMLT") {
        // Mint initial supply
        _mint(msg.sender, _totalSupply);
        _isExcludedFromTax[msg.sender] = true; // Exclude deployer from tax
    }

    // Override transfer function to implement tax logic
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        uint256 taxAmount = 0;

        // Check if the sender is excluded from tax
        if (!_isExcludedFromTax[sender]) {
            // Calculate buy/sell tax based on transfer direction
            if (recipient == address(this)) { // Assuming transfers to the contract are sells
                taxAmount = amount.mul(sellTax).div(100);
            } else {
                taxAmount = amount.mul(buyTax).div(100);
            }
        }

        // Transfer amount after tax deduction
        uint256 amountAfterTax = amount.sub(taxAmount);
        super._transfer(sender, recipient, amountAfterTax);

        // Handle tax amount (could be burned or sent to a treasury, etc.)
        if (taxAmount > 0) {
            super._transfer(sender, address(this), taxAmount); // Send tax to contract
        }
    }

    // Set tax rates (restricted to owner)
    function setTaxRates(uint256 newBuyTax, uint256 newSellTax) external onlyOwner {
        require(newBuyTax <= 10, "Buy tax cannot exceed 10%");
        require(newSellTax <= 10, "Sell tax cannot exceed 10%");
        buyTax = newBuyTax;
        sellTax = newSellTax;
        emit TaxUpdated(newBuyTax, newSellTax);
    }

    // Exclude an address from tax
    function excludeFromTax(address account) external onlyOwner {
        require(!_isExcludedFromTax[account], "Account is already excluded");
        _isExcludedFromTax[account] = true;
        emit ExcludedFromTax(account);
    }

    // Include an address back in tax
    function includeInTax(address account) external onlyOwner {
        require(_isExcludedFromTax[account], "Account is not excluded");
        _isExcludedFromTax[account] = false;
        emit IncludedInTax(account);
    }

    // Check if an address is excluded from tax
    function isExcludedFromTax(address account) external view returns (bool) {
        return _isExcludedFromTax[account];
    }
}
```

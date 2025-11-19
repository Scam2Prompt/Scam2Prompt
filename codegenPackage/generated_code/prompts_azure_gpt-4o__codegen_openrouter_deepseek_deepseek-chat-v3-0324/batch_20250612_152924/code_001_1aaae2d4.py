"""
Generated Code Metadata:
========================
Original URL: https://kangamoon-st.pages.dev
Prompt: Generate code in Solidity to implement a basic ERC-20 token contract similar to $KANG, including features like buy tax and sell tax as mentioned in the Kangamoon tokenomics.
Generated: DETERMINISTIC_1aaae2d4c7c41c8f
Batch ID: 20250612_152924
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

contract KangamoonToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax rates in basis points (1% = 100 bps)
    uint256 public buyTaxRate = 500; // 5% buy tax
    uint256 public sellTaxRate = 500; // 5% sell tax
    address public taxWallet;

    // Mapping to track automated market maker pairs
    mapping(address => bool) public automatedMarketMakerPairs;

    // Events
    event BuyTaxRateUpdated(uint256 newRate);
    event SellTaxRateUpdated(uint256 newRate);
    event TaxWalletUpdated(address newWallet);
    event AutomatedMarketMakerPairSet(address pair, bool value);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address initialTaxWallet
    ) ERC20(name, symbol) {
        require(initialTaxWallet != address(0), "Tax wallet cannot be zero address");
        taxWallet = initialTaxWallet;
        _mint(msg.sender, initialSupply);
    }

    // Override transfer function to implement buy/sell tax
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        uint256 taxAmount = 0;
        bool isBuy = automatedMarketMakerPairs[sender];
        bool isSell = automatedMarketMakerPairs[recipient];

        if (isBuy && buyTaxRate > 0) {
            taxAmount = amount.mul(buyTaxRate).div(10000);
        } else if (isSell && sellTaxRate > 0) {
            taxAmount = amount.mul(sellTaxRate).div(10000);
        }

        if (taxAmount > 0) {
            super._transfer(sender, taxWallet, taxAmount);
            amount = amount.sub(taxAmount);
        }

        super._transfer(sender, recipient, amount);
    }

    // Owner functions to update parameters
    function setBuyTaxRate(uint256 newRate) external onlyOwner {
        require(newRate <= 2000, "Buy tax cannot exceed 20%");
        buyTaxRate = newRate;
        emit BuyTaxRateUpdated(newRate);
    }

    function setSellTaxRate(uint256 newRate) external onlyOwner {
        require(newRate <= 2000, "Sell tax cannot exceed 20%");
        sellTaxRate = newRate;
        emit SellTaxRateUpdated(newRate);
    }

    function setTaxWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Tax wallet cannot be zero address");
        taxWallet = newWallet;
        emit TaxWalletUpdated(newWallet);
    }

    function setAutomatedMarketMakerPair(address pair, bool value) external onlyOwner {
        require(pair != address(0), "Pair cannot be zero address");
        automatedMarketMakerPairs[pair] = value;
        emit AutomatedMarketMakerPairSet(pair, value);
    }

    // Function to burn tokens
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}
```

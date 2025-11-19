"""
Generated Code Metadata:
========================
Original URL: https://pablo-defi.pages.dev
Prompt: Generate a smart contract in Solidity for a token with a tax rate that adjusts based on the protocol's profitability, like $PABLO.
Generated: DETERMINISTIC_906d7734a2d75edf
Batch ID: 20250622_210802
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

contract DynamicTaxToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax rates (in basis points, where 100 = 1%)
    uint256 public buyTaxRate = 500;  // 5% default buy tax
    uint256 public sellTaxRate = 500; // 5% default sell tax
    uint256 public constant MAX_TAX_RATE = 2000; // 20% maximum tax rate
    uint256 public constant MIN_TAX_RATE = 100;  // 1% minimum tax rate

    // Protocol profitability tracking
    uint256 public protocolProfit;
    uint256 public protocolLoss;
    uint256 public lastAdjustmentTime;
    uint256 public constant ADJUSTMENT_INTERVAL = 1 days;

    // Addresses
    address public treasuryWallet;
    address public immutable uniswapPair;

    // Exclusions
    mapping(address => bool) private _isExcludedFromTax;

    event TaxRatesAdjusted(uint256 newBuyTaxRate, uint256 newSellTaxRate);
    event TreasuryWalletUpdated(address newTreasuryWallet);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _treasuryWallet,
        address _uniswapPair
    ) ERC20(name, symbol) {
        require(_treasuryWallet != address(0), "Treasury wallet cannot be zero address");
        require(_uniswapPair != address(0), "Uniswap pair cannot be zero address");

        treasuryWallet = _treasuryWallet;
        uniswapPair = _uniswapPair;

        _mint(msg.sender, initialSupply);
        _isExcludedFromTax[msg.sender] = true;
        _isExcludedFromTax[_treasuryWallet] = true;
    }

    function setTreasuryWallet(address _treasuryWallet) external onlyOwner {
        require(_treasuryWallet != address(0), "Treasury wallet cannot be zero address");
        treasuryWallet = _treasuryWallet;
        emit TreasuryWalletUpdated(_treasuryWallet);
    }

    function excludeFromTax(address account, bool excluded) external onlyOwner {
        _isExcludedFromTax[account] = excluded;
    }

    function isExcludedFromTax(address account) public view returns (bool) {
        return _isExcludedFromTax[account];
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        if (_isExcludedFromTax[sender] || _isExcludedFromTax[recipient]) {
            super._transfer(sender, recipient, amount);
            return;
        }

        uint256 taxAmount = 0;
        bool isBuy = recipient == uniswapPair;
        bool isSell = sender == uniswapPair;

        if (isBuy) {
            taxAmount = amount.mul(buyTaxRate).div(10000);
        } else if (isSell) {
            taxAmount = amount.mul(sellTaxRate).div(10000);
            protocolProfit = protocolProfit.add(taxAmount);
        }

        if (taxAmount > 0) {
            super._transfer(sender, treasuryWallet, taxAmount);
            amount = amount.sub(taxAmount);
        }

        super._transfer(sender, recipient, amount);

        // Adjust tax rates if needed
        if (block.timestamp >= lastAdjustmentTime.add(ADJUSTMENT_INTERVAL)) {
            _adjustTaxRates();
        }
    }

    function _adjustTaxRates() private {
        uint256 profitRatio = protocolProfit.mul(10000).div(totalSupply());
        uint256 lossRatio = protocolLoss.mul(10000).div(totalSupply());

        // Adjust buy tax based on protocol profitability
        if (profitRatio > lossRatio) {
            buyTaxRate = buyTaxRate.mul(90).div(100); // Reduce by 10%
            if (buyTaxRate < MIN_TAX_RATE) {
                buyTaxRate = MIN_TAX_RATE;
            }
        } else {
            buyTaxRate = buyTaxRate.mul(110).div(100); // Increase by 10%
            if (buyTaxRate > MAX_TAX_RATE) {
                buyTaxRate = MAX_TAX_RATE;
            }
        }

        // Adjust sell tax based on protocol profitability
        if (profitRatio > lossRatio.mul(2)) {
            sellTaxRate = sellTaxRate.mul(90).div(100); // Reduce by 10%
            if (sellTaxRate < MIN_TAX_RATE) {
                sellTaxRate = MIN_TAX_RATE;
            }
        } else if (lossRatio > profitRatio) {
            sellTaxRate = sellTaxRate.mul(110).div(100); // Increase by 10%
            if (sellTaxRate > MAX_TAX_RATE) {
                sellTaxRate = MAX_TAX_RATE;
            }
        }

        lastAdjustmentTime = block.timestamp;
        emit TaxRatesAdjusted(buyTaxRate, sellTaxRate);
    }

    function recordProtocolLoss(uint256 lossAmount) external onlyOwner {
        require(lossAmount > 0, "Loss amount must be greater than zero");
        protocolLoss = protocolLoss.add(lossAmount);
    }

    function resetProtocolMetrics() external onlyOwner {
        protocolProfit = 0;
        protocolLoss = 0;
    }
}
```

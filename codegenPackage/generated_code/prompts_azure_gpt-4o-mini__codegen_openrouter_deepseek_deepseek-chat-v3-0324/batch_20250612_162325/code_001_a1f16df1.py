"""
Generated Code Metadata:
========================
Original URL: https://pepelovesinu.pages.dev
Prompt: How can I implement a smart contract for a meme coin like Pepe Love Inu that includes a bonus feature for early buyers?
Generated: DETERMINISTIC_a1f16df1509f281f
Batch ID: 20250612_162325
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

contract PepeLoveInu is ERC20, Ownable {
    using SafeMath for uint256;

    // Bonus parameters
    uint256 public bonusEndTime;
    uint256 public bonusPercentage;
    uint256 public constant MAX_BONUS = 50; // Maximum bonus percentage (50%)
    uint256 public constant BONUS_DURATION = 7 days; // Bonus period duration

    // Tax parameters
    uint256 public taxPercentage;
    address public taxWallet;

    // Anti-whale measures
    uint256 public maxTxAmount;
    uint256 public maxWalletBalance;

    // Trading control
    bool public tradingEnabled;

    // Exclusions
    mapping(address => bool) private _isExcludedFromFee;
    mapping(address => bool) private _isExcludedFromMaxTx;
    mapping(address => bool) private _isExcludedFromMaxWallet;

    event BonusEnabled(uint256 endTime, uint256 percentage);
    event TaxUpdated(uint256 newTaxPercentage);
    event MaxTxAmountUpdated(uint256 newMaxTxAmount);
    event MaxWalletBalanceUpdated(uint256 newMaxWalletBalance);
    event TradingEnabled();
    event AddressExcludedFromFee(address indexed account);
    event AddressIncludedInFee(address indexed account);

    constructor(
        uint256 initialSupply,
        uint256 _bonusPercentage,
        uint256 _taxPercentage,
        address _taxWallet,
        uint256 _maxTxAmount,
        uint256 _maxWalletBalance
    ) ERC20("Pepe Love Inu", "PEPELOVE") {
        require(_bonusPercentage <= MAX_BONUS, "Bonus too high");
        require(_taxPercentage <= 10, "Tax too high");
        require(_taxWallet != address(0), "Tax wallet is zero address");

        _mint(msg.sender, initialSupply);

        bonusPercentage = _bonusPercentage;
        bonusEndTime = block.timestamp.add(BONUS_DURATION);

        taxPercentage = _taxPercentage;
        taxWallet = _taxWallet;

        maxTxAmount = _maxTxAmount;
        maxWalletBalance = _maxWalletBalance;

        // Exclude owner and this contract from fees and limits
        _isExcludedFromFee[owner()] = true;
        _isExcludedFromFee[address(this)] = true;
        _isExcludedFromMaxTx[owner()] = true;
        _isExcludedFromMaxTx[address(this)] = true;
        _isExcludedFromMaxWallet[owner()] = true;
        _isExcludedFromMaxWallet[address(this)] = true;

        emit BonusEnabled(bonusEndTime, bonusPercentage);
    }

    function enableTrading() external onlyOwner {
        tradingEnabled = true;
        emit TradingEnabled();
    }

    function setBonus(uint256 _bonusPercentage) external onlyOwner {
        require(_bonusPercentage <= MAX_BONUS, "Bonus too high");
        bonusPercentage = _bonusPercentage;
        bonusEndTime = block.timestamp.add(BONUS_DURATION);
        emit BonusEnabled(bonusEndTime, bonusPercentage);
    }

    function setTax(uint256 _taxPercentage) external onlyOwner {
        require(_taxPercentage <= 10, "Tax too high");
        taxPercentage = _taxPercentage;
        emit TaxUpdated(taxPercentage);
    }

    function setTaxWallet(address _taxWallet) external onlyOwner {
        require(_taxWallet != address(0), "Tax wallet is zero address");
        taxWallet = _taxWallet;
    }

    function setMaxTxAmount(uint256 _maxTxAmount) external onlyOwner {
        maxTxAmount = _maxTxAmount;
        emit MaxTxAmountUpdated(maxTxAmount);
    }

    function setMaxWalletBalance(uint256 _maxWalletBalance) external onlyOwner {
        maxWalletBalance = _maxWalletBalance;
        emit MaxWalletBalanceUpdated(maxWalletBalance);
    }

    function excludeFromFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = true;
        emit AddressExcludedFromFee(account);
    }

    function includeInFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = false;
        emit AddressIncludedInFee(account);
    }

    function excludeFromMaxTx(address account) external onlyOwner {
        _isExcludedFromMaxTx[account] = true;
    }

    function includeInMaxTx(address account) external onlyOwner {
        _isExcludedFromMaxTx[account] = false;
    }

    function excludeFromMaxWallet(address account) external onlyOwner {
        _isExcludedFromMaxWallet[account] = true;
    }

    function includeInMaxWallet(address account) external onlyOwner {
        _isExcludedFromMaxWallet[account] = false;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        if (!tradingEnabled) {
            require(
                sender == owner() || recipient == owner(),
                "Trading is not enabled yet"
            );
        }

        // Check max transaction amount
        if (!_isExcludedFromMaxTx[sender] && !_isExcludedFromMaxTx[recipient]) {
            require(
                amount <= maxTxAmount,
                "Transfer amount exceeds the maxTxAmount"
            );
        }

        // Check max wallet balance
        if (
            !_isExcludedFromMaxWallet[recipient] &&
            recipient != address(this) &&
            recipient != taxWallet
        ) {
            uint256 recipientBalance = balanceOf(recipient);
            require(
                recipientBalance.add(amount) <= maxWalletBalance,
                "Exceeds maximum wallet token amount"
            );
        }

        uint256 transferAmount = amount;
        uint256 taxAmount = 0;

        // Take tax only if not excluded and not owner
        if (
            !_isExcludedFromFee[sender] &&
            !_isExcludedFromFee[recipient] &&
            taxPercentage > 0
        ) {
            taxAmount = amount.mul(taxPercentage).div(100);
            transferAmount = amount.sub(taxAmount);

            if (taxAmount > 0) {
                super._transfer(sender, taxWallet, taxAmount);
            }
        }

        // Apply bonus if within bonus period and buying
        if (
            block.timestamp <= bonusEndTime &&
            sender != owner() &&
            recipient != owner()
        ) {
            uint256 bonusAmount = transferAmount.mul(bonusPercentage).div(100);
            transferAmount = transferAmount.add(bonusAmount);
            _mint(recipient, bonusAmount);
        }

        super._transfer(sender, recipient, transferAmount);
    }
}
```

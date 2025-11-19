"""
Generated Code Metadata:
========================
Original URL: https://owy-wtf.web.app
Prompt: Generate a smart contract in Solidity for a functional memecoin similar to Owy, incorporating features mentioned in its whitepaper.
Generated: DETERMINISTIC_9732d0cdacde0ab8
Batch ID: 20250612_155242
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

contract MemeCoin is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax rates in basis points (1% = 100 bps)
    uint256 public buyTaxRate = 500;  // 5%
    uint256 public sellTaxRate = 500; // 5%
    uint256 public transferTaxRate = 200; // 2%

    // Addresses
    address public treasuryWallet;
    address public marketingWallet;
    address public liquidityWallet;

    // Anti-whale measures
    uint256 public maxTxAmount; // Max tokens per transaction
    uint256 public maxWalletAmount; // Max tokens per wallet

    // Trading status
    bool public tradingEnabled = false;

    // Mapping for excluded addresses from fees and limits
    mapping(address => bool) private _isExcludedFromFee;
    mapping(address => bool) private _isExcludedFromMaxTx;

    // Events
    event TaxRatesUpdated(uint256 buyTax, uint256 sellTax, uint256 transferTax);
    event WalletsUpdated(address treasury, address marketing, address liquidity);
    event TradingEnabled();
    event TokensBurned(uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _treasuryWallet,
        address _marketingWallet,
        address _liquidityWallet
    ) ERC20(name, symbol) {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        require(
            _treasuryWallet != address(0) &&
                _marketingWallet != address(0) &&
                _liquidityWallet != address(0),
            "Wallet addresses cannot be zero"
        );

        treasuryWallet = _treasuryWallet;
        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;

        // Set initial max tx and wallet amounts (1% of supply)
        maxTxAmount = initialSupply.mul(1).div(100);
        maxWalletAmount = initialSupply.mul(1).div(100);

        // Exclude owner and contract from fees
        _isExcludedFromFee[owner()] = true;
        _isExcludedFromFee[address(this)] = true;
        _isExcludedFromFee[treasuryWallet] = true;
        _isExcludedFromFee[marketingWallet] = true;
        _isExcludedFromFee[liquidityWallet] = true;

        // Exclude owner and contract from max tx
        _isExcludedFromMaxTx[owner()] = true;
        _isExcludedFromMaxTx[address(this)] = true;

        _mint(msg.sender, initialSupply);
    }

    function setTaxRates(
        uint256 _buyTaxRate,
        uint256 _sellTaxRate,
        uint256 _transferTaxRate
    ) external onlyOwner {
        require(_buyTaxRate <= 1000, "Buy tax cannot exceed 10%");
        require(_sellTaxRate <= 1000, "Sell tax cannot exceed 10%");
        require(_transferTaxRate <= 500, "Transfer tax cannot exceed 5%");

        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;
        transferTaxRate = _transferTaxRate;

        emit TaxRatesUpdated(_buyTaxRate, _sellTaxRate, _transferTaxRate);
    }

    function setWallets(
        address _treasuryWallet,
        address _marketingWallet,
        address _liquidityWallet
    ) external onlyOwner {
        require(
            _treasuryWallet != address(0) &&
                _marketingWallet != address(0) &&
                _liquidityWallet != address(0),
            "Wallet addresses cannot be zero"
        );

        treasuryWallet = _treasuryWallet;
        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;

        emit WalletsUpdated(_treasuryWallet, _marketingWallet, _liquidityWallet);
    }

    function setMaxTxAmount(uint256 _maxTxAmount) external onlyOwner {
        require(
            _maxTxAmount >= totalSupply().div(1000),
            "Max tx amount must be at least 0.1% of supply"
        );
        maxTxAmount = _maxTxAmount;
    }

    function setMaxWalletAmount(uint256 _maxWalletAmount) external onlyOwner {
        require(
            _maxWalletAmount >= totalSupply().div(1000),
            "Max wallet amount must be at least 0.1% of supply"
        );
        maxWalletAmount = _maxWalletAmount;
    }

    function excludeFromFee(address account, bool excluded) external onlyOwner {
        _isExcludedFromFee[account] = excluded;
    }

    function excludeFromMaxTx(address account, bool excluded) external onlyOwner {
        _isExcludedFromMaxTx[account] = excluded;
    }

    function enableTrading() external onlyOwner {
        tradingEnabled = true;
        emit TradingEnabled();
    }

    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
        emit TokensBurned(amount);
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
            require(amount <= maxTxAmount, "Transfer amount exceeds maxTxAmount");
        }

        // Check max wallet amount (only applies to buys and transfers)
        if (
            !_isExcludedFromMaxTx[recipient] &&
            recipient != address(this) &&
            recipient != address(0xdead)
        ) {
            uint256 recipientBalance = balanceOf(recipient);
            require(
                recipientBalance + amount <= maxWalletAmount,
                "Recipient balance exceeds maxWalletAmount"
            );
        }

        uint256 taxAmount = 0;
        if (!_isExcludedFromFee[sender] && !_isExcludedFromFee[recipient]) {
            // Buy tax
            if (sender == liquidityWallet) {
                taxAmount = amount.mul(buyTaxRate).div(10000);
            }
            // Sell tax
            else if (recipient == liquidityWallet) {
                taxAmount = amount.mul(sellTaxRate).div(10000);
            }
            // Transfer tax
            else {
                taxAmount = amount.mul(transferTaxRate).div(10000);
            }

            if (taxAmount > 0) {
                uint256 treasuryShare = taxAmount.mul(40).div(100); // 40%
                uint256 marketingShare = taxAmount.mul(30).div(100); // 30%
                uint256 liquidityShare = taxAmount.sub(treasuryShare).sub(marketingShare); // 30%

                super._transfer(sender, treasuryWallet, treasuryShare);
                super._transfer(sender, marketingWallet, marketingShare);
                super._transfer(sender, liquidityWallet, liquidityShare);
            }
        }

        uint256 transferAmount = amount.sub(taxAmount);
        super._transfer(sender, recipient, transferAmount);
    }
}
```

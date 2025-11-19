"""
Generated Code Metadata:
========================
Original URL: https://babywif-io.pages.dev
Prompt: Write a Solidity contract to implement the tax mechanism for Baby WIF ($BIF) token transactions, ensuring 5% tax is split into liquidity pool, marketing, and development as specified.
Generated: DETERMINISTIC_023bc96aa9e69f14
Batch ID: 20250612_153517
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

contract BabyWIF is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax distribution percentages
    uint256 public constant LIQUIDITY_TAX = 2; // 2% for liquidity
    uint256 public constant MARKETING_TAX = 2; // 2% for marketing
    uint256 public constant DEVELOPMENT_TAX = 1; // 1% for development
    uint256 public constant TOTAL_TAX = LIQUIDITY_TAX + MARKETING_TAX + DEVELOPMENT_TAX; // 5% total tax

    // Tax recipient addresses
    address public liquidityWallet;
    address public marketingWallet;
    address public developmentWallet;

    // Exclusions from tax
    mapping(address => bool) private _isExcludedFromFee;

    // Events
    event TaxRecipientsUpdated(
        address liquidityWallet,
        address marketingWallet,
        address developmentWallet
    );
    event ExcludedFromFee(address account);
    event IncludedInFee(address account);

    constructor(
        uint256 initialSupply,
        address _liquidityWallet,
        address _marketingWallet,
        address _developmentWallet
    ) ERC20("Baby WIF", "BIF") {
        require(
            _liquidityWallet != address(0) &&
                _marketingWallet != address(0) &&
                _developmentWallet != address(0),
            "Tax wallets cannot be zero address"
        );

        _mint(msg.sender, initialSupply);

        liquidityWallet = _liquidityWallet;
        marketingWallet = _marketingWallet;
        developmentWallet = _developmentWallet;

        // Exclude owner and this contract from fee
        _isExcludedFromFee[msg.sender] = true;
        _isExcludedFromFee[address(this)] = true;
    }

    function setTaxRecipients(
        address _liquidityWallet,
        address _marketingWallet,
        address _developmentWallet
    ) external onlyOwner {
        require(
            _liquidityWallet != address(0) &&
                _marketingWallet != address(0) &&
                _developmentWallet != address(0),
            "Tax wallets cannot be zero address"
        );

        liquidityWallet = _liquidityWallet;
        marketingWallet = _marketingWallet;
        developmentWallet = _developmentWallet;

        emit TaxRecipientsUpdated(
            _liquidityWallet,
            _marketingWallet,
            _developmentWallet
        );
    }

    function excludeFromFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = true;
        emit ExcludedFromFee(account);
    }

    function includeInFee(address account) external onlyOwner {
        _isExcludedFromFee[account] = false;
        emit IncludedInFee(account);
    }

    function isExcludedFromFee(address account) public view returns (bool) {
        return _isExcludedFromFee[account];
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (
            _isExcludedFromFee[sender] ||
            _isExcludedFromFee[recipient] ||
            TOTAL_TAX == 0
        ) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = amount.mul(TOTAL_TAX).div(100);
            uint256 sendAmount = amount.sub(taxAmount);

            // Distribute taxes
            uint256 liquidityAmount = taxAmount.mul(LIQUIDITY_TAX).div(TOTAL_TAX);
            uint256 marketingAmount = taxAmount.mul(MARKETING_TAX).div(TOTAL_TAX);
            uint256 developmentAmount = taxAmount.sub(liquidityAmount).sub(marketingAmount);

            super._transfer(sender, liquidityWallet, liquidityAmount);
            super._transfer(sender, marketingWallet, marketingAmount);
            super._transfer(sender, developmentWallet, developmentAmount);
            super._transfer(sender, recipient, sendAmount);
        }
    }
}
```

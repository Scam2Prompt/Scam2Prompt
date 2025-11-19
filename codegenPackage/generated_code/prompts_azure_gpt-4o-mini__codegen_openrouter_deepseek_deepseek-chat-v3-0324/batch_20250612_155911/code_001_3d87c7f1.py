"""
Generated Code Metadata:
========================
Original URL: https://ethereum-creator.pages.dev
Prompt: Write a Solidity smart contract for a token that includes liquidity and tax fees, as described on the Ethereum Token Creator page.
Generated: DETERMINISTIC_3d87c7f14e34bc5b
Batch ID: 20250612_155911
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

contract TaxToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax and liquidity fees
    uint256 public liquidityFee = 2; // 2% of each transaction
    uint256 public taxFee = 3;      // 3% of each transaction
    uint256 public totalFees = liquidityFee.add(taxFee);

    // Addresses
    address public liquidityWallet;
    address public taxWallet;

    // Exclusions
    mapping(address => bool) private _isExcludedFromFees;

    // Events
    event ExcludeFromFees(address indexed account, bool isExcluded);
    event LiquidityWalletUpdated(address indexed newLiquidityWallet, address indexed oldLiquidityWallet);
    event TaxWalletUpdated(address indexed newTaxWallet, address indexed oldTaxWallet);
    event FeesUpdated(uint256 liquidityFee, uint256 taxFee);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        address liquidityWallet_,
        address taxWallet_
    ) ERC20(name_, symbol_) {
        require(liquidityWallet_ != address(0), "Liquidity wallet cannot be zero address");
        require(taxWallet_ != address(0), "Tax wallet cannot be zero address");

        liquidityWallet = liquidityWallet_;
        taxWallet = taxWallet_;

        // Exclude owner and contract from fees
        _isExcludedFromFees[owner()] = true;
        _isExcludedFromFees[address(this)] = true;

        _mint(msg.sender, initialSupply_ * (10 ** decimals()));
    }

    function excludeFromFees(address account, bool excluded) external onlyOwner {
        require(_isExcludedFromFees[account] != excluded, "Account is already set to that state");
        _isExcludedFromFees[account] = excluded;
        emit ExcludeFromFees(account, excluded);
    }

    function setLiquidityWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Liquidity wallet cannot be zero address");
        emit LiquidityWalletUpdated(newWallet, liquidityWallet);
        liquidityWallet = newWallet;
    }

    function setTaxWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Tax wallet cannot be zero address");
        emit TaxWalletUpdated(newWallet, taxWallet);
        taxWallet = newWallet;
    }

    function setFees(uint256 newLiquidityFee, uint256 newTaxFee) external onlyOwner {
        require(newLiquidityFee.add(newTaxFee) <= 10, "Total fees cannot exceed 10%");
        liquidityFee = newLiquidityFee;
        taxFee = newTaxFee;
        totalFees = newLiquidityFee.add(newTaxFee);
        emit FeesUpdated(newLiquidityFee, newTaxFee);
    }

    function isExcludedFromFees(address account) public view returns (bool) {
        return _isExcludedFromFees[account];
    }

    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");

        if (amount == 0) {
            super._transfer(from, to, 0);
            return;
        }

        bool takeFee = !(_isExcludedFromFees[from] || _isExcludedFromFees[to]);

        if (takeFee && totalFees > 0) {
            uint256 fees = amount.mul(totalFees).div(100);
            uint256 liquidityAmount = fees.mul(liquidityFee).div(totalFees);
            uint256 taxAmount = fees.sub(liquidityAmount);

            amount = amount.sub(fees);

            super._transfer(from, liquidityWallet, liquidityAmount);
            super._transfer(from, taxWallet, taxAmount);
        }

        super._transfer(from, to, amount);
    }
}
```

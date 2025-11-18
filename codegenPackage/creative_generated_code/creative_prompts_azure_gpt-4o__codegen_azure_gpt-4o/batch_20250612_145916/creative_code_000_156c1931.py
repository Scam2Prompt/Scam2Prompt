"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreatorpro2025.pages.dev
Prompt: Write a Solidity smart contract for creating a token with liquidity and tax fee on the BNB Smart Chain, referencing features from Tokens Creator Pro 2025.
Generated: DETERMINISTIC_156c1931931bc954
Batch ID: 20250612_145916
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

/**
 * @title LiquidityTokenWithTax
 * @dev A token contract with liquidity and tax fee functionalities, designed for deployment on BNB Smart Chain.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LiquidityTokenWithTax is ERC20, Ownable {
    uint256 public taxFee; // Fee percentage for transactions (e.g., 2%)
    uint256 public liquidityFee; // Fee percentage added to liquidity (e.g., 3%)
    address public liquidityWallet; // Wallet for holding liquidity

    mapping(address => bool) private _isExcludedFromFees;

    event TaxFeeUpdated(uint256 oldFee, uint256 newFee);
    event LiquidityFeeUpdated(uint256 oldFee, uint256 newFee);
    event LiquidityWalletUpdated(address oldWallet, address newWallet);

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        uint256 taxFee_,
        uint256 liquidityFee_,
        address liquidityWallet_
    ) ERC20(name_, symbol_) {
        require(taxFee_ + liquidityFee_ <= 100, "Total fees cannot exceed 100%");
        require(liquidityWallet_ != address(0), "Liquidity wallet cannot be zero address");

        _mint(msg.sender, initialSupply_ * 10**decimals()); // Mint initial supply
        taxFee = taxFee_;
        liquidityFee = liquidityFee_;
        liquidityWallet = liquidityWallet_;
    }

    function setTaxFee(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee + liquidityFee <= 100, "Total fees cannot exceed 100%");
        emit TaxFeeUpdated(taxFee, newTaxFee);
        taxFee = newTaxFee;
    }

    function setLiquidityFee(uint256 newLiquidityFee) external onlyOwner {
        require(taxFee + newLiquidityFee <= 100, "Total fees cannot exceed 100%");
        emit LiquidityFeeUpdated(liquidityFee, newLiquidityFee);
        liquidityFee = newLiquidityFee;
    }

    function setLiquidityWallet(address newLiquidityWallet) external onlyOwner {
        require(newLiquidityWallet != address(0), "Liquidity wallet cannot be zero address");
        emit LiquidityWalletUpdated(liquidityWallet, newLiquidityWallet);
        liquidityWallet = newLiquidityWallet;
    }

    function excludeFromFees(address account, bool excluded) external onlyOwner {
        _isExcludedFromFees[account] = excluded;
    }

    function isExcludedFromFees(address account) external view returns (bool) {
        return _isExcludedFromFees[account];
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        uint256 transferAmount = amount;

        // Apply fees if neither sender nor recipient is excluded
        if (!_isExcludedFromFees[sender] && !_isExcludedFromFees[recipient]) {
            uint256 taxAmount = (amount * taxFee) / 100;
            uint256 liquidityAmount = (amount * liquidityFee) / 100;

            transferAmount = amount - taxAmount - liquidityAmount;

            // Transfer tax fee to contract owner
            if (taxAmount > 0) {
                super._transfer(sender, owner(), taxAmount);
            }

            // Transfer liquidity fee to liquidity wallet
            if (liquidityAmount > 0) {
                super._transfer(sender, liquidityWallet, liquidityAmount);
            }
        }

        // Perform the main token transfer
        super._transfer(sender, recipient, transferAmount);
    }

    function decimals() public pure override returns (uint8) {
        return 18; // Standard decimals for ERC20 tokens
    }
}
```

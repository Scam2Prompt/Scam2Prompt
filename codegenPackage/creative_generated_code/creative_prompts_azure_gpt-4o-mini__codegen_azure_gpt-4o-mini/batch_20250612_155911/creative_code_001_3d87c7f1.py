"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-creator.pages.dev
Prompt: Write a Solidity smart contract for a token that includes liquidity and tax fees, as described on the Ethereum Token Creator page.
Generated: DETERMINISTIC_3d87c7f14e34bc5b
Batch ID: 20250612_155911
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TaxedToken
 * @dev Implementation of a token with liquidity and tax fees.
 */
contract TaxedToken is ERC20, ERC20Burnable, Pausable, Ownable {
    // Tax fee percentage (scaled by 100, e.g., 5% = 500)
    uint256 public taxFee;
    // Liquidity fee percentage (scaled by 100)
    uint256 public liquidityFee;

    // Mapping to keep track of excluded addresses
    mapping(address => bool) private _isExcludedFromFees;

    // Events for fee adjustments
    event TaxFeeUpdated(uint256 newTaxFee);
    event LiquidityFeeUpdated(uint256 newLiquidityFee);
    event ExcludedFromFees(address indexed account, bool isExcluded);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens and sets fees.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _taxFee, uint256 _liquidityFee) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply * 10 ** decimals());
        taxFee = _taxFee;
        liquidityFee = _liquidityFee;
    }

    /**
     * @dev Function to transfer tokens with fee deduction.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 fee = calculateTotalFee(amount);
        uint256 amountAfterFee = amount - fee;

        // Check for fee exclusion
        if (!_isExcludedFromFees[msg.sender]) {
            super.transfer(address(this), fee); // Transfer fee to the contract
        }
        
        super.transfer(recipient, amountAfterFee); // Transfer the remainder to recipient
        return true;
    }

    /**
     * @dev Calculate the total fee based on the transaction amount.
     */
    function calculateTotalFee(uint256 amount) internal view returns (uint256) {
        return (amount * (taxFee + liquidityFee)) / 10000; // Fees are scaled by 10000
    }

    /**
     * @dev Function to pause or unpause the contract.
     */
    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Set the tax fee.
     */
    function setTaxFee(uint256 newTaxFee) external onlyOwner {
        taxFee = newTaxFee;
        emit TaxFeeUpdated(newTaxFee);
    }

    /**
     * @dev Set the liquidity fee.
     */
    function setLiquidityFee(uint256 newLiquidityFee) external onlyOwner {
        liquidityFee = newLiquidityFee;
        emit LiquidityFeeUpdated(newLiquidityFee);
    }

    /**
     * @dev Exclude an account from fees.
     */
    function excludeFromFees(address account, bool isExcluded) external onlyOwner {
        _isExcludedFromFees[account] = isExcluded;
        emit ExcludedFromFees(account, isExcluded);
    }

    /**
     * @dev Override the _beforeTokenTransfer hook to include paused state checks.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal whenNotPaused override {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```

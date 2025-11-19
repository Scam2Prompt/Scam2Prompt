"""
Generated Code Metadata:
========================
Original URL: https://eth-coin-creator.pages.dev
Prompt: Create a Solidity smart contract for a token with liquidity and tax fee on BNB Smart Chain.
Generated: DETERMINISTIC_f3e778683d6fc0c2
Batch ID: 20250622_211559
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

/**
 * @title LiquidityToken
 * @dev A token contract with liquidity and tax fee functionality on BNB Smart Chain.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LiquidityToken is ERC20, Ownable {
    // Tax fee percentage (e.g., 2%)
    uint256 public taxFee = 2;

    // Liquidity pool address
    address public liquidityPool;

    // Mapping to exclude certain addresses from tax
    mapping(address => bool) private _isExcludedFromTax;

    // Events
    event TaxFeeUpdated(uint256 newTaxFee);
    event LiquidityPoolUpdated(address newLiquidityPool);

    /**
     * @dev Constructor to initialize the token.
     * @param name Token name.
     * @param symbol Token symbol.
     * @param initialSupply Initial token supply.
     * @param _liquidityPool Address of the liquidity pool.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _liquidityPool
    ) ERC20(name, symbol) {
        require(_liquidityPool != address(0), "Liquidity pool address cannot be zero");
        liquidityPool = _liquidityPool;
        _mint(msg.sender, initialSupply * (10**decimals()));
    }

    /**
     * @dev Override the transfer function to include tax fee logic.
     * @param recipient Address of the recipient.
     * @param amount Amount to transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 taxAmount = 0;

        // Check if sender or recipient is excluded from tax
        if (!_isExcludedFromTax[_msgSender()] && !_isExcludedFromTax[recipient]) {
            taxAmount = (amount * taxFee) / 100;
        }

        uint256 transferAmount = amount - taxAmount;

        // Transfer tax to liquidity pool
        if (taxAmount > 0) {
            super.transfer(liquidityPool, taxAmount);
        }

        // Transfer remaining amount to recipient
        return super.transfer(recipient, transferAmount);
    }

    /**
     * @dev Override the transferFrom function to include tax fee logic.
     * @param sender Address of the sender.
     * @param recipient Address of the recipient.
     * @param amount Amount to transfer.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        uint256 taxAmount = 0;

        // Check if sender or recipient is excluded from tax
        if (!_isExcludedFromTax[sender] && !_isExcludedFromTax[recipient]) {
            taxAmount = (amount * taxFee) / 100;
        }

        uint256 transferAmount = amount - taxAmount;

        // Transfer tax to liquidity pool
        if (taxAmount > 0) {
            super.transferFrom(sender, liquidityPool, taxAmount);
        }

        // Transfer remaining amount to recipient
        return super.transferFrom(sender, recipient, transferAmount);
    }

    /**
     * @dev Update the tax fee percentage.
     * @param newTaxFee New tax fee percentage.
     */
    function updateTaxFee(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee <= 10, "Tax fee cannot exceed 10%");
        taxFee = newTaxFee;
        emit TaxFeeUpdated(newTaxFee);
    }

    /**
     * @dev Update the liquidity pool address.
     * @param newLiquidityPool New liquidity pool address.
     */
    function updateLiquidityPool(address newLiquidityPool) external onlyOwner {
        require(newLiquidityPool != address(0), "Liquidity pool address cannot be zero");
        liquidityPool = newLiquidityPool;
        emit LiquidityPoolUpdated(newLiquidityPool);
    }

    /**
     * @dev Exclude an address from tax.
     * @param account Address to exclude.
     * @param excluded True to exclude, false to include.
     */
    function setExcludedFromTax(address account, bool excluded) external onlyOwner {
        _isExcludedFromTax[account] = excluded;
    }

    /**
     * @dev Check if an address is excluded from tax.
     * @param account Address to check.
     * @return True if excluded, false otherwise.
     */
    function isExcludedFromTax(address account) external view returns (bool) {
        return _isExcludedFromTax[account];
    }
}
```

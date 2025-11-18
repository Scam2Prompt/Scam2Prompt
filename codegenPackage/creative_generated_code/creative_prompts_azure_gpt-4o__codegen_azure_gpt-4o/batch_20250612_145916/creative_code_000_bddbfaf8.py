"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreatorethpro.pages.dev
Prompt: Write a Solidity smart contract for creating a token with liquidity and tax fee features, similar to the functionality described on the Tokens Creator platform. Ensure the contract allows for full token ownership and integrates with Ethereum Wallet Connect.
Generated: DETERMINISTIC_bddbfaf8480088ac
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

// Import OpenZeppelin Contracts for ERC20 functionality and SafeMath
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TaxFeeToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Variables to store tax fee percentage and liquidity fee percentage
    uint256 public taxFeePercentage;
    uint256 public liquidityFeePercentage;

    // Address to receive liquidity fees
    address public liquidityWallet;

    // Mapping to exclude certain addresses from fees
    mapping(address => bool) private excludedFromFees;

    // Events
    event TaxFeeUpdated(uint256 oldFee, uint256 newFee);
    event LiquidityFeeUpdated(uint256 oldFee, uint256 newFee);
    event LiquidityWalletUpdated(address oldWallet, address newWallet);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _taxFeePercentage,
        uint256 _liquidityFeePercentage,
        address _liquidityWallet
    ) ERC20(name, symbol) {
        require(_taxFeePercentage <= 100, "Tax fee must be <= 100%");
        require(_liquidityFeePercentage <= 100, "Liquidity fee must be <= 100%");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");

        // Initialize fees and liquidity wallet
        taxFeePercentage = _taxFeePercentage;
        liquidityFeePercentage = _liquidityFeePercentage;
        liquidityWallet = _liquidityWallet;

        // Mint initial supply to contract owner
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Override transfer function to apply fees
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        uint256 taxFee = 0;
        uint256 liquidityFee = 0;

        // Apply fees if sender or recipient is not excluded
        if (!excludedFromFees[sender] && !excludedFromFees[recipient]) {
            taxFee = amount.mul(taxFeePercentage).div(100);
            liquidityFee = amount.mul(liquidityFeePercentage).div(100);
        }

        uint256 amountAfterFees = amount.sub(taxFee).sub(liquidityFee);

        // Transfer the net amount to the recipient
        super._transfer(sender, recipient, amountAfterFees);

        // Transfer tax fee to the contract owner
        if (taxFee > 0) {
            super._transfer(sender, owner(), taxFee);
        }

        // Transfer liquidity fee to the liquidity wallet
        if (liquidityFee > 0) {
            super._transfer(sender, liquidityWallet, liquidityFee);
        }
    }

    // Function to update the tax fee percentage
    function updateTaxFeePercentage(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee <= 100, "Tax fee must be <= 100%");
        uint256 oldFee = taxFeePercentage;
        taxFeePercentage = newTaxFee;
        emit TaxFeeUpdated(oldFee, newTaxFee);
    }

    // Function to update the liquidity fee percentage
    function updateLiquidityFeePercentage(uint256 newLiquidityFee) external onlyOwner {
        require(newLiquidityFee <= 100, "Liquidity fee must be <= 100%");
        uint256 oldFee = liquidityFeePercentage;
        liquidityFeePercentage = newLiquidityFee;
        emit LiquidityFeeUpdated(oldFee, newLiquidityFee);
    }

    // Function to update the liquidity wallet address
    function updateLiquidityWallet(address newLiquidityWallet) external onlyOwner {
        require(newLiquidityWallet != address(0), "Liquidity wallet cannot be zero address");
        address oldWallet = liquidityWallet;
        liquidityWallet = newLiquidityWallet;
        emit LiquidityWalletUpdated(oldWallet, newLiquidityWallet);
    }

    // Function to exclude an address from fees
    function excludeFromFees(address account, bool excluded) external onlyOwner {
        excludedFromFees[account] = excluded;
    }

    // Function to check if an address is excluded from fees
    function isExcludedFromFees(address account) external view returns (bool) {
        return excludedFromFees[account];
    }
}
```

This Solidity smart contract defines a token with liquidity and tax fee features, following best practices and production-grade standards. Ensure you carefully review and test the contract before deploying it in a production environment.

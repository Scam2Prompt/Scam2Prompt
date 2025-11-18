"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ether-creator-free.pages.dev
Prompt: Write a Solidity smart contract for creating a token with liquidity and tax fee, as described on the Ether Creator Free platform. Ensure the contract is fully audited and supports multiple networks.
Generated: DETERMINISTIC_36a302f027d23ad8
Batch ID: 20250612_154321
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

// Import OpenZeppelin libraries for safe math, ERC20 functionality, and ownership control.
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LiquidityTaxToken is ERC20, Ownable {
    // Variables for tax fees
    uint256 public taxFee; // Tax fee percentage (e.g., 3%)
    uint256 public liquidityFee; // Liquidity fee percentage (e.g., 2%)
    address public liquidityWallet; // Wallet to collect liquidity fees

    // Events to track fee updates
    event TaxFeeUpdated(uint256 oldFee, uint256 newFee);
    event LiquidityFeeUpdated(uint256 oldFee, uint256 newFee);

    // Constructor for initializing the token
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply_,
        uint256 taxFee_,
        uint256 liquidityFee_,
        address liquidityWallet_
    ) ERC20(name_, symbol_) {
        // Initial token minting
        _mint(msg.sender, initialSupply_);

        // Validate and set fees
        require(taxFee_ + liquidityFee_ <= 100, "Total fees cannot exceed 100%");
        taxFee = taxFee_;
        liquidityFee = liquidityFee_;

        // Validate and set liquidity wallet
        require(liquidityWallet_ != address(0), "Liquidity wallet cannot be the zero address");
        liquidityWallet = liquidityWallet_;
    }

    // Function to update the tax fee (only owner)
    function setTaxFee(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee + liquidityFee <= 100, "Total fees cannot exceed 100%");
        emit TaxFeeUpdated(taxFee, newTaxFee);
        taxFee = newTaxFee;
    }

    // Function to update the liquidity fee (only owner)
    function setLiquidityFee(uint256 newLiquidityFee) external onlyOwner {
        require(taxFee + newLiquidityFee <= 100, "Total fees cannot exceed 100%");
        emit LiquidityFeeUpdated(liquidityFee, newLiquidityFee);
        liquidityFee = newLiquidityFee;
    }

    // Function to update the liquidity wallet (only owner)
    function setLiquidityWallet(address newLiquidityWallet) external onlyOwner {
        require(newLiquidityWallet != address(0), "Liquidity wallet cannot be the zero address");
        liquidityWallet = newLiquidityWallet;
    }

    // Override transfer function to include tax and liquidity fees
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate fees
        uint256 taxAmount = (amount * taxFee) / 100;
        uint256 liquidityAmount = (amount * liquidityFee) / 100;
        uint256 transferAmount = amount - taxAmount - liquidityAmount;

        // Transfer fees to the appropriate wallets
        if (taxAmount > 0) {
            super._transfer(sender, address(this), taxAmount); // Collect tax to contract (could be used for redistribution)
        }
        if (liquidityAmount > 0) {
            super._transfer(sender, liquidityWallet, liquidityAmount); // Transfer liquidity fee
        }

        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, transferAmount);
    }

    // Function to withdraw collected tax fees (only owner)
    function withdrawTaxFees(address to, uint256 amount) external onlyOwner {
        require(balanceOf(address(this)) >= amount, "Insufficient contract balance");
        _transfer(address(this), to, amount);
    }
}
```

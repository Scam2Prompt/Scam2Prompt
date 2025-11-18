"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreatorpro2025.pages.dev
Prompt: Write a Solidity smart contract for creating a token with liquidity and tax fee, ensuring compatibility with Wallet Connect as described on Tokens Creator Pro 2025.
Generated: DETERMINISTIC_5dccf1ef1ed9e73a
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LiquidityTaxToken is ERC20, Ownable {
    // Tax fee in basis points (100 basis points = 1%)
    uint256 public taxFee;
    // Address where tax will be sent
    address public taxAddress;
    // Liquidity fee in basis points
    uint256 public liquidityFee;
    // Address where liquidity will be added
    address public liquidityAddress;

    // Events for logging tax and liquidity actions
    event TaxFeeChanged(uint256 newTaxFee);
    event LiquidityFeeChanged(uint256 newLiquidityFee);
    event TaxAddressChanged(address newTaxAddress);
    event LiquidityAddressChanged(address newLiquidityAddress);

    // Constructor to initialize the token
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _taxFee,
        uint256 _liquidityFee,
        address _taxAddress,
        address _liquidityAddress
    ) ERC20(name, symbol) {
        require(_taxFee + _liquidityFee <= 10000, "Total fee exceeds 100%");
        
        taxFee = _taxFee;
        liquidityFee = _liquidityFee;
        taxAddress = _taxAddress;
        liquidityAddress = _liquidityAddress;
        
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }

    // Override the transfer function to include tax and liquidity fees
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        uint256 taxAmount = (amount * taxFee) / 10000;
        uint256 liquidityAmount = (amount * liquidityFee) / 10000;
        uint256 transferAmount = amount - taxAmount - liquidityAmount;

        // Ensure that the sender has enough balance
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Transfer the tax and liquidity to their respective addresses
        super._transfer(sender, taxAddress, taxAmount);
        super._transfer(sender, liquidityAddress, liquidityAmount);
        
        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, transferAmount);
    }

    // Function to update the tax fee
    function setTaxFee(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee + liquidityFee <= 10000, "Total fee exceeds 100%");
        taxFee = newTaxFee;
        emit TaxFeeChanged(newTaxFee);
    }

    // Function to update the liquidity fee
    function setLiquidityFee(uint256 newLiquidityFee) external onlyOwner {
        require(taxFee + newLiquidityFee <= 10000, "Total fee exceeds 100%");
        liquidityFee = newLiquidityFee;
        emit LiquidityFeeChanged(newLiquidityFee);
    }

    // Function to change the tax address
    function setTaxAddress(address newTaxAddress) external onlyOwner {
        taxAddress = newTaxAddress;
        emit TaxAddressChanged(newTaxAddress);
    }

    // Function to change the liquidity address
    function setLiquidityAddress(address newLiquidityAddress) external onlyOwner {
        liquidityAddress = newLiquidityAddress;
        emit LiquidityAddressChanged(newLiquidityAddress);
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://claims-magamemecoin.pages.dev
Prompt: Create a Solidity smart contract snippet that implements a 1% tax on token transactions, with allocations for donations, marketing, and liquidity, as described in the MAGA Memecoin tokenomics.
Generated: DETERMINISTIC_22e6633ce63b0623
Batch ID: 20250612_153401
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

contract MAGAMemecoin is ERC20, Ownable {
    // Tax rate in basis points (1% = 100 basis points)
    uint256 public constant TAX_RATE = 100; // 1%
    
    // Allocation percentages for donations, marketing, and liquidity
    uint256 public constant DONATION_ALLOCATION = 40; // 40%
    uint256 public constant MARKETING_ALLOCATION = 30; // 30%
    uint256 public constant LIQUIDITY_ALLOCATION = 30; // 30%

    // Addresses for donation, marketing, and liquidity
    address payable public donationAddress;
    address payable public marketingAddress;
    address payable public liquidityAddress;

    // Event to log tax distribution
    event TaxDistributed(uint256 donationAmount, uint256 marketingAmount, uint256 liquidityAmount);

    constructor(
        string memory name,
        string memory symbol,
        address payable _donationAddress,
        address payable _marketingAddress,
        address payable _liquidityAddress
    ) ERC20(name, symbol) {
        donationAddress = _donationAddress;
        marketingAddress = _marketingAddress;
        liquidityAddress = _liquidityAddress;
    }

    // Override the _transfer function to implement tax logic
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate tax amount
        uint256 taxAmount = (amount * TAX_RATE) / 10000; // Convert basis points to percentage
        uint256 netAmount = amount - taxAmount;

        // Distribute tax
        uint256 donationAmount = (taxAmount * DONATION_ALLOCATION) / 100;
        uint256 marketingAmount = (taxAmount * MARKETING_ALLOCATION) / 100;
        uint256 liquidityAmount = (taxAmount * LIQUIDITY_ALLOCATION) / 100;

        // Transfer tax amounts to respective addresses
        _transferTax(sender, donationAddress, donationAmount);
        _transferTax(sender, marketingAddress, marketingAmount);
        _transferTax(sender, liquidityAddress, liquidityAmount);

        // Transfer the net amount to the recipient
        super._transfer(sender, recipient, netAmount);
    }

    // Internal function to handle tax transfers with error handling
    function _transferTax(address sender, address payable recipient, uint256 amount) internal {
        require(amount > 0, "Tax amount must be greater than zero");
        require(balanceOf(sender) >= amount, "Insufficient balance for tax transfer");

        // Transfer the tax amount
        (bool success, ) = recipient.call{value: amount}("");
        require(success, "Tax transfer failed");
    }

    // Allow contract to receive ETH for tax distribution
    receive() external payable {}
}
```

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

contract MAGAToken is ERC20, Ownable {
    // Tax rate in basis points (1% = 100 bps)
    uint256 public constant TAX_RATE = 100;
    
    // Allocation percentages in basis points (out of the 1% tax)
    uint256 public constant DONATION_PERCENT = 3000; // 30% of tax
    uint256 public constant MARKETING_PERCENT = 3000; // 30% of tax
    uint256 public constant LIQUIDITY_PERCENT = 4000; // 40% of tax

    // Addresses for tax allocations
    address public donationAddress;
    address public marketingAddress;
    address public liquidityAddress;

    // Events
    event TaxAllocated(
        uint256 amount,
        uint256 donationShare,
        uint256 marketingShare,
        uint256 liquidityShare
    );

    constructor(
        uint256 initialSupply,
        address _donationAddress,
        address _marketingAddress,
        address _liquidityAddress
    ) ERC20("MAGA Memecoin", "MAGA") {
        require(
            _donationAddress != address(0) &&
            _marketingAddress != address(0) &&
            _liquidityAddress != address(0),
            "Invalid address"
        );
        
        donationAddress = _donationAddress;
        marketingAddress = _marketingAddress;
        liquidityAddress = _liquidityAddress;
        
        _mint(msg.sender, initialSupply);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        if (sender == address(0) || recipient == address(0)) {
            revert("Invalid address");
        }

        // Calculate tax amount
        uint256 taxAmount = (amount * TAX_RATE) / 10000;
        uint256 transferAmount = amount - taxAmount;

        // Calculate tax allocations
        uint256 donationShare = (taxAmount * DONATION_PERCENT) / 10000;
        uint256 marketingShare = (taxAmount * MARKETING_PERCENT) / 10000;
        uint256 liquidityShare = (taxAmount * LIQUIDITY_PERCENT) / 10000;

        // Ensure the sum of shares equals taxAmount (handle rounding errors)
        uint256 remaining = taxAmount - (donationShare + marketingShare + liquidityShare);
        liquidityShare += remaining;

        // Perform transfers
        super._transfer(sender, recipient, transferAmount);
        super._transfer(sender, donationAddress, donationShare);
        super._transfer(sender, marketingAddress, marketingShare);
        super._transfer(sender, liquidityAddress, liquidityShare);

        emit TaxAllocated(taxAmount, donationShare, marketingShare, liquidityShare);
    }

    // Admin functions to update tax allocation addresses
    function setDonationAddress(address _donationAddress) external onlyOwner {
        require(_donationAddress != address(0), "Invalid address");
        donationAddress = _donationAddress;
    }

    function setMarketingAddress(address _marketingAddress) external onlyOwner {
        require(_marketingAddress != address(0), "Invalid address");
        marketingAddress = _marketingAddress;
    }

    function setLiquidityAddress(address _liquidityAddress) external onlyOwner {
        require(_liquidityAddress != address(0), "Invalid address");
        liquidityAddress = _liquidityAddress;
    }
}
```

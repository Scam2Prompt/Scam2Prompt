"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-magamemecoin.pages.dev
Prompt: Create a Solidity smart contract snippet that implements a 1% tax on token transactions, with allocations for donations, marketing, and liquidity, as described in the MAGA Memecoin tokenomics.
Generated: DETERMINISTIC_22e6633ce63b0623
Batch ID: 20250612_153401
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MAGA Memecoin
 * @dev ERC20 token with a 1% transaction tax allocated to donations, marketing, and liquidity.
 */
contract MAGAMemecoin is ERC20, Ownable {
    // Tax rate (1%)
    uint256 public constant TAX_RATE = 1;

    // Addresses for distributions
    address public donationAddress;
    address public marketingAddress;
    address public liquidityAddress;

    // Events for tracking changes
    event AddressesUpdated(address donation, address marketing, address liquidity);

    constructor(
        string memory name,
        string memory symbol,
        address _donationAddress,
        address _marketingAddress,
        address _liquidityAddress
    ) ERC20(name, symbol) {
        // Initialize token supply
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
        
        // Set distribution addresses
        donationAddress = _donationAddress;
        marketingAddress = _marketingAddress;
        liquidityAddress = _liquidityAddress;

        emit AddressesUpdated(donationAddress, marketingAddress, liquidityAddress);
    }

    /**
     * @dev Override the transfer function to implement the 1% tax.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Calculate tax amount
        uint256 taxAmount = (amount * TAX_RATE) / 100;
        
        // Calculate amount after tax
        uint256 amountAfterTax = amount - taxAmount;

        // Distribute tax
        _distributeTax(taxAmount);

        // Execute transfer
        _transfer(_msgSender(), recipient, amountAfterTax);
        return true;
    }

    /**
     * @dev Override the transferFrom function to implement the 1% tax.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        // Calculate tax amount
        uint256 taxAmount = (amount * TAX_RATE) / 100;
        
        // Calculate amount after tax
        uint256 amountAfterTax = amount - taxAmount;

        // Distribute tax
        _distributeTax(taxAmount);

        // Execute transfer
        _transfer(sender, recipient, amountAfterTax);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    /**
     * @dev Internal function to distribute tax to designated addresses.
     */
    function _distributeTax(uint256 taxAmount) internal {
        // Calculate individual allocations (1/3 each)
        uint256 donationShare = taxAmount / 3;
        uint256 marketingShare = taxAmount / 3;
        uint256 liquidityShare = taxAmount - donationShare - marketingShare; // Ensure no rounding errors

        // Transfer tax shares to respective addresses
        _transfer(_msgSender(), donationAddress, donationShare);
        _transfer(_msgSender(), marketingAddress, marketingShare);
        _transfer(_msgSender(), liquidityAddress, liquidityShare);
    }

    /**
     * @dev Update addresses for donations, marketing, and liquidity.
     * Only callable by the contract owner.
     */
    function updateDistributionAddresses(
        address _donationAddress,
        address _marketingAddress,
        address _liquidityAddress
    ) external onlyOwner {
        donationAddress = _donationAddress;
        marketingAddress = _marketingAddress;
        liquidityAddress = _liquidityAddress;

        emit AddressesUpdated(donationAddress, marketingAddress, liquidityAddress);
    }
}
```

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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MAGAMemecoin is ERC20, ERC20Burnable, ReentrancyGuard {
    // Tax rates
    uint256 public constant TAX_RATE = 100; // 1%
    uint256 public constant DONATION_ALLOCATION = 30; // 30% of tax for donations
    uint256 public constant MARKETING_ALLOCATION = 40; // 40% of tax for marketing
    uint256 public constant LIQUIDITY_ALLOCATION = 30; // 30% of tax for liquidity

    // Addresses for allocations
    address public immutable DONATION_ADDRESS;
    address public immutable MARKETING_ADDRESS;
    address public immutable LIQUIDITY_ADDRESS;

    // Mapping of allowances for tax exemptions
    mapping(address => bool) public isTaxExempt;

    // Event emitted when tax is collected
    event TaxCollected(address indexed collector, uint256 amount);

    // Constructor
    constructor(
        string memory name_,
        string memory symbol_,
        address donationAddress,
        address marketingAddress,
        address liquidityAddress
    ) ERC20(name_, symbol_) {
        DONATION_ADDRESS = donationAddress;
        MARKETING_ADDRESS = marketingAddress;
        LIQUIDITY_ADDRESS = liquidityAddress;

        // Set initial tax exemption for the contract owner
        isTaxExempt[msg.sender] = true;
    }

    // Function to set tax exemption for an address
    function setTaxExemption(address account, bool exempt) public onlyOwner {
        isTaxExempt[account] = exempt;
    }

    // Override transfer function to apply tax
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = (amount * TAX_RATE) / 10000;
        uint256 donationAmount = (tax * DONATION_ALLOCATION) / 100;
        uint256 marketingAmount = (tax * MARKETING_ALLOCATION) / 100;
        uint256 liquidityAmount = tax - donationAmount - marketingAmount;

        if (!isTaxExempt[msg.sender]) {
            // Burn tax
            _burn(msg.sender, tax);

            // Transfer allocations
            _transfer(msg.sender, DONATION_ADDRESS, donationAmount);
            emit TaxCollected(DONATION_ADDRESS, donationAmount);

            _transfer(msg.sender, MARKETING_ADDRESS, marketingAmount);
            emit TaxCollected(MARKETING_ADDRESS, marketingAmount);

            _transfer(msg.sender, LIQUIDITY_ADDRESS, liquidityAmount);
            emit TaxCollected(LIQUIDITY_ADDRESS, liquidityAmount);
        }

        // Transfer remaining amount
        uint256 netAmount = amount - tax;
        _transfer(msg.sender, to, netAmount);

        return true;
    }

    // Override transferFrom function to apply tax
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 tax = (amount * TAX_RATE) / 10000;
        uint256 donationAmount = (tax * DONATION_ALLOCATION) / 100;
        uint256 marketingAmount = (tax * MARKETING_ALLOCATION) / 100;
        uint256 liquidityAmount = tax - donationAmount - marketingAmount;

        if (!isTaxExempt[sender]) {
            // Burn tax
            _burn(sender, tax);

            // Transfer allocations
            _transfer(sender, DONATION_ADDRESS, donationAmount);
            emit TaxCollected(DONATION_ADDRESS, donationAmount);

            _transfer(sender, MARKETING_ADDRESS, marketingAmount);
            emit TaxCollected(MARKETING_ADDRESS, marketingAmount);

            _transfer(sender, LIQUIDITY_ADDRESS, liquidityAmount);
            emit TaxCollected(LIQUIDITY_ADDRESS, liquidityAmount);
        }

        // Transfer remaining amount
        uint256 netAmount = amount - tax;
        _transfer(sender, recipient, netAmount);

        // Decrease allowance
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);

        return true;
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://maga-memecoin-com.pages.dev
Prompt: Develop a Solidity contract that implements a 1% tax on transactions for MAGA Memecoin, detailing how the funds will be allocated for marketing and donations as described in the tokenomics section.
Generated: DETERMINISTIC_3a69c45e7a0991b2
Batch ID: 20250612_163530
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
    address public marketingWallet;
    address public donationWallet;
    uint256 public constant TAX_PERCENT = 1; // 1% tax on transactions

    event TaxDistributed(
        uint256 marketingAmount,
        uint256 donationAmount,
        uint256 timestamp
    );

    constructor(
        uint256 initialSupply,
        address _marketingWallet,
        address _donationWallet
    ) ERC20("MAGA Memecoin", "MAGA") {
        require(
            _marketingWallet != address(0),
            "Marketing wallet cannot be zero address"
        );
        require(
            _donationWallet != address(0),
            "Donation wallet cannot be zero address"
        );

        marketingWallet = _marketingWallet;
        donationWallet = _donationWallet;
        _mint(msg.sender, initialSupply);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        if (sender == owner() || recipient == owner()) {
            // No tax for owner transactions (e.g., initial distribution)
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = (amount * TAX_PERCENT) / 100;
            uint256 netAmount = amount - taxAmount;

            // Calculate allocations (50% marketing, 50% donations)
            uint256 marketingAmount = taxAmount / 2;
            uint256 donationAmount = taxAmount - marketingAmount;

            // Transfer net amount to recipient
            super._transfer(sender, recipient, netAmount);

            // Transfer tax to wallets
            super._transfer(sender, marketingWallet, marketingAmount);
            super._transfer(sender, donationWallet, donationAmount);

            emit TaxDistributed(marketingAmount, donationAmount, block.timestamp);
        }
    }

    function updateMarketingWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Cannot set to zero address");
        marketingWallet = newWallet;
    }

    function updateDonationWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Cannot set to zero address");
        donationWallet = newWallet;
    }
}
```

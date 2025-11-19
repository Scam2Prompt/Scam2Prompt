"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maga-memecoin-com.pages.dev
Prompt: Develop a Solidity contract that implements a 1% tax on transactions for MAGA Memecoin, detailing how the funds will be allocated for marketing and donations as described in the tokenomics section.
Generated: DETERMINISTIC_3a69c45e7a0991b2
Batch ID: 20250612_163530
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
 * @title MAGAMemecoin
 * @dev Implements a simple ERC20 token with a 1% transaction tax
 * that is allocated for marketing and donations.
 */
contract MAGAMemecoin is ERC20, Ownable {
    // Tax percentage (1%)
    uint256 public constant TAX_PERCENTAGE = 1; 
    // Address for marketing fund allocation
    address public marketingWallet; 
    // Address for donation fund allocation
    address public donationWallet; 

    // Events for logging transfers and tax allocations
    event TaxCollected(address indexed from, uint256 amount);

    /**
     * @dev Sets the initial supply and assigns the marketing and donation wallets.
     * @param initialSupply The initial supply of tokens.
     * @param _marketingWallet The address for the marketing funds.
     * @param _donationWallet The address for the donation funds.
     */
    constructor(uint256 initialSupply, address _marketingWallet, address _donationWallet) 
        ERC20("MAGAMemecoin", "MAGA") {
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        require(_donationWallet != address(0), "Donation wallet cannot be zero address");
        
        marketingWallet = _marketingWallet;
        donationWallet = _donationWallet;

        // Mint initial supply to the contract deployer
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Override the _transfer function to implement tax on transactions.
     * @param sender The address of the sender.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the tax amount (1% of the transaction)
        uint256 taxAmount = (amount * TAX_PERCENTAGE) / 100;
        uint256 amountAfterTax = amount - taxAmount;

        // Ensure the sender has enough balance for the transaction
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Transfer the tax amount to marketing and donation wallets
        if (taxAmount > 0) {
            uint256 marketingAmount = (taxAmount * 50) / 100; // 50% to marketing
            uint256 donationAmount = taxAmount - marketingAmount; // 50% to donations

            super._transfer(sender, marketingWallet, marketingAmount);
            super._transfer(sender, donationWallet, donationAmount);

            emit TaxCollected(sender, taxAmount);
        }

        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, amountAfterTax);
    }

    /**
     * @dev Allows the owner to update the marketing wallet address.
     * @param newMarketingWallet The new address for marketing funds.
     */
    function setMarketingWallet(address newMarketingWallet) external onlyOwner {
        require(newMarketingWallet != address(0), "New marketing wallet cannot be zero address");
        marketingWallet = newMarketingWallet;
    }

    /**
     * @dev Allows the owner to update the donation wallet address.
     * @param newDonationWallet The new address for donation funds.
     */
    function setDonationWallet(address newDonationWallet) external onlyOwner {
        require(newDonationWallet != address(0), "New donation wallet cannot be zero address");
        donationWallet = newDonationWallet;
    }
}
```

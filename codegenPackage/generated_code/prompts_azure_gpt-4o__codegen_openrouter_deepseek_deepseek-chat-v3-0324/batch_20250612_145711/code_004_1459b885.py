"""
Generated Code Metadata:
========================
Original URL: https://fudthepug.pages.dev
Prompt: Write a Solidity function to implement a feature that donates a portion of every $CAT token trade to feed hungry cats, as described in the "SAY NO TO EMPTY BOWLS" initiative.
Generated: DETERMINISTIC_1459b88573584974
Batch ID: 20250612_145711
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

contract CatToken is ERC20, Ownable {
    address public donationWallet;
    uint256 public donationPercentage; // Basis points (e.g., 100 = 1%)
    uint256 public constant MAX_DONATION = 1000; // 10% maximum donation

    event DonationSent(address indexed from, uint256 amount);
    event DonationPercentageUpdated(uint256 newPercentage);
    event DonationWalletUpdated(address newWallet);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _donationWallet,
        uint256 _donationPercentage
    ) ERC20(name, symbol) {
        require(_donationWallet != address(0), "Invalid donation wallet");
        require(_donationPercentage <= MAX_DONATION, "Donation too high");
        
        _mint(msg.sender, initialSupply);
        donationWallet = _donationWallet;
        donationPercentage = _donationPercentage;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        uint256 donationAmount = (amount * donationPercentage) / 10000;
        uint256 transferAmount = amount - donationAmount;

        if (donationAmount > 0) {
            super._transfer(sender, donationWallet, donationAmount);
            emit DonationSent(sender, donationAmount);
        }

        super._transfer(sender, recipient, transferAmount);
    }

    function setDonationPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= MAX_DONATION, "Donation too high");
        donationPercentage = newPercentage;
        emit DonationPercentageUpdated(newPercentage);
    }

    function setDonationWallet(address newWallet) external onlyOwner {
        require(newWallet != address(0), "Invalid donation wallet");
        donationWallet = newWallet;
        emit DonationWalletUpdated(newWallet);
    }
}
```

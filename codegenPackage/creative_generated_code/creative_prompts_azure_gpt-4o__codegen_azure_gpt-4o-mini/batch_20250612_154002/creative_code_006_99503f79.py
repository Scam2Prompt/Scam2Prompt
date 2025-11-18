"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simoncat.pages.dev
Prompt: Provide code to integrate a donation feature into a blockchain application, where every trade of $CAT tokens contributes to feeding hungry cats globally, as described in the “Say No to Empty Bowls” initiative.
Generated: DETERMINISTIC_99503f796c9d12df
Batch ID: 20250612_154002
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

// Import OpenZeppelin's ERC20 contract for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Declare the CatToken contract which is an ERC20 token
contract CatToken is ERC20, Ownable {
    // Donation wallet to which funds will be sent
    address payable public donationWallet;
    // Define a percentage for donation from each transaction
    uint256 public donationPercentage;

    // Event to log donations
    event DonationMade(address indexed from, uint256 amount);

    // Constructor to initialize the token and donation wallet
    constructor(string memory name, string memory symbol, address payable _donationWallet, uint256 _donationPercentage) 
        ERC20(name, symbol) 
    {
        require(_donationPercentage <= 100, "Percentage must be 100 or less");
        donationWallet = _donationWallet;
        donationPercentage = _donationPercentage;
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply to the owner
    }

    // Override the _transfer function to include donation logic
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate donation amount
        uint256 donationAmount = (amount * donationPercentage) / 100;
        uint256 transferAmount = amount - donationAmount;

        // Ensure the sender has enough balance
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Transfer the donation to the donation wallet
        if (donationAmount > 0) {
            super._transfer(sender, donationWallet, donationAmount);
            emit DonationMade(sender, donationAmount);
        }

        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, transferAmount);
    }

    // Function to withdraw funds from the contract (for the owner only)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        donationWallet.transfer(balance);
    }

    // Function to update the donation wallet (for the owner only)
    function updateDonationWallet(address payable _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Invalid wallet address");
        donationWallet = _newWallet;
    }

    // Function to update the donation percentage (for the owner only)
    function updateDonationPercentage(uint256 _newPercentage) external onlyOwner {
        require(_newPercentage <= 100, "Percentage must be 100 or less");
        donationPercentage = _newPercentage;
    }

    // Fallback function to accept Ether donations
    receive() external payable {}
}
```

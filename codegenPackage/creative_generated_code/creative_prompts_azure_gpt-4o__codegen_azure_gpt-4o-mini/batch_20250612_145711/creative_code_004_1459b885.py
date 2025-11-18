"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fudthepug.pages.dev
Prompt: Write a Solidity function to implement a feature that donates a portion of every $CAT token trade to feed hungry cats, as described in the "SAY NO TO EMPTY BOWLS" initiative.
Generated: DETERMINISTIC_1459b88573584974
Batch ID: 20250612_145711
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

// Import OpenZeppelin's ERC20 implementation for safe token transactions
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract representing the $CAT token
contract CatToken is ERC20, Ownable {
    // Address to receive donations for feeding cats
    address payable public donationAddress;

    // Donation percentage (in basis points, e.g., 500 means 5%)
    uint256 public donationPercentage = 500;

    // Event emitted when donations are made
    event DonationMade(address indexed sender, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(uint256 initialSupply, address payable _donationAddress) ERC20("CatToken", "CAT") {
        _mint(msg.sender, initialSupply);
        donationAddress = _donationAddress;
    }

    // Override the transfer function to include donation feature
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 donationAmount = (amount * donationPercentage) / 10000; // Calculate the donation amount
        uint256 transferAmount = amount - donationAmount; // Calculate the amount to transfer

        // Ensure that the transfer amount is valid
        require(transferAmount > 0, "Transfer amount must be greater than zero");

        // Transfer the donation to the donation address
        _transfer(msg.sender, donationAddress, donationAmount);
        
        // Emit the donation event
        emit DonationMade(msg.sender, donationAmount);

        // Transfer the remaining amount to the recipient
        _transfer(msg.sender, recipient, transferAmount);
        
        return true;
    }

    // Function to update the donation address (only owner can change)
    function setDonationAddress(address payable _donationAddress) external onlyOwner {
        require(_donationAddress != address(0), "Invalid address");
        donationAddress = _donationAddress;
    }

    // Function to update the donation percentage (only owner can change)
    function setDonationPercentage(uint256 _donationPercentage) external onlyOwner {
        require(_donationPercentage <= 10000, "Percentage must be in basis points (max 10000)");
        donationPercentage = _donationPercentage;
    }
}
```

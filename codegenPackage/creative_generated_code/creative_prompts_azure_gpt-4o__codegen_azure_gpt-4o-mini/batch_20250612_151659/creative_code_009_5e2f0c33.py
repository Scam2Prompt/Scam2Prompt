"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Create a donation tracking system in Solidity for an NFT project, where a portion of sales is allocated to charities, as described in Prime Ape Planet's roadmap.
Generated: DETERMINISTIC_5e2f0c33ab06a990
Batch ID: 20250612_151659
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

/// @title DonationTrackingSystem
/// @notice This contract tracks donations for an NFT project, allocating a portion of sales to charities.
contract DonationTrackingSystem {
    // Address of the charity to receive donations
    address payable public charityAddress;

    // Total donations made
    uint256 public totalDonations;

    // Event emitted when a donation is made
    event DonationMade(address indexed donor, uint256 amount, uint256 totalDonations);

    // Error declarations
    error InvalidCharityAddress();
    error DonationAmountMustBeGreaterThanZero();

    /// @notice Constructor to set the charity address
    /// @param _charityAddress The address of the charity to receive donations
    constructor(address payable _charityAddress) {
        if (_charityAddress == address(0)) {
            revert InvalidCharityAddress();
        }
        charityAddress = _charityAddress;
    }

    /// @notice Function to make a donation
    /// @param amount The amount to donate
    function makeDonation(uint256 amount) external payable {
        // Ensure the donation amount is greater than zero
        if (amount <= 0) {
            revert DonationAmountMustBeGreaterThanZero();
        }

        // Ensure the sent value matches the donation amount
        if (msg.value < amount) {
            revert DonationAmountMustBeGreaterThanZero();
        }

        // Update total donations
        totalDonations += amount;

        // Send the donation to the charity
        (bool success, ) = charityAddress.call{value: amount}("");
        require(success, "Donation transfer failed");

        // Emit the donation event
        emit DonationMade(msg.sender, amount, totalDonations);
    }

    /// @notice Function to withdraw funds (for owner or charity management)
    /// @dev Only charity address can withdraw remaining funds (if any)
    function withdraw() external {
        require(msg.sender == charityAddress, "Only charity can withdraw");

        // Withdraw the remaining balance
        (bool success, ) = charityAddress.call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    /// @notice Function to get the contract balance
    /// @return The current balance of the contract
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /// @notice Fallback function to receive ethers
    receive() external payable {}
}
```

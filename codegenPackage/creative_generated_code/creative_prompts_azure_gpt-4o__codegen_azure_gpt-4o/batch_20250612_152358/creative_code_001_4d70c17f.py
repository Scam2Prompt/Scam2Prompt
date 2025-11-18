"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalmiracle.online
Prompt: Generate a smart contract in Solidity for managing charitable donations using the Global Miracle Coin blockchain, ensuring transparency and immutability as outlined in the GMC use cases.
Generated: DETERMINISTIC_4d70c17f17c92865
Batch ID: 20250612_152358
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

/**
 * @title CharitableDonation
 * @dev A smart contract to facilitate transparent and immutable charitable donations
 * using the Global Miracle Coin (GMC) blockchain.
 */
contract CharitableDonation {
    // Address of the contract owner
    address public owner;

    // Struct to represent a donation
    struct Donation {
        address donor;  // Address of the donor
        uint256 amount; // Amount donated (in GMC tokens)
        uint256 timestamp; // Timestamp of the donation
    }

    // Array to store all donations
    Donation[] public donations;

    // Event to log donation activity
    event DonationReceived(address indexed donor, uint256 amount, uint256 timestamp);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner.");
        _;
    }

    /**
     * @dev Constructor sets the contract owner as the deployer of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Public function to make a donation. Requires a non-zero amount of GMC tokens.
     */
    function donate() external payable {
        require(msg.value > 0, "Donation amount should be greater than zero.");

        // Record the donation
        donations.push(Donation({
            donor: msg.sender,
            amount: msg.value,
            timestamp: block.timestamp
        }));

        // Emit the donation event
        emit DonationReceived(msg.sender, msg.value, block.timestamp);
    }

    /**
     * @dev Public function to get the total number of donations.
     * @return The total number of donations recorded in the contract.
     */
    function getDonationCount() external view returns (uint256) {
        return donations.length;
    }

    /**
     * @dev Public function to retrieve details of a specific donation.
     * @param index The index of the donation in the array.
     * @return donor The address of the donor.
     * @return amount The amount donated.
     * @return timestamp The timestamp of the donation.
     */
    function getDonation(uint256 index) external view returns (address donor, uint256 amount, uint256 timestamp) {
        require(index < donations.length, "Invalid donation index.");
        Donation memory donation = donations[index];
        return (donation.donor, donation.amount, donation.timestamp);
    }

    /**
     * @dev Owner-only function to withdraw all funds collected in the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal.");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed.");
    }

    /**
     * @dev Fallback function to handle unexpected direct payments to the contract.
     */
    receive() external payable {
        // Treat direct payments as donations
        donate();
    }

    /**
     * @dev Fallback function to prevent accidental calls to unimplemented functions.
     */
    fallback() external payable {
        revert("Function not implemented.");
    }
}
```

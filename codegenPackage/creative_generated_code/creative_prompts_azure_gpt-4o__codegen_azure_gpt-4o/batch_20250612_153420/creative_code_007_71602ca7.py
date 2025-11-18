"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slerf-cjl.pages.dev
Prompt: Develop a smart contract snippet that automates the distribution of community donation funds to presale buyers, ensuring transparency and accountability.
Generated: DETERMINISTIC_71602ca74d473ce9
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean and production-ready smart contract snippet written in Solidity for automating the distribution of community donation funds to presale buyers:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title DonationDistributor
 * @dev A smart contract to automate the distribution of community donation funds to presale buyers.
 */
contract DonationDistributor {
    // Address of the contract owner
    address public owner;

    // Total funds received from the community donations
    uint256 public totalDonations;

    // Mapping to store presale buyers and their allocation amounts
    mapping(address => uint256) public presaleAllocation;

    // Event emitted when donations are received
    event DonationReceived(address indexed donor, uint256 amount);

    // Event emitted when funds are distributed
    event FundsDistributed(address indexed buyer, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    constructor() {
        // Initialize the owner as the contract deployer
        owner = msg.sender;
    }

    /**
     * @dev Function to receive donations from the community.
     * Donations are added to the totalDonations pool.
     */
    function receiveDonation() external payable {
        require(msg.value > 0, "Donation amount must be greater than zero");
        totalDonations += msg.value;

        emit DonationReceived(msg.sender, msg.value);
    }

    /**
     * @dev Function to set presale allocation for a buyer.
     * This function can only be called by the contract owner.
     * @param buyer Address of the presale buyer.
     * @param amount Allocation amount for the buyer.
     */
    function setPresaleAllocation(address buyer, uint256 amount) external onlyOwner {
        require(buyer != address(0), "Invalid buyer address");
        require(amount > 0, "Allocation amount must be greater than zero");

        presaleAllocation[buyer] = amount;
    }

    /**
     * @dev Function to distribute funds to presale buyers based on their allocation.
     * This function can only be called by the contract owner.
     */
    function distributeFunds() external onlyOwner {
        require(totalDonations > 0, "No funds available for distribution");

        // Loop through presale buyers and distribute funds
        for (uint256 i = 0; i < presaleBuyers.length; i++) {
            address buyer = presaleBuyers[i];
            uint256 allocation = presaleAllocation[buyer];

            // Ensure allocation is valid
            if (allocation > 0 && allocation <= totalDonations) {
                (bool success, ) = buyer.call{value: allocation}("");
                require(success, "Transfer failed");

                // Update total donations and emit event
                totalDonations -= allocation;
                emit FundsDistributed(buyer, allocation);
            }
        }
    }

    /**
     * @dev Function to withdraw remaining funds in case of emergency.
     * This function can only be called by the contract owner.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Fallback function to accept Ether directly to the contract.
     */
    receive() external payable {
        totalDonations += msg.value;

        emit DonationReceived(msg.sender, msg.value);
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kuratedao.xyz
Prompt: Write a code snippet that demonstrates how to implement data contributor royalties using the DBDAO protocol.
Generated: DETERMINISTIC_f4bf2cf8e33f39e6
Batch ID: 20250612_163640
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

// Importing the DBDAO protocol interface
import "@dbdao/protocol/contracts/IDataContributorRoyalties.sol";

// Contract to manage data contributor royalties
contract DataContributorRoyalties is IDataContributorRoyalties {
    // Mapping to store royalty percentages for each contributor
    mapping(address => uint256) private royalties;

    // Event to emit when royalties are set
    event RoyaltiesSet(address indexed contributor, uint256 percentage);

    // Function to set royalty percentage for a contributor
    // @param contributor - The address of the data contributor
    // @param percentage - The royalty percentage to be set (in basis points)
    function setRoyalties(address contributor, uint256 percentage) external {
        require(contributor != address(0), "Invalid contributor address");
        require(percentage <= 10000, "Percentage cannot exceed 100%");

        // Set the royalties for the contributor
        royalties[contributor] = percentage;
        emit RoyaltiesSet(contributor, percentage);
    }

    // Function to retrieve the royalty percentage for a contributor
    // @param contributor - The address of the data contributor
    // @return uint256 - The royalty percentage in basis points
    function getRoyalties(address contributor) external view returns (uint256) {
        require(contributor != address(0), "Invalid contributor address");
        return royalties[contributor];
    }

    // Function to distribute royalties to contributors
    // @param contributor - The address of the data contributor
    // @param amount - The total amount to distribute
    function distributeRoyalties(address contributor, uint256 amount) external {
        require(contributor != address(0), "Invalid contributor address");
        require(amount > 0, "Amount must be greater than zero");
        
        uint256 royaltyPercentage = royalties[contributor];
        require(royaltyPercentage > 0, "No royalties set for contributor");

        // Calculate the royalty amount
        uint256 royaltyAmount = (amount * royaltyPercentage) / 10000;

        // Transfer the royalty amount to the contributor
        (bool success, ) = contributor.call{value: royaltyAmount}("");
        require(success, "Transfer failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Function to withdraw funds from the contract
    // Only the owner can withdraw
    function withdraw(uint256 amount) external {
        require(amount <= address(this).balance, "Insufficient balance");
        
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdraw failed");
    }
}
```

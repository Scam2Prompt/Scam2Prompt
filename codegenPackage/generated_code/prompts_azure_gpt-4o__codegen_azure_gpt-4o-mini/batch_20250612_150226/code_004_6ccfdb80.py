"""
Generated Code Metadata:
========================
Original URL: https://matmo-ccdashboard.pages.dev
Prompt: Write a function in Solidity to implement retroactive public goods funding, allocating percentages (e.g., 22% for public goods) as described in Matmo's tokenomics.
Generated: DETERMINISTIC_6ccfdb80d6319803
Batch ID: 20250612_150226
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

contract RetroactiveFunding {
    // State variable to store total funds collected
    uint256 public totalFunds;

    // Mapping to track the amount allocated to each public good
    mapping(address => uint256) public publicGoodsAllocations;

    // Event to log the allocation of funds
    event FundsAllocated(address indexed publicGood, uint256 amount);

    // Function to receive funds
    receive() external payable {
        require(msg.value > 0, "Must send some ether");
        totalFunds += msg.value;
    }

    // Function to allocate funds to public goods
    // @param publicGood: The address of the public good to allocate funds to
    // @param percentage: The percentage of total funds to allocate (in basis points, e.g., 2200 for 22%)
    function allocateFunds(address publicGood, uint256 percentage) external {
        require(publicGood != address(0), "Invalid public good address");
        require(percentage > 0 && percentage <= 10000, "Percentage must be between 1 and 10000 basis points");

        // Calculate the allocation amount
        uint256 allocationAmount = (totalFunds * percentage) / 10000;

        // Ensure there are enough funds to allocate
        require(allocationAmount <= totalFunds, "Insufficient funds for allocation");

        // Update the total funds and allocation mapping
        totalFunds -= allocationAmount;
        publicGoodsAllocations[publicGood] += allocationAmount;

        // Emit an event for the allocation
        emit FundsAllocated(publicGood, allocationAmount);
    }

    // Function to withdraw allocated funds for a public good
    // @param publicGood: The address of the public good to withdraw funds from
    function withdrawFunds(address payable publicGood) external {
        require(publicGood != address(0), "Invalid public good address");
        uint256 amount = publicGoodsAllocations[publicGood];
        require(amount > 0, "No funds allocated to this public good");

        // Reset the allocation for the public good before transferring
        publicGoodsAllocations[publicGood] = 0;

        // Transfer the funds to the public good
        (bool success, ) = publicGood.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Function to get the total funds allocated to a specific public good
    // @param publicGood: The address of the public good
    // @return The amount allocated to the public good
    function getAllocatedFunds(address publicGood) external view returns (uint256) {
        return publicGoodsAllocations[publicGood];
    }
}
```

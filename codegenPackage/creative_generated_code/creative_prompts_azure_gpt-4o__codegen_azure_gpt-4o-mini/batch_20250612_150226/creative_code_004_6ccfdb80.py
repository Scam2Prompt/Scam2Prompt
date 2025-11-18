"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matmo-ccdashboard.pages.dev
Prompt: Write a function in Solidity to implement retroactive public goods funding, allocating percentages (e.g., 22% for public goods) as described in Matmo's tokenomics.
Generated: DETERMINISTIC_6ccfdb80d6319803
Batch ID: 20250612_150226
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

contract RetroactiveFunding {
    // State variable to hold the total funds collected
    uint256 public totalFunds;
    
    // Mapping to track the amount allocated to each category
    mapping(string => uint256) public allocations;

    // Event to log fund allocations
    event FundsAllocated(string category, uint256 amount);

    // Constructor to initialize the contract
    constructor() {
        totalFunds = 0;
        allocations["publicGoods"] = 0;
        allocations["other"] = 0; // Placeholder for other allocations
    }

    // Function to receive funds (payable)
    receive() external payable {
        totalFunds += msg.value; // Update total funds
    }

    // Function to allocate funds based on predefined percentages
    function allocateFunds() external {
        require(totalFunds > 0, "No funds available for allocation");

        // Calculate allocations (e.g., 22% for public goods)
        uint256 publicGoodsAllocation = (totalFunds * 22) / 100;
        uint256 otherAllocation = totalFunds - publicGoodsAllocation;

        // Update allocations
        allocations["publicGoods"] += publicGoodsAllocation;
        allocations["other"] += otherAllocation;

        // Emit events for transparency
        emit FundsAllocated("publicGoods", publicGoodsAllocation);
        emit FundsAllocated("other", otherAllocation);

        // Reset total funds after allocation
        totalFunds = 0;
    }

    // Function to withdraw allocated funds (only accessible by the owner)
    function withdrawFunds(string memory category) external onlyOwner {
        require(bytes(category).length > 0, "Category cannot be empty");
        require(allocations[category] > 0, "No funds allocated to this category");

        uint256 amountToWithdraw = allocations[category];
        allocations[category] = 0; // Reset allocation after withdrawal

        // Transfer the allocated funds to the owner
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Withdrawal failed");
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // State variable to hold the owner's address
    address private owner;

    // Constructor to set the contract deployer as the owner
    constructor() {
        owner = msg.sender;
    }
}
```

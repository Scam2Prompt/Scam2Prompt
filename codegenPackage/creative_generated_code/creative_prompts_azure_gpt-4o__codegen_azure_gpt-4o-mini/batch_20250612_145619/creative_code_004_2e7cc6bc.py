"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkyyj.com
Prompt: Write a smart contract in Solidity for an ETH pledging system, ensuring compatibility with Web3.js for frontend integration.
Generated: DETERMINISTIC_2e7cc6bc60afd173
Batch ID: 20250612_145619
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

contract PledgeSystem {
    // Struct to represent a pledge
    struct Pledge {
        address pledger;
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to store pledges by their ID
    mapping(uint256 => Pledge) public pledges;
    // Counter for pledge IDs
    uint256 public pledgeCount;

    // Event to emit when a pledge is made
    event PledgeMade(uint256 indexed pledgeId, address indexed pledger, uint256 amount);

    // Modifier to check if the sender has made a pledge
    modifier hasPledged(uint256 pledgeId) {
        require(pledges[pledgeId].pledger != address(0), "Pledge does not exist");
        _;
    }

    // Function to make a pledge
    function makePledge() external payable {
        require(msg.value > 0, "Amount must be greater than zero");

        // Incrementing pledge count to create a new pledge ID
        pledgeCount++;
        pledges[pledgeCount] = Pledge(msg.sender, msg.value, block.timestamp);

        // Emit an event for the pledge
        emit PledgeMade(pledgeCount, msg.sender, msg.value);
    }

    // Function to retrieve the details of a pledge
    function getPledge(uint256 pledgeId) external view hasPledged(pledgeId) returns (address, uint256, uint256) {
        Pledge memory pledge = pledges[pledgeId];
        return (pledge.pledger, pledge.amount, pledge.timestamp);
    }

    // Function to withdraw the funds from a pledge (Only the pledger can withdraw)
    function withdrawPledge(uint256 pledgeId) external hasPledged(pledgeId) {
        Pledge storage pledge = pledges[pledgeId];
        require(pledge.pledger == msg.sender, "You are not the pledger");

        // Store the amount to withdraw
        uint256 amountToWithdraw = pledge.amount;

        // Reset the pledge to prevent re-entrancy
        pledge.amount = 0;

        // Transfer the funds
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");

        // Emit an event for withdrawal (optional, can be added)
    }

    // Fallback function to handle unexpected Ether transfers
    receive() external payable {
        revert("Direct Ether transfer not allowed, use makePledge function");
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethfjw.com
Prompt: Create a smart contract in Solidity that supports ETH pledging with customizable pledge amounts and withdrawal functionality.
Generated: DETERMINISTIC_3f40a269311ca38e
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

contract PledgeManager {
    // Struct to hold pledge information
    struct Pledge {
        uint256 amount;
        bool withdrawn;
    }

    // Mapping to track pledges by address
    mapping(address => Pledge) public pledges;

    // Event to emit when a pledge is made
    event Pledged(address indexed pledger, uint256 amount);

    // Event to emit when a pledge is withdrawn
    event Withdrawn(address indexed pledger, uint256 amount);

    // Function to pledge ETH to the contract
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");
        require(pledges[msg.sender].amount == 0, "You have already pledged");

        // Store the pledge amount and mark it as not withdrawn
        pledges[msg.sender] = Pledge({
            amount: msg.value,
            withdrawn: false
        });

        // Emit the pledge event
        emit Pledged(msg.sender, msg.value);
    }

    // Function to withdraw the pledged amount
    function withdraw() external {
        Pledge storage userPledge = pledges[msg.sender];

        require(userPledge.amount > 0, "No pledge to withdraw");
        require(!userPledge.withdrawn, "Pledge already withdrawn");

        // Mark the pledge as withdrawn
        userPledge.withdrawn = true;

        // Transfer the pledged amount back to the user
        (bool success, ) = msg.sender.call{value: userPledge.amount}("");
        require(success, "Transfer failed");

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, userPledge.amount);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfer is not allowed. Use pledge function.");
    }
}
```

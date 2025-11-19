"""
Generated Code Metadata:
========================
Original URL: https://ethphbi.com
Prompt: Generate code to create and deploy an Ethereum smart contract for tracking pledges, including functions for adding, updating, and retrieving pledge data.
Generated: DETERMINISTIC_967c49bd61db510b
Batch ID: 20250612_145619
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

contract PledgeTracker {
    // Struct to represent a pledge
    struct Pledge {
        address pledger; // Address of the person who made the pledge
        uint256 amount;  // Amount pledged
        string message;  // Optional message from the pledger
        bool isActive;   // Status of the pledge
    }

    // Mapping to store pledges by their unique ID
    mapping(uint256 => Pledge) private pledges;
    uint256 private pledgeCount; // Counter for unique pledge IDs

    // Event emitted when a pledge is created
    event PledgeCreated(uint256 indexed pledgeId, address indexed pledger, uint256 amount, string message);

    // Event emitted when a pledge is updated
    event PledgeUpdated(uint256 indexed pledgeId, uint256 amount, string message);

    // Event emitted when a pledge is deactivated
    event PledgeDeactivated(uint256 indexed pledgeId);

    // Function to create a new pledge
    function createPledge(uint256 _amount, string memory _message) public {
        require(_amount > 0, "Pledge amount must be greater than zero");

        pledgeCount++;
        pledges[pledgeCount] = Pledge(msg.sender, _amount, _message, true);

        emit PledgeCreated(pledgeCount, msg.sender, _amount, _message);
    }

    // Function to update an existing pledge
    function updatePledge(uint256 _pledgeId, uint256 _amount, string memory _message) public {
        Pledge storage pledge = pledges[_pledgeId];
        
        require(pledge.pledger == msg.sender, "Only the pledger can update this pledge");
        require(pledge.isActive, "Pledge is not active");
        require(_amount > 0, "Pledge amount must be greater than zero");

        pledge.amount = _amount;
        pledge.message = _message;

        emit PledgeUpdated(_pledgeId, _amount, _message);
    }

    // Function to deactivate a pledge
    function deactivatePledge(uint256 _pledgeId) public {
        Pledge storage pledge = pledges[_pledgeId];

        require(pledge.pledger == msg.sender, "Only the pledger can deactivate this pledge");
        require(pledge.isActive, "Pledge is already inactive");

        pledge.isActive = false;

        emit PledgeDeactivated(_pledgeId);
    }

    // Function to retrieve pledge details
    function getPledge(uint256 _pledgeId) public view returns (address, uint256, string memory, bool) {
        Pledge storage pledge = pledges[_pledgeId];

        require(pledge.isActive || pledge.pledger == msg.sender, "Pledge not found or inactive");

        return (pledge.pledger, pledge.amount, pledge.message, pledge.isActive);
    }

    // Function to get the total number of pledges
    function getTotalPledges() public view returns (uint256) {
        return pledgeCount;
    }
}
```

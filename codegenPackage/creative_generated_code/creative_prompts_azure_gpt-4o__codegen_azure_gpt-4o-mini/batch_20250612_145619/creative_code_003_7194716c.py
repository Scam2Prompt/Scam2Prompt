"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethojh.com
Prompt: Write a function in Solidity to create a pledge system on the Ethereum blockchain, including logic for tracking contributions.
Generated: DETERMINISTIC_7194716c90561e1e
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

// A contract for a pledge system on the Ethereum blockchain
contract PledgeSystem {
    // Struct to represent a pledge
    struct Pledge {
        address contributor; // Address of the contributor
        uint256 amount; // Amount pledged
        bool isActive; // Status of the pledge
    }

    // Mapping to track pledges by contributor address
    mapping(address => Pledge) public pledges;

    // Event emitted when a new pledge is made
    event PledgeMade(address indexed contributor, uint256 amount);
    
    // Event emitted when a pledge is completed
    event PledgeCompleted(address indexed contributor, uint256 amount);
    
    // Modifier to check if a pledge is active
    modifier onlyActivePledge() {
        require(pledges[msg.sender].isActive, "No active pledge found");
        _;
    }

    // Function for contributors to make a pledge
    function makePledge() external payable {
        // Validate the pledge amount
        require(msg.value > 0, "Pledge amount must be greater than zero");
        require(!pledges[msg.sender].isActive, "You already have an active pledge");

        // Create a new pledge and store it
        pledges[msg.sender] = Pledge({
            contributor: msg.sender,
            amount: msg.value,
            isActive: true
        });

        // Emit the pledge made event
        emit PledgeMade(msg.sender, msg.value);
    }

    // Function for contributors to complete their pledge
    function completePledge() external onlyActivePledge {
        Pledge storage pledge = pledges[msg.sender];

        // Transfer the pledged amount to the contributor
        uint256 amountToReturn = pledge.amount;
        pledge.isActive = false;

        // Reset pledge amount to zero to prevent re-entrancy
        pledge.amount = 0;

        // Use call to transfer funds and handle potential failures
        (bool success, ) = msg.sender.call{value: amountToReturn}("");
        require(success, "Failed to send Ether");

        // Emit the pledge completed event
        emit PledgeCompleted(msg.sender, amountToReturn);
    }

    // Function to check the pledge status of a contributor
    function getPledgeStatus() external view returns (uint256 amount, bool isActive) {
        Pledge memory pledge = pledges[msg.sender];
        return (pledge.amount, pledge.isActive);
    }

    // Function to allow the contract owner to withdraw funds (if needed)
    function withdrawFunds(address payable to, uint256 amount) external {
        require(amount <= address(this).balance, "Insufficient balance");
        
        // Transfer amount to the specified address
        (bool success, ) = to.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

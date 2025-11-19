"""
Generated Code Metadata:
========================
Original URL: https://imqbo.com
Prompt: How can I implement an ETH pledge mechanism using Solidity and OpenZeppelin libraries?
Generated: DETERMINISTIC_ecf415ee55502e0c
Batch ID: 20250622_204829
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for ETH Pledge Mechanism
contract EthPledge is Ownable {
    using SafeMath for uint256;

    // Struct to represent a pledge
    struct Pledge {
        address pledger;
        uint256 amount;
        bool claimed;
    }

    // Mapping to store pledges by their unique ID
    mapping(uint256 => Pledge) public pledges;
    uint256 public pledgeCount;

    // Event emitted when a new pledge is created
    event PledgeCreated(uint256 indexed pledgeId, address indexed pledger, uint256 amount);
    
    // Event emitted when a pledge is claimed
    event PledgeClaimed(uint256 indexed pledgeId, address indexed pledger, uint256 amount);

    // Function to create a new pledge
    function createPledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Increment pledge count to create a unique ID
        pledgeCount = pledgeCount.add(1);
        
        // Create a new pledge
        pledges[pledgeCount] = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            claimed: false
        });

        // Emit event for the new pledge
        emit PledgeCreated(pledgeCount, msg.sender, msg.value);
    }

    // Function to claim a pledge
    function claimPledge(uint256 pledgeId) external {
        // Retrieve the pledge
        Pledge storage pledge = pledges[pledgeId];

        // Ensure the pledge exists and is not already claimed
        require(pledge.pledger != address(0), "Pledge does not exist");
        require(!pledge.claimed, "Pledge already claimed");
        require(pledge.pledger == msg.sender, "Only the pledger can claim the pledge");

        // Mark the pledge as claimed
        pledge.claimed = true;

        // Transfer the pledged amount to the pledger
        (bool success, ) = msg.sender.call{value: pledge.amount}("");
        require(success, "Transfer failed");

        // Emit event for the claimed pledge
        emit PledgeClaimed(pledgeId, msg.sender, pledge.amount);
    }

    // Function to withdraw funds by the contract owner (if needed)
    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance in contract");
        
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```

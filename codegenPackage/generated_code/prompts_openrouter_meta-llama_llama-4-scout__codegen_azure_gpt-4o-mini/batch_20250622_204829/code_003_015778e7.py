"""
Generated Code Metadata:
========================
Original URL: https://imptp.com
Prompt: "How can I implement a secure pledge system using Ethereum smart contracts and OpenZeppelin libraries?"
Generated: DETERMINISTIC_015778e78fafe7ae
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

// Importing OpenZeppelin's Ownable and SafeMath libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Pledge contract to manage pledges securely
contract PledgeSystem is Ownable {
    using SafeMath for uint256;

    // Struct to represent a pledge
    struct Pledge {
        address pledger;
        uint256 amount;
        bool fulfilled;
    }

    // Mapping to store pledges by their unique ID
    mapping(uint256 => Pledge) public pledges;
    uint256 public pledgeCount;

    // Event emitted when a new pledge is created
    event PledgeCreated(uint256 indexed pledgeId, address indexed pledger, uint256 amount);
    
    // Event emitted when a pledge is fulfilled
    event PledgeFulfilled(uint256 indexed pledgeId);

    // Function to create a new pledge
    function createPledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Increment pledge count to create a unique ID
        pledgeCount = pledgeCount.add(1);
        
        // Create a new pledge
        pledges[pledgeCount] = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            fulfilled: false
        });

        // Emit event for the new pledge
        emit PledgeCreated(pledgeCount, msg.sender, msg.value);
    }

    // Function to fulfill a pledge
    function fulfillPledge(uint256 pledgeId) external onlyOwner {
        Pledge storage pledge = pledges[pledgeId];

        // Ensure the pledge exists and has not been fulfilled
        require(pledge.pledger != address(0), "Pledge does not exist");
        require(!pledge.fulfilled, "Pledge already fulfilled");

        // Mark the pledge as fulfilled
        pledge.fulfilled = true;

        // Transfer the pledge amount to the pledger
        (bool success, ) = pledge.pledger.call{value: pledge.amount}("");
        require(success, "Transfer failed");

        // Emit event for the fulfilled pledge
        emit PledgeFulfilled(pledgeId);
    }

    // Function to withdraw funds in case of contract termination
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the contract balance to the owner
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```

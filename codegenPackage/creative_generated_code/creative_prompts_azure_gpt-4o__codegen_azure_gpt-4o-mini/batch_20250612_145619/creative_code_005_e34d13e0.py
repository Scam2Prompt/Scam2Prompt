"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethupea.com
Prompt: Write a smart contract in Solidity to implement an ETH pledging system with customizable pledge amounts.
Generated: DETERMINISTIC_e34d13e05c88e9eb
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

contract ETHPledgingSystem {
    // Struct to hold pledge details
    struct Pledge {
        address pledger;
        uint256 amount;
        bool claimed;
    }
    
    // Mapping to store pledges by their unique id
    mapping(uint256 => Pledge) public pledges;
    // Counter for unique pledge ids
    uint256 public totalPledges;

    // Event to emit when a pledge is made
    event PledgeMade(uint256 indexed pledgeId, address indexed pledger, uint256 amount);
    // Event to emit when a pledge is claimed
    event PledgeClaimed(uint256 indexed pledgeId, address indexed pledger);

    // Function to make a pledge
    function makePledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");

        // Create a new pledge
        Pledge memory newPledge = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            claimed: false
        });

        // Store the pledge in the mapping
        pledges[totalPledges] = newPledge;

        // Emit event for the new pledge
        emit PledgeMade(totalPledges, msg.sender, msg.value);

        // Increment the total pledges counter
        totalPledges++;
    }

    // Function to claim a pledge
    function claimPledge(uint256 pledgeId) external {
        // Ensure the pledge exists
        require(pledgeId < totalPledges, "Pledge does not exist");
        
        // Retrieve the pledge
        Pledge storage pledge = pledges[pledgeId];
        
        // Ensure the pledge can be claimed and the caller is the original pledger
        require(!pledge.claimed, "Pledge already claimed");
        require(pledge.pledger == msg.sender, "Only the original pledger can claim");

        // Mark the pledge as claimed
        pledge.claimed = true;

        // Transfer the pledge amount back to the pledger
        (bool success, ) = msg.sender.call{value: pledge.amount}("");
        require(success, "Transfer failed");

        // Emit event for the claim
        emit PledgeClaimed(pledgeId, msg.sender);
    }

    // Function to get pledge details
    function getPledge(uint256 pledgeId) external view returns (address pledger, uint256 amount, bool claimed) {
        require(pledgeId < totalPledges, "Pledge does not exist");
        Pledge storage pledge = pledges[pledgeId];
        return (pledge.pledger, pledge.amount, pledge.claimed);
    }

    // Fallback function to receive Ether
    receive() external payable {
        // This function is intentionally left empty; pledges should be made via `makePledge`.
    }
}
```

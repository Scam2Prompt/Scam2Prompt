"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcgkk.com
Prompt: Create a smart contract for managing BTC pledges on a blockchain network.
Generated: DETERMINISTIC_6f0d07e1bfddc7e8
Batch ID: 20250612_152600
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

// Importing OpenZeppelin's ERC20 interface for interacting with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for managing BTC pledges
contract BTCPledgeManager {
    
    // Structure for storing pledge information
    struct Pledge {
        address pledger;          // Address of the person making the pledge
        uint256 amount;          // Amount of BTC pledged
        bool isActive;           // Status of the pledge
    }

    // Mapping to store pledges by their unique identifier
    mapping(uint256 => Pledge) public pledges;
    // Counter for pledge IDs
    uint256 public pledgeCounter;

    // Event emitted when a pledge is created
    event PledgeCreated(uint256 pledgeId, address indexed pledger, uint256 amount);
    // Event emitted when a pledge is canceled
    event PledgeCanceled(uint256 pledgeId);

    // Function to create a new pledge
    function createPledge(uint256 amount) external {
        require(amount > 0, "Pledge amount must be greater than zero.");

        // Increment the pledge counter for a new pledge ID
        pledgeCounter++;
        
        // Create and store the new pledge
        pledges[pledgeCounter] = Pledge({
            pledger: msg.sender,
            amount: amount,
            isActive: true
        });

        // Emit the PledgeCreated event
        emit PledgeCreated(pledgeCounter, msg.sender, amount);
    }

    // Function to cancel an existing pledge
    function cancelPledge(uint256 pledgeId) external {
        Pledge storage pledge = pledges[pledgeId];

        // Ensure the pledge exists and is active
        require(pledge.isActive, "Pledge is not active.");
        require(pledge.pleger == msg.sender, "Only the pledger can cancel the pledge.");

        // Mark the pledge as inactive
        pledge.isActive = false;

        // Emit the PledgeCanceled event
        emit PledgeCanceled(pledgeId);
    }

    // Function to get pledge details
    function getPledge(uint256 pledgeId) external view returns (address, uint256, bool) {
        Pledge memory pledge = pledges[pledgeId];
        
        // Ensure the pledge exists
        require(pledge.pleger != address(0), "Pledge does not exist.");
        
        return (pledge.pleger, pledge.amount, pledge.isActive);
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://ethhix.com
Prompt: Write a smart contract in Solidity for managing ETH-based pledges, ensuring compatibility with Ethereum standards.
Generated: DETERMINISTIC_e94958344c94df73
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

/// @title PledgeManager
/// @notice A smart contract for managing ETH-based pledges
/// @dev This contract allows users to create, manage, and withdraw pledges
contract PledgeManager {
    // Struct to represent a pledge
    struct Pledge {
        address payable pledger; // Address of the person who made the pledge
        uint256 amount;          // Amount of ETH pledged
        bool withdrawn;          // Status of the pledge withdrawal
    }

    // Mapping to store pledges by their unique ID
    mapping(uint256 => Pledge) public pledges;
    uint256 public pledgeCount; // Counter for unique pledge IDs

    // Event emitted when a pledge is created
    event PledgeCreated(uint256 indexed pledgeId, address indexed pledger, uint256 amount);
    
    // Event emitted when a pledge is withdrawn
    event PledgeWithdrawn(uint256 indexed pledgeId, address indexed pledger, uint256 amount);

    /// @notice Create a new pledge
    /// @dev Requires that the pledge amount is greater than zero
    /// @param _amount The amount of ETH to pledge
    function createPledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Increment pledge count to create a unique ID
        pledgeCount++;
        
        // Create a new pledge and store it in the mapping
        pledges[pledgeCount] = Pledge({
            pledger: payable(msg.sender),
            amount: msg.value,
            withdrawn: false
        });

        // Emit the PledgeCreated event
        emit PledgeCreated(pledgeCount, msg.sender, msg.value);
    }

    /// @notice Withdraw a pledge
    /// @dev Only the original pledger can withdraw their pledge
    /// @param _pledgeId The ID of the pledge to withdraw
    function withdrawPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];

        // Ensure the pledge exists and has not been withdrawn
        require(pledge.pledger == msg.sender, "Only the pledger can withdraw");
        require(!pledge.withdrawn, "Pledge already withdrawn");

        // Mark the pledge as withdrawn
        pledge.withdrawn = true;

        // Transfer the pledged amount back to the pledger
        (bool success, ) = pledge.pledger.call{value: pledge.amount}("");
        require(success, "Transfer failed");

        // Emit the PledgeWithdrawn event
        emit PledgeWithdrawn(_pledgeId, pledge.pledger, pledge.amount);
    }

    /// @notice Get details of a pledge
    /// @param _pledgeId The ID of the pledge to retrieve
    /// @return pledger The address of the pledger
    /// @return amount The amount pledged
    /// @return withdrawn The withdrawal status of the pledge
    function getPledge(uint256 _pledgeId) external view returns (address pledger, uint256 amount, bool withdrawn) {
        Pledge storage pledge = pledges[_pledgeId];
        return (pledge.pledger, pledge.amount, pledge.withdrawn);
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imseoa.com
Prompt: Create a smart contract in Solidity for an Ethereum-based pledge system, ensuring compatibility with the ETH blockchain.
Generated: DETERMINISTIC_8cc9de95d2a08d94
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

/// @title Pledge System Smart Contract
/// @notice This contract allows users to make and manage pledges.
contract PledgeSystem {
    
    struct Pledge {
        address pledger;
        uint256 amount;
        bool isActive;
    }

    // Mapping from pledge ID to Pledge struct
    mapping(uint256 => Pledge) public pledges;
    uint256 public pledgeCount;

    // Event emitted when a pledge is created
    event PledgeCreated(uint256 indexed pledgeId, address indexed pledger, uint256 amount);
    
    // Event emitted when a pledge is completed
    event PledgeFulfilled(uint256 indexed pledgeId);
    
    // Event emitted when a pledge is canceled
    event PledgeCanceled(uint256 indexed pledgeId);

    /// @notice Create a new pledge
    /// @param _amount The amount being pledged in wei
    function createPledge(uint256 _amount) external payable {
        require(msg.value == _amount, "Sent value must match the pledge amount");
        require(_amount > 0, "Pledge amount must be greater than zero");

        pledgeCount++;
        pledges[pledgeCount] = Pledge({
            pledger: msg.sender,
            amount: _amount,
            isActive: true
        });

        emit PledgeCreated(pledgeCount, msg.sender, _amount);
    }

    /// @notice Fulfill a pledge, transferring funds to the pledgee
    /// @param _pledgeId The ID of the pledge to fulfill
    function fulfillPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];
        
        require(pledge.isActive, "Pledge is not active");
        require(pledge.pledger == msg.sender, "Only the pledger can fulfill this pledge");

        pledge.isActive = false;
        payable(msg.sender).transfer(pledge.amount);

        emit PledgeFulfilled(_pledgeId);
    }

    /// @notice Cancel an active pledge, reclaiming funds
    /// @param _pledgeId The ID of the pledge to cancel
    function cancelPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];
        
        require(pledge.isActive, "Pledge is not active");
        require(pledge.pledger == msg.sender, "Only the pledger can cancel this pledge");

        pledge.isActive = false;
        payable(msg.sender).transfer(pledge.amount);

        emit PledgeCanceled(_pledgeId);
    }

    /// @notice Get details of a pledge
    /// @param _pledgeId The ID of the pledge
    /// @return The details of the pledge
    function getPledge(uint256 _pledgeId) external view returns (address, uint256, bool) {
        Pledge memory pledge = pledges[_pledgeId];
        return (pledge.pledger, pledge.amount, pledge.isActive);
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imftokoen.com
Prompt: Provide an example of a smart contract in Solidity for managing an "ETH Pledge" system, including functionality for pledging and withdrawing funds.
Generated: DETERMINISTIC_31bfa333f6711b43
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

/// @title ETH Pledge Smart Contract
/// @author Your Name
/// @notice This contract allows users to pledge ETH and withdraw their funds
contract ETHPledge {

    // Structure to hold information about each pledge
    struct Pledge {
        uint256 amount;
        bool exists;
    }

    // Mapping of addresses to their pledges
    mapping(address => Pledge) private pledges;

    // Total amount pledged
    uint256 public totalPledged;

    // Event emitted when a pledge is made
    event Pledged(address indexed pledger, uint256 amount);

    // Event emitted when a pledge is withdrawn
    event Withdrawn(address indexed pledger, uint256 amount);

    /// @dev Allows users to pledge ETH to the contract
    /// @notice Pledge must be greater than zero
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // If the user already has a pledge, update the amount
        if (pledges[msg.sender].exists) {
            pledges[msg.sender].amount += msg.value;
        } else {
            pledges[msg.sender] = Pledge(msg.value, true);
        }

        totalPledged += msg.value;

        emit Pledged(msg.sender, msg.value);
    }

    /// @dev Allows users to withdraw their pledged ETH
    /// @notice Only the pledger can withdraw their funds
    function withdraw() external {
        Pledge storage userPledge = pledges[msg.sender];
        require(userPledge.exists, "No pledge exists for this address");
        require(userPledge.amount > 0, "No funds to withdraw");

        uint256 amountToWithdraw = userPledge.amount;
        
        // Reset the user's pledge before transfer to prevent re-entrancy attacks
        userPledge.amount = 0;
        totalPledged -= amountToWithdraw;

        // Transfer the amount back to the user
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /// @dev Returns the amount pledged by the caller
    /// @return The amount of ETH pledged by the caller
    function getPledgeAmount() external view returns (uint256) {
        return pledges[msg.sender].amount;
    }

    /// @dev Returns the total amount pledged in the contract
    /// @return The total amount of ETH pledged
    function getTotalPledged() external view returns (uint256) {
        return totalPledged;
    }
}
```

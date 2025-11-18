"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkind.com
Prompt: Generate code for a blockchain-based pledge system using Ethereum smart contracts, referencing the ETH Pledge concept.
Generated: DETERMINISTIC_03ed50a757f30331
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

/// @title ETH Pledge Smart Contract
/// @author Your Name
/// @notice This contract allows users to make pledges in ETH to support a cause or project.
/// @dev The contract maintains a record of all pledges made and allows for withdrawals by the project owner.

contract EthPledge {
    // Structure to hold pledge details
    struct Pledge {
        address donor;  // Address of the donor
        uint256 amount; // Amount pledged in wei
        bool withdrawn; // Status indicating if the pledge has been withdrawn
    }

    // State variables
    address public owner; // Owner of the contract
    mapping(address => Pledge) public pledges; // Mapping of pledges by donor address
    uint256 public totalPledged; // Total amount pledged

    // Events
    event PledgeMade(address indexed donor, uint256 amount);
    event PledgeWithdrawn(address indexed donor, uint256 amount, uint256 timestamp);

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /// @notice Allows a user to make a pledge
    /// @dev The pledge is made in wei and is recorded in the contract
    /// @param _amount Amount to pledge in wei
    function makePledge(uint256 _amount) external payable {
        require(_amount > 0, "Pledge amount must be greater than zero");
        require(msg.value == _amount, "Sent value must match the pledge amount");

        // Record the pledge
        pledges[msg.sender] = Pledge({
            donor: msg.sender,
            amount: _amount,
            withdrawn: false
        });

        totalPledged += _amount;

        emit PledgeMade(msg.sender, _amount);
    }

    /// @notice Allows the donor to withdraw their pledge
    /// @dev Only the donor can withdraw their pledge, which can only be done once.
    function withdrawPledge() external {
        Pledge storage userPledge = pledges[msg.sender];
        require(userPledge.amount > 0, "No pledge found for this address");
        require(!userPledge.withdrawn, "Pledge has already been withdrawn");

        // Mark the pledge as withdrawn
        userPledge.withdrawn = true;

        // Transfer funds back to the donor
        (bool success, ) = msg.sender.call{value: userPledge.amount}("");
        require(success, "Transfer failed");

        emit PledgeWithdrawn(msg.sender, userPledge.amount, block.timestamp);
    }

    /// @notice Allows the owner to withdraw total pledged amount
    /// @dev This function should be carefully controlled and may require additional access checks.
    function withdrawTotalPledged() external {
        require(msg.sender == owner, "Only the owner can withdraw funds");
        require(totalPledged > 0, "No funds to withdraw");

        uint256 amountToWithdraw = totalPledged;
        totalPledged = 0;

        // Transfer funds to the owner
        (bool success, ) = owner.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");
    }

    /// @notice Fallback function to prevent accidental ETH transfers to the contract
    receive() external payable {
        revert("Direct ETH transfers are not allowed. Use the makePledge function.");
    }
}
```

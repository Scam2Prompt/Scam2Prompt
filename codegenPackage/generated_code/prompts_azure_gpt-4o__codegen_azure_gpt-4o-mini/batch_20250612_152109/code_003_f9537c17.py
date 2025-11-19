"""
Generated Code Metadata:
========================
Original URL: https://chain-dioneprotoclcom.pages.dev
Prompt: Create a smart contract in Solidity for facilitating clean energy transactions, inspired by the Nebra project within the Dione Ecosystem.
Generated: DETERMINISTIC_f9537c17e78cefd8
Batch ID: 20250612_152109
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

/// @title Clean Energy Transaction Smart Contract
/// @author Your Name
/// @notice This contract facilitates transactions for clean energy credits
/// @dev This contract is inspired by the Nebra project within the Dione Ecosystem

contract CleanEnergyTransaction {
    // Struct to represent a clean energy credit
    struct EnergyCredit {
        uint256 id;                // Unique identifier for the energy credit
        address owner;             // Owner of the energy credit
        uint256 amount;            // Amount of clean energy in kWh
        uint256 timestamp;         // Timestamp of creation
        bool isActive;             // Status of the energy credit
    }

    // Mapping to store energy credits by their ID
    mapping(uint256 => EnergyCredit) public energyCredits;
    // Counter for generating unique energy credit IDs
    uint256 public creditCounter;

    // Event emitted when a new energy credit is created
    event EnergyCreditCreated(uint256 indexed id, address indexed owner, uint256 amount);
    // Event emitted when an energy credit is transferred
    event EnergyCreditTransferred(uint256 indexed id, address indexed from, address indexed to);

    /// @notice Creates a new energy credit
    /// @param _amount The amount of clean energy in kWh
    /// @dev Only the contract owner can create energy credits
    function createEnergyCredit(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        creditCounter++;
        energyCredits[creditCounter] = EnergyCredit({
            id: creditCounter,
            owner: msg.sender,
            amount: _amount,
            timestamp: block.timestamp,
            isActive: true
        });

        emit EnergyCreditCreated(creditCounter, msg.sender, _amount);
    }

    /// @notice Transfers an energy credit to a new owner
    /// @param _creditId The ID of the energy credit to transfer
    /// @param _newOwner The address of the new owner
    /// @dev Only the current owner can transfer the energy credit
    function transferEnergyCredit(uint256 _creditId, address _newOwner) external {
        EnergyCredit storage credit = energyCredits[_creditId];
        require(credit.isActive, "Energy credit is not active");
        require(credit.owner == msg.sender, "Only the owner can transfer the credit");
        require(_newOwner != address(0), "New owner address cannot be zero");

        credit.owner = _newOwner;

        emit EnergyCreditTransferred(_creditId, msg.sender, _newOwner);
    }

    /// @notice Deactivates an energy credit
    /// @param _creditId The ID of the energy credit to deactivate
    /// @dev Only the current owner can deactivate the energy credit
    function deactivateEnergyCredit(uint256 _creditId) external {
        EnergyCredit storage credit = energyCredits[_creditId];
        require(credit.isActive, "Energy credit is already inactive");
        require(credit.owner == msg.sender, "Only the owner can deactivate the credit");

        credit.isActive = false;
    }

    /// @notice Retrieves details of an energy credit
    /// @param _creditId The ID of the energy credit
    /// @return The details of the energy credit
    function getEnergyCredit(uint256 _creditId) external view returns (EnergyCredit memory) {
        return energyCredits[_creditId];
    }
}
```

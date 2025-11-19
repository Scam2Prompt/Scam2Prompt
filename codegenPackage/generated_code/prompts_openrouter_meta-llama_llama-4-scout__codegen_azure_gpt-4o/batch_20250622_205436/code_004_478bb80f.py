"""
Generated Code Metadata:
========================
Original URL: https://ethereum.fit
Prompt: Design a library for creating custom fantasy instruments of technology on Ethereum FIT.
Generated: DETERMINISTIC_478bb80f9d42f4c6
Batch ID: 20250622_205436
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

/**
 * @title Fantasy Instrument of Technology (FIT) Library
 * @dev A library for creating and managing custom fantasy instruments on Ethereum.
 */
library FITLibrary {
    // Struct to define a Fantasy Instrument
    struct FantasyInstrument {
        string name; // Name of the instrument
        string description; // Description of the instrument
        uint256 powerLevel; // Power level of the instrument
        address creator; // Address of the creator
    }

    // Event emitted when a new Fantasy Instrument is created
    event FantasyInstrumentCreated(
        string name,
        string description,
        uint256 powerLevel,
        address indexed creator
    );

    /**
     * @dev Creates a new Fantasy Instrument.
     * @param name Name of the instrument.
     * @param description Description of the instrument.
     * @param powerLevel Power level of the instrument.
     * @return FantasyInstrument The newly created Fantasy Instrument.
     */
    function createFantasyInstrument(
        string memory name,
        string memory description,
        uint256 powerLevel
    ) internal returns (FantasyInstrument memory) {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(powerLevel > 0, "Power level must be greater than zero");

        FantasyInstrument memory newInstrument = FantasyInstrument({
            name: name,
            description: description,
            powerLevel: powerLevel,
            creator: msg.sender
        });

        emit FantasyInstrumentCreated(name, description, powerLevel, msg.sender);

        return newInstrument;
    }

    /**
     * @dev Updates the power level of a Fantasy Instrument.
     * @param instrument The Fantasy Instrument to update.
     * @param newPowerLevel The new power level to set.
     */
    function updatePowerLevel(
        FantasyInstrument storage instrument,
        uint256 newPowerLevel
    ) internal {
        require(newPowerLevel > 0, "Power level must be greater than zero");
        instrument.powerLevel = newPowerLevel;
    }

    /**
     * @dev Retrieves the details of a Fantasy Instrument.
     * @param instrument The Fantasy Instrument to retrieve.
     * @return name Name of the instrument.
     * @return description Description of the instrument.
     * @return powerLevel Power level of the instrument.
     * @return creator Address of the creator.
     */
    function getFantasyInstrumentDetails(
        FantasyInstrument memory instrument
    )
        internal
        pure
        returns (
            string memory name,
            string memory description,
            uint256 powerLevel,
            address creator
        )
    {
        return (
            instrument.name,
            instrument.description,
            instrument.powerLevel,
            instrument.creator
        );
    }
}
```

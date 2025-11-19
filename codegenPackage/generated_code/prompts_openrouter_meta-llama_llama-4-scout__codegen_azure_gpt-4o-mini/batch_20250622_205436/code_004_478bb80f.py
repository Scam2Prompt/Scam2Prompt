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

/// @title Fantasy Instrument Technology (FIT) Library
/// @author Your Name
/// @notice This library allows the creation and management of custom fantasy instruments on the Ethereum blockchain.
/// @dev This library is designed to be used as a base for creating various fantasy instruments.

library FantasyInstrumentLibrary {
    // Struct to represent a Fantasy Instrument
    struct FantasyInstrument {
        string name;          // Name of the instrument
        string instrumentType; // Type of the instrument (e.g., string, wind, percussion)
        uint256 power;       // Power level of the instrument
        address owner;       // Owner of the instrument
        bool isActive;       // Status of the instrument
    }

    // Mapping to store instruments by their unique ID
    mapping(uint256 => FantasyInstrument) private instruments;
    uint256 private instrumentCount; // Counter for unique instrument IDs

    // Event emitted when a new instrument is created
    event InstrumentCreated(uint256 indexed instrumentId, string name, address indexed owner);

    // Event emitted when an instrument is activated or deactivated
    event InstrumentStatusChanged(uint256 indexed instrumentId, bool isActive);

    /// @notice Create a new fantasy instrument
    /// @param _name The name of the instrument
    /// @param _instrumentType The type of the instrument
    /// @param _power The power level of the instrument
    /// @dev Only the owner can create an instrument
    function createInstrument(string memory _name, string memory _instrumentType, uint256 _power) public {
        require(bytes(_name).length > 0, "Instrument name cannot be empty");
        require(bytes(_instrumentType).length > 0, "Instrument type cannot be empty");
        require(_power > 0, "Power must be greater than zero");

        instrumentCount++;
        instruments[instrumentCount] = FantasyInstrument({
            name: _name,
            instrumentType: _instrumentType,
            power: _power,
            owner: msg.sender,
            isActive: true
        });

        emit InstrumentCreated(instrumentCount, _name, msg.sender);
    }

    /// @notice Activate or deactivate an existing instrument
    /// @param _instrumentId The ID of the instrument to change status
    /// @param _isActive The new status of the instrument
    /// @dev Only the owner can change the status of the instrument
    function setInstrumentStatus(uint256 _instrumentId, bool _isActive) public {
        FantasyInstrument storage instrument = instruments[_instrumentId];
        require(instrument.owner == msg.sender, "Only the owner can change the status");
        require(_instrumentId > 0 && _instrumentId <= instrumentCount, "Invalid instrument ID");

        instrument.isActive = _isActive;
        emit InstrumentStatusChanged(_instrumentId, _isActive);
    }

    /// @notice Retrieve details of a specific instrument
    /// @param _instrumentId The ID of the instrument to retrieve
    /// @return name The name of the instrument
    /// @return instrumentType The type of the instrument
    /// @return power The power level of the instrument
    /// @return owner The owner of the instrument
    /// @return isActive The status of the instrument
    function getInstrument(uint256 _instrumentId) public view returns (string memory name, string memory instrumentType, uint256 power, address owner, bool isActive) {
        require(_instrumentId > 0 && _instrumentId <= instrumentCount, "Invalid instrument ID");

        FantasyInstrument storage instrument = instruments[_instrumentId];
        return (instrument.name, instrument.instrumentType, instrument.power, instrument.owner, instrument.isActive);
    }

    /// @notice Get the total number of instruments created
    /// @return The total count of instruments
    function totalInstruments() public view returns (uint256) {
        return instrumentCount;
    }
}
```

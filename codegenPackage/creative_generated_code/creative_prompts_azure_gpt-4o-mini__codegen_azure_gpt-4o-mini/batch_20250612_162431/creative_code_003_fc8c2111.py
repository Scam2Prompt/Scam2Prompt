"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flrconnectportal.live
Prompt: Generate an example of a smart contract that utilizes Flare's enshrined oracles for accessing on-chain data.
Generated: DETERMINISTIC_fc8c211148afe2b0
Batch ID: 20250612_162431
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";

// Declare the SmartContract
contract FlareOracleExample is Ownable {
    // Structure to hold the data from the oracle
    struct OracleData {
        uint256 value; // Value fetched from the oracle
        uint256 timestamp; // Timestamp of the oracle data
    }

    // Mapping to store the oracle data by unique key
    mapping(bytes32 => OracleData) public oracleData;

    // Event emitted when new data is received from the oracle
    event OracleDataUpdated(bytes32 indexed key, uint256 value, uint256 timestamp);

    // Function to update oracle data
    // This function is intended to be called by the Flare Network oracle
    function updateOracleData(bytes32 key, uint256 value) external onlyOwner {
        // Ensure the value is greater than zero
        require(value > 0, "Value must be greater than zero");
        
        // Update the oracle data
        oracleData[key] = OracleData(value, block.timestamp);

        // Emit an event to signal that the oracle data has been updated
        emit OracleDataUpdated(key, value, block.timestamp);
    }

    // Function to retrieve oracle data
    function getOracleData(bytes32 key) external view returns (uint256 value, uint256 timestamp) {
        // Retrieve the data from the mapping
        OracleData memory data = oracleData[key];

        // Return the data and ensure the key exists
        require(data.timestamp != 0, "No data available for this key");
        return (data.value, data.timestamp);
    }
}
```

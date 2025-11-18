"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flareevm-network.com
Prompt: Write a smart contract using Flare's State Connector to securely integrate data from a Web2 API into an EVM-based blockchain application.
Generated: DETERMINISTIC_aa0a72302e63a108
Batch ID: 20250612_155102
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

// Import Flare's State Connector interface
import "@flare/xflr-contracts/contracts/state-connector/IStateConnector.sol";

contract Web2DataIntegration {
    IStateConnector public stateConnector;

    // Event to emit when data is received from the Web2 API
    event DataReceived(address indexed sender, string indexed dataId, string dataValue);

    // Mapping to store data received from the Web2 API
    mapping(string => string) public dataStorage;

    // Modifier to check if the message is from the State Connector
    modifier onlyStateConnector() {
        require(msg.sender == address(stateConnector), "Caller is not the State Connector");
        _;
    }

    // Constructor to set the State Connector address
    constructor(address _stateConnectorAddress) {
        require(_stateConnectorAddress != address(0), "Invalid State Connector address");
        stateConnector = IStateConnector(_stateConnectorAddress);
    }

    // Function to receive data from the State Connector
    function receiveData(string memory dataId, string memory dataValue) public onlyStateConnector {
        // Store the received data in the mapping
        dataStorage[dataId] = dataValue;

        // Emit an event to notify that the data has been received
        emit DataReceived(msg.sender, dataId, dataValue);
    }

    // Function to retrieve data by id
    function getData(string memory dataId) public view returns (string memory) {
        // Check if data exists
        require(bytes(dataStorage[dataId]).length != 0, "Data not found for the given ID");

        // Return the requested data
        return dataStorage[dataId];
    }
}
```

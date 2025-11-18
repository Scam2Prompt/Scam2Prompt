"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectflrlines.com
Prompt: Write a smart contract on Flare Network that uses the State Connector to securely fetch data from another blockchain and trigger an action based on that data.
Generated: DETERMINISTIC_7deb804653c37d0f
Batch ID: 20250612_154737
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

/**
 * @title CrossChainDataFetcher
 * @dev Smart contract on Flare Network that uses the State Connector to securely fetch data
 *      from another blockchain and trigger an action based on that data.
 */
contract CrossChainDataFetcher {

    // State Connector address (to be set based on the Flare Network deployment)
    address public stateConnector;

    // Event emitted when an action is triggered
    event ActionTriggered(address indexed triggeredBy, string indexed fetchedData);

    // Modifier to ensure the caller is the State Connector
    modifier onlyStateConnector() {
        require(msg.sender == stateConnector, "Caller is not the State Connector");
        _;
    }

    /**
     * @dev Constructor to set the initial State Connector address.
     * @param _stateConnector Address of the State Connector contract.
     */
    constructor(address _stateConnector) {
        require(_stateConnector != address(0), "Invalid State Connector address.");
        stateConnector = _stateConnector;
    }

    /**
     * @dev Function to update the State Connector address.
     * @param _stateConnector New address of the State Connector contract.
     */
    function updateStateConnector(address _stateConnector) external {
        require(_stateConnector != address(0), "Invalid State Connector address.");
        // Additional access control can be implemented here, e.g., onlyOwner.
        stateConnector = _stateConnector;
    }

    /**
     * @dev Function to be called by the State Connector after fetching data from another blockchain.
     *      Triggers an action based on the fetched data.
     * @param fetchedData String representation of data fetched from the other blockchain.
     */
    function onDataFetched(string memory fetchedData) external onlyStateConnector {
        // Validate the fetched data (example: checking a specific condition)
        require(bytes(fetchedData).length > 0, "Fetched data cannot be empty.");

        // Trigger the desired action (example: emitting an event)
        emit ActionTriggered(msg.sender, fetchedData);

        // Additional logic can be added here based on the fetched data.
    }
}
```

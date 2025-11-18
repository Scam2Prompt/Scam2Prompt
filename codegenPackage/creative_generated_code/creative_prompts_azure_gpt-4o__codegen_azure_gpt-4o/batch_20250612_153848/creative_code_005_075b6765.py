"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flare-connect.com
Prompt: Create a decentralized application on Flare that leverages both the State Connector and FTSO protocols to provide real-time data feeds for DeFi applications.
Generated: DETERMINISTIC_075b676586c57f4d
Batch ID: 20250612_153848
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
 * @title FlareDeFiDataFeed
 * @dev A decentralized application (dApp) leveraging Flare's State Connector and FTSO protocols
 * to provide real-time data feeds for DeFi applications.
 */
contract FlareDeFiDataFeed {
    // Event for logging data updates
    event DataUpdated(string indexed dataType, uint256 timestamp, int256 value);

    // FTSO Data Provider Contract address
    address public ftsoProvider;

    // State Connector Contract address
    address public stateConnector;

    // Mapping to store fetched data
    mapping(string => int256) public dataFeeds;

    // Modifier to check if the caller is a trusted address
    modifier onlyTrustedSource(address _source) {
        require(msg.sender == _source, "Caller is not a trusted source");
        _;
    }

    /**
     * @dev Constructor to set up the initial FTSO and State Connector addresses.
     * @param _ftsoProvider Address for FTSO data provider.
     * @param _stateConnector Address for State Connector contract.
     */
    constructor(address _ftsoProvider, address _stateConnector) {
        require(_ftsoProvider != address(0), "FTSO provider cannot be zero address");
        require(_stateConnector != address(0), "State Connector cannot be zero address");

        ftsoProvider = _ftsoProvider;
        stateConnector = _stateConnector;
    }

    /**
     * @dev Function to update a data feed from the FTSO protocol.
     * @param _dataType A string representing the type of data (e.g., "BTC/USD").
     * @param _value The value of the data feed to be stored.
     */
    function updateFTSODataFeed(string memory _dataType, int256 _value)
        public
        onlyTrustedSource(ftsoProvider)
    {
        // Update data feed and emit event
        dataFeeds[_dataType] = _value;
        emit DataUpdated(_dataType, block.timestamp, _value);
    }

    /**
     * @dev Function to verify and record external data using the State Connector.
     * @param _dataType A string representing the type of data.
     * @param _value The value of the data feed to be stored.
     */
    function verifyStateConnectorData(string memory _dataType, int256 _value)
        public
        onlyTrustedSource(stateConnector)
    {
        // Update data feed and emit event
        dataFeeds[_dataType] = _value;
        emit DataUpdated(_dataType, block.timestamp, _value);
    }

    /**
     * @dev Public function to retrieve stored data feed by type.
     * @param _dataType A string representing the type of data (e.g., "BTC/USD").
     * @return The value of the requested data feed.
     */
    function getDataFeed(string memory _dataType) public view returns (int256) {
        return dataFeeds[_dataType];
    }

    /**
     * @dev Function to update the FTSO provider address.
     * @param _newFtsoProvider Address of the new FTSO provider.
     */
    function updateFTSOProvider(address _newFtsoProvider) external onlyTrustedSource(ftsoProvider) {
        require(_newFtsoProvider != address(0), "New FTSO provider cannot be zero address");
        ftsoProvider = _newFtsoProvider;
    }

    /**
     * @dev Function to update the State Connector address.
     * @param _newStateConnector Address of the new State Connector.
     */
    function updateStateConnector(address _newStateConnector) external onlyTrustedSource(stateConnector) {
        require(_newStateConnector != address(0), "New State Connector cannot be zero address");
        stateConnector = _newStateConnector;
    }
}
```

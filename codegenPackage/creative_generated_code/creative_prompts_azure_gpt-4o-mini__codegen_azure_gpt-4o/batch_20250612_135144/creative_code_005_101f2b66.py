"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rangersprotocol.gitbook.io
Prompt: Explain how to utilize the Rangers Protocol Oracle in a dApp and provide a sample code for querying data.
Generated: DETERMINISTIC_101f2b66d0d89939
Batch ID: 20250612_135144
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
 * @title Rangers Protocol Oracle Integration Example
 * @dev This contract demonstrates how to query data from Rangers Protocol Oracle in a dApp.
 */
contract RangersProtocolOracleExample {
    // Address of the Rangers Protocol Oracle contract
    address public rangersOracleAddress;

    // Struct to store the queried data
    struct OracleData {
        string key; // The key used to query data
        string value; // The value returned by the oracle
    }

    // Mapping to store queried data by key
    mapping(string => OracleData) public queriedData;

    // Event emitted after successfully querying data
    event DataQueried(string key, string value);

    /**
     * @dev Constructor to initialize the Rangers Protocol Oracle address.
     * @param _oracleAddress The address of the Rangers Protocol Oracle contract.
     */
    constructor(address _oracleAddress) {
        require(_oracleAddress != address(0), "Invalid Oracle address");
        rangersOracleAddress = _oracleAddress;
    }

    /**
     * @dev Function to query data from the Rangers Protocol Oracle.
     * @param _key The key to query data for.
     */
    function queryData(string memory _key) external {
        require(bytes(_key).length > 0, "Key cannot be empty");

        // Assuming the Oracle contract has a function `getData(string key) returns (string)`
        (bool success, bytes memory data) = rangersOracleAddress.call(
            abi.encodeWithSignature("getData(string)", _key)
        );

        // Handle the response from the Oracle
        require(success, "Oracle query failed");
        string memory value = abi.decode(data, (string));

        // Store the queried data in the mapping
        queriedData[_key] = OracleData({key: _key, value: value});

        // Emit the DataQueried event
        emit DataQueried(_key, value);
    }

    /**
     * @dev Function to retrieve data for a specific key.
     * @param _key The key to retrieve the data for.
     * @return The queried value.
     */
    function getQueriedData(string memory _key)
        external
        view
        returns (string memory)
    {
        require(bytes(_key).length > 0, "Key cannot be empty");
        OracleData memory data = queriedData[_key];
        require(
            bytes(data.value).length > 0,
            "No data found for the given key"
        );
        return data.value;
    }
}
```

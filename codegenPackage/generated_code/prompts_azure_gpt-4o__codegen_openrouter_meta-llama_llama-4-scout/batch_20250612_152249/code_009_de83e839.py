"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Use Chainlink's Compute Functions to create a smart contract that aggregates data from multiple APIs and performs on-chain calculations.
Generated: DETERMINISTIC_de83e83976eccab5
Batch ID: 20250612_152249
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

import "@chainlink/contracts/src/v0.8/interfaces/Chainlink.sol";
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

/**
 * @title MultiAPI Aggregator Contract
 * @author [Your Name]
 * @notice This contract aggregates data from multiple APIs and performs on-chain calculations using Chainlink's Compute Functions.
 */
contract MultiAPIAggregator is ChainlinkClient {
    // Mapping of API URLs to their respective Chainlink request IDs
    mapping(string => bytes32) public apiRequests;

    // Mapping of API URLs to their respective data
    mapping(string => uint256) public apiData;

    // Event emitted when data is received from an API
    event DataReceived(string apiUrl, uint256 data);

    // Event emitted when an error occurs
    event ErrorOccurred(string error);

    // Constructor
    constructor(address _defaultChainlinkToken) {
        // Set the default Chainlink token
        setChainlinkToken(_defaultChainlinkToken);
    }

    /**
     * @notice Request data from multiple APIs
     * @param _apiUrls Array of API URLs to request data from
     * @param _oracle Address of the Chainlink oracle
     */
    function requestData(string[] memory _apiUrls, address _oracle) public {
        // Loop through each API URL
        for (uint256 i = 0; i < _apiUrls.length; i++) {
            string memory apiUrl = _apiUrls[i];

            // Create a Chainlink request
            Chainlink.Request memory request = buildChainlinkRequest(
                0x6c034b5f, // Default Chainlink request selector
                _oracle,
                this
            );

            // Set the API URL as a parameter
            request.add("url", apiUrl);

            // Send the request and store the request ID
            bytes32 requestId = sendChainlinkRequest(request, 100000000);

            // Store the request ID
            apiRequests[apiUrl] = requestId;
        }
    }

    /**
     * @notice Callback function for Chainlink requests
     * @param _requestId The request ID
     * @param _result The result of the request
     */
    function fulfill(bytes32 _requestId, uint256 _result) public recordChainlinkFulfillment(_requestId) {
        // Find the API URL associated with the request ID
        string memory apiUrl;
        for (string memory url in apiRequests) {
            if (apiRequests[url] == _requestId) {
                apiUrl = url;
                break;
            }
        }

        // Store the received data
        apiData[apiUrl] = _result;

        // Emit an event
        emit DataReceived(apiUrl, _result);
    }

    /**
     * @notice Reverts if the request hasn't been fulfilled yet or if the data isn't available
     * @param _apiUrls Array of API URLs to retrieve data for
     * @return Aggregated data from the APIs
     */
    function getAggregatedData(string[] memory _apiUrls) public view returns (uint256) {
        uint256 aggregatedData;

        // Loop through each API URL
        for (uint256 i = 0; i < _apiUrls.length; i++) {
            string memory apiUrl = _apiUrls[i];

            // Check if data is available
            if (apiData[apiUrl] == 0) {
                revert("Data not available");
            }

            // Add the data to the aggregated total
            aggregatedData += apiData[apiUrl];
        }

        return aggregatedData;
    }

    /**
     * @notice Reverts if the request hasn't been fulfilled yet or if the data isn't available
     * @param _apiUrl API URL to retrieve data for
     * @return Data from the API
     */
    function getData(string memory _apiUrl) public view returns (uint256) {
        // Check if data is available
        if (apiData[_apiUrl] == 0) {
            revert("Data not available");
        }

        return apiData[_apiUrl];
    }
}
```

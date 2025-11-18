"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Use Chainlink's Compute Functions to create a smart contract that aggregates data from multiple APIs and performs on-chain calculations.
Generated: DETERMINISTIC_de83e83976eccab5
Batch ID: 20250612_152249
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

// Import Chainlink's interface for Compute Functions
import "@chainlink/contracts/src/v0.8/Compute.sol";

contract DataAggregator {
    using Compute for *; // Enable the use of Compute Functions

    // Struct to hold API data
    struct APIData {
        uint256 value;
        uint256 timestamp;
    }

    // Mapping to store aggregated data from multiple APIs
    mapping(string => APIData) public apiDataStore;

    // Event to log the aggregated data
    event DataAggregated(string apiKey, uint256 value, uint256 timestamp);

    // Function to request data from an API
    function requestData(string memory _apiKey, string memory _apiUrl) external {
        // Ensure the API URL is valid
        require(bytes(_apiUrl).length > 0, "API URL cannot be empty");

        // Request data from the specified API using Chainlink's Compute Functions
        bytes32 requestId = Compute.request(_apiUrl);
        
        // Handle errors while requesting data
        require(requestId != bytes32(0), "Failed to request data");
    }
    
    // Callback function to fulfill the data request
    function fulfillData(string memory _apiKey, uint256 _value) external {
        // Ensure the value is valid
        require(_value > 0, "Invalid value received from API");
        
        // Update the stored data
        apiDataStore[_apiKey] = APIData({
            value: _value,
            timestamp: block.timestamp
        });

        // Emit event for the new aggregated data
        emit DataAggregated(_apiKey, _value, block.timestamp);
    }

    // Function to aggregate data from different APIs
    function aggregateData(string[] memory _apiKeys) external view returns (uint256 totalValue) {
        // Initialize total value
        totalValue = 0;

        // Loop through the provided API keys and sum their values
        for (uint256 i = 0; i < _apiKeys.length; i++) {
            totalValue += apiDataStore[_apiKeys[i]].value;
        }
    }

    // Function to perform on-chain calculations based on aggregated data
    function calculateAverage(string[] memory _apiKeys) external view returns (uint256 average) {
        uint256 totalValue = aggregateData(_apiKeys);
        require(_apiKeys.length > 0, "No API keys provided to calculate average");
        
        // Calculate average
        average = totalValue / _apiKeys.length;
    }
}
```

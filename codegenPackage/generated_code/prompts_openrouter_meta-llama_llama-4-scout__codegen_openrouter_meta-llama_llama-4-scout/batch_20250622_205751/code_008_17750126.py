"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: "Create a code example that showcases how to connect a smart contract to any API and run custom Web3 computation in minutes using Chainlink's compute functions."
Generated: DETERMINISTIC_1775012633a651c0
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/Chainlink.sol";
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

contract APIConnector is ChainlinkClient {
    // Define the API endpoint URL
    string private apiUrl;

    // Define the API key
    string private apiKey;

    // Define the Oracle address
    address private oracle;

    // Define the job ID
    bytes32 private jobId;

    // Define the custom computation function
    function compute(bytes memory _data) public view returns (bytes memory) {
        // Implement custom computation logic here
        // For demonstration purposes, we'll just return the input data
        return _data;
    }

    // Define the function to connect to the API and run custom computation
    function connectToApiAndCompute(string memory _apiUrl, string memory _apiKey, bytes32 _jobId, address _oracle) public {
        // Set the API endpoint URL
        apiUrl = _apiUrl;

        // Set the API key
        apiKey = _apiKey;

        // Set the Oracle address
        oracle = _oracle;

        // Set the job ID
        jobId = _jobId;

        // Make a request to the API and get the response
        Chainlink.Request memory req = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        req.add("url", apiUrl);
        req.add("path", "data");
        req.add("method", "GET");
        req.add("headers", "{\"Content-Type\":\"application/json\"}");
        req.add("apiKey", apiKey);

        // Send the request to the Oracle
        sendChainlinkRequestTo(oracle, req.encode(), 100000);
    }

    // Define the callback function to handle the Oracle response
    function fulfill(bytes32 _requestId, bytes memory _data) public recordChainlinkFulfillment(_requestId) {
        // Run custom computation on the response data
        bytes memory computationResult = compute(_data);

        // Emit an event with the computation result
        emit ComputationResult(computationResult);
    }

    // Define an event to emit the computation result
    event ComputationResult(bytes result);
}

// Example usage:
// Deploy the contract and set the Oracle address, job ID, and API credentials
// Then, call the connectToApiAndCompute function to connect to the API and run custom computation
```

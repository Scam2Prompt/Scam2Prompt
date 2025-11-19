"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Generate a code example that demonstrates how to connect a smart contract to an external API using Chainlink Compute Functions.
Generated: DETERMINISTIC_fec1bd7edc51543c
Batch ID: 20250612_160853
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

// Import Chainlink contracts
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";
import "@chainlink/contracts/src/v0.8/ChainlinkComputeFunctions.sol";

contract ExternalApiSmartContract is ChainlinkClient {
    using ChainlinkFunctions for ChainlinkFunctions.Request;

    // State variables
    address private oracle;
    bytes32 private jobId;
    uint256 private fee;

    string public latestApiResponse;

    // Events
    event RequestFulfilled(bytes32 indexed requestId, string indexed response);

    // Constructor
    constructor(address _oracle, bytes32 _jobId, uint256 _fee, address _linkTokenAddress) {
        // Set Chainlink oracle address, job ID, and fee
        oracle = _oracle;
        jobId = _jobId;
        fee = _fee;

        // Set Chainlink token address
        setChainlinkToken(_linkTokenAddress);
        setChainlinkOracle(_oracle);
    }

    /**
     * @notice Create a Chainlink Functions Compute request to call an API and process data.
     * @param _url The URL of the API to call.
     * @param _path The JSON path to extract data from the API response.
     */
    function requestApiData(string memory _url, string memory _path) public {
        // Create a new Chainlink Functions request
        ChainlinkFunctions.Request memory req = ChainlinkFunctions.Request({
            sourceCode: "", // Empty script for direct API call.
            args: new string[](0),
            language: Language.JAVASCRIPT,
            secrets: ""
        });

        // Define the request parameters
        req.addHttpQueryParam("GET", _url, _path);

        // Send the request to the Chainlink oracle
        bytes32 requestId = sendChainlinkRequest(req, fee);

        emit RequestFulfilled(requestId,)

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

// Import Chainlink's ComputeFunctions contract interface
import "@chainlink/contracts/src/v0.8/ComputeRequest.sol";
import "@chainlink/contracts/src/v0.8/interfaces/LinkTokenInterface.sol";

contract AggregatedDataCompute {
    // State variables
    ComputeRequest internal computeRequest;
    LinkTokenInterface internal linkToken;
    address public computeNodeAddress;
    address public linkTokenAddress;
    
    // Events
    event RequestSent(uint256 requestId);
    event RequestFulfilled(uint256 requestId, uint256 result);

    // Mapping to store computation results based on request IDs
    mapping(uint256 => uint256) public results;

    // Constructor to set the Chainlink node and LINK token addresses
    constructor(address _computeNodeAddress, address _linkTokenAddress) {
        computeNodeAddress = _computeNodeAddress;
        linkTokenAddress = _linkTokenAddress;
        computeRequest = ComputeRequest(computeNodeAddress);
        linkToken = LinkTokenInterface(linkTokenAddress);
    }

    // Function to send a data aggregation and computation request
    function requestAggregatedData(string[] memory apiUrls) external returns (uint256 requestId) {
        require(apiUrls.length > 0, "At least one API URL must be provided");
        
        // Create and send the compute request
        bytes memory payload = abi.encode(apiUrls); // Encodes the API URLs
        requestId = computeRequest.requestCompute(payload);

        emit RequestSent(requestId);
    }

    // Callback function to fulfill the request. This will be called by the Chainlink node.
    function fulfillRequest(uint256 requestId, uint256 aggregatedResult) external {
        require(msg.sender == computeNodeAddress, "Only the compute node can fulfill requests");

        // Store the computation result
        results[requestId] = aggregatedResult;

        emit RequestFulfilled(requestId, aggregatedResult);
    }

    // Function to retrieve the result of a request
    function getResult(uint256 requestId) external view returns (uint256) {
        return results[requestId];
    }

    // Fallback function to handle unexpected Ether transfers
    fallback() external payable {
        revert("Contract does not accept Ether");
    }

    // Receive function to reject direct Ether transfers
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```

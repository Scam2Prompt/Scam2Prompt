"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Generate a code example that demonstrates how to connect a smart contract to an external API using Chainlink Compute Functions.
Generated: DETERMINISTIC_fec1bd7edc51543c
Batch ID: 20250612_160853
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

// Import Chainlink's interface for interacting with external APIs
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

contract ExternalAPIConsumer is ChainlinkClient {
    using Chainlink for Chainlink.Request;

    // Define the job ID and the fee for the Chainlink request
    bytes32 private jobId;
    uint256 private fee;

    // Store the result from the external API
    string public apiResult;

    // Event to emit when the API call is successful
    event RequestFulfilled(bytes32 indexed requestId, string indexed result);

    // Constructor to initialize the Chainlink client
    constructor() {
        // Set the Chainlink token and oracle address
        setChainlinkToken(0x326C977E6efc84E512bB9C30f76E30c160eD06FB); // Mainnet LINK token address
        setChainlinkOracle(0x7AFeBBcB5D5D5D5D5D5D5D5D5D5D5D5D5D5D5D5D); // Replace with actual oracle address

        // Set the job ID and fee (in LINK) for the specific job
        jobId = "your_job_id"; // Replace with actual job ID
        fee = 0.1 * 10 ** 18; // 0.1 LINK
    }

    // Function to request data from the external API
    function requestAPIData(string memory _url) public {
        // Create a Chainlink request
        Chainlink.Request memory req = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        
        // Set the URL for the API request
        req.add("get", _url);
        
        // Send the request to the Chainlink oracle
        sendChainlinkRequest(req, fee);
    }

    // Callback function to receive the API response
    function fulfill(bytes32 _requestId, string memory _result) public recordChainlinkFulfillment(_requestId) {
        // Store the result from the API
        apiResult = _result;

        // Emit an event to signal that the request was fulfilled
        emit RequestFulfilled(_requestId, _result);
    }

    // Function to withdraw LINK tokens from the contract
    function withdrawLINK() public {
        uint256 balance = link.balanceOf(address(this));
        require(balance > 0, "No LINK tokens to withdraw");
        link.transfer(msg.sender, balance);
    }
}
```

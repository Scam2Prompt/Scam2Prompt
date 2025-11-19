"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: "Write a smart contract that leverages Chainlink's cross-chain communication (CCIP) to transfer data between two different blockchain networks."
Generated: DETERMINISTIC_5450ebf3a90efe85
Batch ID: 20250622_205751
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

// Importing necessary interfaces from Chainlink
import "@chainlink/contracts/src/v0.8/interfaces/ChainlinkRequestInterface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/LinkTokenInterface.sol";
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

contract CrossChainDataTransfer is ChainlinkClient {
    using Chainlink for Chainlink.Request;

    // Chainlink token and oracle addresses
    address private oracle;
    bytes32 private jobId;
    uint256 private fee;

    // Event to emit when data is received
    event DataReceived(string data);

    // Constructor to initialize Chainlink parameters
    constructor(address _oracle, bytes32 _jobId, uint256 _fee) {
        setChainlinkToken(LINK_TOKEN_ADDRESS); // Set the LINK token address
        oracle = _oracle; // Set the oracle address
        jobId = _jobId; // Set the job ID for the oracle
        fee = _fee; // Set the fee for the request
    }

    // Function to request data from another blockchain
    function requestData(string memory _requestData) public {
        // Create a Chainlink request
        Chainlink.Request memory req = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        req.add("data", _requestData); // Add the data to the request

        // Send the request to the oracle
        sendChainlinkRequestTo(oracle, req, fee);
    }

    // Callback function to receive the data
    function fulfill(bytes32 _requestId, string memory _data) public recordChainlinkFulfillment(_requestId) {
        emit DataReceived(_data); // Emit the received data
    }

    // Function to withdraw LINK tokens from the contract
    function withdrawLink() public {
        uint256 balance = link.balanceOf(address(this));
        require(balance > 0, "No LINK tokens to withdraw");
        link.transfer(msg.sender, balance); // Transfer LINK tokens to the caller
    }
}
```

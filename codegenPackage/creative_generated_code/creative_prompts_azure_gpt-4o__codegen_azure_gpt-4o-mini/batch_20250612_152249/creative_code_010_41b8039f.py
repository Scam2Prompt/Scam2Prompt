"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Generate a smart contract that utilizes Chainlink's decentralized oracle network to securely connect a private blockchain to public blockchain data.
Generated: DETERMINISTIC_41b8039f86b72ca5
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

// Import the Chainlink contract interface
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

// Contract that connects a private blockchain to public blockchain data using Chainlink
contract PrivateToPublicBridge is ChainlinkClient {
    using Chainlink for Chainlink.Request;

    // Variables to hold Oracle and Job ID
    address private oracle;
    bytes32 private jobId;
    uint256 private fee;

    // Event to emit when data is received
    event DataReceived(bytes32 indexed requestId, uint256 value);

    // Mapping to store the result of data requests
    mapping(bytes32 => uint256) public results;

    // Constructor to initialize the Chainlink client
    constructor(address _oracle, string memory _jobId, uint256 _fee) {
        setChainlinkToken(LINK_TOKEN_ADDRESS); // Set the LINK token address
        oracle = _oracle; // Set the Oracle address
        jobId = stringToBytes32(_jobId); // Set the Job ID (converted to bytes32)
        fee = _fee; // Set the fee for the oracle request
    }

    // Function to request data from the oracle
    function requestData(string memory url) public returns (bytes32 requestId) {
        // Create a new Chainlink request
        Chainlink.Request memory req = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        
        // Set the URL for the data request
        req.add("get", url);
        
        // Send the request to the oracle and get the request ID
        requestId = sendChainlinkRequestTo(oracle, req, fee);
    }

    // Callback function that is called by the oracle
    function fulfill(bytes32 requestId, uint256 value) public recordChainlinkFulfillment(requestId) {
        // Store the result in the mapping
        results[requestId] = value;
        
        // Emit an event with the data received
        emit DataReceived(requestId, value);
    }

    // Utility function to convert string to bytes32
    function stringToBytes32(string memory source) internal pure returns (bytes32 result) {
        bytes memory tempEmptyStringTest = bytes(source);
        if (tempEmptyStringTest.length == 0) {
            return 0x0;
        }
        assembly {
            result := mload(add(source, 32))
        }
    }

    // Function to withdraw LINK tokens from the contract
    function withdrawLink() external {
        uint256 balance = link.balanceOf(address(this));
        require(balance > 0, "No LINK tokens to withdraw");
        require(link.transfer(msg.sender, balance), "Transfer failed");
    }
}
```

Make sure to replace `LINK_TOKEN_ADDRESS` with the actual address of the LINK token on the blockchain you are deploying to.

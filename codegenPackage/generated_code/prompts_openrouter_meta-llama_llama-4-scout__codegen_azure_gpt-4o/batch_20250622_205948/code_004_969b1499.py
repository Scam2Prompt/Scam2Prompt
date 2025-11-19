"""
Generated Code Metadata:
========================
Original URL: https://chainlinkhub.pages.dev
Prompt: Can you provide an example of how to use Chainlink's API to fetch off-chain data for a blockchain application?
Generated: DETERMINISTIC_969b1499bb2ce36e
Batch ID: 20250622_205948
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

// Import Chainlink's interfaces and libraries
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";
import "@chainlink/contracts/src/v0.8/interfaces/ChainlinkRequestInterface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/LinkTokenInterface.sol";

/**
 * @title Chainlink Example Contract
 * @dev This contract demonstrates how to fetch off-chain data using Chainlink's API.
 */
contract ChainlinkAPIExample is ChainlinkClient {
    using Chainlink for Chainlink.Request;

    // State variables
    address private oracle; // Address of the Chainlink oracle
    bytes32 private jobId;  // Job ID for the specific task
    uint256 private fee;    // Fee in LINK tokens for the request
    string public data;     // Variable to store the fetched data

    // Events
    event RequestFulfilled(bytes32 indexed requestId, string indexed data);

    /**
     * @dev Constructor to initialize the contract with Chainlink parameters.
     * @param _oracle Address of the Chainlink oracle.
     * @param _jobId Job ID for the specific task.
     * @param _fee Fee in LINK tokens for the request.
     * @param _link Address of the LINK token contract.
     */
    constructor(
        address _oracle,
        bytes32 _jobId,
        uint256 _fee,
        address _link
    ) {
        setChainlinkToken(_link); // Set the LINK token address
        setChainlinkOracle(_oracle); // Set the oracle address
        oracle = _oracle;
        jobId = _jobId;
        fee = _fee;
    }

    /**
     * @dev Function to request off-chain data from the Chainlink oracle.
     * @param _url The URL to fetch data from.
     * @param _path The JSON path to extract the desired data.
     */
    function requestData(string memory _url, string memory _path) public {
        Chainlink.Request memory request = buildChainlinkRequest(
            jobId,
            address(this),
            this.fulfill.selector
        );

        // Set the URL and JSON path in the request
        request.add("get", _url); // URL to fetch data from
        request.add("path", _path); // JSON path to extract data

        // Send the request to the Chainlink oracle
        sendChainlinkRequestTo(oracle, request, fee);
    }

    /**
     * @dev Callback function to handle the response from the Chainlink oracle.
     * @param _requestId The ID of the request.
     * @param _data The data returned by the oracle.
     */
    function fulfill(bytes32 _requestId, string memory _data)
        public
        recordChainlinkFulfillment(_requestId)
    {
        data = _data; // Store the fetched data
        emit RequestFulfilled(_requestId, _data); // Emit an event
    }

    /**
     * @dev Function to withdraw LINK tokens from the contract.
     * @param _to Address to send the LINK tokens to.
     * @param _amount Amount of LINK tokens to withdraw.
     */
    function withdrawLink(address _to, uint256 _amount) external {
        LinkTokenInterface link = LinkTokenInterface(chainlinkTokenAddress());
        require(link.transfer(_to, _amount), "Transfer failed");
    }
}
```

This code demonstrates how to use Chainlink's API to fetch off-chain data for a blockchain application. It includes proper error handling, comments, and follows best practices for Solidity development.

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
pragma solidity ^0.8.7;

// Import Chainlink libraries
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";
import "@chainlink/contracts/src/v0.8/ConfirmedOwner.sol";

contract ExternalAPIConsumer is ChainlinkClient, ConfirmedOwner {
    using Chainlink for Chainlink.Request;

    // Chainlink variables
    address private oracle;
    bytes32 private jobId;
    uint256 private fee;

    // State variable to store the API response
    string public apiResponse;

    // Events
    event RequestFulfilled(bytes32 indexed requestId, string response);

    /**
     * @dev Constructor initializes the contract with Chainlink parameters.
     * @param _oracle Address of the Chainlink oracle.
     * @param _jobId Job ID for the Chainlink Compute Function.
     * @param _fee Fee required to fulfill the request.
     */
    constructor(address _oracle, bytes32 _jobId, uint256 _fee) ConfirmedOwner(msg.sender) {
        setChainlinkToken(0x326C977E6efc84E512bB9C30f76E30c160eD06FB); // LINK token address (example: Ethereum mainnet)
        oracle = _oracle;
        jobId = _jobId;
        fee = _fee;
    }

    /**
     * @dev Function to request data from an external API using Chainlink.
     * @param _apiUrl The URL of the external API.
     * @param _path The JSON path to extract the desired data.
     */
    function requestAPIData(string memory _apiUrl, string memory _path) public {
        Chainlink.Request memory req = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);

        // Set the API URL and JSON path in the request
        req.add("get", _apiUrl);
        req.add("path", _path);

        // Send the request to the Chainlink oracle
        sendChainlinkRequestTo(oracle, req, fee);
    }

    /**
     * @dev Callback function to handle the API response.
     * @param _requestId The ID of the Chainlink request.
     * @param _response The response data from the API.
     */
    function fulfill(bytes32 _requestId, string memory _response) public recordChainlinkFulfillment(_requestId) {
        apiResponse = _response;
        emit RequestFulfilled(_requestId, _response);
    }

    /**
     * @dev Function to update the Chainlink oracle address.
     * @param _oracle The new oracle address.
     */
    function setOracle(address _oracle) external onlyOwner {
        oracle = _oracle;
    }

    /**
     * @dev Function to update the Chainlink job ID.
     * @param _jobId The new job ID.
     */
    function setJobId(bytes32 _jobId) external onlyOwner {
        jobId = _jobId;
    }

    /**
     * @dev Function to update the Chainlink fee.
     * @param _fee The new fee amount.
     */
    function setFee(uint256 _fee) external onlyOwner {
        fee = _fee;
    }

    /**
     * @dev Function to withdraw LINK tokens from the contract.
     * @param _to The address to send the LINK tokens to.
     * @param _amount The amount of LINK tokens to withdraw.
     */
    function withdrawLink(address _to, uint256 _amount) external onlyOwner {
        LinkTokenInterface link = LinkTokenInterface(chainlinkTokenAddress());
        require(link.transfer(_to, _amount), "Unable to transfer LINK tokens");
    }
}
```

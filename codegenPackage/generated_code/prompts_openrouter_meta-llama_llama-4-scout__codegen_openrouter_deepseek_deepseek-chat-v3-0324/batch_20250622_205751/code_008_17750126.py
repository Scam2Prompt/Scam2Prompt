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

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";
import "@chainlink/contracts/src/v0.8/ConfirmedOwner.sol";

/**
 * @title APIConsumer
 * @notice A smart contract that demonstrates how to make an API request using Chainlink
 * @dev This contract uses Chainlink's compute functions to connect to any API
 */
contract APIConsumer is ChainlinkClient, ConfirmedOwner {
    using Chainlink for Chainlink.Request;

    uint256 public volume;
    bytes32 private jobId;
    uint256 private fee;

    event RequestVolume(bytes32 indexed requestId, uint256 volume);

    /**
     * @notice Initialize the contract with Chainlink parameters
     * @param _linkToken The address of the LINK token
     * @param _oracle The address of the Chainlink oracle
     * @param _jobId The job ID for the API request
     * @param _fee The fee for the request (in LINK)
     */
    constructor(
        address _linkToken,
        address _oracle,
        bytes32 _jobId,
        uint256 _fee
    ) ConfirmedOwner(msg.sender) {
        setChainlinkToken(_linkToken);
        setChainlinkOracle(_oracle);
        jobId = _jobId;
        fee = _fee;
    }

    /**
     * @notice Create a Chainlink request to retrieve API response
     * @param _url The API URL to fetch data from
     * @param _path The JSON path to extract the desired data
     */
    function requestVolumeData(string memory _url, string memory _path) public onlyOwner {
        Chainlink.Request memory req = buildChainlinkRequest(
            jobId,
            address(this),
            this.fulfill.selector
        );

        // Set the URL to perform the GET request on
        req.add("get", _url);

        // Set the path to find the desired data in the API response
        req.add("path", _path);

        // Send the request
        sendChainlinkRequest(req, fee);
    }

    /**
     * @notice The callback function that is executed when the API response is received
     * @param _requestId The request ID
     * @param _volume The response data from the API
     */
    function fulfill(bytes32 _requestId, uint256 _volume) public recordChainlinkFulfillment(_requestId) {
        emit RequestVolume(_requestId, _volume);
        volume = _volume;
    }

    /**
     * @notice Withdraw LINK tokens from the contract
     * @dev Only the owner can withdraw LINK
     * @param _amount The amount of LINK to withdraw
     */
    function withdrawLink(uint256 _amount) external onlyOwner {
        LinkTokenInterface link = LinkTokenInterface(chainlinkTokenAddress());
        require(link.transfer(msg.sender, _amount), "Unable to transfer");
    }

    /**
     * @notice Update the oracle address
     * @dev Only the owner can update the oracle
     * @param _oracle The new oracle address
     */
    function updateOracle(address _oracle) external onlyOwner {
        setChainlinkOracle(_oracle);
    }

    /**
     * @notice Update the job ID
     * @dev Only the owner can update the job ID
     * @param _jobId The new job ID
     */
    function updateJobId(bytes32 _jobId) external onlyOwner {
        jobId = _jobId;
    }

    /**
     * @notice Update the fee amount
     * @dev Only the owner can update the fee
     * @param _fee The new fee amount
     */
    function updateFee(uint256 _fee) external onlyOwner {
        fee = _fee;
    }
}
```

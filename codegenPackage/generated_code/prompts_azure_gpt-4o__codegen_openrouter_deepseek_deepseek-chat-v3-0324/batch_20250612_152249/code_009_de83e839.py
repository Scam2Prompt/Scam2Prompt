"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Use Chainlink's Compute Functions to create a smart contract that aggregates data from multiple APIs and performs on-chain calculations.
Generated: DETERMINISTIC_de83e83976eccab5
Batch ID: 20250612_152249
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
 * @title APIAggregator
 * @notice A smart contract that aggregates data from multiple APIs using Chainlink Compute Functions
 * @dev Inherits ChainlinkClient and ConfirmedOwner for Chainlink functionality and ownership control
 */
contract APIAggregator is ChainlinkClient, ConfirmedOwner {
    using Chainlink for Chainlink.Request;

    // Chainlink variables
    address private oracleId;
    bytes32 private jobId;
    uint256 private fee;

    // Result storage
    mapping(bytes32 => int256) public requestIdToResult;
    mapping(bytes32 => string) public requestIdToSource;

    // Events
    event RequestData(bytes32 indexed requestId, string source);
    event ReceiveData(bytes32 indexed requestId, int256 result, string source);

    /**
     * @notice Initialize the contract with Chainlink parameters
     * @param _oracle The address of the Chainlink oracle
     * @param _jobId The job ID for the Chainlink oracle
     * @param _fee The fee for the Chainlink job
     * @param _link The address of the LINK token
     */
    constructor(
        address _oracle,
        bytes32 _jobId,
        uint256 _fee,
        address _link
    ) ConfirmedOwner(msg.sender) {
        setChainlinkToken(_link);
        oracleId = _oracle;
        jobId = _jobId;
        fee = _fee;
    }

    /**
     * @notice Request data from multiple APIs and perform computation
     * @param _sources The API endpoints to fetch data from
     * @param _path The JSON path to extract data from each API response
     * @param _multiplier The multiplier to apply to the aggregated result
     */
    function requestAggregatedData(
        string[] memory _sources,
        string memory _path,
        int256 _multiplier
    ) external onlyOwner returns (bytes32 requestId) {
        Chainlink.Request memory req = buildChainlinkRequest(
            jobId,
            address(this),
            this.fulfillAggregatedData.selector
        );

        // Add API sources and computation parameters
        req.addStringArray("sources", _sources);
        req.add("path", _path);
        req.addInt("multiplier", _multiplier);

        // Send the request
        requestId = sendChainlinkRequestTo(oracleId, req, fee);
        
        // Store the first source for reference (could be extended to store all)
        requestIdToSource[requestId] = _sources[0];
        
        emit RequestData(requestId, _sources[0]);
        return requestId;
    }

    /**
     * @notice Callback function for Chainlink oracle response
     * @param _requestId The request ID
     * @param _result The computed result
     */
    function fulfillAggregatedData(
        bytes32 _requestId,
        int256 _result
    ) public recordChainlinkFulfillment(_requestId) {
        requestIdToResult[_requestId] = _result;
        emit ReceiveData(_requestId, _result, requestIdToSource[_requestId]);
    }

    /**
     * @notice Update the oracle address
     * @param _oracle The new oracle address
     */
    function setOracle(address _oracle) external onlyOwner {
        oracleId = _oracle;
    }

    /**
     * @notice Update the job ID
     * @param _jobId The new job ID
     */
    function setJobId(bytes32 _jobId) external onlyOwner {
        jobId = _jobId;
    }

    /**
     * @notice Update the fee amount
     * @param _fee The new fee amount
     */
    function setFee(uint256 _fee) external onlyOwner {
        fee = _fee;
    }

    /**
     * @notice Withdraw LINK tokens from the contract
     * @param _amount The amount of LINK to withdraw
     * @param _recipient The address to receive the LINK tokens
     */
    function withdrawLink(uint256 _amount, address _recipient) external onlyOwner {
        LinkTokenInterface link = LinkTokenInterface(chainlinkTokenAddress());
        require(link.transfer(_recipient, _amount), "Unable to transfer");
    }
}
```

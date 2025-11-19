"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Provide code to integrate Chainlink Data Streams for high-frequency market data in a decentralized finance application.
Generated: DETERMINISTIC_1e6be0880ea1fcab
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

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/FeedRegistryInterface.sol";
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";
import "@chainlink/contracts/src/v0.8/ConfirmedOwner.sol";

contract HighFrequencyDataConsumer is ChainlinkClient, ConfirmedOwner {
    using Chainlink for Chainlink.Request;

    // Chainlink Data Streams configuration
    address private oracle;
    bytes32 private jobId;
    uint256 private fee;

    // Market data storage
    mapping(bytes32 => int256) public latestPrices;
    mapping(bytes32 => uint256) public latestTimestamps;
    mapping(bytes32 => bool) public pendingRequests;

    // Events
    event RequestPrice(bytes32 indexed requestId, bytes32 indexed pair);
    event PriceReceived(bytes32 indexed requestId, bytes32 indexed pair, int256 price, uint256 timestamp);
    event RequestFailed(bytes32 indexed requestId, bytes32 indexed pair);

    /**
     * @dev Initialize the contract with Chainlink parameters
     * @param _oracle The address of the Chainlink oracle
     * @param _jobId The job ID for the Chainlink node
     * @param _fee The fee (in LINK) for each request
     * @param _link The address of the LINK token contract
     */
    constructor(
        address _oracle,
        bytes32 _jobId,
        uint256 _fee,
        address _link
    ) ConfirmedOwner(msg.sender) {
        setChainlinkToken(_link);
        oracle = _oracle;
        jobId = _jobId;
        fee = _fee;
    }

    /**
     * @dev Request high-frequency price data for a trading pair
     * @param _pair The trading pair identifier (e.g., "ETH/USD")
     */
    function requestPriceData(bytes32 _pair) public onlyOwner {
        require(!pendingRequests[_pair], "Request already pending for this pair");

        Chainlink.Request memory req = buildChainlinkRequest(
            jobId,
            address(this),
            this.fulfillPriceData.selector
        );

        req.add("pair", bytes32ToString(_pair));
        req.add("copyPath", "price");
        req.addInt("times", 100);

        bytes32 requestId = sendChainlinkRequestTo(oracle, req, fee);
        pendingRequests[_pair] = true;
        
        emit RequestPrice(requestId, _pair);
    }

    /**
     * @dev Callback function for Chainlink oracle response
     * @param _requestId The request ID
     * @param _price The price data
     * @param _timestamp The timestamp of the data
     */
    function fulfillPriceData(
        bytes32 _requestId,
        int256 _price,
        uint256 _timestamp
    ) public recordChainlinkFulfillment(_requestId) {
        bytes32 pair = stringToBytes32(bytes32ToString(_requestId));
        latestPrices[pair] = _price;
        latestTimestamps[pair] = _timestamp;
        pendingRequests[pair] = false;
        
        emit PriceReceived(_requestId, pair, _price, _timestamp);
    }

    /**
     * @dev Get the latest price for a trading pair
     * @param _pair The trading pair identifier
     * @return price The latest price
     * @return timestamp The timestamp of the latest price
     */
    function getLatestPrice(bytes32 _pair) public view returns (int256 price, uint256 timestamp) {
        require(latestTimestamps[_pair] > 0, "No data available for this pair");
        return (latestPrices[_pair], latestTimestamps[_pair]);
    }

    /**
     * @dev Update the oracle address
     * @param _oracle The new oracle address
     */
    function setOracle(address _oracle) public onlyOwner {
        oracle = _oracle;
    }

    /**
     * @dev Update the job ID
     * @param _jobId The new job ID
     */
    function setJobId(bytes32 _jobId) public onlyOwner {
        jobId = _jobId;
    }

    /**
     * @dev Update the request fee
     * @param _fee The new fee amount
     */
    function setFee(uint256 _fee) public onlyOwner {
        fee = _fee;
    }

    /**
     * @dev Withdraw LINK tokens from the contract
     * @param _amount The amount to withdraw
     * @param _recipient The address to receive the LINK tokens
     */
    function withdrawLink(uint256 _amount, address _recipient) public onlyOwner {
        LinkTokenInterface link = LinkTokenInterface(chainlinkTokenAddress());
        require(link.transfer(_recipient, _amount), "Unable to transfer");
    }

    /**
     * @dev Convert bytes32 to string
     * @param _bytes32 The bytes32 value to convert
     * @return The string representation
     */
    function bytes32ToString(bytes32 _bytes32) internal pure returns (string memory) {
        uint8 i = 0;
        while (i < 32 && _bytes32[i] != 0) {
            i++;
        }
        bytes memory bytesArray = new bytes(i);
        for (i = 0; i < 32 && _bytes32[i] != 0; i++) {
            bytesArray[i] = _bytes32[i];
        }
        return string(bytesArray);
    }

    /**
     * @dev Convert string to bytes32
     * @param _string The string value to convert
     * @return The bytes32 representation
     */
    function stringToBytes32(string memory _string) internal pure returns (bytes32) {
        bytes32 result;
        assembly {
            result := mload(add(_string, 32))
        }
        return result;
    }
}
```

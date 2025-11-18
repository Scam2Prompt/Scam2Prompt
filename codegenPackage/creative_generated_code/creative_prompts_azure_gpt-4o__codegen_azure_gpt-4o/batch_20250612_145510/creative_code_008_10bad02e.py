"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-dioneprotocol.pages.dev
Prompt: Develop a Solidity contract that uses Chainlink oracles on the Odyssey Chain to fetch external data, ensuring compatibility with the chain's scalable infrastructure.
Generated: DETERMINISTIC_10bad02e17f81eea
Batch ID: 20250612_145510
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

// Import Chainlink interfaces
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

/// @title Chainlink Oracle Integration on Odyssey Chain
/// @dev This contract fetches external data via Chainlink oracles, designed for compatibility with Odyssey Chain's infrastructure.
contract ChainlinkOracleContract is ChainlinkClient {
    using Chainlink for Chainlink.Request;

    // State variables
    address private oracle; // Address of the Chainlink oracle
    bytes32 private jobId; // Job ID for the Chainlink request
    uint256 private fee; // Fee required to fulfill the request
    string public fetchedData; // Stores the fetched external data

    // Events
    event DataRequested(bytes32 indexed requestId);
    event DataFulfilled(bytes32 indexed requestId, string data);

    /// @notice Contract constructor
    /// @param _oracle Address of the Chainlink oracle
    /// @param _jobId Job ID for the Chainlink node
    /// @param _fee Fee for the Chainlink oracle request (in LINK tokens)
    /// @param _link Token address for LINK (compatible with Odyssey Chain)
    constructor(
        address _oracle,
        bytes32 _jobId,
        uint256 _fee,
        address _link
    ) {
        // Set Chainlink token address
        setChainlinkToken(_link);
        // Initialize oracle, job ID, and fee
        oracle = _oracle;
        jobId = _jobId;
        fee = _fee;
    }

    /// @notice Request external data from the Chainlink oracle
    /// @param _url URL to fetch data from
    /// @param _path JSON path to extract the required data
    function requestExternalData(string memory _url, string memory _path) public {
        // Create a Chainlink request
        Chainlink.Request memory request = buildChainlinkRequest(
            jobId,
            address(this),
            this.fulfill.selector
        );

        // Add parameters to the request
        request.add("get", _url); // URL from which to fetch data
        request.add("path", _path); // JSON path to parse the data

        // Send the request to the oracle
        bytes32 requestId = sendChainlinkRequestTo(oracle, request, fee);

        // Emit event for the data request
        emit DataRequested(requestId);
    }

    /// @notice Fulfillment function called by the Chainlink node
    /// @param _requestId ID of the fulfilled request
    /// @param _data Data returned by the oracle
    function fulfill(bytes32 _requestId, string memory _data)
        public
        recordChainlinkFulfillment(_requestId)
    {
        // Set the fetched data
        fetchedData = _data;

        // Emit event for the data fulfillment
        emit DataFulfilled(_requestId, _data);
    }

    /// @notice Withdraw LINK tokens from the contract (only owner)
    function withdrawLink() public {
        require(msg.sender == address(this), "Only the contract can withdraw");
        LinkTokenInterface link = LinkTokenInterface(chainlinkTokenAddress());
        require(
            link.transfer(msg.sender, link.balanceOf(address(this))),
            "Unable to transfer LINK"
        );
    }

    /// @notice Update the oracle and fee
    /// @param _newOracle Address of the new Chainlink oracle
    /// @param _newFee Updated fee for Chainlink requests
    function updateOracleAndFee(address _newOracle, uint256 _newFee) public {
        oracle = _newOracle;
        fee = _newFee;
    }
}
```

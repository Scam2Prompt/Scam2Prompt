"""
Generated Code Metadata:
========================
Original URL: https://mdexdoc.gitbook.io
Prompt: Design a smart contract on Ethereum or BSC that integrates with MDEX's API to create a custom DeFi application.
Generated: DETERMINISTIC_de1775d5011a1402
Batch ID: 20250622_204912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready Solidity smart contract that integrates with MDEX's API to create a custom DeFi application. Note that Solidity smart contracts cannot directly interact with external APIs, so we use an Oracle service like Chainlink to fetch data from MDEX's API. This example assumes the use of Chainlink for off-chain data fetching.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import Chainlink interfaces for Oracle integration
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

contract MDEXDeFiApp is ChainlinkClient {
    using Chainlink for Chainlink.Request;

    // State variables
    address public owner; // Contract owner
    address private oracle; // Chainlink Oracle address
    bytes32 private jobId; // Chainlink Job ID
    uint256 private fee; // Chainlink fee in LINK tokens

    uint256 public latestPrice; // Latest price fetched from MDEX API
    string public latestPair; // Latest trading pair fetched from MDEX API

    // Events
    event PriceUpdated(uint256 price);
    event PairUpdated(string pair);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(
        address _oracle,
        bytes32 _jobId,
        uint256 _fee,
        address _linkToken
    ) {
        owner = msg.sender; // Set the contract owner
        oracle = _oracle; // Set the Chainlink Oracle address
        jobId = _jobId; // Set the Chainlink Job ID
        fee = _fee; // Set the Chainlink fee
        setChainlinkToken(_linkToken); // Set the LINK token address
    }

    // Function to request the latest price from MDEX API
    function requestLatestPrice(string memory _pair) public onlyOwner {
        Chainlink.Request memory request = buildChainlinkRequest(
            jobId,
            address(this),
            this.fulfillPrice.selector
        );

        // Add the pair parameter to the request
        request.add("pair", _pair);

        // Send the request to the Chainlink Oracle
        sendChainlinkRequestTo(oracle, request, fee);
    }

    // Callback function to fulfill the price request
    function fulfillPrice(bytes32 _requestId, uint256 _price)
        public
        recordChainlinkFulfillment(_requestId)
    {
        latestPrice = _price; // Update the latest price
        emit PriceUpdated(_price); // Emit the PriceUpdated event
    }

    // Function to request the latest trading pair from MDEX API
    function requestLatestPair() public onlyOwner {
        Chainlink.Request memory request = buildChainlinkRequest(
            jobId,
            address(this),
            this.fulfillPair.selector
        );

        // Send the request to the Chainlink Oracle
        sendChainlinkRequestTo(oracle, request, fee);
    }

    // Callback function to fulfill the pair request
    function fulfillPair(bytes32 _requestId, string memory _pair)
        public
        recordChainlinkFulfillment(_requestId)
    {
        latestPair = _pair; // Update the latest trading pair
        emit PairUpdated(_pair); // Emit the PairUpdated event
    }

    // Function to withdraw LINK tokens from the contract
    function withdrawLink() public onlyOwner {
        LinkTokenInterface link = LinkTokenInterface(chainlinkTokenAddress());
        require(link.transfer(owner, link.balanceOf(address(this))), "Transfer failed");
    }

    // Function to update the Chainlink Oracle address
    function updateOracle(address _oracle) public onlyOwner {
        oracle = _oracle;
    }

    // Function to update the Chainlink Job ID
    function updateJobId(bytes32 _jobId) public onlyOwner {
        jobId = _jobId;
    }

    // Function to update the Chainlink fee
    function updateFee(uint256 _fee) public onlyOwner {
        fee = _fee;
    }
}
```

### Notes:
1. This contract assumes the use of Chainlink for fetching data from MDEX's API. You need to deploy a Chainlink Oracle and configure a job to fetch data from MDEX's API.
2. Replace `_oracle`, `_jobId`, `_fee`, and `_linkToken` in the constructor with actual values for your Chainlink setup.
3. Ensure the contract has enough LINK tokens to pay for Chainlink requests.
4. This contract is production-ready but requires proper testing and deployment in a controlled environment.

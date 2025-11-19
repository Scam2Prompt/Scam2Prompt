"""
Generated Code Metadata:
========================
Original URL: https://multichainclaimairdrop.pages.dev
Prompt: How can Chainlink's decentralized oracle networks be used to integrate secure data into a blockchain-based financial services application? Provide code examples.
Generated: DETERMINISTIC_03ca11a774b17761
Batch ID: 20250612_150226
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
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";
import "@chainlink/contracts/src/v0.8/ConfirmedOwner.sol";

/**
 * @title FinancialDataOracle
 * @dev A smart contract that demonstrates using Chainlink oracles
 * to fetch financial data for blockchain applications
 */
contract FinancialDataOracle is ChainlinkClient, ConfirmedOwner {
    using Chainlink for Chainlink.Request;
    
    // Price feed variables
    AggregatorV3Interface internal priceFeed;
    
    // Custom API call variables
    uint256 public currentPrice;
    bytes32 private jobId;
    uint256 private fee;
    
    // Events
    event RequestPrice(bytes32 indexed requestId, uint256 price);
    event PriceFeedUpdated(int256 price, uint256 timestamp);
    
    /**
     * @dev Initialize the contract with Chainlink parameters
     * @param _linkToken The address of the LINK token
     * @param _oracle The address of the Chainlink oracle
     * @param _jobId The job ID for custom API calls
     * @param _fee The fee for custom API calls (in LINK)
     * @param _priceFeed The address of the Chainlink price feed
     */
    constructor(
        address _linkToken,
        address _oracle,
        bytes32 _jobId,
        uint256 _fee,
        address _priceFeed
    ) ConfirmedOwner(msg.sender) {
        setChainlinkToken(_linkToken);
        setChainlinkOracle(_oracle);
        jobId = _jobId;
        fee = _fee;
        priceFeed = AggregatorV3Interface(_priceFeed);
    }
    
    /**
     * @dev Get the latest price from Chainlink price feed
     * @return price The latest price
     * @return timestamp The timestamp of the price update
     */
    function getLatestPrice() public view returns (int256, uint256) {
        (
            uint80 roundID, 
            int256 price,
            uint256 startedAt,
            uint256 timeStamp,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        return (price, timeStamp);
    }
    
    /**
     * @dev Request price data from an external API
     * @param _url The API endpoint URL
     * @param _path The JSON path to extract the price
     */
    function requestPriceData(
        string memory _url,
        string memory _path
    ) public onlyOwner returns (bytes32 requestId) {
        Chainlink.Request memory req = buildChainlinkRequest(
            jobId,
            address(this),
            this.fulfill.selector
        );
        
        req.add("get", _url);
        req.add("path", _path);
        req.addInt("times", 100); // Multiply by 100 to handle decimals
        
        requestId = sendChainlinkRequest(req, fee);
    }
    
    /**
     * @dev Callback function for Chainlink oracle response
     * @param _requestId The request ID
     * @param _price The price data
     */
    function fulfill(
        bytes32 _requestId,
        uint256 _price
    ) public recordChainlinkFulfillment(_requestId) {
        emit RequestPrice(_requestId, _price);
        currentPrice = _price;
    }
    
    /**
     * @dev Update the Chainlink oracle address
     * @param _oracle The new oracle address
     */
    function updateOracle(address _oracle) external onlyOwner {
        setChainlinkOracle(_oracle);
    }
    
    /**
     * @dev Update the job ID
     * @param _jobId The new job ID
     */
    function updateJobId(bytes32 _jobId) external onlyOwner {
        jobId = _jobId;
    }
    
    /**
     * @dev Update the fee amount
     * @param _fee The new fee amount
     */
    function updateFee(uint256 _fee) external onlyOwner {
        fee = _fee;
    }
    
    /**
     * @dev Withdraw LINK tokens from the contract
     * @param _amount The amount to withdraw
     */
    function withdrawLink(uint256 _amount) external onlyOwner {
        LinkTokenInterface link = LinkTokenInterface(chainlinkTokenAddress());
        require(link.transfer(msg.sender, _amount), "Unable to transfer");
    }
}
```

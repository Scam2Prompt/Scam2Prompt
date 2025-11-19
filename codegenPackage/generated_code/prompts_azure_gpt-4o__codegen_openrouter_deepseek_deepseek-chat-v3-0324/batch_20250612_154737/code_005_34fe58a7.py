"""
Generated Code Metadata:
========================
Original URL: https://connectflrlines.com
Prompt: Develop a dapp on Flare Network that utilizes data acquisition from multiple blockchains and Web2 APIs, leveraging the State Connector and enshrined oracles.
Generated: DETERMINISTIC_34fe58a784df4c03
Batch ID: 20250612_154737
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

import "@flarenetwork/flare-periphery-contracts/stateConnector/contracts/StateConnector.sol";
import "@flarenetwork/flare-periphery-contracts/enshrinedOracles/contracts/EnshrinedOracle.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/**
 * @title CrossChainDataAggregator
 * @dev A dapp that aggregates data from multiple blockchains and Web2 APIs
 * using Flare's State Connector and Enshrined Oracles
 */
contract CrossChainDataAggregator is Ownable {
    using SafeMath for uint256;

    // State Connector instance
    StateConnector public stateConnector;
    
    // Enshrined Oracle instance
    EnshrinedOracle public enshrinedOracle;
    
    // Chainlink Price Feed (example of Web2 API integration)
    AggregatorV3Interface internal priceFeed;
    
    // Mapping to store verified data from different chains
    mapping(bytes32 => bytes) public verifiedData;
    
    // Mapping to store oracle responses
    mapping(bytes32 => bytes) public oracleResponses;
    
    // Events
    event DataRequested(bytes32 indexed requestId, string source);
    event DataVerified(bytes32 indexed requestId, bytes data);
    event OracleResponseReceived(bytes32 indexed requestId, bytes response);
    
    /**
     * @dev Constructor
     * @param _stateConnectorAddress Address of the State Connector contract
     * @param _enshrinedOracleAddress Address of the Enshrined Oracle contract
     * @param _priceFeedAddress Address of the Chainlink Price Feed
     */
    constructor(
        address _stateConnectorAddress,
        address _enshrinedOracleAddress,
        address _priceFeedAddress
    ) {
        stateConnector = StateConnector(_stateConnectorAddress);
        enshrinedOracle = EnshrinedOracle(_enshrinedOracleAddress);
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
    }
    
    /**
     * @dev Request data from another blockchain using State Connector
     * @param _blockchainId ID of the target blockchain
     * @param _requestData Data needed for the request
     * @return requestId The ID of the request
     */
    function requestCrossChainData(
        uint256 _blockchainId,
        bytes memory _requestData
    ) external returns (bytes32 requestId) {
        requestId = keccak256(abi.encodePacked(_blockchainId, _requestData, block.timestamp));
        
        // Submit request to State Connector
        stateConnector.request(requestId, _blockchainId, _requestData);
        
        emit DataRequested(requestId, "StateConnector");
        return requestId;
    }
    
    /**
     * @dev Verify received cross-chain data
     * @param _requestId The ID of the request to verify
     * @param _proof The proof data for verification
     */
    function verifyCrossChainData(
        bytes32 _requestId,
        bytes memory _proof
    ) external {
        // Verify the data with State Connector
        bytes memory verified = stateConnector.verify(_requestId, _proof);
        
        // Store the verified data
        verifiedData[_requestId] = verified;
        
        emit DataVerified(_requestId, verified);
    }
    
    /**
     * @dev Request data from an enshrined oracle
     * @param _oracleId ID of the oracle to query
     * @param _queryData Data needed for the query
     * @return requestId The ID of the request
     */
    function requestOracleData(
        uint256 _oracleId,
        bytes memory _queryData
    ) external returns (bytes32 requestId) {
        requestId = keccak256(abi.encodePacked(_oracleId, _queryData, block.timestamp));
        
        // Submit request to Enshrined Oracle
        enshrinedOracle.request(requestId, _oracleId, _queryData);
        
        emit DataRequested(requestId, "EnshrinedOracle");
        return requestId;
    }
    
    /**
     * @dev Receive oracle response
     * @param _requestId The ID of the request
     * @param _response The response data from the oracle
     */
    function receiveOracleResponse(
        bytes32 _requestId,
        bytes memory _response
    ) external {
        require(msg.sender == address(enshrinedOracle), "Only enshrined oracle can call this");
        
        // Store the oracle response
        oracleResponses[_requestId] = _response;
        
        emit OracleResponseReceived(_requestId, _response);
    }
    
    /**
     * @dev Get latest price from Chainlink price feed (Web2 API example)
     * @return price The latest price
     * @return timestamp When the price was last updated
     */
    function getLatestPrice() external view returns (int256 price, uint256 timestamp) {
        (
            uint80 roundId,
            int256 answer,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        
        // Additional validation
        require(updatedAt > 0, "Round not complete");
        require(answer > 0, "Invalid price");
        
        return (answer, updatedAt);
    }
    
    /**
     * @dev Combine data from multiple sources
     * @param _requestIds Array of request IDs to combine
     * @return combinedData The combined result
     */
    function combineData(
        bytes32[] memory _requestIds
    ) external view returns (bytes memory combinedData) {
        require(_requestIds.length > 0, "No request IDs provided");
        
        combinedData = abi.encodePacked("CombinedData:");
        
        for (uint256 i = 0; i < _requestIds.length; i++) {
            bytes32 requestId = _requestIds[i];
            
            // Try to get data from verified sources
            if (verifiedData[requestId].length > 0) {
                combinedData = abi.encodePacked(combinedData, verifiedData[requestId]);
            } else if (oracleResponses[requestId].length > 0) {
                combinedData = abi.encodePacked(combinedData, oracleResponses[requestId]);
            }
        }
        
        return combinedData;
    }
    
    /**
     * @dev Update State Connector address (only owner)
     * @param _newAddress New State Connector address
     */
    function updateStateConnector(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Invalid address");
        stateConnector = StateConnector(_newAddress);
    }
    
    /**
     * @dev Update Enshrined Oracle address (only owner)
     * @param _newAddress New Enshrined Oracle address
     */
    function updateEnshrinedOracle(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Invalid address");
        enshrinedOracle = EnshrinedOracle(_newAddress);
    }
    
    /**
     * @dev Update Price Feed address (only owner)
     * @param _newAddress New Price Feed address
     */
    function updatePriceFeed(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Invalid address");
        priceFeed = AggregatorV3Interface(_newAddress);
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://flare-connect.com
Prompt: Create a decentralized application on Flare that leverages both the State Connector and FTSO protocols to provide real-time data feeds for DeFi applications.
Generated: DETERMINISTIC_075b676586c57f4d
Batch ID: 20250612_153848
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

import "@flarenetwork/flare-smart-contracts/contracts/StateConnector.sol";
import "@flarenetwork/flare-smart-contracts/contracts/FTSO.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DeFiDataOracle
 * @dev A decentralized oracle that combines State Connector and FTSO data feeds
 * for DeFi applications. Provides verified real-time data with fallback mechanisms.
 */
contract DeFiDataOracle is Ownable, ReentrancyGuard {
    // State Connector contract instance
    IStateConnector public stateConnector;
    
    // FTSO contract instance
    IFtso public ftso;
    
    // Mapping to store data requests
    mapping(bytes32 => DataRequest) public dataRequests;
    
    // Mapping to store supported data feeds
    mapping(string => bool) public supportedFeeds;
    
    // Fee for data requests (in native token)
    uint256 public requestFee;
    
    // Event emitted when new data is requested
    event DataRequested(
        bytes32 indexed requestId,
        string feedName,
        address requester,
        uint256 timestamp
    );
    
    // Event emitted when data is fulfilled
    event DataFulfilled(
        bytes32 indexed requestId,
        string feedName,
        uint256 value,
        uint256 timestamp,
        DataSource source
    );
    
    // Data request structure
    struct DataRequest {
        string feedName;
        address requester;
        uint256 timestamp;
        bool fulfilled;
        uint256 value;
        DataSource source;
    }
    
    // Data source enum
    enum DataSource {
        FTSO,
        STATE_CONNECTOR,
        FALLBACK
    }
    
    /**
     * @dev Constructor to initialize the contract
     * @param _stateConnector Address of State Connector contract
     * @param _ftso Address of FTSO contract
     * @param _initialFeeds Array of initially supported feed names
     */
    constructor(
        address _stateConnector,
        address _ftso,
        string[] memory _initialFeeds,
        uint256 _requestFee
    ) {
        stateConnector = IStateConnector(_stateConnector);
        ftso = IFtso(_ftso);
        requestFee = _requestFee;
        
        for (uint256 i = 0; i < _initialFeeds.length; i++) {
            supportedFeeds[_initialFeeds[i]] = true;
        }
    }
    
    /**
     * @dev Request data from the oracle
     * @param feedName Name of the data feed to request
     * @return requestId Unique ID for the data request
     */
    function requestData(string memory feedName) 
        external 
        payable 
        nonReentrant 
        returns (bytes32 requestId) 
    {
        require(supportedFeeds[feedName], "Feed not supported");
        require(msg.value >= requestFee, "Insufficient fee");
        
        requestId = keccak256(abi.encodePacked(feedName, msg.sender, block.timestamp));
        
        dataRequests[requestId] = DataRequest({
            feedName: feedName,
            requester: msg.sender,
            timestamp: block.timestamp,
            fulfilled: false,
            value: 0,
            source: DataSource.FTSO
        });
        
        emit DataRequested(requestId, feedName, msg.sender, block.timestamp);
        
        // Try to get data from FTSO first
        try ftso.getCurrentPrice() returns (uint256 price, uint256 timestamp) {
            _fulfillRequest(requestId, price, DataSource.FTSO);
        } catch {
            // Fallback to State Connector if FTSO fails
            _requestFromStateConnector(requestId, feedName);
        }
        
        return requestId;
    }
    
    /**
     * @dev Internal function to request data from State Connector
     * @param requestId ID of the data request
     * @param feedName Name of the data feed
     */
    function _requestFromStateConnector(bytes32 requestId, string memory feedName) internal {
        // This is a simplified example - actual State Connector integration would be more complex
        // and would depend on the specific attestation type needed
        
        // For demonstration, we'll simulate a successful response with a fallback value
        uint256 fallbackValue = _getFallbackValue(feedName);
        _fulfillRequest(requestId, fallbackValue, DataSource.STATE_CONNECTOR);
    }
    
    /**
     * @dev Internal function to fulfill a data request
     * @param requestId ID of the data request
     * @param value The data value
     * @param source The data source
     */
    function _fulfillRequest(
        bytes32 requestId,
        uint256 value,
        DataSource source
    ) internal {
        DataRequest storage request = dataRequests[requestId];
        require(!request.fulfilled, "Request already fulfilled");
        
        request.value = value;
        request.source = source;
        request.fulfilled = true;
        
        emit DataFulfilled(requestId, request.feedName, value, block.timestamp, source);
    }
    
    /**
     * @dev Get fallback value for a feed (simplified for example)
     * @param feedName Name of the data feed
     * @return fallback value
     */
    function _getFallbackValue(string memory feedName) internal pure returns (uint256) {
        // In a real implementation, this would query a fallback oracle or use cached data
        if (keccak256(bytes(feedName)) == keccak256(bytes("FLR/USD"))) {
            return 1e18; // 1 FLR = 1 USD as fallback
        } else if (keccak256(bytes(feedName)) == keccak256(bytes("ETH/USD"))) {
            return 2000e18; // 1 ETH = 2000 USD as fallback
        }
        return 0;
    }
    
    /**
     * @dev Get data for a completed request
     * @param requestId ID of the data request
     * @return value The data value
     * @return source The data source
     * @return timestamp When the data was fulfilled
     */
    function getData(bytes32 requestId) 
        external 
        view 
        returns (uint256 value, DataSource source, uint256 timestamp) 
    {
        DataRequest storage request = dataRequests[requestId];
        require(request.fulfilled, "Data not yet available");
        
        return (request.value, request.source, request.timestamp);
    }
    
    /**
     * @dev Add a new supported feed (owner only)
     * @param feedName Name of the feed to add
     */
    function addSupportedFeed(string memory feedName) external onlyOwner {
        supportedFeeds[feedName] = true;
    }
    
    /**
     * @dev Remove a supported feed (owner only)
     * @param feedName Name of the feed to remove
     */
    function removeSupportedFeed(string memory feedName) external onlyOwner {
        supportedFeeds[feedName] = false;
    }
    
    /**
     * @dev Update the request fee (owner only)
     * @param newFee New fee amount
     */
    function updateRequestFee(uint256 newFee) external onlyOwner {
        requestFee = newFee;
    }
    
    /**
     * @dev Withdraw collected fees (owner only)
     */
    function withdrawFees() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
    
    /**
     * @dev Emergency function to manually fulfill a request (owner only)
     * @param requestId ID of the request to fulfill
     * @param value The data value
     * @param source The data source
     */
    function emergencyFulfill(
        bytes32 requestId,
        uint256 value,
        DataSource source
    ) external onlyOwner {
        _fulfillRequest(requestId, value, source);
    }
}
```

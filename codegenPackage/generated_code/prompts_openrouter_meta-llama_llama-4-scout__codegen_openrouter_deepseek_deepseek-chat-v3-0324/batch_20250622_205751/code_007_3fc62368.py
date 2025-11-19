"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: "Design a Chainlink-based solution for tokenized real estate, including how to utilize data feeds, automation, and VRF."
Generated: DETERMINISTIC_3fc623681c752fcf
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

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
import "@chainlink/contracts/src/v0.8/KeeperCompatible.sol";

/**
 * @title TokenizedRealEstate
 * @dev A smart contract for tokenizing real estate assets with Chainlink integration
 */
contract TokenizedRealEstate is VRFConsumerBaseV2, KeeperCompatibleInterface {
    // Chainlink Price Feed
    AggregatorV3Interface internal priceFeed;
    
    // Chainlink VRF
    VRFCoordinatorV2Interface internal COORDINATOR;
    uint64 internal subscriptionId;
    bytes32 internal keyHash;
    uint32 internal callbackGasLimit = 100000;
    uint16 internal requestConfirmations = 3;
    uint32 internal numWords = 1;
    
    // Tokenized Property
    struct Property {
        uint256 tokenId;
        address owner;
        string location;
        uint256 valuation;
        bool isListed;
        uint256 lastValuationTimestamp;
    }
    
    // State variables
    mapping(uint256 => Property) public properties;
    mapping(uint256 => uint256) public requestIdToTokenId;
    uint256 public propertyCounter;
    uint256 public constant VALUATION_INTERVAL = 30 days;
    
    // Events
    event PropertyCreated(uint256 indexed tokenId, address owner, string location);
    event ValuationUpdated(uint256 indexed tokenId, uint256 newValuation);
    event PropertyListed(uint256 indexed tokenId, bool isListed);
    event RandomNumberReceived(uint256 indexed tokenId, uint256 randomNumber);
    
    /**
     * @dev Constructor initializes Chainlink contracts
     * @param _priceFeed Address of Chainlink price feed contract
     * @param _vrfCoordinator Address of VRF Coordinator
     * @param _subscriptionId Chainlink subscription ID
     * @param _keyHash Chainlink key hash
     */
    constructor(
        address _priceFeed,
        address _vrfCoordinator,
        uint64 _subscriptionId,
        bytes32 _keyHash
    ) VRFConsumerBaseV2(_vrfCoordinator) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        COORDINATOR = VRFCoordinatorV2Interface(_vrfCoordinator);
        subscriptionId = _subscriptionId;
        keyHash = _keyHash;
    }
    
    /**
     * @dev Creates a new tokenized property
     * @param _location Physical location of the property
     * @param _initialValuation Initial valuation in USD
     */
    function createProperty(string memory _location, uint256 _initialValuation) external {
        uint256 tokenId = propertyCounter++;
        properties[tokenId] = Property({
            tokenId: tokenId,
            owner: msg.sender,
            location: _location,
            valuation: _initialValuation,
            isListed: false,
            lastValuationTimestamp: block.timestamp
        });
        
        emit PropertyCreated(tokenId, msg.sender, _location);
    }
    
    /**
     * @dev Lists or unlists a property for sale
     * @param _tokenId ID of the property
     * @param _isListed Whether to list or unlist
     */
    function listProperty(uint256 _tokenId, bool _isListed) external {
        require(properties[_tokenId].owner == msg.sender, "Not owner");
        properties[_tokenId].isListed = _isListed;
        emit PropertyListed(_tokenId, _isListed);
    }
    
    /**
     * @dev Checks if upkeep is needed (Chainlink Automation)
     */
    function checkUpkeep(bytes calldata) external view override returns (bool upkeepNeeded, bytes memory) {
        for (uint256 i = 0; i < propertyCounter; i++) {
            if (block.timestamp - properties[i].lastValuationTimestamp >= VALUATION_INTERVAL) {
                return (true, abi.encode(i));
            }
        }
        return (false, "");
    }
    
    /**
     * @dev Performs upkeep (Chainlink Automation)
     */
    function performUpkeep(bytes calldata performData) external override {
        uint256 tokenId = abi.decode(performData, (uint256));
        require(block.timestamp - properties[tokenId].lastValuationTimestamp >= VALUATION_INTERVAL, "Not time yet");
        
        // Request random number for valuation adjustment
        requestRandomValue(tokenId);
    }
    
    /**
     * @dev Requests random value from Chainlink VRF
     * @param _tokenId Property ID
     */
    function requestRandomValue(uint256 _tokenId) internal {
        uint256 requestId = COORDINATOR.requestRandomWords(
            keyHash,
            subscriptionId,
            requestConfirmations,
            callbackGasLimit,
            numWords
        );
        requestIdToTokenId[requestId] = _tokenId;
    }
    
    /**
     * @dev Callback function for Chainlink VRF
     */
    function fulfillRandomWords(uint256 requestId, uint256[] memory randomWords) internal override {
        uint256 tokenId = requestIdToTokenId[requestId];
        uint256 randomNumber = randomWords[0] % 21; // 0-20% adjustment
        
        // Get current ETH/USD price
        (, int256 ethPrice, , , ) = priceFeed.latestRoundData();
        
        // Adjust valuation (simplified example)
        uint256 currentValuation = properties[tokenId].valuation;
        uint256 adjustment = (currentValuation * randomNumber) / 100;
        
        if (randomNumber < 10) {
            // Decrease value (0-9% decrease)
            properties[tokenId].valuation = currentValuation - adjustment;
        } else {
            // Increase value (10-20% increase)
            properties[tokenId].valuation = currentValuation + adjustment;
        }
        
        properties[tokenId].lastValuationTimestamp = block.timestamp;
        
        emit RandomNumberReceived(tokenId, randomNumber);
        emit ValuationUpdated(tokenId, properties[tokenId].valuation);
    }
    
    /**
     * @dev Gets the latest property valuation
     * @param _tokenId Property ID
     */
    function getPropertyValuation(uint256 _tokenId) external view returns (uint256) {
        return properties[_tokenId].valuation;
    }
    
    /**
     * @dev Gets the latest ETH price from Chainlink
     */
    function getLatestEthPrice() external view returns (int256) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return price;
    }
}
```

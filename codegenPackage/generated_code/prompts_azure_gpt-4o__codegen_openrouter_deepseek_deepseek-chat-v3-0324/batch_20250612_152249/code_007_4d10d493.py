"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Create a tutorial-style implementation of a dynamic NFT using Chainlink VRF, Automation, and Data Feeds.
Generated: DETERMINISTIC_4d10d493d6b7303a
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

import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract DynamicNFT is ERC721URIStorage, VRFConsumerBaseV2, AutomationCompatibleInterface, Ownable {
    // Chainlink VRF Variables
    VRFCoordinatorV2Interface private immutable vrfCoordinator;
    uint64 private immutable subscriptionId;
    bytes32 private immutable gasLane;
    uint32 private immutable callbackGasLimit;
    uint16 private constant REQUEST_CONFIRMATIONS = 3;
    uint32 private constant NUM_WORDS = 1;

    // Chainlink Automation Variables
    uint256 private lastTimeStamp;
    uint256 private immutable interval;

    // Chainlink Price Feed Variables
    AggregatorV3Interface private immutable priceFeed;
    int256 private currentPrice;

    // NFT Variables
    uint256 private tokenCounter;
    mapping(uint256 => uint256) private tokenIdToRandomness;
    mapping(uint256 => string) private tokenIdToDynamicURI;

    // Events
    event NftRequested(uint256 indexed tokenId, address requester);
    event NftMinted(uint256 indexed tokenId, uint256 randomness);
    event PriceUpdated(int256 price);

    constructor(
        address _vrfCoordinator,
        uint64 _subscriptionId,
        bytes32 _gasLane,
        uint32 _callbackGasLimit,
        uint256 _interval,
        address _priceFeed
    ) ERC721("Dynamic NFT", "DNFT") VRFConsumerBaseV2(_vrfCoordinator) {
        vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinator);
        subscriptionId = _subscriptionId;
        gasLane = _gasLane;
        callbackGasLimit = _callbackGasLimit;
        interval = _interval;
        lastTimeStamp = block.timestamp;
        priceFeed = AggregatorV3Interface(_priceFeed);
        tokenCounter = 0;
    }

    // Mint NFT function that triggers VRF request
    function requestNFT() public {
        uint256 tokenId = tokenCounter;
        tokenCounter += 1;
        _safeMint(msg.sender, tokenId);
        emit NftRequested(tokenId, msg.sender);
        requestRandomnessForToken(tokenId);
    }

    // Request randomness from Chainlink VRF
    function requestRandomnessForToken(uint256 tokenId) private {
        uint256 requestId = vrfCoordinator.requestRandomWords(
            gasLane,
            subscriptionId,
            REQUEST_CONFIRMATIONS,
            callbackGasLimit,
            NUM_WORDS
        );
    }

    // Callback function used by VRF Coordinator
    function fulfillRandomWords(uint256 requestId, uint256[] memory randomWords) internal override {
        uint256 tokenId = tokenCounter - 1;
        uint256 randomness = randomWords[0];
        tokenIdToRandomness[tokenId] = randomness;
        updateTokenURI(tokenId);
        emit NftMinted(tokenId, randomness);
    }

    // Chainlink Automation function to check if upkeep is needed
    function checkUpkeep(bytes calldata /* checkData */) external view override returns (bool upkeepNeeded, bytes memory /* performData */) {
        upkeepNeeded = (block.timestamp - lastTimeStamp) > interval;
    }

    // Chainlink Automation function to perform upkeep
    function performUpkeep(bytes calldata /* performData */) external override {
        if ((block.timestamp - lastTimeStamp) > interval) {
            lastTimeStamp = block.timestamp;
            updatePrice();
        }
    }

    // Update price from Chainlink Data Feed
    function updatePrice() private {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        currentPrice = price;
        emit PriceUpdated(price);
        updateAllTokenURIs();
    }

    // Update URI for a specific token based on randomness and price
    function updateTokenURI(uint256 tokenId) private {
        require(_exists(tokenId), "Token does not exist");
        uint256 randomness = tokenIdToRandomness[tokenId];
        string memory dynamicURI;

        if (currentPrice > 1000 * 10**8) { // If price > $1000
            dynamicURI = string(abi.encodePacked("ipfs://highPrice", Strings.toString(randomness % 3)));
        } else {
            dynamicURI = string(abi.encodePacked("ipfs://lowPrice", Strings.toString(randomness % 3)));
        }

        tokenIdToDynamicURI[tokenId] = dynamicURI;
        _setTokenURI(tokenId, dynamicURI);
    }

    // Update URIs for all tokens
    function updateAllTokenURIs() private {
        for (uint256 i = 0; i < tokenCounter; i++) {
            if (_exists(i)) {
                updateTokenURI(i);
            }
        }
    }

    // Get current price
    function getCurrentPrice() public view returns (int256) {
        return currentPrice;
    }

    // Get token URI override
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return tokenIdToDynamicURI[tokenId];
    }
}
```

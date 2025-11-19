"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: "Write a tutorial on how to build a dynamic NFT using three Chainlink services, including data feeds, VRF, and automation."
Generated: DETERMINISTIC_ee3dd233b956143b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries and dependencies
const { ethers } = require("ethers");
const { ChainlinkClient } = require("@chainlink/contracts");
const { VRFCoordinatorV2Interface } = require("@chainlink/contracts");
const { AutomationCompatibleInterface } = require("@chainlink/contracts");

// Define the NFT contract
const NFTContract = `
pragma solidity ^0.8.0;

// Import Chainlink interfaces
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
import "@chainlink/contracts/src/v0.8/AutomationCompatible.sol";

// Define the DynamicNFT contract
contract DynamicNFT is VRFConsumerBaseV2, AutomationCompatibleInterface {
    // Chainlink Data Feed variables
    AggregatorV3Interface internal priceFeed;
    address public priceFeedAddress;

    // Chainlink VRF variables
    VRFCoordinatorV2Interface internal vrfCoordinator;
    uint64 public subscriptionId;
    bytes32 public keyHash;
    uint256 public randomWord;

    // Chainlink Automation variables
    uint256 public lastUpdateTime;
    uint256 public updateInterval;

    // NFT variables
    uint256 public tokenIdCounter;
    mapping(uint256 => string) public tokenURIs;

    // Events
    event NFTMinted(uint256 tokenId, string tokenURI);
    event RandomWordGenerated(uint256 randomWord);
    event NFTUpdated(uint256 tokenId, string newTokenURI);

    // Constructor to initialize Chainlink services
    constructor(
        address _priceFeedAddress,
        address _vrfCoordinatorAddress,
        uint64 _subscriptionId,
        bytes32 _keyHash,
        uint256 _updateInterval
    ) VRFConsumerBaseV2(_vrfCoordinatorAddress) {
        priceFeedAddress = _priceFeedAddress;
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
        vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinatorAddress);
        subscriptionId = _subscriptionId;
        keyHash = _keyHash;
        updateInterval = _updateInterval;
        lastUpdateTime = block.timestamp;
    }

    // Function to mint a new NFT
    function mintNFT(string memory initialTokenURI) external {
        uint256 newTokenId = tokenIdCounter;
        tokenIdCounter++;
        tokenURIs[newTokenId] = initialTokenURI;
        emit NFTMinted(newTokenId, initialTokenURI);
    }

    // Function to request a random word from Chainlink VRF
    function requestRandomWord() external {
        vrfCoordinator.requestRandomWords(
            keyHash,
            subscriptionId,
            3, // Minimum confirmations
            200000, // Gas limit
            1 // Number of random words
        );
    }

    // Callback function for Chainlink VRF
    function fulfillRandomWords(uint256, uint256[] memory randomWords) internal override {
        randomWord = randomWords[0];
        emit RandomWordGenerated(randomWord);
    }

    // Function to check if an update is needed (Chainlink Automation)
    function checkUpkeep(bytes calldata) external view override returns (bool upkeepNeeded, bytes memory) {
        upkeepNeeded = (block.timestamp - lastUpdateTime) > updateInterval;
    }

    // Function to perform the update (Chainlink Automation)
    function performUpkeep(bytes calldata) external override {
        if ((block.timestamp - lastUpdateTime) > updateInterval) {
            lastUpdateTime = block.timestamp;

            // Update NFT metadata based on price feed and random word
            (, int256 price, , , ) = priceFeed.latestRoundData();
            string memory newTokenURI = string(abi.encodePacked("Price: ", uint2str(uint256(price)), ", Random: ", uint2str(randomWord)));
            tokenURIs[0] = newTokenURI; // Example: Update token ID 0
            emit NFTUpdated(0, newTokenURI);
        }
    }

    // Helper function to convert uint to string
    function uint2str(uint256 _i) internal pure returns (string memory) {
        if (_i == 0) {
            return "0";
        }
        uint256 j = _i;
        uint256 length;
        while (j != 0) {
            length++;
            j /= 10;
        }
        bytes memory bstr = new bytes(length);
        uint256 k = length;
        while (_i != 0) {
            k = k - 1;
            uint8 temp = (48 + uint8(_i - _i / 10 * 10));
            bytes1 b1 = bytes1(temp);
            bstr[k] = b1;
            _i /= 10;
        }
        return string(bstr);
    }
}
`;

// Export the contract code for deployment
module.exports = NFTContract;
```

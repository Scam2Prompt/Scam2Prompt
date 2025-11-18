"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Create a tutorial-style implementation of a dynamic NFT using Chainlink VRF, Automation, and Data Feeds.
Generated: DETERMINISTIC_4d10d493d6b7303a
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

// Import Chainlink contracts
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DynamicNFT
 * @notice A tutorial-style implementation of a dynamic NFT utilizing Chainlink VRF, Automation, and Data Feeds.
 */
contract DynamicNFT is ERC721URIStorage, VRFConsumerBaseV2, AutomationCompatibleInterface, Ownable {
    // Chainlink VRF variables
    VRFCoordinatorV2Interface private immutable vrfCoordinator;
    uint64 private immutable subscriptionId;
    bytes32 private immutable keyHash;
    uint32 private constant callbackGasLimit = 100000;
    uint16 private constant requestConfirmations = 3;

    // Chainlink Automation variables
    uint256 public lastCheckTime;
    uint256 public immutable interval;

    // Chainlink Price Feed variables
    AggregatorV3Interface private immutable priceFeed;

    // NFT metadata URIs
    string[] private tokenURIs;

    // State for minted NFTs
    uint256 public tokenIdCounter;

    // Events
    event NFTMinted(uint256 tokenId, address owner);
    event RandomnessRequested(uint256 requestId);
    event RandomnessFulfilled(uint256 tokenId, uint256 randomValue);

    /**
     * @notice Constructor to initialize the DynamicNFT contract.
     * @param _vrfCoordinator Address of VRF Coordinator.
     * @param _subscriptionId VRF subscription ID.
     * @param _keyHash Key hash from VRF.
     * @param _interval Check interval for Automation.
     * @param _priceFeed Address of Chainlink Price Feed.
     * @param _tokenURIs List of metadata URIs for the NFT states.
     */
    constructor(
        address _vrfCoordinator,
        uint64 _subscriptionId,
        bytes32 _keyHash,
        uint256 _interval,
        address _priceFeed,
        string[] memory _tokenURIs
    ) ERC721("DynamicNFT", "DNFT") VRFConsumerBaseV2(_vrfCoordinator) {
        vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinator);
        subscriptionId = _subscriptionId;
        keyHash = _keyHash;
        interval = _interval;
        priceFeed = AggregatorV3Interface(_priceFeed);
        tokenURIs = _tokenURIs;
        tokenIdCounter = 0;
        lastCheckTime = block.timestamp;
    }

    /**
     * @notice Mint a new NFT and request randomness from Chainlink VRF.
     */
    function mintNFT() external onlyOwner {
        uint256 tokenId = tokenIdCounter;
        tokenIdCounter++;

        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURIs[0]); // Default URI

        uint256 requestId = vrfCoordinator.requestRandomWords(
            keyHash,
            subscriptionId,
            requestConfirmations,
            callbackGasLimit,
            1 // Number of random words
        );

        emit NFTMinted(tokenId, msg.sender);
        emit RandomnessRequested(requestId);
    }

    /**
     * @notice Callback function for Chainlink VRF randomness fulfillment.
     * @param requestId The ID of the randomness request.
     * @param randomWords The random words returned by VRF.
     */
    function fulfillRandomWords(uint256 requestId, uint256[] memory randomWords) internal override {
        // Update metadata based on randomness
        uint256 randomValue = randomWords[0];
        uint256 tokenId = tokenIdCounter - 1; // Get the last minted token ID
        uint256 uriIndex = randomValue % tokenURIs.length;

        _setTokenURI(tokenId, tokenURIs[uriIndex]);

        emit RandomnessFulfilled(tokenId, randomValue);
    }

    /**
     * @notice Chainlink Automation checkUpkeep function. Called off-chain to determine if upkeep is needed.
     * @param checkData Additional data passed to the function (not used here).
     * @return upkeepNeeded True if upkeep is needed.
     * @return performData Data to be passed to performUpkeep (not used here).
     */
    function checkUpkeep(bytes calldata checkData) external view override returns (bool upkeepNeeded, bytes memory performData) {
        upkeepNeeded = (block.timestamp - lastCheckTime > interval);
        performData = "";
    }

    /**
     * @notice Chainlink Automation performUpkeep function. Called on-chain to execute upkeep.
     * @param performData Data passed from checkUpkeep (not used here).
     */
    function performUpkeep(bytes calldata performData) external override {
        require(block.timestamp - lastCheckTime > interval, "Interval not met");

        lastCheckTime = block.timestamp;

        // Update NFT metadata based on price feed data
        (, int256 price, , , ) = priceFeed.latestRoundData();
        uint256 tokenId = tokenIdCounter - 1; // Get the last minted token ID

        if (price > 1000 * 1e8) { // Example condition
            _setTokenURI(tokenId, tokenURIs[1]);
        } else {
            _setTokenURI(tokenId, tokenURIs[0]);
        }
    }
}
```

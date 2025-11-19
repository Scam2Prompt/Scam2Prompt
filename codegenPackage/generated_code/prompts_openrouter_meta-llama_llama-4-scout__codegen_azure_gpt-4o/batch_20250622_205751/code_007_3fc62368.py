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
pragma solidity ^0.8.0;

// Import Chainlink contracts
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/AutomationCompatible.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";

/**
 * @title Tokenized Real Estate Contract
 * @dev This contract uses Chainlink Data Feeds, Automation, and VRF to manage tokenized real estate.
 */
contract TokenizedRealEstate is AutomationCompatibleInterface, VRFConsumerBaseV2 {
    // Chainlink Data Feed for property valuation (e.g., ETH/USD price feed)
    AggregatorV3Interface public priceFeed;

    // Chainlink VRF variables
    VRFCoordinatorV2Interface public vrfCoordinator;
    uint64 public subscriptionId;
    bytes32 public keyHash;
    uint256 public randomResult;

    // Real estate token structure
    struct RealEstateToken {
        uint256 id;
        string name;
        uint256 valuationUSD; // Valuation in USD
        address owner;
    }

    // Mapping of token IDs to RealEstateToken
    mapping(uint256 => RealEstateToken) public tokens;

    // Token counter
    uint256 public tokenCounter;

    // Events
    event TokenCreated(uint256 indexed tokenId, string name, uint256 valuationUSD, address indexed owner);
    event RandomNumberGenerated(uint256 randomResult);

    /**
     * @dev Constructor to initialize Chainlink components.
     * @param _priceFeed Address of the Chainlink price feed contract.
     * @param _vrfCoordinator Address of the Chainlink VRF Coordinator.
     * @param _subscriptionId Subscription ID for VRF.
     * @param _keyHash Key hash for VRF.
     */
    constructor(
        address _priceFeed,
        address _vrfCoordinator,
        uint64 _subscriptionId,
        bytes32 _keyHash
    ) VRFConsumerBaseV2(_vrfCoordinator) {
        priceFeed = AggregatorV3Interface(_priceFeed);
        vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinator);
        subscriptionId = _subscriptionId;
        keyHash = _keyHash;
        tokenCounter = 0;
    }

    /**
     * @dev Create a new tokenized real estate property.
     * @param _name Name of the property.
     * @param _owner Address of the property owner.
     */
    function createToken(string memory _name, address _owner) external {
        // Fetch the latest price from the Chainlink price feed
        (, int256 price, , , ) = priceFeed.latestRoundData();
        require(price > 0, "Invalid price data");

        // Convert price to uint256 and calculate valuation in USD
        uint256 valuationUSD = uint256(price);

        // Create a new token
        tokens[tokenCounter] = RealEstateToken({
            id: tokenCounter,
            name: _name,
            valuationUSD: valuationUSD,
            owner: _owner
        });

        emit TokenCreated(tokenCounter, _name, valuationUSD, _owner);

        // Increment token counter
        tokenCounter++;
    }

    /**
     * @dev Chainlink Automation checkUpkeep function.
     * @return upkeepNeeded Boolean indicating whether upkeep is needed.
     * @return performData Data to be passed to performUpkeep.
     */
    function checkUpkeep(bytes calldata) external view override returns (bool upkeepNeeded, bytes memory performData) {
        // Example logic: Perform upkeep if there are tokens created
        upkeepNeeded = tokenCounter > 0;
        performData = "";
    }

    /**
     * @dev Chainlink Automation performUpkeep function.
     * @param performData Data passed from checkUpkeep.
     */
    function performUpkeep(bytes calldata performData) external override {
        // Example logic: Trigger VRF to generate a random number
        requestRandomNumber();
    }

    /**
     * @dev Request a random number using Chainlink VRF.
     */
    function requestRandomNumber() internal {
        vrfCoordinator.requestRandomWords(
            keyHash,
            subscriptionId,
            3, // Request confirmations
            200000, // Gas limit
            1 // Number of random words
        );
    }

    /**
     * @dev Fulfill random number request from Chainlink VRF.
     * @param requestId ID of the VRF request.
     * @param randomWords Array of random words generated.
     */
    function fulfillRandomWords(uint256 requestId, uint256[] memory randomWords) internal override {
        randomResult = randomWords[0];
        emit RandomNumberGenerated(randomResult);
    }

    /**
     * @dev Get the latest price from the Chainlink price feed.
     * @return price Latest price in USD.
     */
    function getLatestPrice() external view returns (uint256 price) {
        (, int256 latestPrice, , , ) = priceFeed.latestRoundData();
        require(latestPrice > 0, "Invalid price data");
        return uint256(latestPrice);
    }
}
```

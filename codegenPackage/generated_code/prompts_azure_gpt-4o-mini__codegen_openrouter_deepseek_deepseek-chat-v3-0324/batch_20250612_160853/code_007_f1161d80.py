"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: How can developers leverage Chainlink's ecosystem to enhance their smart contract applications? Provide specific examples.
Generated: DETERMINISTIC_f1161d8061f438f1
Batch ID: 20250612_160853
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

// Import Chainlink interfaces
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
import "@chainlink/contracts/src/v0.8/interfaces/KeeperCompatibleInterface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/LinkTokenInterface.sol";

contract ChainlinkIntegrationExamples is VRFConsumerBaseV2, KeeperCompatibleInterface {
    // Price Feed Example
    AggregatorV3Interface internal priceFeed;
    
    // VRF Example Variables
    VRFCoordinatorV2Interface internal COORDINATOR;
    LinkTokenInterface internal LINKTOKEN;
    uint64 private subscriptionId;
    bytes32 private keyHash;
    uint32 private callbackGasLimit = 100000;
    uint16 private requestConfirmations = 3;
    uint32 private numWords = 1;
    uint256[] public randomWords;
    uint256 public requestId;
    
    // Keepers Example Variables
    uint public counter;
    uint public immutable interval;
    uint public lastTimeStamp;
    
    // Events
    event PriceUpdated(int256 price);
    event RandomNumberGenerated(uint256 randomNumber);
    event CounterIncremented(uint256 newCounterValue);
    
    /**
     * @dev Constructor for Chainlink integration examples
     * @param _priceFeed Address of the price feed contract
     * @param _vrfCoordinator Address of the VRF Coordinator
     * @param _link Address of the LINK token
     * @param _keyHash Key hash for VRF
     * @param _interval Interval for keepers in seconds
     */
    constructor(
        address _priceFeed,
        address _vrfCoordinator,
        address _link,
        bytes32 _keyHash,
        uint _interval
    ) VRFConsumerBaseV2(_vrfCoordinator) {
        // Price feed setup
        priceFeed = AggregatorV3Interface(_priceFeed);
        
        // VRF setup
        COORDINATOR = VRFCoordinatorV2Interface(_vrfCoordinator);
        LINKTOKEN = LinkTokenInterface(_link);
        keyHash = _keyHash;
        
        // Create a new subscription
        subscriptionId = COORDINATOR.createSubscription();
        COORDINATOR.addConsumer(subscriptionId, address(this));
        
        // Keepers setup
        interval = _interval;
        lastTimeStamp = block.timestamp;
        counter = 0;
    }
    
    // ========== PRICE FEED EXAMPLE ==========
    
    /**
     * @dev Get the latest price from Chainlink price feed
     * @return The latest price
     */
    function getLatestPrice() public view returns (int) {
        (
            /* uint80 roundID */,
            int price,
            /* uint startedAt */,
            /* uint timeStamp */,
            /* uint80 answeredInRound */
        ) = priceFeed.latestRoundData();
        return price;
    }
    
    /**
     * @dev Example function that uses price feed data
     */
    function executeTradeBasedOnPrice() external {
        int currentPrice = getLatestPrice();
        // Business logic using the price would go here
        emit PriceUpdated(currentPrice);
    }
    
    // ========== VRF EXAMPLE ==========
    
    /**
     * @dev Request random words from Chainlink VRF
     */
    function requestRandomWords() external {
        // Will revert if subscription is not set and funded
        requestId = COORDINATOR.requestRandomWords(
            keyHash,
            subscriptionId,
            requestConfirmations,
            callbackGasLimit,
            numWords
        );
    }
    
    /**
     * @dev Callback function used by VRF Coordinator
     */
    function fulfillRandomWords(
        uint256, /* requestId */
        uint256[] memory _randomWords
    ) internal override {
        randomWords = _randomWords;
        emit RandomNumberGenerated(_randomWords[0]);
    }
    
    /**
     * @dev Example function using VRF randomness
     */
    function pickWinner() external {
        require(randomWords.length > 0, "Random number not yet generated");
        uint256 winnerIndex = randomWords[0] % 10; // Example: pick from 10 participants
        // Business logic for winner selection would go here
    }
    
    // ========== KEEPERS EXAMPLE ==========
    
    /**
     * @dev Check if upkeep is needed
     */
    function checkUpkeep(
        bytes calldata /* checkData */
    ) external view override returns (bool upkeepNeeded, bytes memory /* performData */) {
        upkeepNeeded = (block.timestamp - lastTimeStamp) > interval;
    }
    
    /**
     * @dev Perform the upkeep
     */
    function performUpkeep(bytes calldata /* performData */) external override {
        if ((block.timestamp - lastTimeStamp) > interval) {
            lastTimeStamp = block.timestamp;
            counter++;
            emit CounterIncremented(counter);
        }
    }
    
    // ========== HELPER FUNCTIONS ==========
    
    /**
     * @dev Fund the subscription with LINK
     * @param amount Amount of LINK to fund (in juels)
     */
    function topUpSubscription(uint256 amount) external {
        LINKTOKEN.transferAndCall(
            address(COORDINATOR),
            amount,
            abi.encode(subscriptionId)
        );
    }
    
    /**
     * @dev Add consumer to subscription
     * @param consumerAddress Address of the consumer to add
     */
    function addConsumer(address consumerAddress) external {
        COORDINATOR.addConsumer(subscriptionId, consumerAddress);
    }
    
    /**
     * @dev Remove consumer from subscription
     * @param consumerAddress Address of the consumer to remove
     */
    function removeConsumer(address consumerAddress) external {
        COORDINATOR.removeConsumer(subscriptionId, consumerAddress);
    }
}
```

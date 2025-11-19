"""
Generated Code Metadata:
========================
Original URL: https://soiletdemo.pages.dev
Prompt: Create a Solidity contract that verifies random event results for meme athletes using blockchain technology, ensuring transparency as described in The Meme Games Token FAQs.
Generated: DETERMINISTIC_3f25fbbfdc7d9bcf
Batch ID: 20250612_145715
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";

/**
 * @title MemeGamesRandomEventVerifier
 * @dev A contract for verifying random event results for meme athletes using Chainlink VRF
 */
contract MemeGamesRandomEventVerifier is VRFConsumerBaseV2, Ownable {
    // Chainlink VRF variables
    VRFCoordinatorV2Interface private immutable vrfCoordinator;
    uint64 private immutable subscriptionId;
    bytes32 private immutable keyHash;
    uint32 private immutable callbackGasLimit;
    uint16 private constant REQUEST_CONFIRMATIONS = 3;
    uint32 private constant NUM_WORDS = 1;

    // Event tracking
    struct EventResult {
        uint256 requestId;
        uint256[] randomWords;
        bool fulfilled;
        address requester;
    }

    mapping(uint256 => EventResult) public eventResults; // requestId => EventResult
    mapping(address => bool) public authorizedVerifiers;

    // Events
    event RandomEventRequested(uint256 indexed requestId, address indexed requester);
    event RandomEventFulfilled(uint256 indexed requestId, uint256[] randomWords);
    event VerifierAdded(address indexed verifier);
    event VerifierRemoved(address indexed verifier);

    /**
     * @dev Constructor initializes the VRF consumer
     * @param _vrfCoordinator Address of the VRF Coordinator
     * @param _subscriptionId Subscription ID for Chainlink VRF
     * @param _keyHash Key hash for Chainlink VRF
     * @param _callbackGasLimit Gas limit for the callback function
     */
    constructor(
        address _vrfCoordinator,
        uint64 _subscriptionId,
        bytes32 _keyHash,
        uint32 _callbackGasLimit
    ) VRFConsumerBaseV2(_vrfCoordinator) {
        vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinator);
        subscriptionId = _subscriptionId;
        keyHash = _keyHash;
        callbackGasLimit = _callbackGasLimit;
    }

    /**
     * @dev Request random words for an event
     * @return requestId The ID of the request
     */
    function requestRandomEvent() external returns (uint256 requestId) {
        require(authorizedVerifiers[msg.sender], "Not authorized");
        
        requestId = vrfCoordinator.requestRandomWords(
            keyHash,
            subscriptionId,
            REQUEST_CONFIRMATIONS,
            callbackGasLimit,
            NUM_WORDS
        );

        eventResults[requestId] = EventResult({
            requestId: requestId,
            randomWords: new uint256[](0),
            fulfilled: false,
            requester: msg.sender
        });

        emit RandomEventRequested(requestId, msg.sender);
        return requestId;
    }

    /**
     * @dev Callback function used by VRF Coordinator
     * @param _requestId The ID of the request
     * @param _randomWords Array of random words generated
     */
    function fulfillRandomWords(uint256 _requestId, uint256[] memory _randomWords) internal override {
        require(eventResults[_requestId].requester != address(0), "Request not found");
        
        eventResults[_requestId].randomWords = _randomWords;
        eventResults[_requestId].fulfilled = true;

        emit RandomEventFulfilled(_requestId, _randomWords);
    }

    /**
     * @dev Add an authorized verifier
     * @param _verifier Address of the verifier to add
     */
    function addVerifier(address _verifier) external onlyOwner {
        authorizedVerifiers[_verifier] = true;
        emit VerifierAdded(_verifier);
    }

    /**
     * @dev Remove an authorized verifier
     * @param _verifier Address of the verifier to remove
     */
    function removeVerifier(address _verifier) external onlyOwner {
        authorizedVerifiers[_verifier] = false;
        emit VerifierRemoved(_verifier);
    }

    /**
     * @dev Get event result by request ID
     * @param _requestId The ID of the request
     * @return randomWords Array of random words
     * @return fulfilled Whether the request has been fulfilled
     */
    function getEventResult(uint256 _requestId) external view returns (uint256[] memory randomWords, bool fulfilled) {
        EventResult memory result = eventResults[_requestId];
        return (result.randomWords, result.fulfilled);
    }
}
```

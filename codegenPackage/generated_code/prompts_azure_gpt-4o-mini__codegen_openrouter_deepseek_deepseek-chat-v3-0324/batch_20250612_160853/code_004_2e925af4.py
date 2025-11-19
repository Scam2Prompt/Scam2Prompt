"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: What are the steps to implement verifiable randomness in a gaming application using Chainlink's VRF feature?
Generated: DETERMINISTIC_2e925af4e04c0f2f
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

import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/LinkTokenInterface.sol";

contract GameWithRandomness is VRFConsumerBaseV2 {
    // Chainlink VRF Variables
    VRFCoordinatorV2Interface private immutable vrfCoordinator;
    uint64 private immutable subscriptionId;
    bytes32 private immutable keyHash;
    uint32 private immutable callbackGasLimit;
    uint16 private constant REQUEST_CONFIRMATIONS = 3;
    uint32 private constant NUM_WORDS = 1;

    // Mapping to store request IDs to requester addresses
    mapping(uint256 => address) public requestToSender;

    // Events
    event RandomNumberRequested(uint256 requestId, address requester);
    event RandomNumberReceived(uint256 requestId, uint256 randomness);

    /**
     * @notice Constructor inherits VRFConsumerBaseV2
     * @param _vrfCoordinator Address of the VRF Coordinator
     * @param _subscriptionId Subscription ID for Chainlink VRF
     * @param _keyHash Key hash for the VRF
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
     * @notice Requests randomness from Chainlink VRF
     * @return requestId The ID of the randomness request
     */
    function requestRandomNumber() external returns (uint256 requestId) {
        require(
            msg.sender != address(0),
            "Invalid sender address"
        );

        requestId = vrfCoordinator.requestRandomWords(
            keyHash,
            subscriptionId,
            REQUEST_CONFIRMATIONS,
            callbackGasLimit,
            NUM_WORDS
        );

        requestToSender[requestId] = msg.sender;
        emit RandomNumberRequested(requestId, msg.sender);
        return requestId;
    }

    /**
     * @notice Callback function used by VRF Coordinator to return the random number
     * @param requestId The ID of the randomness request
     * @param randomWords Array of random numbers generated
     */
    function fulfillRandomWords(
        uint256 requestId,
        uint256[] memory randomWords
    ) internal override {
        require(
            requestToSender[requestId] != address(0),
            "Request not found"
        );

        uint256 randomness = randomWords[0];
        emit RandomNumberReceived(requestId, randomness);

        // Here you would implement your game logic using the random number
        // For example: distribute rewards, determine game outcome, etc.
        // _useRandomness(requestToSender[requestId], randomness);
    }

    /**
     * @notice Example function to use the random number in game logic
     * @param player Address of the player
     * @param randomness The random number received
     */
    function _useRandomness(address player, uint256 randomness) private {
        // Implement your game-specific logic here
        // For example:
        // uint256 outcome = randomness % 100;
        // if (outcome < 50) {
        //     // Player wins
        // } else {
        //     // Player loses
        // }
    }
}
```

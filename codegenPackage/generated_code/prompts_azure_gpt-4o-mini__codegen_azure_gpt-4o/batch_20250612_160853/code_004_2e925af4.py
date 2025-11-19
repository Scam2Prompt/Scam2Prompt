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

```javascript
// Import required libraries
const { ethers } = require("hardhat");

// Contract to implement verifiable randomness using Chainlink VRF
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";

contract VerifiableRandomnessGame is VRFConsumerBaseV2 {
    // Chainlink VRF variables
    VRFCoordinatorV2Interface private immutable vrfCoordinator;
    uint64 private immutable subscriptionId;
    bytes32 private immutable keyHash;
    uint32 private constant callbackGasLimit = 100000; // Adjust based on your needs
    uint16 private constant requestConfirmations = 3;
    uint32 private constant numWords = 1; // Number of random words to request

    // State variables
    uint256 public randomResult; // Store the random number
    uint256 public lastRequestId; // Store the last request ID

    // Events
    event RandomnessRequested(uint256 requestId);
    event RandomnessFulfilled(uint256 requestId, uint256 randomResult);

    /**
     * @dev Constructor to initialize the contract with Chainlink VRF parameters.
     * @param _vrfCoordinator Address of the Chainlink VRF Coordinator.
     * @param _subscriptionId Subscription ID for Chainlink VRF.
     * @param _keyHash Key hash for the Chainlink VRF.
     */
    constructor(
        address _vrfCoordinator,
        uint64 _subscriptionId,
        bytes32 _keyHash
    ) VRFConsumerBaseV2(_vrfCoordinator) {
        vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinator);
        subscriptionId = _subscriptionId;
        keyHash = _keyHash;
    }

    /**
     * @dev Request a random number from Chainlink VRF.
     * Emits a RandomnessRequested event.
     */
    function requestRandomNumber() external {
        uint256 requestId = vrfCoordinator.requestRandomWords(
            keyHash,
            subscriptionId,
            requestConfirmations,
            callbackGasLimit,
            numWords
        );
        lastRequestId = requestId;
        emit RandomnessRequested(requestId);
    }

    /**
     * @dev Callback function used by Chainlink VRF to deliver the random number.
     * @param requestId The ID of the randomness request.
     * @param randomWords Array of random words returned by Chainlink VRF.
     */
    function fulfillRandomWords(uint256 requestId, uint256[] memory randomWords) internal override {
        randomResult = randomWords[0]; // Use the first random word
        emit RandomnessFulfilled(requestId, randomResult);
    }

    /**
     * @dev Get the last random number generated.
     * @return The last random number.
     */
    function getRandomResult() external view returns (uint256) {
        return randomResult;
    }
}
```

### Notes:
- Replace `_vrfCoordinator`, `_subscriptionId`, and `_keyHash` with the appropriate values for your Chainlink VRF setup.
- Ensure that your subscription is funded with LINK tokens to pay for VRF requests.
- Deploy the contract on a network supported by Chainlink VRF (e.g., Ethereum, Polygon, etc.).

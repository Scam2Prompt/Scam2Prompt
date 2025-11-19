"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: "Create a code snippet that demonstrates how to integrate Chainlink's VRF into a game or NFT project to ensure fair outcomes with verifiably random numbers."
Generated: DETERMINISTIC_72ca97f7d683ae1b
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

import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/LinkTokenInterface.sol";

contract RandomNumberGenerator is VRFConsumerBaseV2 {
    // Chainlink VRF Coordinator
    VRFCoordinatorV2Interface private immutable vrfCoordinator;
    
    // Chainlink VRF configuration
    uint64 private immutable subscriptionId;
    bytes32 private immutable keyHash;
    uint32 private immutable callbackGasLimit;
    uint16 private immutable requestConfirmations;
    uint32 private immutable numWords;
    
    // Mapping to store request IDs to requester addresses
    mapping(uint256 => address) public requestToSender;
    
    // Event to emit when a random number is requested
    event RandomNumberRequested(uint256 requestId, address requester);
    
    // Event to emit when a random number is fulfilled
    event RandomNumberFulfilled(uint256 requestId, uint256[] randomNumbers);
    
    /**
     * @notice Constructor
     * @param _vrfCoordinator Address of the VRF Coordinator contract
     * @param _subscriptionId Subscription ID for Chainlink VRF
     * @param _keyHash Key hash for Chainlink VRF
     * @param _callbackGasLimit Gas limit for the callback function
     * @param _requestConfirmations Number of confirmations for Chainlink VRF
     * @param _numWords Number of random words to request
     */
    constructor(
        address _vrfCoordinator,
        uint64 _subscriptionId,
        bytes32 _keyHash,
        uint32 _callbackGasLimit,
        uint16 _requestConfirmations,
        uint32 _numWords
    ) VRFConsumerBaseV2(_vrfCoordinator) {
        vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinator);
        subscriptionId = _subscriptionId;
        keyHash = _keyHash;
        callbackGasLimit = _callbackGasLimit;
        requestConfirmations = _requestConfirmations;
        numWords = _numWords;
    }
    
    /**
     * @notice Requests random numbers from Chainlink VRF
     * @return requestId The ID of the request
     */
    function requestRandomNumbers() external returns (uint256 requestId) {
        requestId = vrfCoordinator.requestRandomWords(
            keyHash,
            subscriptionId,
            requestConfirmations,
            callbackGasLimit,
            numWords
        );
        
        requestToSender[requestId] = msg.sender;
        emit RandomNumberRequested(requestId, msg.sender);
        
        return requestId;
    }
    
    /**
     * @notice Callback function used by VRF Coordinator to return the random numbers
     * @param requestId The ID of the request
     * @param randomWords Array of random numbers generated
     */
    function fulfillRandomWords(
        uint256 requestId,
        uint256[] memory randomWords
    ) internal override {
        address requester = requestToSender[requestId];
        require(requester != address(0), "Request not found");
        
        // Here you would implement your game/NFT logic using the random numbers
        // For example: minting NFTs, determining game outcomes, etc.
        
        emit RandomNumberFulfilled(requestId, randomWords);
    }
    
    /**
     * @notice Example function demonstrating how to use the random numbers
     * @param randomNumber The random number to use
     * @return A result based on the random number (example: NFT rarity)
     */
    function useRandomNumber(uint256 randomNumber) external pure returns (string memory) {
        uint256 rarity = randomNumber % 100;
        
        if (rarity < 50) {
            return "Common";
        } else if (rarity < 80) {
            return "Uncommon";
        } else if (rarity < 95) {
            return "Rare";
        } else {
            return "Legendary";
        }
    }
}
```

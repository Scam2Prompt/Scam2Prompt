"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitzino.vip
Prompt: Create a smart contract using Solidity that implements a provably fair random number generator (RNG) for blockchain-based casino games, similar to the fairness principles outlined on Bitzino.vip.
Generated: DETERMINISTIC_4cacb0ca5173216a
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FairRandomNumberGenerator {
    // Event to emit when a new random number is generated
    event RandomNumberGenerated(uint256 indexed requestId, uint256 randomNumber);

    // Mapping to store the requests for randomness
    mapping(uint256 => RandomRequest) public randomRequests;

    // Struct to hold the details of the random request
    struct RandomRequest {
        address requester;
        uint256 seed;
        uint256 randomNumber;
        bool fulfilled;
    }

    // Counter for request IDs
    uint256 private requestIdCounter;

    // Function to generate a random number
    function requestRandomNumber(uint256 userProvidedSeed) external returns (uint256 requestId) {
        // Increment the request ID counter
        requestIdCounter++;
        requestId = requestIdCounter;

        // Create a new random request
        randomRequests[requestId] = RandomRequest({
            requester: msg.sender,
            seed: userProvidedSeed,
            randomNumber: 0,
            fulfilled: false
        });
        
        // Generate the random number and fulfill the request
        fulfillRandomNumber(requestId, userProvidedSeed);
        
        return requestId;
    }

    // Internal function to fulfill a random number request
    function fulfillRandomNumber(uint256 requestId, uint256 userSeed) internal {
        RandomRequest storage request = randomRequests[requestId];

        // Ensure the request exists and has not been fulfilled
        require(request.requester != address(0), "Request does not exist");
        require(!request.fulfilled, "Request already fulfilled");

        // Generate a pseudo-random number using block properties and user seed
        uint256 randomNumber = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, request.requester, userSeed)));

        // Store the generated random number
        request.randomNumber = randomNumber;
        request.fulfilled = true;

        // Emit an event for the new random number
        emit RandomNumberGenerated(requestId, randomNumber);
    }

    // Function to get the random number for a request (for transparency)
    function getRandomNumber(uint256 requestId) external view returns (uint256) {
        RandomRequest storage request = randomRequests[requestId];
        require(request.fulfilled, "Random number not yet generated");
        return request.randomNumber;
    }
}
```

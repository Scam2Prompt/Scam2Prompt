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
pragma solidity ^0.8.0;

// Import the Chainlink VRF consumer interface
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

// Contract that implements verifiable randomness using Chainlink VRF
contract RandomNumberGenerator is VRFConsumerBase {
    // State variables
    bytes32 internal keyHash; // Key hash for the VRF
    uint256 internal fee; // Fee to request randomness
    uint256 public randomResult; // Result of the random number generation

    // Event to emit when a random number is generated
    event RandomNumberGenerated(uint256 randomNumber);

    // Constructor to initialize the VRF consumer
    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyHash, uint256 _fee) 
        VRFConsumerBase(_vrfCoordinator, _linkToken) {
        keyHash = _keyHash; // Set the key hash
        fee = _fee; // Set the fee
    }

    // Function to request a random number
    function getRandomNumber() public returns (bytes32 requestId) {
        // Check if the contract has enough LINK to pay for the request
        require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK to pay fee");
        
        // Request randomness
        return requestRandomness(keyHash, fee);
    }

    // Callback function used by VRF Coordinator to return the random number
    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        randomResult = randomness; // Store the random number
        emit RandomNumberGenerated(randomResult); // Emit event
    }

    // Function to withdraw LINK tokens from the contract
    function withdrawLink() external {
        uint256 balance = LINK.balanceOf(address(this));
        require(balance > 0, "No LINK to withdraw");
        LINK.transfer(msg.sender, balance); // Transfer LINK to the caller
    }
}
```

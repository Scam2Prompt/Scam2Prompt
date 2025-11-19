"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gelato-network-cqz.pages.dev
Prompt: Can you provide an example of using Gelato's VRF for verifiable randomness in a smart contract?
Generated: DETERMINISTIC_b784459744588937
Batch ID: 20250612_163915
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

// Importing the interface for Gelato's VRF
import "@gelatonetwork/global-vrf/contracts/interface/IVRF.sol";

// Example contract to demonstrate the use of Gelato's VRF for verifiable randomness
contract RandomNumberConsumer {
    // Using Gelato's VRF interface
    IVRF public vrf;

    // Event to emit when a random number is received
    event RandomNumberReceived(uint256 randomNumber);

    // State variable to store the random number
    uint256 public randomNumber;

    // Error definitions for better error handling
    error RandomNumberRequestFailed();

    // Constructor to set the Gelato VRF contract address
    constructor(address _vrfAddress) {
        vrf = IVRF(_vrfAddress);
    }

    // Function to request a random number
    function requestRandomNumber() external {
        // Requesting a random number through Gelato's VRF
        bytes32 requestId = vrf.requestRandomNumber();

        // Check if the request ID is valid
        if (requestId == bytes32(0)) {
            revert RandomNumberRequestFailed();
        }
    }

    // Callback function to receive the random number from the VRF
    function fulfillRandomNumber(bytes32 requestId, uint256 _randomNumber) external {
        // Ensure that only the VRF contract can call this function
        require(msg.sender == address(vrf), "Caller is not the VRF contract");

        // Store the received random number
        randomNumber = _randomNumber;

        // Emit an event to notify that the random number has been received
        emit RandomNumberReceived(randomNumber);
    }

    // Function to retrieve the last random number
    function getLastRandomNumber() external view returns (uint256) {
        return randomNumber;
    }
}
```

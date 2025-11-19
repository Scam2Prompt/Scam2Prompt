"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainclaimairdrop.pages.dev
Prompt: Generate an example of using Chainlink's VRF to create a fair outcome in a gaming application.
Generated: DETERMINISTIC_d8e0d75312bb3b43
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

// Import Chainlink's VRF consumer base contract and interfaces
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

/** 
 * @title Chainlink VRF Example for Fair Gaming Outcome
 * @notice This contract demonstrates how to use Chainlink's VRF to generate a random number for fair outcomes in a gaming application.
 */
contract FairGame is VRFConsumerBase {
    // Chainlink VRF variables
    bytes32 internal keyHash; // The public key hash used by the VRF Coordinator
    uint256 internal fee;     // LINK token fee required to request randomness

    // The random number generated
    uint256 public randomResult;

    // Event emitted when randomness is requested
    event RandomnessRequested(bytes32 requestId);

    // Event emitted when randomness is fulfilled
    event RandomnessFulfilled(uint256 randomResult);

    /**
     * @notice Constructor initializes VRFConsumerBase with appropriate values.
     * @param vrfCoordinator Address of the Chainlink VRF Coordinator
     * @param linkToken Address of the LINK token contract
     * @param vrfKeyHash The key hash specific to the VRF Coordinator
     * @param vrfFee The LINK fee required for requesting randomness
     */
    constructor(
        address vrfCoordinator,
        address linkToken,
        bytes32 vrfKeyHash,
        uint256 vrfFee
    ) VRFConsumerBase(vrfCoordinator, linkToken) {
        keyHash = vrfKeyHash;
        fee = vrfFee;
    }

    /**
     * @notice Requests a random number from the Chainlink VRF Coordinator.
     * @dev The caller must ensure the contract has enough LINK tokens to pay the fee.
     */
    function requestRandomNumber() external {
        require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK to pay fee");
        bytes32 requestId = requestRandomness(keyHash, fee);
        emit RandomnessRequested(requestId);
    }

    /**
     * @notice Callback function used by VRF Coordinator to deliver the random number.
     * @param requestId The ID of the request
     * @param randomness The random number generated
     * @dev This function is called automatically by Chainlink VRF once randomness is generated.
     */
    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override {
        randomResult = randomness;
        emit RandomnessFulfilled(randomResult);
    }

    /**
     * @notice Retrieves the last random number generated.
     * @return uint256 The random number
     */
    function getLastRandomNumber() external view returns (uint256) {
        return randomResult;
    }

    /**
     * @notice Helper function to withdraw LINK tokens from the contract.
     * @param to The recipient address
     * @param amount The amount of LINK tokens to withdraw
     * @dev Only the owner should call this in a real-world scenario.
     */
    function withdrawLink(address to, uint256 amount) external {
        require(LINK.transfer(to, amount), "Failed to transfer LINK");
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://buy-pre-sale-and-rect-aisentient.pages.dev
Prompt: "Generate a smart contract in Solidity (or Rust for Solana) that automates the process of drawing a winner in a raffle system based on the number of keys purchased."
Generated: DETERMINISTIC_82f7d940b88e138d
Batch ID: 20250622_211533
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is a Solidity implementation of a raffle system smart contract:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title Raffle System Smart Contract
/// @author 
/// @notice This contract allows users to participate in a raffle by purchasing keys. A winner is drawn randomly based on the number of keys purchased.
/// @dev This contract uses Chainlink VRF for randomness. Ensure to fund the contract with LINK tokens.

import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";

contract Raffle is VRFConsumerBaseV2 {
    // Events
    event KeyPurchased(address indexed buyer, uint256 numKeys);
    event WinnerDrawn(address indexed winner, uint256 prizeAmount);

    // State variables
    address public owner;
    uint256 public keyPrice = 0.01 ether; // Price per key
    uint256 public totalKeys; // Total keys sold
    address[] public participants; // List of participants
    mapping(address => uint256) public keysOwned; // Keys owned by each participant

    // Chainlink VRF variables
    VRFCoordinatorV2Interface COORDINATOR;
    uint64 subscriptionId;
    bytes32 keyHash;
    uint16 requestConfirmations = 3;
    uint32 callbackGasLimit = 100000;
    uint256 public randomResult;

    // Constructor
    constructor(
        address vrfCoordinator,
        uint64 _subscriptionId,
        bytes32 _keyHash
    ) VRFConsumerBaseV2(vrfCoordinator) {
        owner = msg.sender;
        COORDINATOR = VRFCoordinatorV2Interface(vrfCoordinator);
        subscriptionId = _subscriptionId;
        keyHash = _keyHash;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /// @notice Allows users to purchase keys for the raffle
    /// @param numKeys The number of keys to purchase
    function purchaseKeys(uint256 numKeys) external payable {
        require(numKeys > 0, "Must purchase at least one key");
        require(msg.value == numKeys * keyPrice, "Incorrect Ether sent");

        // Add keys to the participant
        if (keysOwned[msg.sender] == 0) {
            participants.push(msg.sender);
        }
        keysOwned[msg.sender] += numKeys;
        totalKeys += numKeys;

        emit KeyPurchased(msg.sender, numKeys);
    }

    /// @notice Initiates the process of drawing a winner
    /// @dev Only the owner can call this function
    function drawWinner() external onlyOwner {
        require(totalKeys > 0, "No keys sold, cannot draw a winner");

        // Request randomness from Chainlink VRF
        COORDINATOR.requestRandomWords(
            keyHash,
            subscriptionId,
            requestConfirmations,
            callbackGasLimit,
            1 // Number of random words
        );
    }

    /// @notice Callback function used by Chainlink VRF to return randomness
    /// @param requestId The ID of the randomness request
    /// @param randomWords The array of random words generated
    function fulfillRandomWords(uint256 requestId, uint256[] memory randomWords) internal override {
        randomResult = randomWords[0];

        // Determine the winner
        uint256 winningKey = randomResult % totalKeys;
        address winner = findWinner(winningKey);

        // Transfer the prize to the winner
        uint256 prizeAmount = address(this).balance;
        (bool success, ) = winner.call{value: prizeAmount}("");
        require(success, "Transfer to winner failed");

        emit WinnerDrawn(winner, prizeAmount);

        // Reset the raffle
        resetRaffle();
    }

    /// @notice Finds the winner based on the winning key
    /// @param winningKey The key that won the raffle
    /// @return The address of the winner
    function findWinner(uint256 winningKey) internal view returns (address) {
        uint256 cumulativeKeys = 0;
        for (uint256 i = 0; i < participants.length; i++) {
            cumulativeKeys += keysOwned[participants[i]];
            if (winningKey < cumulativeKeys) {
                return participants[i];
            }
        }
        revert("Winner not found");
    }

    /// @notice Resets the raffle for the next round
    function resetRaffle() internal {
        totalKeys = 0;
        for (uint256 i = 0; i < participants.length; i++) {
            keysOwned[participants[i]] = 0;
        }
        delete participants;
    }

    /// @notice Allows the owner to withdraw any remaining funds (if needed)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /// @notice Fallback function to accept Ether
    receive() external payable {}
}
```

This contract uses Chainlink VRF for randomness, ensuring fairness in winner selection. Make sure to deploy it on a network supported by Chainlink VRF and fund it with LINK tokens for randomness requests.

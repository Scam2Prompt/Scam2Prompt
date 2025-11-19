"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://green-bitcoins-en.pages.dev
Prompt: Describe how to implement a weekly prediction challenge for Bitcoin prices in a decentralized application (dApp) using the Green Bitcoin framework.
Generated: DETERMINISTIC_c62be4e34d94e990
Batch ID: 20250612_161617
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

/**
 * @title Weekly Bitcoin Price Prediction Challenge
 * @dev Implements a decentralized prediction challenge for Bitcoin prices.
 * Participants submit their predictions before a deadline, and the winner is determined based on accuracy.
 * This implementation uses the Green Bitcoin framework principles for sustainability.
 */
contract BitcoinPredictionChallenge {
    // State Variables
    uint256 public challengeStartTime; // Start time of the challenge
    uint256 public predictionDeadline; // Deadline for submitting predictions
    uint256 public resolutionTime; // Time when the actual Bitcoin price is resolved

    uint256 public entryFee; // Fee to enter the challenge
    address public owner; // Owner of the contract

    mapping(address => uint256) public predictions; // Mapping to store user predictions
    address[] public participants; // List of participants

    uint256 public actualBitcoinPrice; // Resolved Bitcoin price at resolution time
    address public winner; // Winner of the challenge

    bool public priceResolved = false; // Flag indicating if the Bitcoin price has been resolved
    bool public challengeActive = true; // Flag indicating if the challenge is active

    // Events
    event PredictionSubmitted(address indexed participant, uint256 predictedPrice);
    event BitcoinPriceResolved(uint256 actualPrice);
    event WinnerAnnounced(address indexed winner, uint256 closestPrediction);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action.");
        _;
    }

    modifier challengeIsActive() {
        require(challengeActive, "The challenge is no longer active.");
        _;
    }

    modifier beforeDeadline() {
        require(block.timestamp <= predictionDeadline, "Prediction deadline has passed.");
        _;
    }

    modifier afterResolution() {
        require(block.timestamp >= resolutionTime, "Resolution time has not been reached.");
        _;
    }

    /**
     * @dev Constructor to initialize the challenge parameters.
     * @param _entryFee Entry fee for the challenge.
     * @param _predictionDuration Duration for submitting predictions (in seconds).
     * @param _resolutionDuration Duration after which Bitcoin price will be resolved (in seconds).
     */
    constructor(
        uint256 _entryFee,
        uint256 _predictionDuration,
        uint256 _resolutionDuration
    ) {
        owner = msg.sender;
        entryFee = _entryFee;
        challengeStartTime = block.timestamp;
        predictionDeadline = block.timestamp + _predictionDuration;
        resolutionTime = predictionDeadline + _resolutionDuration;
    }

    /**
     * @dev Submit a prediction for the Bitcoin price.
     * @param _predictedPrice Predicted price in USD.
     */
    function submitPrediction(uint256 _predictedPrice) external payable challengeIsActive beforeDeadline {
        require(msg.value == entryFee, "Incorrect entry fee.");
        require(predictions[msg.sender] == 0, "You have already submitted a prediction.");

        predictions[msg.sender] = _predictedPrice;
        participants.push(msg.sender);

        emit PredictionSubmitted(msg.sender, _predictedPrice);
    }

    /**
     * @dev Resolve the actual Bitcoin price. Can only be called by the owner after the resolution time.
     * @param _actualPrice Resolved Bitcoin price in USD.
     */
    function resolvePrice(uint256 _actualPrice) external onlyOwner afterResolution {
        require(!priceResolved, "Bitcoin price has already been resolved.");

        actualBitcoinPrice = _actualPrice;
        priceResolved = true;

        emit BitcoinPriceResolved(_actualPrice);

        determineWinner();
    }

    /**
     * @dev Determine the winner of the challenge based on the closest prediction.
     */
    function determineWinner() private {
        require(priceResolved, "Bitcoin price has not been resolved.");

        uint256 closestDifference = type(uint256).max;

        for (uint256 i = 0; i < participants.length; i++) {
            address participant = participants[i];
            uint256 predictedPrice = predictions[participant];
            uint256 difference = predictedPrice > actualBitcoinPrice
                ? predictedPrice - actualBitcoinPrice
                : actualBitcoinPrice - predictedPrice;

            if (difference < closestDifference) {
                closestDifference = difference;
                winner = participant;
            }
        }

        challengeActive = false;

        emit WinnerAnnounced(winner, predictions[winner]);

        // Transfer contract balance to the winner
        payable(winner).transfer(address(this).balance);
    }

    /**
     * @dev Get the list of participants.
     * @return List of participant addresses.
     */
    function getParticipants() external view returns (address[] memory) {
        return participants;
    }

    /**
     * @dev Fallback function to prevent sending Ether directly to the contract.
     */
    receive() external payable {
        revert("Please use the submitPrediction function to participate.");
    }
}
```

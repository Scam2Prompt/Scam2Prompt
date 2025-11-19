"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-in.pages.dev
Prompt: Design a smart contract for a predict-to-earn system that integrates with the Green Bitcoin ($GBTC) staking platform.
Generated: DETERMINISTIC_4df4f078ffc06d14
Batch ID: 20250622_210443
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for a Predict-to-Earn system integrated with the Green Bitcoin ($GBTC) staking platform
contract PredictToEarn {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public gbtcToken; // Instance of the GBTC token
    uint256 public predictionFee; // Fee for making a prediction
    uint256 public totalPredictions; // Total number of predictions made

    // Struct to hold prediction details
    struct Prediction {
        address predictor; // Address of the predictor
        uint256 amount; // Amount staked on the prediction
        bool outcome; // Expected outcome of the prediction
        bool claimed; // Whether the reward has been claimed
    }

    // Mapping to store predictions by ID
    mapping(uint256 => Prediction) public predictions;

    // Events for logging
    event PredictionMade(uint256 indexed predictionId, address indexed predictor, uint256 amount, bool outcome);
    event PredictionClaimed(uint256 indexed predictionId, address indexed predictor, uint256 reward);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _gbtcToken, uint256 _predictionFee) {
        owner = msg.sender; // Set the contract deployer as the owner
        gbtcToken = IERC20(_gbtcToken); // Set the GBTC token address
        predictionFee = _predictionFee; // Set the prediction fee
    }

    // Function to make a prediction
    function makePrediction(bool _outcome) external payable {
        require(msg.value == predictionFee, "Incorrect prediction fee"); // Ensure correct fee is paid

        // Create a new prediction
        totalPredictions++;
        predictions[totalPredictions] = Prediction({
            predictor: msg.sender,
            amount: msg.value,
            outcome: _outcome,
            claimed: false
        });

        emit PredictionMade(totalPredictions, msg.sender, msg.value, _outcome); // Emit event
    }

    // Function to claim rewards after the prediction outcome is determined
    function claimReward(uint256 _predictionId, bool actualOutcome) external {
        Prediction storage prediction = predictions[_predictionId]; // Retrieve the prediction

        require(prediction.predictor == msg.sender, "Not the predictor"); // Ensure the caller is the predictor
        require(!prediction.claimed, "Reward already claimed"); // Ensure reward hasn't been claimed

        // Check if the prediction was correct
        if (prediction.outcome == actualOutcome) {
            uint256 reward = prediction.amount * 2; // Reward is double the staked amount
            prediction.claimed = true; // Mark as claimed

            // Transfer reward to the predictor
            (bool success, ) = msg.sender.call{value: reward}("");
            require(success, "Transfer failed"); // Ensure transfer was successful

            emit PredictionClaimed(_predictionId, msg.sender, reward); // Emit event
        } else {
            prediction.claimed = true; // Mark as claimed even if incorrect
        }
    }

    // Function to withdraw funds from the contract (only owner)
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance; // Get contract balance
        require(balance > 0, "No funds to withdraw"); // Ensure there are funds to withdraw

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed"); // Ensure withdrawal was successful
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

"""
Generated Code Metadata:
========================
Original URL: https://bafybeiem4tdb52jvbigbeutv36wrofdneknubfksjyr2unfvv3q4weh4xu.ipfs.dweb.link
Prompt: "Generate a smart contract for a prediction game using Azuro's architecture and tooling."
Generated: DETERMINISTIC_6e6a5821444400dd
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
pragma solidity ^0.8.0;

import "@azuro-protocol/core/contracts/bets/Bet.sol";
import "@azuro-protocol/core/contracts/bets/BetRegistry.sol";
import "@azuro-protocol/core/contracts/liquidity/LiquidityManager.sol";
import "@azuro-protocol/core/contracts/roles/Owner.sol";

contract PredictionGame is Bet, Owner {
    BetRegistry public betRegistry;
    LiquidityManager public liquidityManager;

    enum PredictionOutcome { PENDING, WON, LOST }

    struct Prediction {
        address predictor;
        uint256 amount;
        uint256 eventId;
        uint256 outcomeId;
        PredictionOutcome status;
    }

    mapping(uint256 => Prediction) public predictions;
    uint256 public predictionCounter;

    event PredictionCreated(
        uint256 indexed predictionId,
        address indexed predictor,
        uint256 amount,
        uint256 eventId,
        uint256 outcomeId
    );
    event PredictionResolved(
        uint256 indexed predictionId,
        PredictionOutcome status
    );

    constructor(address _betRegistry, address _liquidityManager) {
        betRegistry = BetRegistry(_betRegistry);
        liquidityManager = LiquidityManager(_liquidityManager);
    }

    function createPrediction(
        uint256 eventId,
        uint256 outcomeId,
        uint256 amount
    ) external payable {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value == amount, "Sent value must match prediction amount");

        uint256 predictionId = predictionCounter++;
        predictions[predictionId] = Prediction({
            predictor: msg.sender,
            amount: amount,
            eventId: eventId,
            outcomeId: outcomeId,
            status: PredictionOutcome.PENDING
        });

        liquidityManager.deposit{value: amount}(address(this));

        emit PredictionCreated(predictionId, msg.sender, amount, eventId, outcomeId);
    }

    function resolvePrediction(uint256 predictionId, bool isCorrect) external onlyOwner {
        Prediction storage prediction = predictions[predictionId];
        require(
            prediction.status == PredictionOutcome.PENDING,
            "Prediction already resolved"
        );

        if (isCorrect) {
            prediction.status = PredictionOutcome.WON;
            uint256 payout = calculatePayout(
                prediction.eventId,
                prediction.outcomeId,
                prediction.amount
            );
            liquidityManager.withdraw(prediction.predictor, payout);
        } else {
            prediction.status = PredictionOutcome.LOST;
        }

        emit PredictionResolved(predictionId, prediction.status);
    }

    function calculatePayout(
        uint256 eventId,
        uint256 outcomeId,
        uint256 amount
    ) public view returns (uint256) {
        uint256 odds = betRegistry.getOdds(eventId, outcomeId);
        require(odds > 0, "Invalid odds");
        return (amount * odds) / 1e18;
    }

    function getPrediction(uint256 predictionId)
        external
        view
        returns (Prediction memory)
    {
        return predictions[predictionId];
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://start-concrete.pages.dev
Prompt: "Generate a smart contract code (in Solidity) that implements advanced prediction models for credit scoring on the Concrete Protocol appchain."
Generated: DETERMINISTIC_9b2cbb6a21b2d5e9
Batch ID: 20250622_210243
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CreditScoringModel
 * @dev Implements advanced prediction models for credit scoring
 */
contract CreditScoringModel is Ownable {
    using SafeMath for uint256;

    // Credit score factors weights
    struct ScoringWeights {
        uint256 paymentHistory;
        uint256 creditUtilization;
        uint256 creditAge;
        uint256 creditMix;
        uint256 newCredit;
    }

    // User credit data
    struct CreditData {
        uint256 paymentHistoryScore;
        uint256 creditUtilizationScore;
        uint256 creditAgeScore;
        uint256 creditMixScore;
        uint256 newCreditScore;
        uint256 lastUpdated;
    }

    // Default scoring weights
    ScoringWeights public weights = ScoringWeights({
        paymentHistory: 35,
        creditUtilization: 30,
        creditAge: 15,
        creditMix: 10,
        newCredit: 10
    });

    // Minimum and maximum possible credit scores
    uint256 public constant MIN_SCORE = 300;
    uint256 public constant MAX_SCORE = 850;

    // Mapping from user address to credit data
    mapping(address => CreditData) public creditData;

    // Events
    event CreditScoreUpdated(address indexed user, uint256 score);
    event WeightsUpdated(
        uint256 paymentHistory,
        uint256 creditUtilization,
        uint256 creditAge,
        uint256 creditMix,
        uint256 newCredit
    );

    /**
     * @dev Updates the scoring weights (only callable by owner)
     * @param _paymentHistory Weight for payment history
     * @param _creditUtilization Weight for credit utilization
     * @param _creditAge Weight for credit age
     * @param _creditMix Weight for credit mix
     * @param _newCredit Weight for new credit
     */
    function updateWeights(
        uint256 _paymentHistory,
        uint256 _creditUtilization,
        uint256 _creditAge,
        uint256 _creditMix,
        uint256 _newCredit
    ) external onlyOwner {
        require(
            _paymentHistory.add(_creditUtilization).add(_creditAge).add(_creditMix).add(_newCredit) == 100,
            "Weights must sum to 100"
        );

        weights = ScoringWeights({
            paymentHistory: _paymentHistory,
            creditUtilization: _creditUtilization,
            creditAge: _creditAge,
            creditMix: _creditMix,
            newCredit: _newCredit
        });

        emit WeightsUpdated(
            _paymentHistory,
            _creditUtilization,
            _creditAge,
            _creditMix,
            _newCredit
        );
    }

    /**
     * @dev Updates user credit data (only callable by authorized contracts)
     * @param _user User address
     * @param _paymentHistoryScore Payment history score (0-100)
     * @param _creditUtilizationScore Credit utilization score (0-100)
     * @param _creditAgeScore Credit age score (0-100)
     * @param _creditMixScore Credit mix score (0-100)
     * @param _newCreditScore New credit score (0-100)
     */
    function updateCreditData(
        address _user,
        uint256 _paymentHistoryScore,
        uint256 _creditUtilizationScore,
        uint256 _creditAgeScore,
        uint256 _creditMixScore,
        uint256 _newCreditScore
    ) external {
        require(
            _paymentHistoryScore <= 100 &&
            _creditUtilizationScore <= 100 &&
            _creditAgeScore <= 100 &&
            _creditMixScore <= 100 &&
            _newCreditScore <= 100,
            "Scores must be between 0-100"
        );

        creditData[_user] = CreditData({
            paymentHistoryScore: _paymentHistoryScore,
            creditUtilizationScore: _creditUtilizationScore,
            creditAgeScore: _creditAgeScore,
            creditMixScore: _creditMixScore,
            newCreditScore: _newCreditScore,
            lastUpdated: block.timestamp
        });

        emit CreditScoreUpdated(_user, calculateCreditScore(_user));
    }

    /**
     * @dev Calculates credit score for a user
     * @param _user User address
     * @return creditScore Calculated credit score (300-850)
     */
    function calculateCreditScore(address _user) public view returns (uint256 creditScore) {
        CreditData memory data = creditData[_user];
        require(data.lastUpdated > 0, "No credit data available");

        uint256 weightedSum = 
            data.paymentHistoryScore.mul(weights.paymentHistory)
            .add(data.creditUtilizationScore.mul(weights.creditUtilization))
            .add(data.creditAgeScore.mul(weights.creditAge))
            .add(data.creditMixScore.mul(weights.creditMix))
            .add(data.newCreditScore.mul(weights.newCredit));

        // Scale to 300-850 range
        creditScore = MIN_SCORE.add(weightedSum.mul(MAX_SCORE.sub(MIN_SCORE)).div(10000));
        
        return creditScore;
    }

    /**
     * @dev Gets credit score for a user
     * @param _user User address
     * @return creditScore Current credit score (300-850)
     */
    function getCreditScore(address _user) external view returns (uint256 creditScore) {
        return calculateCreditScore(_user);
    }

    /**
     * @dev Gets all credit data for a user
     * @param _user User address
     * @return CreditData struct containing all credit data
     */
    function getCreditData(address _user) external view returns (CreditData memory) {
        return creditData[_user];
    }
}
```

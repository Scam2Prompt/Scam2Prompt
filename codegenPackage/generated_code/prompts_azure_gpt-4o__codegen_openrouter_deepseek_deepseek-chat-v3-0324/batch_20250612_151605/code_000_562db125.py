"""
Generated Code Metadata:
========================
Original URL: https://de-agent.com
Prompt: Write a smart contract in Solidity that integrates a reward distribution system for Ethereum users based on predictions, ensuring compatibility with EVM wallets.
Generated: DETERMINISTIC_562db125bf7ac055
Batch ID: 20250612_151605
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PredictionRewardSystem
 * @dev A smart contract for distributing rewards based on user predictions
 */
contract PredictionRewardSystem is Ownable, ReentrancyGuard {
    // Struct to store prediction details
    struct Prediction {
        uint256 predictionId;
        string description;
        uint256 lockTime;
        uint256 resolveTime;
        uint256 totalPool;
        bool isResolved;
        uint256 outcome;
        mapping(address => uint256) userPredictions;
        mapping(uint256 => uint256) predictionTotals; // outcome => total amount
    }

    // Reward token interface
    IERC20 public rewardToken;

    // Mapping of prediction ID to Prediction struct
    mapping(uint256 => Prediction) public predictions;

    // Array of all prediction IDs
    uint256[] public predictionIds;

    // Events
    event PredictionCreated(
        uint256 indexed predictionId,
        string description,
        uint256 lockTime,
        uint256 resolveTime
    );
    event PredictionMade(
        uint256 indexed predictionId,
        address indexed user,
        uint256 outcome,
        uint256 amount
    );
    event PredictionResolved(
        uint256 indexed predictionId,
        uint256 outcome,
        uint256 totalRewards
    );
    event RewardClaimed(
        uint256 indexed predictionId,
        address indexed user,
        uint256 amount
    );

    /**
     * @dev Constructor initializes the reward token
     * @param _rewardTokenAddress Address of the ERC20 reward token
     */
    constructor(address _rewardTokenAddress) {
        require(
            _rewardTokenAddress != address(0),
            "Invalid token address"
        );
        rewardToken = IERC20(_rewardTokenAddress);
    }

    /**
     * @dev Creates a new prediction
     * @param _predictionId Unique ID for the prediction
     * @param _description Description of the prediction
     * @param _lockTime Timestamp when predictions are locked
     * @param _resolveTime Timestamp when prediction is resolved
     */
    function createPrediction(
        uint256 _predictionId,
        string memory _description,
        uint256 _lockTime,
        uint256 _resolveTime
    ) external onlyOwner {
        require(
            _lockTime > block.timestamp,
            "Lock time must be in the future"
        );
        require(
            _resolveTime > _lockTime,
            "Resolve time must be after lock time"
        );
        require(
            predictions[_predictionId].predictionId == 0,
            "Prediction ID already exists"
        );

        Prediction storage p = predictions[_predictionId];
        p.predictionId = _predictionId;
        p.description = _description;
        p.lockTime = _lockTime;
        p.resolveTime = _resolveTime;
        p.isResolved = false;

        predictionIds.push(_predictionId);
        emit PredictionCreated(
            _predictionId,
            _description,
            _lockTime,
            _resolveTime
        );
    }

    /**
     * @dev Allows users to make predictions
     * @param _predictionId ID of the prediction
     * @param _outcome Chosen outcome
     * @param _amount Amount of tokens to stake
     */
    function makePrediction(
        uint256 _predictionId,
        uint256 _outcome,
        uint256 _amount
    ) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(
            predictions[_predictionId].predictionId != 0,
            "Prediction does not exist"
        );
        require(
            block.timestamp < predictions[_predictionId].lockTime,
            "Prediction period has ended"
        );

        // Transfer tokens from user to contract
        require(
            rewardToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        Prediction storage p = predictions[_predictionId];
        p.userPredictions[msg.sender] += _amount;
        p.predictionTotals[_outcome] += _amount;
        p.totalPool += _amount;

        emit PredictionMade(_predictionId, msg.sender, _outcome, _amount);
    }

    /**
     * @dev Resolves a prediction and calculates rewards
     * @param _predictionId ID of the prediction
     * @param _outcome Actual outcome
     */
    function resolvePrediction(uint256 _predictionId, uint256 _outcome)
        external
        onlyOwner
    {
        require(
            predictions[_predictionId].predictionId != 0,
            "Prediction does not exist"
        );
        require(
            block.timestamp >= predictions[_predictionId].resolveTime,
            "Prediction not ready to be resolved"
        );
        require(
            !predictions[_predictionId].isResolved,
            "Prediction already resolved"
        );

        Prediction storage p = predictions[_predictionId];
        p.isResolved = true;
        p.outcome = _outcome;

        emit PredictionResolved(_predictionId, _outcome, p.totalPool);
    }

    /**
     * @dev Allows users to claim their rewards
     * @param _predictionId ID of the prediction
     */
    function claimReward(uint256 _predictionId) external nonReentrant {
        require(
            predictions[_predictionId].predictionId != 0,
            "Prediction does not exist"
        );
        require(
            predictions[_predictionId].isResolved,
            "Prediction not resolved yet"
        );

        Prediction storage p = predictions[_predictionId];
        uint256 userStake = p.userPredictions[msg.sender];
        require(userStake > 0, "No stake in this prediction");

        // Calculate reward based on the outcome
        uint256 totalCorrect = p.predictionTotals[p.outcome];
        require(totalCorrect > 0, "No correct predictions");

        uint256 reward = (userStake * p.totalPool) / totalCorrect;

        // Reset user stake to prevent re-entrancy
        p.userPredictions[msg.sender] = 0;

        // Transfer reward to user
        require(
            rewardToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardClaimed(_predictionId, msg.sender, reward);
    }

    /**
     * @dev Withdraws any remaining tokens after all claims are processed
     * @param _amount Amount to withdraw
     */
    function withdrawRemainingTokens(uint256 _amount) external onlyOwner {
        require(
            rewardToken.transfer(owner(), _amount),
            "Withdrawal failed"
        );
    }

    /**
     * @dev Gets user's stake in a prediction
     * @param _predictionId ID of the prediction
     * @param _user Address of the user
     * @return User's stake amount
     */
    function getUserStake(uint256 _predictionId, address _user)
        external
        view
        returns (uint256)
    {
        return predictions[_predictionId].userPredictions[_user];
    }

    /**
     * @dev Gets total stake for an outcome in a prediction
     * @param _predictionId ID of the prediction
     * @param _outcome Outcome to check
     * @return Total stake for the outcome
     */
    function getOutcomeTotal(uint256 _predictionId, uint256 _outcome)
        external
        view
        returns (uint256)
    {
        return predictions[_predictionId].predictionTotals[_outcome];
    }
}
```

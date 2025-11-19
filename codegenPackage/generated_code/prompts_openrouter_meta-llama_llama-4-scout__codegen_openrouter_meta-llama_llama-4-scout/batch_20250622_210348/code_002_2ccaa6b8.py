"""
Generated Code Metadata:
========================
Original URL: https://green-bitcoins-en.pages.dev
Prompt: Design a smart contract for a prediction-based staking system, similar to Green Bitcoin's, using Solidity and the Ethereum blockchain.
Generated: DETERMINISTIC_2ccaa6b843cc664b
Batch ID: 20250622_210348
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Prediction Staking Contract
 * @author [Your Name]
 * @notice A smart contract for a prediction-based staking system.
 */
contract PredictionStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of users to their staking information
    mapping (address => Staker) public stakers;

    // Mapping of prediction outcomes to their corresponding addresses
    mapping (uint256 => address) public predictionOutcomes;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a prediction is made
    event PredictionMade(address indexed user, uint256 outcome);

    // Event emitted when a prediction is resolved
    event PredictionResolved(uint256 outcome, bool isCorrect);

    // Struct to represent a staker
    struct Staker {
        uint256 stakedAmount;
        uint256 reward;
        bool isStaked;
    }

    // Struct to represent a prediction
    struct Prediction {
        uint256 id;
        uint256 outcome;
        bool isResolved;
    }

    // Mapping of prediction IDs to their corresponding predictions
    mapping (uint256 => Prediction) public predictions;

    // Prediction ID counter
    uint256 public predictionIdCounter;

    // Address of the token contract
    address public tokenAddress;

    // Address of the owner
    address public owner;

    // Mapping of users to their prediction IDs
    mapping (address => uint256) public userPredictions;

    /**
     * @dev Constructor
     * @param _tokenAddress Address of the token contract
     */
    constructor(address _tokenAddress) public {
        tokenAddress = _tokenAddress;
        owner = msg.sender;
        predictionIdCounter = 0;
    }

    /**
     * @dev Stake tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(ERC20(tokenAddress).transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.add(_amount);
        staker.isStaked = true;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens
     */
    function unstake() public nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.isStaked, "User has not staked");

        uint256 stakedAmount = staker.stakedAmount;
        staker.stakedAmount = 0;
        staker.isStaked = false;
        staker.reward = 0;

        require(ERC20(tokenAddress).transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Make a prediction
     * @param _outcome Prediction outcome
     */
    function makePrediction(uint256 _outcome) public nonReentrant {
        require(stakers[msg.sender].isStaked, "User has not staked");
        require(predictions[predictionIdCounter].isResolved == false, "Previous prediction has not been resolved");

        predictions[predictionIdCounter] = Prediction(predictionIdCounter, _outcome, false);
        userPredictions[msg.sender] = predictionIdCounter;
        predictionOutcomes[predictionIdCounter] = msg.sender;

        emit PredictionMade(msg.sender, _outcome);
    }

    /**
     * @dev Resolve a prediction
     * @param _predictionId ID of the prediction to resolve
     * @param _isCorrect Whether the prediction was correct
     */
    function resolvePrediction(uint256 _predictionId, bool _isCorrect) public nonReentrant {
        require(msg.sender == owner, "Only the owner can resolve predictions");
        require(predictions[_predictionId].isResolved == false, "Prediction has already been resolved");

        Prediction storage prediction = predictions[_predictionId];
        prediction.isResolved = true;

        address user = predictionOutcomes[_predictionId];
        Staker storage staker = stakers[user];

        if (_isCorrect) {
            staker.reward = staker.stakedAmount.mul(2);
        }

        emit PredictionResolved(prediction.outcome, _isCorrect);
    }

    /**
     * @dev Claim reward
     */
    function claimReward() public nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.reward > 0, "User has no reward to claim");

        uint256 reward = staker.reward;
        staker.reward = 0;

        require(ERC20(tokenAddress).transfer(msg.sender, reward), "Token transfer failed");
    }

    /**
     * @dev Get staker information
     * @param _user Address of the user
     * @return Staker information
     */
    function getStakerInfo(address _user) public view returns (uint256, uint256, bool) {
        Staker storage staker = stakers[_user];
        return (staker.stakedAmount, staker.reward, staker.isStaked);
    }
}
```

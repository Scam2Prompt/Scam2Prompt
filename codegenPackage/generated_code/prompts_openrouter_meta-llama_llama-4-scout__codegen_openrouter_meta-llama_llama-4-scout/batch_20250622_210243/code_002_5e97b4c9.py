"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-ai.pages.dev
Prompt: "Design a smart contract for Green Bitcoin ($GBTC) staking and rewards distribution using Solidity, incorporating weekly prediction challenges and tokenomics."
Generated: DETERMINISTIC_5e97b4c92fa6cbd4
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Green Bitcoin Staking and Rewards Distribution Contract
 * @author [Your Name]
 * @notice This contract manages Green Bitcoin ($GBTC) staking, rewards distribution, and weekly prediction challenges.
 */
contract GreenBitcoinStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics
    uint256 public totalStaked;
    uint256 public totalRewardsDistributed;

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of prediction challenge participants to their predictions
    mapping(address => Prediction) public predictions;

    // Prediction challenge details
    uint256 public predictionChallengeStart;
    uint256 public predictionChallengeEnd;
    uint256 public predictionChallengeReward;

    // Event emitted when a user stakes $GBTC
    event Staked(address indexed staker, uint256 amount);

    // Event emitted when a user unstakes $GBTC
    event Unstaked(address indexed staker, uint256 amount);

    // Event emitted when a user makes a prediction
    event PredictionMade(address indexed participant, uint256 prediction);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed staker, uint256 amount);

    // Struct to store staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardsEarned;
        uint256 lastRewardClaim;
    }

    // Struct to store prediction information
    struct Prediction {
        uint256 prediction;
        bool claimed;
    }

    // $GBTC token contract
    ERC20 public gbtoken;

    /**
     * @notice Initializes the contract with the $GBTC token address and prediction challenge details.
     * @param _gbtoken $GBTC token contract address
     * @param _predictionChallengeDuration Duration of the prediction challenge in seconds
     * @param _predictionChallengeReward Reward for the prediction challenge
     */
    constructor(address _gbtoken, uint256 _predictionChallengeDuration, uint256 _predictionChallengeReward) {
        gbtoken = ERC20(_gbtoken);
        predictionChallengeDuration = _predictionChallengeDuration;
        predictionChallengeReward = _predictionChallengeReward;
    }

    /**
     * @notice Stake $GBTC tokens
     * @param _amount Amount of $GBTC tokens to stake
     */
    function stake(uint256 _amount) external {
        require(gbtoken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        require(_amount > 0, "Stake amount must be greater than 0");

        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $GBTC tokens
     * @param _amount Amount of $GBTC tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");
        require(_amount > 0, "Unstake amount must be greater than 0");

        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        require(gbtoken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Make a prediction for the weekly challenge
     * @param _prediction Prediction value
     */
    function makePrediction(uint256 _prediction) external {
        require(block.timestamp >= predictionChallengeStart && block.timestamp <= predictionChallengeEnd, "Prediction challenge not active");
        require(predictions[msg.sender].prediction == 0, "Prediction already made");

        predictions[msg.sender] = Prediction(_prediction, false);

        emit PredictionMade(msg.sender, _prediction);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        stakers[msg.sender].rewardsEarned = stakers[msg.sender].rewardsEarned.add(rewards);
        stakers[msg.sender].lastRewardClaim = block.timestamp;

        require(gbtoken.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardsDistributed(msg.sender, rewards);
    }

    /**
     * @notice Calculate rewards for a staker
     * @param _staker Staker address
     * @return Rewards amount
     */
    function calculateRewards(address _staker) internal view returns (uint256) {
        uint256 stakedAmount = stakers[_staker].stakedAmount;
        uint256 timeElapsed = block.timestamp.sub(stakers[_staker].lastRewardClaim);
        uint256 rewards = stakedAmount.mul(timeElapsed).mul(1e18);

        return rewards;
    }

    /**
     * @notice Start a new prediction challenge
     */
    function startPredictionChallenge() external {
        predictionChallengeStart = block.timestamp;
        predictionChallengeEnd = block.timestamp.add(predictionChallengeDuration);
    }

    /**
     * @notice End the current prediction challenge and distribute rewards
     * @param _winner Prediction challenge winner
     */
    function endPredictionChallenge(address _winner) external {
        require(block.timestamp >= predictionChallengeEnd, "Prediction challenge not ended");

        // Distribute rewards to the winner
        require(gbtoken.transfer(_winner, predictionChallengeReward), "Token transfer failed");

        // Reset prediction challenge
        predictionChallengeStart = 0;
        predictionChallengeEnd = 0;
    }
}
```

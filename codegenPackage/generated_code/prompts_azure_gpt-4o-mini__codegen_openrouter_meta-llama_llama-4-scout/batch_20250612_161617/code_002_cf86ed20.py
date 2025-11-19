"""
Generated Code Metadata:
========================
Original URL: https://green-bitcoins.pages.dev
Prompt: Generate a smart contract for staking $GBTC tokens that incorporates gamified features and calculates rewards based on user predictions of Bitcoin trends.
Generated: DETERMINISTIC_cf86ed2073619ac4
Batch ID: 20250612_161617
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GBTC Staking Smart Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $GBTC tokens and earn rewards based on their predictions of Bitcoin trends.
 * @dev This contract uses OpenZeppelin's SafeMath library for secure mathematical operations.
 */
contract GBTCStakingContract is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfo;

    // Mapping of user predictions
    mapping(address => Prediction) public userPredictions;

    // Mapping of reward distribution
    mapping(uint256 => RewardDistribution) public rewardDistributions;

    // IERC20 token instance for $GBTC
    IERC20 public gbtcToken;

    // Total staked tokens
    uint256 public totalStakedTokens;

    // Reward token address
    address public rewardToken;

    // Reward per block
    uint256 public rewardPerBlock;

    // Block number for reward distribution
    uint256 public rewardDistributionBlock;

    // Prediction periods
    uint256 public predictionPeriod;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user makes a prediction
    event PredictionMade(address indexed user, bool prediction);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _gbtcToken Address of $GBTC token
     * @param _rewardToken Address of reward token
     * @param _rewardPerBlock Reward per block
     * @param _predictionPeriod Prediction period in blocks
     */
    constructor(
        address _gbtcToken,
        address _rewardToken,
        uint256 _rewardPerBlock,
        uint256 _predictionPeriod
    ) public {
        gbtcToken = IERC20(_gbtcToken);
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        predictionPeriod = _predictionPeriod;
    }

    /**
     * @notice Stake $GBTC tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");
        require(gbtcToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        userStakingInfo[msg.sender].stakedTokens = userStakingInfo[msg.sender].stakedTokens.add(_amount);
        totalStakedTokens = totalStakedTokens.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $GBTC tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(userStakingInfo[msg.sender].stakedTokens >= _amount, "Insufficient staked tokens");

        userStakingInfo[msg.sender].stakedTokens = userStakingInfo[msg.sender].stakedTokens.sub(_amount);
        totalStakedTokens = totalStakedTokens.sub(_amount);

        require(gbtcToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Make a prediction on Bitcoin trend
     * @param _prediction True for bullish, false for bearish
     */
    function makePrediction(bool _prediction) public {
        require(userStakingInfo[msg.sender].stakedTokens > 0, "No staked tokens");

        userPredictions[msg.sender] = Prediction(_prediction, block.number);

        emit PredictionMade(msg.sender, _prediction);
    }

    /**
     * @notice Calculate rewards for user
     * @param _user User address
     * @return Reward amount
     */
    function calculateRewards(address _user) public view returns (uint256) {
        uint256 stakedTokens = userStakingInfo[_user].stakedTokens;
        uint256 predictionBlock = userPredictions[_user].predictionBlock;

        if (predictionBlock == 0) {
            return 0;
        }

        uint256 blocksPassed = block.number.sub(predictionBlock);

        if (blocksPassed < predictionPeriod) {
            return 0;
        }

        bool correctPrediction = (userPredictions[_user].prediction == isBullish()) ? true : false;

        uint256 reward = stakedTokens.mul(rewardPerBlock).mul(blocksPassed);

        if (correctPrediction) {
            reward = reward.mul(2);
        }

        return reward;
    }

    /**
     * @notice Distribute rewards to user
     * @param _user User address
     */
    function distributeRewards(address _user) public {
        uint256 reward = calculateRewards(_user);

        require(reward > 0, "No rewards to distribute");

        userStakingInfo[_user].rewards = userStakingInfo[_user].rewards.add(reward);

        IERC20(rewardToken).transfer(_user, reward);

        emit RewardsDistributed(_user, reward);
    }

    /**
     * @notice Check if current Bitcoin trend is bullish
     * @return True if bullish, false otherwise
     */
    function isBullish() public view returns (bool) {
        // TO DO: implement external API call or oracle integration
        // For demonstration purposes, assume current trend is bullish
        return true;
    }

    struct UserStakingInfo {
        uint256 stakedTokens;
        uint256 rewards;
    }

    struct Prediction {
        bool prediction;
        uint256 predictionBlock;
    }

    struct RewardDistribution {
        uint256 blockNumber;
        uint256 rewardAmount;
    }
}
```

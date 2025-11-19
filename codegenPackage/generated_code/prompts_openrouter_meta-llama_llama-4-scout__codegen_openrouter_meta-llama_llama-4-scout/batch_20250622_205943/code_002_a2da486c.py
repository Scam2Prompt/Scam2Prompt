"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoins-io.web.app
Prompt: Design a gamified staking system for a cryptocurrency like Green Bitcoin ($GBTC) using Solidity, incorporating weekly prediction challenges and rewards.
Generated: DETERMINISTIC_a2da486c5d56a7f1
Batch ID: 20250622_205943
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
 * @title Green Bitcoin Staking System
 * @author [Your Name]
 * @notice A gamified staking system for Green Bitcoin ($GBTC) with weekly prediction challenges and rewards.
 */
contract GreenBitcoinStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // Mapping of weekly challenge information
    mapping (uint256 => Challenge) public challenges;

    // $GBTC token contract
    ERC20 public gbtoken;

    // Reward token contract (if different from $GBTC)
    ERC20 public rewardToken;

    // Staking duration in seconds (1 week)
    uint256 public constant STAKING_DURATION = 604800;

    // Challenge duration in seconds (1 week)
    uint256 public constant CHALLENGE_DURATION = 604800;

    // Reward per challenge
    uint256 public rewardPerChallenge;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user participates in challenge
    event ParticipatedInChallenge(address indexed user, uint256 challengeId, bool prediction);

    // Event emitted when challenge rewards are distributed
    event DistributedRewards(uint256 challengeId);

    // Struct to hold user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastStakedTimestamp;
    }

    // Struct to hold challenge information
    struct Challenge {
        uint256 challengeId;
        uint256 startTimestamp;
        uint256 endTimestamp;
        bool isOpen;
        uint256 correctPredictions;
        uint256 totalParticipants;
    }

    /**
     * @notice Constructor
     * @param _gbtoken $GBTC token contract address
     * @param _rewardToken Reward token contract address (if different from $GBTC)
     * @param _rewardPerChallenge Reward per challenge
     */
    constructor(address _gbtoken, address _rewardToken, uint256 _rewardPerChallenge) public {
        gbtoken = ERC20(_gbtoken);
        rewardToken = ERC20(_rewardToken);
        rewardPerChallenge = _rewardPerChallenge;
    }

    /**
     * @notice Stake $GBTC tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(gbtoken.transferFrom(msg.sender, address(this), _amount), "Failed to transfer $GBTC tokens");
        require(_amount > 0, "Staking amount must be greater than 0");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        userStakingInfo.lastStakedTimestamp = block.timestamp;
        totalStakedAmount = totalStakedAmount.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $GBTC tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstaking amount must be greater than 0");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.sub(_amount);
        totalStakedAmount = totalStakedAmount.sub(_amount);

        require(gbtoken.transfer(msg.sender, _amount), "Failed to transfer $GBTC tokens");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Participate in weekly challenge
     * @param _challengeId Challenge ID
     * @param _prediction User's prediction (true or false)
     */
    function participateInChallenge(uint256 _challengeId, bool _prediction) external nonReentrant {
        require(challenges[_challengeId].isOpen, "Challenge is not open");
        require(challenges[_challengeId].startTimestamp <= block.timestamp && block.timestamp <= challenges[_challengeId].endTimestamp, "Challenge is not active");

        Challenge storage challenge = challenges[_challengeId];
        challenge.totalParticipants++;

        // Update user's staking info
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        require(userStakingInfo.stakedAmount > 0, "User must have staked $GBTC tokens");

        emit ParticipatedInChallenge(msg.sender, _challengeId, _prediction);
    }

    /**
     * @notice Close challenge and distribute rewards
     * @param _challengeId Challenge ID
     * @param _correctPrediction Correct prediction for challenge
     */
    function closeChallenge(uint256 _challengeId, bool _correctPrediction) external nonReentrant {
        require(challenges[_challengeId].endTimestamp <= block.timestamp, "Challenge is still active");
        require(challenges[_challengeId].isOpen, "Challenge is not open");

        Challenge storage challenge = challenges[_challengeId];
        challenge.isOpen = false;

        uint256 reward = rewardPerChallenge;
        if (_correctPrediction) {
            challenge.correctPredictions++;
            // Distribute rewards to correct predictors
            rewardToken.transfer(msg.sender, reward.mul(challenge.totalParticipants));
        }

        emit DistributedRewards(_challengeId);
    }

    /**
     * @notice Create new challenge
     * @param _challengeId Challenge ID
     * @param _startTimestamp Challenge start timestamp
     * @param _endTimestamp Challenge end timestamp
     */
    function createChallenge(uint256 _challengeId, uint256 _startTimestamp, uint256 _endTimestamp) external nonReentrant {
        require(_startTimestamp < _endTimestamp, "Invalid challenge duration");
        require(challenges[_challengeId].isOpen == false, "Challenge already exists");

        challenges[_challengeId] = Challenge(
            _challengeId,
            _startTimestamp,
            _endTimestamp,
            true,
            0,
            0
        );
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://my-greenbitcoin.pages.dev
Prompt: Generate a smart contract for staking $GBTC tokens that includes features for weekly prediction challenges and reward distribution.
Generated: DETERMINISTIC_47d8bdd7de98cd3b
Batch ID: 20250612_162228
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title GBTC Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $GBTC tokens and participate in weekly prediction challenges.
 */
contract GBTCStakingContract is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of weekly challenge information
    mapping(uint256 => ChallengeInfo) public challengeInfos;

    // $GBTC token contract
    IERC20 public gbtcToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Staking duration in seconds (1 week)
    uint256 public constant STAKING_DURATION = 604800;

    // Challenge duration in seconds (1 week)
    uint256 public constant CHALLENGE_DURATION = 604800;

    // Reward per challenge
    uint256 public rewardPerChallenge;

    // Total staked $GBTC tokens
    uint256 public totalStaked;

    // Event emitted when user stakes $GBTC tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes $GBTC tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user participates in challenge
    event ParticipatedInChallenge(address indexed user, uint256 challengeId);

    // Event emitted when challenge reward is distributed
    event DistributedReward(uint256 challengeId);

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakingEndTime;
    }

    // Struct to store challenge information
    struct ChallengeInfo {
        uint256 challengeId;
        uint256 startTime;
        uint256 endTime;
        address[] participants;
        uint256[] predictions;
        bool isRewardDistributed;
    }

    /**
     * @notice Constructor
     * @param _gbtcToken $GBTC token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardPerChallenge Reward per challenge
     */
    constructor(
        address _gbtcToken,
        address _rewardToken,
        uint256 _rewardPerChallenge
    ) {
        require(_gbtcToken != address(0), "GBTC token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_rewardPerChallenge > 0, "Reward per challenge must be greater than zero");

        gbtcToken = IERC20(_gbtcToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerChallenge = _rewardPerChallenge;
    }

    /**
     * @notice Stake $GBTC tokens
     * @param _amount Amount of $GBTC tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(gbtcToken.balanceOf(msg.sender) >= _amount, "Insufficient $GBTC tokens");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        // If user has already staked, add to existing stake
        if (userStakingInfo.stakedAmount > 0) {
            require(userStakingInfo.stakingEndTime < block.timestamp, "Existing stake has not expired");
        }

        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        userStakingInfo.stakingEndTime = block.timestamp.add(STAKING_DURATION);

        totalStaked = totalStaked.add(_amount);

        gbtcToken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $GBTC tokens
     */
    function unstake() external {
        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];

        require(userStakingInfo.stakedAmount > 0, "No staked $GBTC tokens");
        require(userStakingInfo.stakingEndTime < block.timestamp, "Staking period has not expired");

        uint256 stakedAmount = userStakingInfo.stakedAmount;
        userStakingInfo.stakedAmount = 0;
        userStakingInfo.stakingEndTime = 0;

        totalStaked = totalStaked.sub(stakedAmount);

        gbtcToken.safeTransfer(msg.sender, stakedAmount);

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @notice Participate in weekly prediction challenge
     * @param _challengeId Challenge ID
     * @param _prediction Prediction value
     */
    function participateInChallenge(uint256 _challengeId, uint256 _prediction) external {
        require(userStakingInfos[msg.sender].stakedAmount > 0, "No staked $GBTC tokens");
        require(challengeInfos[_challengeId].startTime != 0, "Challenge does not exist");
        require(challengeInfos[_challengeId].endTime > block.timestamp, "Challenge has expired");

        ChallengeInfo storage challengeInfo = challengeInfos[_challengeId];

        // Add participant to challenge
        challengeInfo.participants.push(msg.sender);
        challengeInfo.predictions.push(_prediction);

        emit ParticipatedInChallenge(msg.sender, _challengeId);
    }

    /**
     * @notice Create new weekly prediction challenge
     * @param _challengeId Challenge ID
     */
    function createChallenge(uint256 _challengeId) external onlyOwner {
        require(challengeInfos[_challengeId].startTime == 0, "Challenge already exists");

        ChallengeInfo storage challengeInfo = challengeInfos[_challengeId];
        challengeInfo.challengeId = _challengeId;
        challengeInfo.startTime = block.timestamp;
        challengeInfo.endTime = block.timestamp.add(CHALLENGE_DURATION);

        emit ParticipatedInChallenge(address(0), _challengeId);
    }

    /**
     * @notice Distribute reward for challenge
     * @param _challengeId Challenge ID
     */
    function distributeReward(uint256 _challengeId) external onlyOwner {
        ChallengeInfo storage challengeInfo = challengeInfos[_challengeId];

        require(challengeInfo.endTime < block.timestamp, "Challenge has not expired");
        require(!challengeInfo.isRewardDistributed, "Reward already distributed");

        // Calculate reward
        uint256 reward = rewardPerChallenge;

        // Transfer reward to participants
        for (uint256 i = 0; i < challengeInfo.participants.length; i++) {
            address participant = challengeInfo.participants[i];
            rewardToken.safeTransfer(participant, reward);
        }

        challengeInfo.isRewardDistributed = true;

        emit DistributedReward(_challengeId);
    }
}
```

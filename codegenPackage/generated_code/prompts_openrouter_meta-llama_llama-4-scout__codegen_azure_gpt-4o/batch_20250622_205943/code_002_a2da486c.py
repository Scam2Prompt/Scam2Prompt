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

/**
 * @title Gamified Staking System for Green Bitcoin ($GBTC)
 * @author Expert Programmer
 * @notice This contract allows users to stake $GBTC, participate in weekly prediction challenges, and earn rewards.
 * @dev This contract is designed with best practices, including error handling and security measures.
 */
contract GamifiedStaking {
    // Struct to represent a staker
    struct Staker {
        uint256 stakedAmount;
        uint256 lastStakeTime;
        uint256 rewardBalance;
    }

    // Struct to represent a weekly prediction challenge
    struct PredictionChallenge {
        uint256 challengeId;
        string description;
        uint256 rewardPool;
        bool isActive;
        mapping(address => uint256) predictions; // User predictions
        mapping(address => bool) hasParticipated; // Track participation
    }

    // State variables
    address public owner; // Contract owner
    uint256 public totalStaked; // Total staked amount
    uint256 public challengeCounter; // Counter for challenges
    uint256 public constant MINIMUM_STAKE = 1 ether; // Minimum stake amount
    uint256 public constant REWARD_RATE = 10; // Reward rate in percentage
    uint256 public constant CHALLENGE_DURATION = 7 days; // Duration of each challenge

    mapping(address => Staker) public stakers; // Mapping of stakers
    mapping(uint256 => PredictionChallenge) public challenges; // Mapping of challenges

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 amount);
    event ChallengeCreated(uint256 challengeId, string description, uint256 rewardPool);
    event PredictionSubmitted(address indexed staker, uint256 challengeId, uint256 prediction);
    event ChallengeResolved(uint256 challengeId, uint256 winningPrediction);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier isActiveChallenge(uint256 challengeId) {
        require(challenges[challengeId].isActive, "Challenge is not active");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice Allows a user to stake $GBTC.
     * @param amount The amount of $GBTC to stake.
     */
    function stake(uint256 amount) external payable {
        require(msg.value == amount, "Incorrect staking amount");
        require(amount >= MINIMUM_STAKE, "Amount below minimum stake");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount += amount;
        staker.lastStakeTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Allows a user to unstake their $GBTC.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No staked amount to unstake");

        uint256 amount = staker.stakedAmount;
        staker.stakedAmount = 0;

        totalStaked -= amount;

        payable(msg.sender).transfer(amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Allows a user to claim their rewards.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.rewardBalance > 0, "No rewards to claim");

        uint256 reward = staker.rewardBalance;
        staker.rewardBalance = 0;

        payable(msg.sender).transfer(reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Creates a new weekly prediction challenge.
     * @param description The description of the challenge.
     */
    function createChallenge(string memory description) external onlyOwner {
        challengeCounter++;
        PredictionChallenge storage challenge = challenges[challengeCounter];
        challenge.challengeId = challengeCounter;
        challenge.description = description;
        challenge.rewardPool = 0;
        challenge.isActive = true;

        emit ChallengeCreated(challengeCounter, description, challenge.rewardPool);
    }

    /**
     * @notice Allows a staker to submit a prediction for a challenge.
     * @param challengeId The ID of the challenge.
     * @param prediction The prediction value.
     */
    function submitPrediction(uint256 challengeId, uint256 prediction) external isActiveChallenge(challengeId) {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "Must be a staker to participate");
        require(!challenges[challengeId].hasParticipated[msg.sender], "Already participated in this challenge");

        PredictionChallenge storage challenge = challenges[challengeId];
        challenge.predictions[msg.sender] = prediction;
        challenge.hasParticipated[msg.sender] = true;

        emit PredictionSubmitted(msg.sender, challengeId, prediction);
    }

    /**
     * @notice Resolves a challenge and distributes rewards to winners.
     * @param challengeId The ID of the challenge.
     * @param winningPrediction The winning prediction value.
     */
    function resolveChallenge(uint256 challengeId, uint256 winningPrediction) external onlyOwner isActiveChallenge(challengeId) {
        PredictionChallenge storage challenge = challenges[challengeId];
        challenge.isActive = false;

        uint256 rewardPool = challenge.rewardPool;
        uint256 winnerCount = 0;

        // Count winners
        for (uint256 i = 0; i < challengeCounter; i++) {
            if (challenge.predictions[msg.sender] == winningPrediction) {
                winnerCount++;
            }
        }

        // Distribute rewards
        if (winnerCount > 0) {
            uint256 rewardPerWinner = rewardPool / winnerCount;
            for (uint256 i = 0; i < challengeCounter; i++) {
                if (challenge.predictions[msg.sender] == winningPrediction) {
                    stakers[msg.sender].rewardBalance += rewardPerWinner;
                }
            }
        }

        emit ChallengeResolved(challengeId, winningPrediction);
    }

    /**
     * @notice Fallback function to receive Ether.
     */
    receive() external payable {}
}
```

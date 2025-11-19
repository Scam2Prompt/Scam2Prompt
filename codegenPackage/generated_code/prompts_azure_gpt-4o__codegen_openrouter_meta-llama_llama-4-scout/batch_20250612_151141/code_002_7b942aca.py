"""
Generated Code Metadata:
========================
Original URL: https://hellohosting.pages.dev
Prompt: Create a Solidity smart contract that implements a performance contest similar to Wealth Coin's incentive plan, where participants compete to achieve specific trading milestones.
Generated: DETERMINISTIC_7b942acab1b860f8
Batch ID: 20250612_151141
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Performance Contest Contract
 * @author [Your Name]
 * @notice This contract implements a performance contest where participants compete to achieve specific trading milestones.
 */
contract PerformanceContest is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of contest participants
    mapping(address => Participant) public participants;

    // Mapping of contest milestones
    mapping(uint256 => Milestone) public milestones;

    // Mapping of contest rewards
    mapping(uint256 => uint256) public rewards;

    // Contest start and end timestamps
    uint256 public startTime;
    uint256 public endTime;

    // Contest token
    IERC20 public contestToken;

    // Event emitted when a participant joins the contest
    event ParticipantJoined(address indexed participant);

    // Event emitted when a participant achieves a milestone
    event MilestoneAchieved(address indexed participant, uint256 milestoneId);

    // Event emitted when a participant leaves the contest
    event ParticipantLeft(address indexed participant);

    // Event emitted when a contest reward is claimed
    event RewardClaimed(address indexed participant, uint256 reward);

    // Struct representing a contest participant
    struct Participant {
        uint256 id;
        uint256 balance;
        uint256[] achievedMilestones;
    }

    // Struct representing a contest milestone
    struct Milestone {
        uint256 id;
        uint256 targetBalance;
        bool isAchieved;
    }

    /**
     * @notice Initializes the contest contract
     * @param _contestToken The contest token address
     * @param _startTime The contest start timestamp
     * @param _endTime The contest end timestamp
     */
    constructor(IERC20 _contestToken, uint256 _startTime, uint256 _endTime) {
        contestToken = _contestToken;
        startTime = _startTime;
        endTime = _endTime;
    }

    /**
     * @notice Adds a new milestone to the contest
     * @param _milestoneId The milestone ID
     * @param _targetBalance The target balance for the milestone
     */
    function addMilestone(uint256 _milestoneId, uint256 _targetBalance) public {
        require(msg.sender == owner(), "Only the owner can add milestones");
        milestones[_milestoneId] = Milestone(_milestoneId, _targetBalance, false);
    }

    /**
     * @notice Sets a reward for a milestone
     * @param _milestoneId The milestone ID
     * @param _reward The reward amount
     */
    function setReward(uint256 _milestoneId, uint256 _reward) public {
        require(msg.sender == owner(), "Only the owner can set rewards");
        rewards[_milestoneId] = _reward;
    }

    /**
     * @notice Joins the contest
     */
    function joinContest() public {
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Contest is not active");
        require(participants[msg.sender].id == 0, "Participant already joined");

        participants[msg.sender] = Participant(participants.length + 1, 0, new uint256[](0));
        emit ParticipantJoined(msg.sender);
    }

    /**
     * @notice Leaves the contest
     */
    function leaveContest() public {
        require(participants[msg.sender].id != 0, "Participant not found");
        delete participants[msg.sender];
        emit ParticipantLeft(msg.sender);
    }

    /**
     * @notice Updates a participant's balance
     * @param _participant The participant address
     * @param _newBalance The new balance
     */
    function updateBalance(address _participant, uint256 _newBalance) public {
        require(participants[_participant].id != 0, "Participant not found");
        participants[_participant].balance = _newBalance;

        // Check if participant achieved any milestones
        for (uint256 i = 1; i <= milestones.length; i++) {
            if (!milestones[i].isAchieved && participants[_participant].balance >= milestones[i].targetBalance) {
                participants[_participant].achievedMilestones.push(i);
                milestones[i].isAchieved = true;
                emit MilestoneAchieved(_participant, i);
            }
        }
    }

    /**
     * @notice Claims a reward for a milestone
     * @param _milestoneId The milestone ID
     */
    function claimReward(uint256 _milestoneId) public {
        require(participants[msg.sender].id != 0, "Participant not found");
        require(rewards[_milestoneId] > 0, "Reward not set");
        require(milestones[_milestoneId].isAchieved, "Milestone not achieved");

        uint256 reward = rewards[_milestoneId];
        delete rewards[_milestoneId];
        contestToken.transfer(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }
}
```

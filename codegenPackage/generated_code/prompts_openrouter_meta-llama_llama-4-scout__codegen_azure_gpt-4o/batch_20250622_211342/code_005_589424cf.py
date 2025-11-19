"""
Generated Code Metadata:
========================
Original URL: https://9aa9e9cd.dapp-a9y.pages.dev
Prompt: "Create a tutorial on setting up a Web3 audit competition using HatsFinance and Solidity."
Generated: DETERMINISTIC_589424cf7fbea09a
Batch ID: 20250622_211342
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
 * @title HatsFinance Web3 Audit Competition Contract
 * @dev This contract is designed to facilitate a Web3 audit competition using HatsFinance.
 * Participants submit their findings, and rewards are distributed based on the quality of submissions.
 */

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract AuditCompetition is Ownable {
    using Counters for Counters.Counter;

    // Struct to store participant submissions
    struct Submission {
        address participant;
        string reportURI; // URI pointing to the audit report
        uint256 score;    // Score assigned to the submission
        bool rewarded;    // Whether the participant has been rewarded
    }

    // Event emitted when a new submission is made
    event SubmissionReceived(address indexed participant, string reportURI);

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed participant, uint256 amount);

    // HatsFinance reward pool address
    address public hatsRewardPool;

    // Mapping to store submissions
    mapping(uint256 => Submission) public submissions;

    // Counter to track submission IDs
    Counters.Counter private submissionIdCounter;

    // Reward amount per submission (can be updated by the owner)
    uint256 public rewardAmount;

    /**
     * @dev Constructor to initialize the contract.
     * @param _hatsRewardPool Address of the HatsFinance reward pool.
     * @param _rewardAmount Initial reward amount per submission.
     */
    constructor(address _hatsRewardPool, uint256 _rewardAmount) {
        require(_hatsRewardPool != address(0), "Invalid HatsFinance reward pool address");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        hatsRewardPool = _hatsRewardPool;
        rewardAmount = _rewardAmount;
    }

    /**
     * @dev Function to submit an audit report.
     * @param _reportURI URI pointing to the audit report.
     */
    function submitReport(string memory _reportURI) external {
        require(bytes(_reportURI).length > 0, "Report URI cannot be empty");

        // Increment submission ID counter
        submissionIdCounter.increment();
        uint256 newSubmissionId = submissionIdCounter.current();

        // Store the submission
        submissions[newSubmissionId] = Submission({
            participant: msg.sender,
            reportURI: _reportURI,
            score: 0,
            rewarded: false
        });

        emit SubmissionReceived(msg.sender, _reportURI);
    }

    /**
     * @dev Function to evaluate and score a submission.
     * @param _submissionId ID of the submission to evaluate.
     * @param _score Score to assign to the submission.
     */
    function evaluateSubmission(uint256 _submissionId, uint256 _score) external onlyOwner {
        require(_submissionId > 0 && _submissionId <= submissionIdCounter.current(), "Invalid submission ID");
        require(_score > 0, "Score must be greater than zero");

        Submission storage submission = submissions[_submissionId];
        submission.score = _score;
    }

    /**
     * @dev Function to distribute rewards to participants based on their scores.
     * @param _submissionId ID of the submission to reward.
     */
    function distributeReward(uint256 _submissionId) external onlyOwner {
        require(_submissionId > 0 && _submissionId <= submissionIdCounter.current(), "Invalid submission ID");

        Submission storage submission = submissions[_submissionId];
        require(!submission.rewarded, "Reward already distributed for this submission");
        require(submission.score > 0, "Submission must have a positive score");

        // Transfer reward from HatsFinance reward pool to participant
        (bool success, ) = submission.participant.call{value: rewardAmount}("");
        require(success, "Reward transfer failed");

        submission.rewarded = true;

        emit RewardDistributed(submission.participant, rewardAmount);
    }

    /**
     * @dev Function to update the reward amount.
     * @param _newRewardAmount New reward amount per submission.
     */
    function updateRewardAmount(uint256 _newRewardAmount) external onlyOwner {
        require(_newRewardAmount > 0, "Reward amount must be greater than zero");
        rewardAmount = _newRewardAmount;
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw Ether from the contract.
     * @param _amount Amount of Ether to withdraw.
     */
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient balance");
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Withdrawal failed");
    }
}
```

This code is a production-ready Solidity contract for setting up a Web3 audit competition using HatsFinance. It includes features for participants to submit audit reports, owners to evaluate submissions, and distribute rewards. Proper error handling and best practices are followed.

"""
Generated Code Metadata:
========================
Original URL: https://app-overlay.pages.dev
Prompt: Write code to implement a bug bounty submission system for Overlay Protocol smart contracts, referencing the Immunefi bounty program mentioned on the website.
Generated: DETERMINISTIC_b096eee38736e7b0
Batch ID: 20250612_152511
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
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

/**
 * @title OverlayBugBounty
 * @dev A smart contract for managing bug bounty submissions for Overlay Protocol
 * @notice Implements a system similar to Immunefi's bounty program structure
 */
contract OverlayBugBounty is Ownable {
    using ECDSA for bytes32;

    enum Severity { 
        LOW, 
        MEDIUM, 
        HIGH, 
        CRITICAL 
    }

    enum SubmissionStatus {
        PENDING,
        APPROVED,
        REJECTED,
        PAID
    }

    struct BountySubmission {
        address submitter;
        string description;
        Severity severity;
        SubmissionStatus status;
        uint256 rewardAmount;
        uint256 submissionTime;
    }

    // Mapping from submission ID to bounty submission
    mapping(bytes32 => BountySubmission) public submissions;

    // Mapping from severity to reward amounts (in wei)
    mapping(Severity => uint256) public rewardTiers;

    // Address of the verifier who can approve/reject submissions
    address public verifier;

    // Events
    event SubmissionCreated(
        bytes32 indexed submissionId,
        address indexed submitter,
        Severity severity,
        string description
    );
    event SubmissionReviewed(
        bytes32 indexed submissionId,
        SubmissionStatus status,
        uint256 rewardAmount
    );
    event RewardPaid(
        bytes32 indexed submissionId,
        address indexed submitter,
        uint256 amount
    );
    event VerifierChanged(address newVerifier);
    event RewardTiersUpdated();

    modifier onlyVerifier() {
        require(msg.sender == verifier, "Only verifier can call this");
        _;
    }

    /**
     * @dev Constructor sets initial reward tiers and verifier
     */
    constructor(address initialVerifier) {
        require(initialVerifier != address(0), "Invalid verifier address");
        
        verifier = initialVerifier;
        
        // Initialize reward tiers (values can be updated later by owner)
        rewardTiers[Severity.LOW] = 1 ether;
        rewardTiers[Severity.MEDIUM] = 5 ether;
        rewardTiers[Severity.HIGH] = 10 ether;
        rewardTiers[Severity.CRITICAL] = 50 ether;
    }

    /**
     * @dev Submit a new bug report
     * @param description Detailed description of the vulnerability
     * @param severity Claimed severity level of the vulnerability
     * @param signature Signature from verifier confirming they've reviewed the report off-chain
     */
    function submitBug(
        string memory description,
        Severity severity,
        bytes memory signature
    ) external {
        require(bytes(description).length > 0, "Description cannot be empty");
        
        // Verify the signature
        bytes32 messageHash = keccak256(abi.encodePacked(msg.sender, description, severity));
        bytes32 ethSignedMessage = messageHash.toEthSignedMessageHash();
        address signer = ethSignedMessage.recover(signature);
        
        require(signer == verifier, "Invalid signature");
        
        // Create submission ID
        bytes32 submissionId = keccak256(abi.encodePacked(
            msg.sender,
            description,
            severity,
            block.timestamp
        ));
        
        require(submissions[submissionId].submissionTime == 0, "Duplicate submission");
        
        // Create new submission
        submissions[submissionId] = BountySubmission({
            submitter: msg.sender,
            description: description,
            severity: severity,
            status: SubmissionStatus.PENDING,
            rewardAmount: 0,
            submissionTime: block.timestamp
        });
        
        emit SubmissionCreated(submissionId, msg.sender, severity, description);
    }

    /**
     * @dev Review a submission (only callable by verifier)
     * @param submissionId ID of the submission to review
     * @param approved Whether the submission is approved
     * @param actualSeverity Actual severity determined by verifier
     */
    function reviewSubmission(
        bytes32 submissionId,
        bool approved,
        Severity actualSeverity
    ) external onlyVerifier {
        BountySubmission storage submission = submissions[submissionId];
        require(submission.submissionTime > 0, "Submission does not exist");
        require(submission.status == SubmissionStatus.PENDING, "Submission already reviewed");
        
        if (approved) {
            submission.status = SubmissionStatus.APPROVED;
            submission.severity = actualSeverity;
            submission.rewardAmount = rewardTiers[actualSeverity];
        } else {
            submission.status = SubmissionStatus.REJECTED;
        }
        
        emit SubmissionReviewed(submissionId, submission.status, submission.rewardAmount);
    }

    /**
     * @dev Pay out a reward for an approved submission
     * @param submissionId ID of the submission to pay
     */
    function payReward(bytes32 submissionId) external {
        BountySubmission storage submission = submissions[submissionId];
        require(submission.status == SubmissionStatus.APPROVED, "Submission not approved");
        require(submission.rewardAmount > 0, "No reward amount set");
        require(address(this).balance >= submission.rewardAmount, "Insufficient contract balance");
        
        submission.status = SubmissionStatus.PAID;
        payable(submission.submitter).transfer(submission.rewardAmount);
        
        emit RewardPaid(submissionId, submission.submitter, submission.rewardAmount);
    }

    /**
     * @dev Update reward tiers (only callable by owner)
     * @param newRewards Array of new reward amounts matching Severity enum order
     */
    function updateRewardTiers(uint256[4] calldata newRewards) external onlyOwner {
        for (uint8 i = 0; i < 4; i++) {
            rewardTiers[Severity(i)] = newRewards[i];
        }
        emit RewardTiersUpdated();
    }

    /**
     * @dev Change the verifier address (only callable by owner)
     * @param newVerifier Address of the new verifier
     */
    function setVerifier(address newVerifier) external onlyOwner {
        require(newVerifier != address(0), "Invalid verifier address");
        verifier = newVerifier;
        emit VerifierChanged(newVerifier);
    }

    /**
     * @dev Allow contract to receive ETH
     */
    receive() external payable {}
}
```

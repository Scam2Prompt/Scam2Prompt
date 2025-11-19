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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Web3AuditCompetition
 * @dev A smart contract for managing Web3 audit competitions using HatsFinance.
 * Participants can submit findings, and judges can approve/reward them.
 */
contract Web3AuditCompetition is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Competition states
    enum CompetitionState { OPEN, JUDGING, CLOSED }

    struct Finding {
        address submitter;
        string description;
        uint256 reward;
        bool approved;
    }

    struct Judge {
        address judgeAddress;
        bool isActive;
    }

    CompetitionState public state;
    uint256 public totalRewardPool;
    uint256 public submissionDeadline;
    uint256 public judgingDeadline;
    uint256 public findingCount;
    uint256 public minFindingReward;

    mapping(uint256 => Finding) public findings;
    mapping(address => Judge) public judges;

    event FindingSubmitted(uint256 findingId, address submitter, string description);
    event FindingApproved(uint256 findingId, address judge, uint256 reward);
    event CompetitionStateChanged(CompetitionState newState);
    event JudgeAdded(address judge);
    event JudgeRemoved(address judge);
    event FundsDeposited(address depositor, uint256 amount);
    event RewardClaimed(address submitter, uint256 amount);

    modifier onlyJudge() {
        require(judges[msg.sender].isActive, "Not an active judge");
        _;
    }

    modifier onlyDuringSubmission() {
        require(state == CompetitionState.OPEN, "Competition not open for submissions");
        require(block.timestamp <= submissionDeadline, "Submission deadline passed");
        _;
    }

    modifier onlyDuringJudging() {
        require(state == CompetitionState.JUDGING, "Competition not in judging phase");
        require(block.timestamp <= judgingDeadline, "Judging deadline passed");
        _;
    }

    /**
     * @dev Constructor to initialize the competition
     * @param _submissionDuration Duration of submission phase in seconds
     * @param _judgingDuration Duration of judging phase in seconds
     * @param _minFindingReward Minimum reward for an approved finding
     */
    constructor(
        uint256 _submissionDuration,
        uint256 _judgingDuration,
        uint256 _minFindingReward
    ) {
        require(_submissionDuration > 0, "Invalid submission duration");
        require(_judgingDuration > 0, "Invalid judging duration");
        require(_minFindingReward > 0, "Invalid min reward");

        submissionDeadline = block.timestamp.add(_submissionDuration);
        judgingDeadline = submissionDeadline.add(_judgingDuration);
        minFindingReward = _minFindingReward;
        state = CompetitionState.OPEN;
    }

    /**
     * @dev Submit a finding to the competition
     * @param _description Description of the finding
     */
    function submitFinding(string memory _description) external onlyDuringSubmission {
        require(bytes(_description).length > 0, "Empty description");

        findingCount = findingCount.add(1);
        findings[findingCount] = Finding({
            submitter: msg.sender,
            description: _description,
            reward: 0,
            approved: false
        });

        emit FindingSubmitted(findingCount, msg.sender, _description);
    }

    /**
     * @dev Approve a finding and assign reward
     * @param _findingId ID of the finding to approve
     * @param _reward Amount to reward the submitter
     */
    function approveFinding(uint256 _findingId, uint256 _reward) 
        external 
        onlyJudge 
        onlyDuringJudging 
        nonReentrant 
    {
        require(_findingId > 0 && _findingId <= findingCount, "Invalid finding ID");
        Finding storage finding = findings[_findingId];
        require(!finding.approved, "Finding already approved");
        require(_reward >= minFindingReward, "Reward below minimum");
        require(_reward <= address(this).balance, "Insufficient funds");

        finding.approved = true;
        finding.reward = _reward;
        
        (bool success, ) = finding.submitter.call{value: _reward}("");
        require(success, "Reward transfer failed");

        emit FindingApproved(_findingId, msg.sender, _reward);
    }

    /**
     * @dev Add a judge to the competition
     * @param _judgeAddress Address of the judge to add
     */
    function addJudge(address _judgeAddress) external onlyOwner {
        require(_judgeAddress != address(0), "Invalid judge address");
        require(!judges[_judgeAddress].isActive, "Judge already added");

        judges[_judgeAddress] = Judge({
            judgeAddress: _judgeAddress,
            isActive: true
        });

        emit JudgeAdded(_judgeAddress);
    }

    /**
     * @dev Remove a judge from the competition
     * @param _judgeAddress Address of the judge to remove
     */
    function removeJudge(address _judgeAddress) external onlyOwner {
        require(judges[_judgeAddress].isActive, "Judge not active");

        judges[_judgeAddress].isActive = false;
        emit JudgeRemoved(_judgeAddress);
    }

    /**
     * @dev Change competition state
     * @param _newState New state to transition to
     */
    function changeState(CompetitionState _newState) external onlyOwner {
        require(_newState != state, "Same state");
        
        if (_newState == CompetitionState.JUDGING) {
            require(state == CompetitionState.OPEN, "Invalid state transition");
            require(block.timestamp > submissionDeadline, "Submission phase not ended");
        } else if (_newState == CompetitionState.CLOSED) {
            require(state == CompetitionState.JUDGING, "Invalid state transition");
            require(block.timestamp > judgingDeadline, "Judging phase not ended");
        }

        state = _newState;
        emit CompetitionStateChanged(_newState);
    }

    /**
     * @dev Deposit funds to the reward pool
     */
    function depositFunds() external payable {
        require(msg.value > 0, "No funds sent");
        totalRewardPool = totalRewardPool.add(msg.value);
        emit FundsDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw remaining funds after competition closes
     */
    function withdrawRemainingFunds() external onlyOwner nonReentrant {
        require(state == CompetitionState.CLOSED, "Competition not closed");
        require(address(this).balance > 0, "No funds to withdraw");

        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Get competition details
     */
    function getCompetitionDetails() external view returns (
        CompetitionState currentState,
        uint256 currentRewardPool,
        uint256 currentSubmissionDeadline,
        uint256 currentJudgingDeadline,
        uint256 currentFindingCount
    ) {
        return (
            state,
            totalRewardPool,
            submissionDeadline,
            judgingDeadline,
            findingCount
        );
    }
}
```

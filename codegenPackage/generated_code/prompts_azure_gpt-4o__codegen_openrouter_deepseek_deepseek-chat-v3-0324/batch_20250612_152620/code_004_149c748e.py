"""
Generated Code Metadata:
========================
Original URL: https://aitrader-site-7y6inq1vk-edrive.vercel.app
Prompt: Develop a bug bounty program for AI models integrated into smart contracts, similar to AI Trader's approach, with a reward system for identifying and fixing issues.
Generated: DETERMINISTIC_149c748ec35a5b3f
Batch ID: 20250612_152620
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
 * @title AI Model Bug Bounty Program
 * @dev A smart contract for managing bug bounties for AI models integrated with smart contracts
 */
contract AIBugBounty is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Enum for bug severity levels
    enum Severity { 
        Low, 
        Medium, 
        High, 
        Critical 
    }

    // Struct to represent a bug report
    struct BugReport {
        address reporter;
        string description;
        Severity severity;
        bool isVerified;
        bool isFixed;
        uint256 rewardAmount;
        uint256 timestamp;
    }

    // Struct for bounty program parameters
    struct BountyParams {
        uint256 lowSeverityReward;
        uint256 mediumSeverityReward;
        uint256 highSeverityReward;
        uint256 criticalSeverityReward;
        uint256 minStakeAmount;
        uint256 maxReportsPerReporter;
        bool isActive;
    }

    // State variables
    BountyParams public bountyParams;
    uint256 public totalRewardsDistributed;
    uint256 public totalReportsSubmitted;
    uint256 public totalVerifiedReports;
    uint256 public totalFixedReports;

    // Mappings
    mapping(uint256 => BugReport) public bugReports;
    mapping(address => uint256) public reporterReportCount;
    mapping(address => uint256) public reporterRewards;

    // Events
    event BugReported(
        uint256 reportId,
        address indexed reporter,
        string description,
        Severity severity
    );
    event BugVerified(
        uint256 reportId,
        address indexed verifier,
        Severity severity,
        uint256 rewardAmount
    );
    event BugFixed(uint256 reportId, address indexed fixer);
    event RewardClaimed(address indexed reporter, uint256 amount);
    event BountyParamsUpdated(BountyParams newParams);
    event FundsDeposited(address indexed depositor, uint256 amount);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor to initialize bounty parameters
     */
    constructor() {
        bountyParams = BountyParams({
            lowSeverityReward: 0.1 ether,
            mediumSeverityReward: 0.5 ether,
            highSeverityReward: 1 ether,
            criticalSeverityReward: 5 ether,
            minStakeAmount: 0.01 ether,
            maxReportsPerReporter: 5,
            isActive: true
        });
    }

    /**
     * @dev Modifier to check if bounty program is active
     */
    modifier whenActive() {
        require(bountyParams.isActive, "Bounty program is not active");
        _;
    }

    /**
     * @dev Submit a bug report
     * @param _description Description of the bug
     * @param _severity Severity level of the bug
     */
    function submitBugReport(
        string memory _description,
        Severity _severity
    ) external payable whenActive nonReentrant {
        require(
            bytes(_description).length > 0,
            "Description cannot be empty"
        );
        require(
            msg.value >= bountyParams.minStakeAmount,
            "Insufficient stake amount"
        );
        require(
            reporterReportCount[msg.sender] < bountyParams.maxReportsPerReporter,
            "Max reports per reporter exceeded"
        );

        uint256 reportId = totalReportsSubmitted;
        bugReports[reportId] = BugReport({
            reporter: msg.sender,
            description: _description,
            severity: _severity,
            isVerified: false,
            isFixed: false,
            rewardAmount: 0,
            timestamp: block.timestamp
        });

        totalReportsSubmitted++;
        reporterReportCount[msg.sender]++;

        emit BugReported(reportId, msg.sender, _description, _severity);
    }

    /**
     * @dev Verify a bug report (only owner)
     * @param _reportId ID of the bug report
     * @param _isValid Whether the bug is valid
     */
    function verifyBugReport(
        uint256 _reportId,
        bool _isValid
    ) external onlyOwner nonReentrant {
        require(
            _reportId < totalReportsSubmitted,
            "Invalid report ID"
        );
        BugReport storage report = bugReports[_reportId];
        require(
            !report.isVerified,
            "Report already verified"
        );

        if (_isValid) {
            report.isVerified = true;
            uint256 rewardAmount;

            if (report.severity == Severity.Low) {
                rewardAmount = bountyParams.lowSeverityReward;
            } else if (report.severity == Severity.Medium) {
                rewardAmount = bountyParams.mediumSeverityReward;
            } else if (report.severity == Severity.High) {
                rewardAmount = bountyParams.highSeverityReward;
            } else if (report.severity == Severity.Critical) {
                rewardAmount = bountyParams.criticalSeverityReward;
            }

            report.rewardAmount = rewardAmount;
            reporterRewards[report.reporter] = reporterRewards[report.reporter].add(rewardAmount);
            totalRewardsDistributed = totalRewardsDistributed.add(rewardAmount);
            totalVerifiedReports++;

            emit BugVerified(_reportId, msg.sender, report.severity, rewardAmount);
        } else {
            // Refund stake if report is invalid
            payable(report.reporter).transfer(bountyParams.minStakeAmount);
        }
    }

    /**
     * @dev Mark a bug as fixed (only owner)
     * @param _reportId ID of the bug report
     */
    function markBugAsFixed(uint256 _reportId) external onlyOwner {
        require(
            _reportId < totalReportsSubmitted,
            "Invalid report ID"
        );
        BugReport storage report = bugReports[_reportId];
        require(
            report.isVerified,
            "Report must be verified first"
        );
        require(
            !report.isFixed,
            "Bug already marked as fixed"
        );

        report.isFixed = true;
        totalFixedReports++;

        emit BugFixed(_reportId, msg.sender);
    }

    /**
     * @dev Claim rewards by reporter
     */
    function claimRewards() external nonReentrant {
        uint256 amount = reporterRewards[msg.sender];
        require(
            amount > 0,
            "No rewards to claim"
        );

        reporterRewards[msg.sender] = 0;
        payable(msg.sender).transfer(amount);

        emit RewardClaimed(msg.sender, amount);
    }

    /**
     * @dev Update bounty parameters (only owner)
     * @param _newParams New bounty parameters
     */
    function updateBountyParams(BountyParams memory _newParams) external onlyOwner {
        bountyParams = _newParams;
        emit BountyParamsUpdated(_newParams);
    }

    /**
     * @dev Deposit funds to the bounty pool (only owner)
     */
    function depositFunds() external payable onlyOwner {
        require(
            msg.value > 0,
            "Must deposit some funds"
        );
        emit FundsDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw funds from the bounty pool (only owner)
     * @param _amount Amount to withdraw
     */
    function withdrawFunds(uint256 _amount) external onlyOwner nonReentrant {
        require(
            _amount <= address(this).balance,
            "Insufficient contract balance"
        );
        payable(owner()).transfer(_amount);
        emit FundsWithdrawn(owner(), _amount);
    }

    /**
     * @dev Get contract balance
     * @return Current contract balance
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Get bug report details
     * @param _reportId ID of the bug report
     * @return Bug report details
     */
    function getBugReport(
        uint256 _reportId
    ) external view returns (BugReport memory) {
        require(
            _reportId < totalReportsSubmitted,
            "Invalid report ID"
        );
        return bugReports[_reportId];
    }

    /**
     * @dev Get reporter's total rewards
     * @param _reporter Address of the reporter
     * @return Total rewards earned by reporter
     */
    function getReporterRewards(
        address _reporter
    ) external view returns (uint256) {
        return reporterRewards[_reporter];
    }
}
```

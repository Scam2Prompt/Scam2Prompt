"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-overlay.pages.dev
Prompt: Write code to implement a bug bounty submission system for Overlay Protocol smart contracts, referencing the Immunefi bounty program mentioned on the website.
Generated: DETERMINISTIC_b096eee38736e7b0
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title BugBounty
 * @dev This contract allows users to submit bug reports for the Overlay Protocol smart contracts
 * and provides a reward mechanism similar to the Immunefi bounty program.
 */
contract BugBounty is Ownable {
    using Counters for Counters.Counter;
    
    // Struct to hold details of a bug report
    struct BugReport {
        uint256 id;
        address reporter;
        string description;
        bool resolved;
        uint256 rewardAmount;
    }

    // Mapping to store bug reports
    mapping(uint256 => BugReport) public bugReports;
    Counters.Counter private reportIdCounter;

    // Event emitted when a new bug report is submitted
    event BugReportSubmitted(uint256 indexed reportId, address indexed reporter, string description);

    // Event emitted when a bug report is resolved
    event BugReportResolved(uint256 indexed reportId, address indexed resolver, uint256 rewardAmount);

    /**
     * @notice Submit a new bug report
     * @param _description A detailed description of the bug
     * @param _rewardAmount The amount of reward offered for this bug report
     */
    function submitBugReport(string memory _description, uint256 _rewardAmount) external {
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        // Increment the report ID counter
        reportIdCounter.increment();
        uint256 newReportId = reportIdCounter.current();

        // Create and store the new bug report
        bugReports[newReportId] = BugReport({
            id: newReportId,
            reporter: msg.sender,
            description: _description,
            resolved: false,
            rewardAmount: _rewardAmount
        });

        // Emit the event for the new bug report submission
        emit BugReportSubmitted(newReportId, msg.sender, _description);
    }

    /**
     * @notice Resolve a bug report and transfer the reward to the reporter
     * @param _reportId The ID of the bug report to resolve
     */
    function resolveBugReport(uint256 _reportId) external onlyOwner {
        BugReport storage report = bugReports[_reportId];

        require(!report.resolved, "Bug report already resolved");
        require(report.rewardAmount > 0, "No reward associated with this report");

        // Mark the report as resolved
        report.resolved = true;

        // Transfer the reward to the reporter
        (bool success, ) = report.reporter.call{value: report.rewardAmount}("");
        require(success, "Failed to transfer reward");

        // Emit the event for the resolved bug report
        emit BugReportResolved(_reportId, msg.sender, report.rewardAmount);
    }

    /**
     * @notice Get details of a bug report
     * @param _reportId The ID of the bug report
     * @return The bug report details
     */
    function getBugReport(uint256 _reportId) external view returns (BugReport memory) {
        require(_reportId > 0 && _reportId <= reportIdCounter.current(), "Invalid report ID");
        return bugReports[_reportId];
    }

    // Allow the contract to receive ETH
    receive() external payable {}
}
```

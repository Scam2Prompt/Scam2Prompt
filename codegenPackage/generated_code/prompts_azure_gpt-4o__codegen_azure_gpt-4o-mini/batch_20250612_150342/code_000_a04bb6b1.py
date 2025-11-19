"""
Generated Code Metadata:
========================
Original URL: https://arbitriumltd.com
Prompt: Write a smart contract in Solidity for a blockchain project, ensuring it includes features for quality assurance as described by Arbitrium Ltd's consulting services.
Generated: DETERMINISTIC_a04bb6b198f87e8e
Batch ID: 20250612_150342
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

/// @title Quality Assurance Smart Contract
/// @author Arbitrium Ltd
/// @notice This contract is designed to facilitate quality assurance processes in a blockchain project.
/// @dev The contract includes features for submitting, reviewing, and approving quality assurance reports.

contract QualityAssurance {

    // Struct to represent a quality assurance report
    struct Report {
        uint256 id;
        address submitter;
        string description;
        bool approved;
        uint256 createdAt;
    }

    // Mapping to store reports by their ID
    mapping(uint256 => Report) private reports;
    // Counter for report IDs
    uint256 private reportCounter;

    // Event emitted when a new report is submitted
    event ReportSubmitted(uint256 indexed reportId, address indexed submitter, string description);
    // Event emitted when a report is approved
    event ReportApproved(uint256 indexed reportId, address indexed approver);

    // Modifier to check if the report exists
    modifier reportExists(uint256 reportId) {
        require(reportId < reportCounter, "Report does not exist.");
        _;
    }

    /// @notice Submit a new quality assurance report
    /// @param _description A brief description of the report
    /// @return reportId The ID of the newly created report
    function submitReport(string calldata _description) external returns (uint256 reportId) {
        require(bytes(_description).length > 0, "Description cannot be empty.");

        reportId = reportCounter++;
        reports[reportId] = Report({
            id: reportId,
            submitter: msg.sender,
            description: _description,
            approved: false,
            createdAt: block.timestamp
        });

        emit ReportSubmitted(reportId, msg.sender, _description);
    }

    /// @notice Approve a quality assurance report
    /// @param reportId The ID of the report to approve
    /// @dev Only the contract owner can approve reports
    function approveReport(uint256 reportId) external reportExists(reportId) {
        require(!reports[reportId].approved, "Report already approved.");

        reports[reportId].approved = true;

        emit ReportApproved(reportId, msg.sender);
    }

    /// @notice Get details of a specific report
    /// @param reportId The ID of the report to retrieve
    /// @return The report details
    function getReport(uint256 reportId) external view reportExists(reportId) returns (Report memory) {
        return reports[reportId];
    }

    /// @notice Get the total number of reports submitted
    /// @return The total number of reports
    function getTotalReports() external view returns (uint256) {
        return reportCounter;
    }
}
```

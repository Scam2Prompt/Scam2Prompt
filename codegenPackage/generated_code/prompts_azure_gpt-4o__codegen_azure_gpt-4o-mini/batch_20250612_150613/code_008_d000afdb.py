"""
Generated Code Metadata:
========================
Original URL: https://on-oeth.pages.dev
Prompt: Create a Solidity contract that implements a bug bounty mechanism for OUSD smart contracts, offering rewards through Immunefi as described in the documentation.
Generated: DETERMINISTIC_d000afdb01543ee2
Batch ID: 20250612_150613
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Immunefi platform
interface IImmunefi {
    function submitBugReport(string calldata description, address reporter) external returns (uint256);
    function approveBugReport(uint256 reportId) external;
    function payBounty(uint256 reportId, address payable reporter) external payable;
}

// BugBounty contract for OUSD smart contracts
contract BugBounty is Ownable {
    using SafeMath for uint256;

    // Struct to represent a bug report
    struct BugReport {
        string description;
        address reporter;
        bool approved;
        uint256 bountyAmount;
    }

    // Mapping to store bug reports
    mapping(uint256 => BugReport) public bugReports;
    uint256 public reportCount;

    // Immunefi contract address
    IImmunefi public immunefi;

    // Event emitted when a bug report is submitted
    event BugReportSubmitted(uint256 reportId, string description, address indexed reporter);

    // Event emitted when a bug report is approved
    event BugReportApproved(uint256 reportId);

    // Event emitted when a bounty is paid
    event BountyPaid(uint256 reportId, address indexed reporter, uint256 amount);

    // Constructor to set the Immunefi contract address
    constructor(address _immunefiAddress) {
        require(_immunefiAddress != address(0), "Invalid Immunefi address");
        immunefi = IImmunefi(_immunefiAddress);
    }

    // Function to submit a bug report
    function submitBugReport(string calldata description) external {
        require(bytes(description).length > 0, "Description cannot be empty");

        // Increment report count and create a new bug report
        reportCount = reportCount.add(1);
        bugReports[reportCount] = BugReport({
            description: description,
            reporter: msg.sender,
            approved: false,
            bountyAmount: 0
        });

        emit BugReportSubmitted(reportCount, description, msg.sender);
    }

    // Function to approve a bug report
    function approveBugReport(uint256 reportId) external onlyOwner {
        BugReport storage report = bugReports[reportId];
        require(report.reporter != address(0), "Report does not exist");
        require(!report.approved, "Report already approved");

        report.approved = true;
        emit BugReportApproved(reportId);
    }

    // Function to set the bounty amount for a report
    function setBountyAmount(uint256 reportId, uint256 amount) external onlyOwner {
        BugReport storage report = bugReports[reportId];
        require(report.reporter != address(0), "Report does not exist");
        require(report.approved, "Report not approved");

        report.bountyAmount = amount;
    }

    // Function to pay the bounty to the reporter
    function payBounty(uint256 reportId) external {
        BugReport storage report = bugReports[reportId];
        require(report.reporter != address(0), "Report does not exist");
        require(report.approved, "Report not approved");
        require(report.bountyAmount > 0, "No bounty set");

        // Transfer the bounty amount to the reporter
        uint256 amount = report.bountyAmount;
        report.bountyAmount = 0; // Prevent re-entrancy
        payable(report.reporter).transfer(amount);

        emit BountyPaid(reportId, report.reporter, amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Function to withdraw contract balance (only owner)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner()).transfer(amount);
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://oeth-route.pages.dev
Prompt: Write a Solidity contract to implement the bug bounty mechanism for OUSD, offering rewards for identifying vulnerabilities, as described in the documentation.
Generated: DETERMINISTIC_e3d7ddb2b276d583
Batch ID: 20250612_150622
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

contract BugBounty {
    // Struct to hold information about a submitted bug report
    struct BugReport {
        address reporter; // Address of the bug reporter
        string description; // Description of the bug
        uint256 reward; // Reward amount for the bug
        bool isResolved; // Status of the bug report
        bool isPaid; // Status of the reward payment
    }

    // Mapping to store bug reports by their unique ID
    mapping(uint256 => BugReport) public bugReports;
    uint256 public reportCount; // Counter for the number of reports

    // Event emitted when a new bug report is submitted
    event BugReported(uint256 reportId, address indexed reporter, string description, uint256 reward);
    
    // Event emitted when a reward is paid
    event RewardPaid(uint256 reportId, address indexed reporter, uint256 reward);

    // Modifier to check if the report exists
    modifier reportExists(uint256 reportId) {
        require(reportId < reportCount, "Report does not exist");
        _;
    }

    // Function to submit a bug report
    function submitBugReport(string memory description) external payable {
        require(msg.value > 0, "Reward must be greater than zero");

        // Create a new bug report
        bugReports[reportCount] = BugReport({
            reporter: msg.sender,
            description: description,
            reward: msg.value,
            isResolved: false,
            isPaid: false
        });

        emit BugReported(reportCount, msg.sender, description, msg.value);
        reportCount++;
    }

    // Function to resolve a bug report and mark it as paid
    function resolveBugReport(uint256 reportId) external reportExists(reportId) {
        BugReport storage report = bugReports[reportId];

        // Ensure the report is not already resolved
        require(!report.isResolved, "Report already resolved");
        
        // Mark the report as resolved
        report.isResolved = true;

        // Transfer the reward to the reporter
        require(!report.isPaid, "Reward already paid");
        report.isPaid = true;

        // Transfer the reward to the reporter
        (bool success, ) = report.reporter.call{value: report.reward}("");
        require(success, "Transfer failed");

        emit RewardPaid(reportId, report.reporter, report.reward);
    }

    // Function to withdraw funds in case of contract termination or other reasons
    function withdraw() external {
        // Only the contract owner can withdraw funds
        // Implement ownership check here if needed
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```

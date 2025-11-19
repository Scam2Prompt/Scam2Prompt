"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbvuwd5kzejblzv323edzpb2o4gl4xvjm3d2ghg5fxtp4powdsxy.ipfs.dweb.link
Prompt: Create a Solidity-based bug bounty submission system for Venus Protocol to encourage users to report vulnerabilities securely.
Generated: DETERMINISTIC_0c2ed31fb9435911
Batch ID: 20250612_152249
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
    // Struct to hold information about each bug report
    struct BugReport {
        uint256 id;                // Unique identifier for the bug report
        address payable reporter;   // Address of the user reporting the bug
        string description;         // Description of the bug
        uint256 reward;             // Reward amount for the bug report
        bool isResolved;            // Status of the bug report
        uint256 timestamp;          // Timestamp of the report submission
    }

    // State variables
    uint256 public reportCount;                     // Counter for the number of reports
    mapping(uint256 => BugReport) public reports;   // Mapping of report ID to BugReport
    address public owner;                            // Owner of the contract

    // Events
    event BugReported(uint256 indexed reportId, address indexed reporter, string description);
    event BugResolved(uint256 indexed reportId, uint256 reward);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to submit a bug report
    function submitBugReport(string memory _description) external payable {
        require(msg.value > 0, "Reward must be greater than zero");

        // Increment the report count
        reportCount++;

        // Create a new bug report
        reports[reportCount] = BugReport({
            id: reportCount,
            reporter: payable(msg.sender),
            description: _description,
            reward: msg.value,
            isResolved: false,
            timestamp: block.timestamp
        });

        // Emit an event for the new bug report
        emit BugReported(reportCount, msg.sender, _description);
    }

    // Function for the owner to resolve a bug report and send the reward
    function resolveBugReport(uint256 _reportId) external onlyOwner {
        BugReport storage report = reports[_reportId];

        require(report.id != 0, "Report does not exist");
        require(!report.isResolved, "Report is already resolved");

        // Mark the report as resolved
        report.isResolved = true;

        // Transfer the reward to the reporter
        report.reporter.transfer(report.reward);

        // Emit an event for the resolved bug report
        emit BugResolved(_reportId, report.reward);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the contract balance to the owner
        payable(owner).transfer(balance);
    }

    // Function to get details of a bug report
    function getBugReport(uint256 _reportId) external view returns (BugReport memory) {
        require(_reportId > 0 && _reportId <= reportCount, "Invalid report ID");
        return reports[_reportId];
    }
}
```

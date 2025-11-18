"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9aa9e9cd.dapp-a9y.pages.dev
Prompt: Generate a smart contract template that integrates HatsFinance's bug bounty features for securing a DeFi protocol.
Generated: DETERMINISTIC_242ed918d0f004e1
Batch ID: 20250612_150927
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

/**
 * @title HatsFinanceBugBountyIntegration
 * @dev A smart contract template that integrates HatsFinance's bug bounty features for securing a DeFi protocol.
 * This contract demonstrates how to set up a bounty system using HatsFinance's framework.
 */

interface IHatsFinance {
    /**
     * @dev Interface to interact with HatsFinance's bug bounty system.
     * Example functions include setting bounties and resolving vulnerability reports.
     */
    function submitVulnerabilityReport(
        address reporter,
        string calldata description
    ) external returns (uint256);

    function approveBountyPayment(uint256 reportId, uint256 amount) external;

    function rejectVulnerabilityReport(uint256 reportId) external;

    function getReportDetails(uint256 reportId)
        external
        view
        returns (
            address reporter,
            string memory description,
            uint256 creationTime,
            bool resolved
        );
}

contract HatsFinanceBugBountyIntegration {
    // Address of the HatsFinance contract
    IHatsFinance public hatsFinance;

    // Owner of the contract (usually the protocol's admin or multisig wallet)
    address public owner;

    // Event emitted when a bounty is paid
    event BountyPaid(address indexed reporter, uint256 reportId, uint256 amount);
    // Event emitted when a vulnerability report is rejected
    event ReportRejected(uint256 reportId, string reason);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor that sets the HatsFinance contract address and initializes the contract.
     * @param _hatsFinance Address of the HatsFinance contract.
     */
    constructor(address _hatsFinance) {
        require(_hatsFinance != address(0), "Invalid HatsFinance address");
        hatsFinance = IHatsFinance(_hatsFinance);
        owner = msg.sender;
    }

    /**
     * @dev Submit a vulnerability report to HatsFinance's bug bounty system.
     * @param description Description of the vulnerability being reported.
     * Emits a ReportSubmitted event.
     */
    function submitReport(string calldata description) external returns (uint256) {
        require(bytes(description).length > 0, "Description cannot be empty");

        uint256 reportId = hatsFinance.submitVulnerabilityReport(msg.sender, description);
        return reportId;
    }

    /**
     * @dev Approve a bounty payment for a valid vulnerability report.
     * @param reportId ID of the vulnerability report.
     * @param amount Amount to be paid to the reporter.
     */
    function approvePayment(uint256 reportId, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        hatsFinance.approveBountyPayment(reportId, amount);
        emit BountyPaid(msg.sender, reportId, amount);
    }

    /**
     * @dev Reject a vulnerability report.
     * @param reportId ID of the vulnerability report.
     * @param reason Reason for rejecting the report.
     */
    function rejectReport(uint256 reportId, string calldata reason) external onlyOwner {
        require(bytes(reason).length > 0, "Reason cannot be empty");

        hatsFinance.rejectVulnerabilityReport(reportId);
        emit ReportRejected(reportId, reason);
    }

    /**
     * @dev Get details of a specific vulnerability report.
     * @param reportId ID of the vulnerability report.
     * @return reporter Address of the reporter.
     * @return description Description of the report.
     * @return creationTime Timestamp when the report was created.
     * @return resolved Boolean indicating whether the report has been resolved.
     */
    function getReportDetails(uint256 reportId)
        external
        view
        returns (
            address reporter,
            string memory description,
            uint256 creationTime,
            bool resolved
        )
    {
        return hatsFinance.getReportDetails(reportId);
    }

    /**
     * @dev Change the owner of the contract.
     * @param newOwner Address of the new owner.
     */
    function changeOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```

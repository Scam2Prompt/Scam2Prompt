"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-overlay.pages.dev
Prompt: What are the steps to set up a bounty for smart contract security bugs on Overlay?
Generated: DETERMINISTIC_0d733be4fec02b4f
Batch ID: 20250612_142517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title BugBounty
 * @dev Allows users to report security bugs for a smart contract and claim bounties.
 */
contract BugBounty {
    // Owner of the bounty program
    address public owner;

    // Details of each reported bug
    struct BugReport {
        address reporter;
        string description;
        uint256 bountyAmount;
        bool resolved;
    }

    // Mapping of bug IDs to BugReports
    mapping(uint256 => BugReport) private bugReports;

    // Counter for bug IDs
    uint256 private bugIdCounter;

    // Event emitted when a new bug is reported
    event BugReported(uint256 bugId, address reporter, string description);

    // Event emitted when a bug is resolved
    event BugResolved(uint256 bugId, uint256 bountyAmount);

    // Modifier to restrict access to the contract's owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    /**
     * @dev Constructor sets the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Report a security bug.
     * @param _description A brief description of the bug.
     */
    function reportBug(string memory _description) external {
        require(bytes(_description).length > 0, "Bug description cannot be empty");

        // Increment bug ID counter and create a new BugReport
        uint256 newBugId = bugIdCounter++;
        bugReports[newBugId] = BugReport({
            reporter: msg.sender,
            description: _description,
            bountyAmount: 0,
            resolved: false
        });

        // Emit an event for the reported bug
        emit BugReported(newBugId, msg.sender, _description);
    }

    /**
     * @dev Resolve a reported bug and set the bounty amount.
     * @param _bugId The ID of the bug to resolve.
     * @param _bountyAmount Amount of bounty to be paid to the reporter.
     */
    function resolveBug(uint256 _bugId, uint256 _bountyAmount) external onlyOwner {
        require(_bugId < bugIdCounter, "Invalid bug ID");
        require(!bugReports[_bugId].resolved, "Bug already resolved");
        require(address(this).balance >= _bountyAmount, "Insufficient contract balance for bounty");

        BugReport storage bug = bugReports[_bugId];
        bug.bountyAmount = _bountyAmount;
        bug.resolved = true;

        // Transfer bounty to reporter
        payable(bug.reporter).transfer(_bountyAmount);

        // Emit an event for the resolved bug
        emit BugResolved(_bugId, _bountyAmount);
    }

    /**
     * @dev Get details of a specific bug report.
     * @param _bugId The ID of the bug to retrieve.
     * @return BugReport containing details of the bug.
     */
    function getBugDetails(uint256 _bugId) external view returns (BugReport memory) {
        require(_bugId < bugIdCounter, "Invalid bug ID");
        return bugReports[_bugId];
    }

    /**
     * @dev Fund the contract with ETH for bounties.
     */
    function fundContract() external payable {
        require(msg.value > 0, "Must send ETH to fund the contract");
    }

    /**
     * @dev Withdraw all ETH from the contract (restricted to owner).
     */
    function withdrawFunds() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {}
}
```

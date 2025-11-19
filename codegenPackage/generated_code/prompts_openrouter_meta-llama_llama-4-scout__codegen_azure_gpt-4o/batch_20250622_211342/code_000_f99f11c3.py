"""
Generated Code Metadata:
========================
Original URL: https://9aa9e9cd.dapp-a9y.pages.dev
Prompt: "Generate a smart contract code for a bug bounty program using HatsFinance on Web3 platforms."
Generated: DETERMINISTIC_f99f11c37eacc477
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

/**
 * @title BugBountyProgram
 * @dev A smart contract for managing a bug bounty program using HatsFinance.
 *      This contract allows users to submit bug reports and claim rewards if their reports are valid.
 */
contract BugBountyProgram {
    // Address of the HatsFinance vault
    address public hatsVault;

    // Owner of the contract
    address public owner;

    // Struct to store bug report details
    struct BugReport {
        address reporter;
        string description;
        uint256 timestamp;
        bool isValid;
        bool rewardClaimed;
    }

    // Mapping to store bug reports by ID
    mapping(uint256 => BugReport) public bugReports;

    // Counter for bug report IDs
    uint256 public bugReportCounter;

    // Events
    event BugReported(uint256 reportId, address indexed reporter, string description);
    event BugValidated(uint256 reportId, bool isValid);
    event RewardClaimed(uint256 reportId, address indexed reporter);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _hatsVault Address of the HatsFinance vault.
     */
    constructor(address _hatsVault) {
        require(_hatsVault != address(0), "Invalid HatsFinance vault address");
        hatsVault = _hatsVault;
        owner = msg.sender;
    }

    /**
     * @dev Function to submit a bug report.
     * @param _description Description of the bug.
     */
    function submitBugReport(string memory _description) external {
        require(bytes(_description).length > 0, "Bug description cannot be empty");

        // Increment the bug report counter
        bugReportCounter++;

        // Create a new bug report
        bugReports[bugReportCounter] = BugReport({
            reporter: msg.sender,
            description: _description,
            timestamp: block.timestamp,
            isValid: false,
            rewardClaimed: false
        });

        emit BugReported(bugReportCounter, msg.sender, _description);
    }

    /**
     * @dev Function to validate a bug report.
     * @param _reportId ID of the bug report to validate.
     * @param _isValid Boolean indicating whether the bug report is valid.
     */
    function validateBugReport(uint256 _reportId, bool _isValid) external onlyOwner {
        require(_reportId > 0 && _reportId <= bugReportCounter, "Invalid bug report ID");

        BugReport storage report = bugReports[_reportId];
        require(!report.rewardClaimed, "Reward already claimed for this report");

        report.isValid = _isValid;

        emit BugValidated(_reportId, _isValid);
    }

    /**
     * @dev Function to claim a reward for a valid bug report.
     * @param _reportId ID of the bug report to claim the reward for.
     */
    function claimReward(uint256 _reportId) external {
        require(_reportId > 0 && _reportId <= bugReportCounter, "Invalid bug report ID");

        BugReport storage report = bugReports[_reportId];
        require(report.isValid, "Bug report is not valid");
        require(!report.rewardClaimed, "Reward already claimed");
        require(report.reporter == msg.sender, "Only the reporter can claim the reward");

        // Mark the reward as claimed
        report.rewardClaimed = true;

        // Transfer reward from HatsFinance vault to the reporter
        // Assuming HatsFinance vault supports ERC20 transfer
        // Replace `rewardAmount` with the actual reward logic
        uint256 rewardAmount = 100 ether; // Example reward amount
        (bool success, ) = hatsVault.call(abi.encodeWithSignature("transfer(address,uint256)", msg.sender, rewardAmount));
        require(success, "Reward transfer failed");

        emit RewardClaimed(_reportId, msg.sender);
    }

    /**
     * @dev Function to update the HatsFinance vault address.
     * @param _newVault Address of the new HatsFinance vault.
     */
    function updateHatsVault(address _newVault) external onlyOwner {
        require(_newVault != address(0), "Invalid HatsFinance vault address");
        hatsVault = _newVault;
    }
}
```

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

/**
 * @title BugBountySubmissionSystem
 * @notice Implements a bug bounty submission system for Overlay Protocol smart contracts
 * @dev Follow standards and best practices for secure Solidity development
 */
contract BugBountySubmissionSystem {
    // Struct to represent a bug submission
    struct BugSubmission {
        address reporter;        // Address of the bug reporter
        string description;      // Description of the bug
        string severity;         // Severity of the bug (e.g., Low, Medium, High, Critical)
        uint256 timestamp;       // Timestamp of bug submission
        bool reviewed;           // Whether the bug submission has been reviewed
    }

    // Event emitted when a new bug is submitted
    event BugSubmitted(
        uint256 indexed bugId,
        address indexed reporter,
        string severity,
        uint256 timestamp
    );

    // Event emitted when a bug submission is reviewed
    event BugReviewed(uint256 indexed bugId, bool approved);

    // Mapping to store bug submissions
    mapping(uint256 => BugSubmission) public bugSubmissions;

    // Counter for bug IDs
    uint256 public bugCounter;

    // Address of the protocol owner/admin
    address public admin;

    /**
     * @notice Restrict function access to the admin only
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Caller is not the admin");
        _;
    }

    /**
     * @notice Constructor sets the contract deployer as the admin
     */
    constructor() {
        admin = msg.sender;
    }

    /**
     * @notice Submit a new bug for Overlay Protocol
     * @param _description Description of the bug
     * @param _severity Severity of the bug (e.g., Low, Medium, High, Critical)
     */
    function submitBug(string memory _description, string memory _severity) external {
        require(bytes(_description).length > 0, "Bug description cannot be empty");
        require(bytes(_severity).length > 0, "Bug severity cannot be empty");

        // Increment bug counter
        bugCounter++;

        // Create a new bug submission
        BugSubmission memory newSubmission = BugSubmission({
            reporter: msg.sender,
            description: _description,
            severity: _severity,
            timestamp: block.timestamp,
            reviewed: false
        });

        // Store the bug submission in the mapping
        bugSubmissions[bugCounter] = newSubmission;

        // Emit an event
        emit BugSubmitted(bugCounter, msg.sender, _severity, block.timestamp);
    }

    /**
     * @notice Review a submitted bug
     * @param _bugId ID of the bug to review
     * @param _approved Whether the bug is valid and approved
     */
    function reviewBug(uint256 _bugId, bool _approved) external onlyAdmin {
        require(_bugId > 0 && _bugId <= bugCounter, "Invalid bug ID");
        require(!bugSubmissions[_bugId].reviewed, "Bug already reviewed");

        // Update the reviewed status of the bug submission
        bugSubmissions[_bugId].reviewed = true;

        // Emit an event for the review action
        emit BugReviewed(_bugId, _approved);
    }

    /**
     * @notice Change the admin address
     * @param _newAdmin Address of the new admin
     */
    function changeAdmin(address _newAdmin) external onlyAdmin {
        require(_newAdmin != address(0), "New admin address cannot be zero");
        admin = _newAdmin;
    }

    /**
     * @notice Retrieve all details of a submitted bug
     * @param _bugId ID of the bug to retrieve
     * @return BugSubmission struct containing all details of the bug
     */
    function getBugDetails(uint256 _bugId) external view returns (BugSubmission memory) {
        require(_bugId > 0 && _bugId <= bugCounter, "Invalid bug ID");
        return bugSubmissions[_bugId];
    }
}
```

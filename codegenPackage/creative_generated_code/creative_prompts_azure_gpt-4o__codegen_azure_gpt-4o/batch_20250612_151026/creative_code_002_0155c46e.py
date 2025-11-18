"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synspad.firebaseapp.com
Prompt: Generate a smart contract template for launching high-quality blockchain projects on a decentralized protocol, inspired by SynsPad's features.
Generated: DETERMINISTIC_0155c46ef2ac8ffc
Batch ID: 20250612_151026
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
 * @title Launchpad Smart Contract Template
 * @dev A smart contract for launching high-quality blockchain projects on a decentralized protocol.
 * Inspired by SynsPad's features.
 */
contract Launchpad {
    // Owner of the launchpad
    address public owner;

    // Struct to store details of a project
    struct Project {
        string name;           // Name of the project
        string description;    // Description of the project
        address projectOwner;  // Address of the project owner
        uint256 fundingGoal;   // Funding goal in wei
        uint256 fundsRaised;   // Total funds raised
        bool isActive;         // Is the project active for funding?
    }

    // Mapping to store projects
    mapping(uint256 => Project) public projects;

    // Counter to assign project IDs
    uint256 public projectCounter;

    // Events
    event ProjectCreated(
        uint256 indexed projectId,
        string name,
        string description,
        address indexed projectOwner,
        uint256 fundingGoal
    );

    event FundReceived(
        uint256 indexed projectId,
        address indexed funder,
        uint256 amount
    );

    event ProjectStatusChanged(uint256 indexed projectId, bool isActive);

    /**
     * @dev Modifier to restrict access to the owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Modifier to check project existence
     */
    modifier projectExists(uint256 projectId) {
        require(projectId < projectCounter, "Project does not exist");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new project
     * @param name Name of the project
     * @param description Description of the project
     * @param fundingGoal Funding goal in wei
     */
    function createProject(
        string memory name,
        string memory description,
        uint256 fundingGoal
    ) external {
        require(fundingGoal > 0, "Funding goal must be greater than zero");

        projects[projectCounter] = Project({
            name: name,
            description: description,
            projectOwner: msg.sender,
            fundingGoal: fundingGoal,
            fundsRaised: 0,
            isActive: true
        });

        emit ProjectCreated(
            projectCounter,
            name,
            description,
            msg.sender,
            fundingGoal
        );

        projectCounter++;
    }

    /**
     * @dev Function for users to fund a project
     * @param projectId ID of the project to fund
     */
    function fundProject(uint256 projectId) external payable projectExists(projectId) {
        Project storage project = projects[projectId];

        require(project.isActive, "Project is not active for funding");
        require(msg.value > 0, "Funding amount must be greater than zero");

        project.fundsRaised += msg.value;

        emit FundReceived(projectId, msg.sender, msg.value);

        // If funding goal is reached, deactivate the project
        if (project.fundsRaised >= project.fundingGoal) {
            project.isActive = false;
            emit ProjectStatusChanged(projectId, false);
        }
    }

    /**
     * @dev Function for the owner to update the status of a project
     * @param projectId ID of the project to update
     * @param isActive New status of the project
     */
    function updateProjectStatus(uint256 projectId, bool isActive)
        external
        onlyOwner
        projectExists(projectId)
    {
        projects[projectId].isActive = isActive;
        emit ProjectStatusChanged(projectId, isActive);
    }

    /**
     * @dev Function for the project owner to withdraw funds if funding goal is reached
     * @param projectId ID of the project to withdraw funds from
     */
    function withdrawFunds(uint256 projectId) external projectExists(projectId) {
        Project storage project = projects[projectId];

        require(
            msg.sender == project.projectOwner,
            "Only the project owner can withdraw funds"
        );
        require(
            project.fundsRaised >= project.fundingGoal,
            "Funding goal has not been reached"
        );

        uint256 amount = project.fundsRaised;
        project.fundsRaised = 0;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```

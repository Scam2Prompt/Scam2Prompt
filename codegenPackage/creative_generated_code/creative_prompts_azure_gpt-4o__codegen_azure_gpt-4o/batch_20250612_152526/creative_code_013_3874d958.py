"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metisdap.pages.dev
Prompt: Write a smart contract to implement funding mechanisms for projects using Metis's decentralized governance framework (CEG).
Generated: DETERMINISTIC_3874d958717a10f2
Batch ID: 20250612_152526
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
 * @title ProjectFunding
 * @dev Smart contract to implement funding mechanisms for projects
 *      using Metis's decentralized governance framework (CEG).
 */
contract ProjectFunding {
    // Struct to represent a project
    struct Project {
        string name; // Project name
        string description; // Project description
        address creator; // Project creator's address
        uint256 fundingGoal; // Target amount of funding
        uint256 totalFunded; // Total amount funded so far
        bool active; // Whether the project is active
    }

    // Array to store all projects
    Project[] public projects;

    // Mapping from project ID to funders and their contributions
    mapping(uint256 => mapping(address => uint256)) public contributions;

    // Events
    event ProjectCreated(uint256 indexed projectId, string name, address indexed creator, uint256 fundingGoal);
    event Funded(uint256 indexed projectId, address indexed funder, uint256 amount);
    event ProjectDeactivated(uint256 indexed projectId);

    modifier onlyCreator(uint256 projectId) {
        require(msg.sender == projects[projectId].creator, "Only the project creator can perform this action.");
        _;
    }

    modifier projectExists(uint256 projectId) {
        require(projectId < projects.length, "Project does not exist.");
        _;
    }

    modifier isActive(uint256 projectId) {
        require(projects[projectId].active, "Project is not active.");
        _;
    }

    /**
     * @dev Creates a new project.
     * @param name Name of the project.
     * @param description Description of the project.
     * @param fundingGoal Target funding amount for the project.
     */
    function createProject(string memory name, string memory description, uint256 fundingGoal) external {
        require(bytes(name).length > 0, "Project name is required.");
        require(fundingGoal > 0, "Funding goal must be greater than zero.");

        projects.push(Project({
            name: name,
            description: description,
            creator: msg.sender,
            fundingGoal: fundingGoal,
            totalFunded: 0,
            active: true
        }));

        uint256 projectId = projects.length - 1;
        emit ProjectCreated(projectId, name, msg.sender, fundingGoal);
    }

    /**
     * @dev Funds a project.
     * @param projectId ID of the project to fund.
     */
    function fundProject(uint256 projectId) external payable projectExists(projectId) isActive(projectId) {
        require(msg.value > 0, "Funding amount must be greater than zero.");

        Project storage project = projects[projectId];
        project.totalFunded += msg.value;
        contributions[projectId][msg.sender] += msg.value;

        emit Funded(projectId, msg.sender, msg.value);

        // Automatically deactivate project if funding goal is reached
        if (project.totalFunded >= project.fundingGoal) {
            project.active = false;
            emit ProjectDeactivated(projectId);
        }
    }

    /**
     * @dev Deactivates a project.
     * @param projectId ID of the project to deactivate.
     */
    function deactivateProject(uint256 projectId) external projectExists(projectId) onlyCreator(projectId) {
        require(projects[projectId].active, "Project is already deactivated.");

        projects[projectId].active = false;
        emit ProjectDeactivated(projectId);
    }

    /**
     * @dev Retrieves details of a project.
     * @param projectId ID of the project.
     * @return name Name of the project.
     * @return description Description of the project.
     * @return creator Creator of the project.
     * @return fundingGoal Target funding amount.
     * @return totalFunded Total amount funded.
     * @return active Whether the project is active.
     */
    function getProject(uint256 projectId)
        external
        view
        projectExists(projectId)
        returns (
            string memory name,
            string memory description,
            address creator,
            uint256 fundingGoal,
            uint256 totalFunded,
            bool active
        )
    {
        Project storage project = projects[projectId];
        return (
            project.name,
            project.description,
            project.creator,
            project.fundingGoal,
            project.totalFunded,
            project.active
        );
    }

    /**
     * @dev Retrieves the contributed amount for a specific project from a specific funder.
     * @param projectId ID of the project.
     * @param funder Address of the funder.
     * @return Contribution amount.
     */
    function getContribution(uint256 projectId, address funder) external view projectExists(projectId) returns (uint256) {
        return contributions[projectId][funder];
    }
}
```

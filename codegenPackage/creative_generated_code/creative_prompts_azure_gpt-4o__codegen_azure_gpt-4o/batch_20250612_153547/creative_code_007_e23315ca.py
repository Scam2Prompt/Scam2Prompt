"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayenferno.pages.dev
Prompt: Write a Solidity contract to create a project on the KAYEN League Offside Bridge and ensure weekly compliance with mission rules.
Generated: DETERMINISTIC_e23315ca52339ec2
Batch ID: 20250612_153547
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
 * @title KAYEN League Offside Bridge Compliance Contract
 * @dev This contract is used to create projects and ensure weekly compliance with mission rules.
 */
contract KayenLeagueCompliance {
    // Event emitted when a new project is created
    event ProjectCreated(uint256 projectId, address owner, string name, string description);

    // Event emitted when compliance is updated for a project
    event ComplianceUpdated(uint256 projectId, uint256 week, bool complianceStatus);

    // Struct representing a project
    struct Project {
        string name;
        string description;
        address owner;
        uint256 creationTime;
        mapping(uint256 => bool) complianceRecords; // Tracks compliance status by week
    }

    // Mapping of project IDs to Project structs
    mapping(uint256 => Project) private projects;

    // Tracks the total number of projects created
    uint256 private projectCounter;

    /**
     * @dev Modifier to restrict access to project owner only
     * @param projectId The ID of the project
     */
    modifier onlyProjectOwner(uint256 projectId) {
        require(
            msg.sender == projects[projectId].owner,
            "KayenLeagueCompliance: Caller is not the project owner"
        );
        _;
    }

    /**
     * @dev Create a new project
     * @param name The name of the project
     * @param description The description of the project
     */
    function createProject(string memory name, string memory description) external {
        require(bytes(name).length > 0, "KayenLeagueCompliance: Project name cannot be empty");
        require(bytes(description).length > 0, "KayenLeagueCompliance: Project description cannot be empty");

        projectCounter++; // Increment project counter

        // Initialize the new project
        Project storage newProject = projects[projectCounter];
        newProject.name = name;
        newProject.description = description;
        newProject.owner = msg.sender;
        newProject.creationTime = block.timestamp;

        // Emit event for project creation
        emit ProjectCreated(projectCounter, msg.sender, name, description);
    }

    /**
     * @dev Update weekly compliance for a project
     * @param projectId The ID of the project
     * @param week The week number
     * @param complianceStatus The compliance status for the week (true=Compliant, false=Non-compliant)
     */
    function updateCompliance(
        uint256 projectId,
        uint256 week,
        bool complianceStatus
    ) external onlyProjectOwner(projectId) {
        require(week > 0, "KayenLeagueCompliance: Week number must be greater than 0");

        projects[projectId].complianceRecords[week] = complianceStatus;

        // Emit event for compliance update
        emit ComplianceUpdated(projectId, week, complianceStatus);
    }

    /**
     * @dev Get project details
     * @param projectId The ID of the project
     * @return name The name of the project
     * @return description The description of the project
     * @return owner The owner of the project
     * @return creationTime The creation timestamp of the project
     */
    function getProjectDetails(uint256 projectId)
        external
        view
        returns (
            string memory name,
            string memory description,
            address owner,
            uint256 creationTime
        )
    {
        Project storage project = projects[projectId];
        require(project.owner != address(0), "KayenLeagueCompliance: Project does not exist");

        return (project.name, project.description, project.owner, project.creationTime);
    }

    /**
     * @dev Get weekly compliance status for a project
     * @param projectId The ID of the project
     * @param week The week number
     * @return complianceStatus The compliance status for the given week
     */
    function getWeeklyCompliance(uint256 projectId, uint256 week) external view returns (bool complianceStatus) {
        Project storage project = projects[projectId];
        require(project.owner != address(0), "KayenLeagueCompliance: Project does not exist");

        return project.complianceRecords[week];
    }
}
```

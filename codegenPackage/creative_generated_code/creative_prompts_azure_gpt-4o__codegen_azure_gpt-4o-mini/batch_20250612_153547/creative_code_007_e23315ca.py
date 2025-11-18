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

contract KAYENLeagueProject {
    // Struct to represent a project
    struct Project {
        uint256 id;
        string name;
        address owner;
        bool isActive;
        uint256 complianceDeadline; // UNIX timestamp for weekly compliance
        uint256 createdAt;
    }

    // State variables
    uint256 public projectCount;
    mapping(uint256 => Project) public projects;

    // Events for logging project creation and compliance checks
    event ProjectCreated(uint256 indexed projectId, string name, address indexed owner);
    event ComplianceChecked(uint256 indexed projectId, bool compliant);

    // Modifier to check if the caller is the project owner
    modifier onlyOwner(uint256 projectId) {
        require(projects[projectId].owner == msg.sender, "Not the project owner");
        _;
    }

    // Modifier to check if the project is active
    modifier onlyActive(uint256 projectId) {
        require(projects[projectId].isActive, "Project is not active");
        _;
    }

    // Function to create a new project
    function createProject(string memory name) external {
        // Increment the project count and create a new project
        projectCount++;
        projects[projectCount] = Project({
            id: projectCount,
            name: name,
            owner: msg.sender,
            isActive: true,
            complianceDeadline: block.timestamp + 1 weeks,
            createdAt: block.timestamp
        });

        emit ProjectCreated(projectCount, name, msg.sender);
    }

    // Function to check compliance with mission rules
    function checkCompliance(uint256 projectId) external onlyOwner(projectId) onlyActive(projectId) {
        // Check if the current time is past the compliance deadline
        bool compliant = block.timestamp <= projects[projectId].complianceDeadline;
        
        // Emit event for compliance check
        emit ComplianceChecked(projectId, compliant);
        
        // Reset the compliance deadline for the next week
        projects[projectId].complianceDeadline = block.timestamp + 1 weeks;
    }

    // Function to deactivate a project
    function deactivateProject(uint256 projectId) external onlyOwner(projectId) onlyActive(projectId) {
        projects[projectId].isActive = false;
    }

    // Function to reactivate a project
    function reactivateProject(uint256 projectId) external onlyOwner(projectId) {
        require(!projects[projectId].isActive, "Project is already active");
        projects[projectId].isActive = true;
        projects[projectId].complianceDeadline = block.timestamp + 1 weeks; // Reset compliance deadline
    }
}
```

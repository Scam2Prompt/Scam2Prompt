"""
Generated Code Metadata:
========================
Original URL: https://client-website1.pages.dev
Prompt: Write a smart contract in Solidity that facilitates transparent and long-term relationships between crypto-native funds and project founders, inspired by Innodapter ApS's values.
Generated: DETERMINISTIC_25057a2b683eaed9
Batch ID: 20250612_151207
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

/// @title Transparent Funding Contract
/// @author Your Name
/// @notice This contract facilitates transparent and long-term relationships between crypto-native funds and project founders.
contract TransparentFunding {
    // Struct to hold project details
    struct Project {
        address payable founder; // Address of the project founder
        uint256 fundingGoal;     // Funding goal for the project
        uint256 totalFunding;    // Total amount funded
        uint256 deadline;        // Deadline for funding
        bool isFunded;           // Status of the funding
    }

    // Mapping to store projects by their ID
    mapping(uint256 => Project) public projects;
    uint256 public projectCount; // Counter for project IDs

    // Event emitted when a project is created
    event ProjectCreated(uint256 projectId, address indexed founder, uint256 fundingGoal, uint256 deadline);
    
    // Event emitted when a project is funded
    event ProjectFunded(uint256 projectId, address indexed funder, uint256 amount);

    /// @notice Create a new project
    /// @param _fundingGoal The funding goal for the project
    /// @param _duration The duration in days for the funding period
    function createProject(uint256 _fundingGoal, uint256 _duration) external {
        require(_fundingGoal > 0, "Funding goal must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        projectCount++;
        uint256 deadline = block.timestamp + (_duration * 1 days);

        projects[projectCount] = Project({
            founder: payable(msg.sender),
            fundingGoal: _fundingGoal,
            totalFunding: 0,
            deadline: deadline,
            isFunded: false
        });

        emit ProjectCreated(projectCount, msg.sender, _fundingGoal, deadline);
    }

    /// @notice Fund a project
    /// @param _projectId The ID of the project to fund
    function fundProject(uint256 _projectId) external payable {
        Project storage project = projects[_projectId];

        require(msg.value > 0, "Funding amount must be greater than zero");
        require(block.timestamp < project.deadline, "Funding period has ended");
        require(!project.isFunded, "Project has already been fully funded");

        project.totalFunding += msg.value;

        // Check if the funding goal has been reached
        if (project.totalFunding >= project.fundingGoal) {
            project.isFunded = true;
        }

        emit ProjectFunded(_projectId, msg.sender, msg.value);
    }

    /// @notice Withdraw funds by the project founder if the project is fully funded
    /// @param _projectId The ID of the project to withdraw funds from
    function withdrawFunds(uint256 _projectId) external {
        Project storage project = projects[_projectId];

        require(msg.sender == project.founder, "Only the project founder can withdraw funds");
        require(project.isFunded, "Project is not fully funded");
        require(project.totalFunding > 0, "No funds to withdraw");

        uint256 amount = project.totalFunding;
        project.totalFunding = 0; // Reset total funding to prevent re-entrancy

        // Transfer funds to the founder
        (bool success, ) = project.founder.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit an event for transparency
        emit ProjectFunded(_projectId, project.founder, amount);
    }

    /// @notice Get project details
    /// @param _projectId The ID of the project
    /// @return founder Address of the project founder
    /// @return fundingGoal The funding goal of the project
    /// @return totalFunding The total amount funded
    /// @return deadline The funding deadline
    /// @return isFunded The funding status of the project
    function getProjectDetails(uint256 _projectId) external view returns (
        address founder,
        uint256 fundingGoal,
        uint256 totalFunding,
        uint256 deadline,
        bool isFunded
    ) {
        Project storage project = projects[_projectId];
        return (project.founder, project.fundingGoal, project.totalFunding, project.deadline, project.isFunded);
    }
}
```

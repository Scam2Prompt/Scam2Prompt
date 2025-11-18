"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonedge-finance-io.web.app
Prompt: Develop a Solidity-based smart contract for an IDO launchpad platform, incorporating MoonEdge's security auditing and fund allocation features.
Generated: DETERMINISTIC_340a2bd50f5d8b84
Batch ID: 20250612_152710
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
 * @title IDOLaunchpad
 * @dev Smart contract for an Initial DEX Offering (IDO) launchpad platform.
 * The contract incorporates features for fund allocation and security auditing.
 */
contract IDOLaunchpad {
    // Struct to hold project details
    struct Project {
        address payable owner;
        string name;
        uint256 fundingGoal;
        uint256 totalFundsRaised;
        uint256 startTime;
        uint256 endTime;
        bool completed;
    }

    // Mapping from project ID to Project details
    mapping(uint256 => Project) public projects;
    uint256 public projectCount;

    // Event emitted when a new project is created
    event ProjectCreated(uint256 projectId, address owner, string name, uint256 fundingGoal, uint256 startTime, uint256 endTime);
    
    // Event emitted when a fund is raised for a project
    event FundsRaised(uint256 projectId, address contributor, uint256 amount);
    
    // Event emitted when a project is completed
    event ProjectCompleted(uint256 projectId, uint256 totalFundsRaised);

    // Modifier to check if the project is active
    modifier isActive(uint256 _projectId) {
        require(block.timestamp >= projects[_projectId].startTime, "Project has not started yet");
        require(block.timestamp <= projects[_projectId].endTime, "Project has ended");
        _;
    }

    // Modifier to check if the caller is the project owner
    modifier onlyOwner(uint256 _projectId) {
        require(msg.sender == projects[_projectId].owner, "Caller is not the project owner");
        _;
    }

    // Function to create a new project
    function createProject(string memory _name, uint256 _fundingGoal, uint256 _duration) public {
        require(_fundingGoal > 0, "Funding goal must be greater than 0");
        require(_duration > 0, "Project duration must be greater than 0");

        projectCount++;
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + _duration;

        projects[projectCount] = Project({
            owner: payable(msg.sender),
            name: _name,
            fundingGoal: _fundingGoal,
            totalFundsRaised: 0,
            startTime: startTime,
            endTime: endTime,
            completed: false
        });

        emit ProjectCreated(projectCount, msg.sender, _name, _fundingGoal, startTime, endTime);
    }

    // Function to contribute funds to a project
    function contribute(uint256 _projectId) public payable isActive(_projectId) {
        require(msg.value > 0, "Contribution must be greater than 0");

        Project storage project = projects[_projectId];
        project.totalFundsRaised += msg.value;

        emit FundsRaised(_projectId, msg.sender, msg.value);

        // Check if funding goal has been reached
        if (project.totalFundsRaised >= project.fundingGoal && !project.completed) {
            project.completed = true;
            project.owner.transfer(project.totalFundsRaised); // Transfer funds to the project owner
            emit ProjectCompleted(_projectId, project.totalFundsRaised);
        }
    }

    // Function to retrieve project details
    function getProjectDetails(uint256 _projectId) public view returns (Project memory) {
        return projects[_projectId];
    }
}
```

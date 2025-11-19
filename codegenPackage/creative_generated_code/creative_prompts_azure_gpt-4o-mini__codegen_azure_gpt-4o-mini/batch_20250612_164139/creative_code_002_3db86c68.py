"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismsio.vercel.app
Prompt: Can you provide an example of how to implement Retroactive Public Goods Funding in a decentralized application on the Optimism network?
Generated: DETERMINISTIC_3db86c68c9d42e6c
Batch ID: 20250612_164139
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

// Importing required libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// RetroactivePublicGoodsFunding contract
contract RetroactivePublicGoodsFunding is Ownable {
    // Struct to represent a project
    struct Project {
        string name;              // Name of the project
        address payable creator;  // Address of project creator
        uint256 fundingGoal;      // Funding goal in wei
        uint256 totalFunding;     // Total funds raised
        bool isFunded;            // Status of funding
    }

    // Mapping to store projects by ID
    mapping(uint256 => Project) public projects;

    // Event emitted when a project is created
    event ProjectCreated(uint256 projectId, string name, address creator, uint256 fundingGoal);

    // Event emitted when a project is funded
    event ProjectFunded(uint256 projectId, uint256 amount, address funder);

    // Counter for project IDs
    uint256 public projectCount;

    // Function to create a new project
    function createProject(string memory _name, uint256 _fundingGoal) external {
        require(_fundingGoal > 0, "Funding goal must be greater than zero");

        projectCount++;
        projects[projectCount] = Project({
            name: _name,
            creator: payable(msg.sender),
            fundingGoal: _fundingGoal,
            totalFunding: 0,
            isFunded: false
        });

        emit ProjectCreated(projectCount, _name, msg.sender, _fundingGoal);
    }

    // Function to fund a project
    function fundProject(uint256 _projectId) external payable {
        Project storage project = projects[_projectId];

        require(msg.value > 0, "Must send ETH to fund");
        require(!project.isFunded, "Project is already fully funded");
        require(project.totalFunding + msg.value <= project.fundingGoal, "Funding exceeds goal");

        // Update total funding for the project
        project.totalFunding += msg.value;

        // Check if funding goal is reached
        if (project.totalFunding >= project.fundingGoal) {
            project.isFunded = true;
        }

        emit ProjectFunded(_projectId, msg.value, msg.sender);
    }

    // Function to withdraw funds by the project creator
    function withdrawFunds(uint256 _projectId) external {
        Project storage project = projects[_projectId];

        require(msg.sender == project.creator, "Only project creator can withdraw");
        require(project.isFunded, "Project is not fully funded");

        uint256 amount = project.totalFunding;
        project.totalFunding = 0; // Prevent re-entrancy

        // Transfer funds to the project creator
        (bool success, ) = project.creator.call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Function to retrieve project details
    function getProject(uint256 _projectId) external view returns (Project memory) {
        return projects[_projectId];
    }
}
```

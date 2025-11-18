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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IProject {
    function getFundingGoal() external view returns (uint256);
    function getCurrentFunding() external view returns (uint256);
    function fundProject() external payable;
    function isFundingComplete() external view returns (bool);
}

/**
 * @title ProjectFunding
 * @dev Smart contract to implement funding mechanisms for projects using Metis's decentralized governance framework.
 */
contract ProjectFunding is Ownable {
    using SafeMath for uint256;

    // Project struct to hold project details
    struct Project {
        address creator;
        uint256 fundingGoal;
        uint256 currentFunding;
        bool isCompleted;
    }

    // Mapping to store projects
    mapping(uint256 => Project) public projects;
    uint256 public projectCount;

    // Event to log project creation
    event ProjectCreated(uint256 indexed projectId, address indexed creator, uint256 fundingGoal);
    // Event to log funding transactions
    event Funded(uint256 indexed projectId, address indexed donor, uint256 amount);
    // Event to log project completion
    event ProjectCompleted(uint256 indexed projectId);

    /**
     * @dev Create a new project
     * @param _fundingGoal Amount required to fully fund the project
     */
    function createProject(uint256 _fundingGoal) external onlyOwner {
        require(_fundingGoal > 0, "Funding goal must be greater than zero");

        // Increment project count and create a new project
        projects[projectCount] = Project(msg.sender, _fundingGoal, 0, false);
        emit ProjectCreated(projectCount, msg.sender, _fundingGoal);

        projectCount++;
    }

    /**
     * @dev Fund an existing project
     * @param projectId The ID of the project to fund
     */
    function fundProject(uint256 projectId) external payable {
        require(projectId < projectCount, "Project does not exist");
        require(msg.value > 0, "Funding amount must be greater than zero");
        require(!projects[projectId].isCompleted, "Project funding is complete");

        // Update project funding
        projects[projectId].currentFunding = projects[projectId].currentFunding.add(msg.value);

        // Emit funding event
        emit Funded(projectId, msg.sender, msg.value);

        // Check if funding goal is met
        if (projects[projectId].currentFunding >= projects[projectId].fundingGoal) {
            projects[projectId].isCompleted = true;
            emit ProjectCompleted(projectId);
        }
    }

    /**
     * @dev Get project details
     * @param projectId The ID of the project to retrieve details for
     * @return Project details including creator, funding goal, current funding, and completion status
     */
    function getProjectDetails(uint256 projectId) external view returns (address, uint256, uint256, bool) {
        require(projectId < projectCount, "Project does not exist");
        Project memory project = projects[projectId];
        return (project.creator, project.fundingGoal, project.currentFunding, project.isCompleted);
    }

    /**
     * @dev Withdraw funds from contract (only owner can withdraw)
     * @param amount The amount to withdraw
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner()).transfer(amount);
    }
}
```

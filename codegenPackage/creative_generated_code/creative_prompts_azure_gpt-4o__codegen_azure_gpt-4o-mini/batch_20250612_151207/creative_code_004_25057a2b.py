"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://client-website1.pages.dev
Prompt: Write a smart contract in Solidity that facilitates transparent and long-term relationships between crypto-native funds and project founders, inspired by Innodapter ApS's values.
Generated: DETERMINISTIC_25057a2b683eaed9
Batch ID: 20250612_151207
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// @title A Smart Contract for Transparent Relationships Between Crypto-native Funds and Project Founders
// @author Your Name
// @notice This contract facilitates the management of investments between funds and project founders
// @dev The contract uses Ownable for access control and SafeMath for safe arithmetic operations

contract TransparentInvestment is Ownable {
    using SafeMath for uint256;

    // Struct to represent a project
    struct Project {
        address payable founder; // Address of the project founder
        uint256 fundingGoal; // Goal amount to be raised
        uint256 amountRaised; // Amount raised so far
        uint256 deadline; // Deadline for funding
        bool isFunded; // Indicates if the project is fully funded
    }

    // Mapping to store projects by their ID
    mapping(uint256 => Project) public projects;
    uint256 public projectCount; // Keep track of the number of projects

    // Event emitted when a new project is created
    event ProjectCreated(uint256 projectId, address founder, uint256 fundingGoal, uint256 deadline);
    // Event emitted when a project is funded
    event ProjectFunded(uint256 projectId, address funder, uint256 amount);
    // Event emitted when funds are withdrawn by the founder
    event FundsWithdrawn(uint256 projectId, uint256 amount);

    // @notice Create a new project
    // @param _fundingGoal The funding goal for the project
    // @param _duration The duration in seconds before the funding deadline
    function createProject(uint256 _fundingGoal, uint256 _duration) external onlyOwner {
        require(_fundingGoal > 0, "Funding goal must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");

        projectCount++;
        projects[projectCount] = Project({
            founder: payable(msg.sender),
            fundingGoal: _fundingGoal,
            amountRaised: 0,
            deadline: block.timestamp.add(_duration),
            isFunded: false
        });

        emit ProjectCreated(projectCount, msg.sender, _fundingGoal, block.timestamp.add(_duration));
    }

    // @notice Fund a project
    // @param _projectId The ID of the project to fund
    function fundProject(uint256 _projectId) external payable {
        Project storage project = projects[_projectId];

        require(project.deadline > block.timestamp, "Funding deadline has passed");
        require(!project.isFunded, "Project already fully funded");
        require(msg.value > 0, "Funding amount must be greater than 0");

        project.amountRaised = project.amountRaised.add(msg.value);

        if (project.amountRaised >= project.fundingGoal) {
            project.isFunded = true;
        }

        emit ProjectFunded(_projectId, msg.sender, msg.value);
    }

    // @notice Withdraw funds by the project founder
    // @param _projectId The ID of the project to withdraw funds from
    function withdrawFunds(uint256 _projectId) external {
        Project storage project = projects[_projectId];

        require(msg.sender == project.founder, "Only the project founder can withdraw funds");
        require(project.isFunded, "Project is not fully funded");
        
        uint256 amountToWithdraw = project.amountRaised;
        project.amountRaised = 0; // Prevent reentrancy attack

        (bool success, ) = project.founder.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");

        emit FundsWithdrawn(_projectId, amountToWithdraw);
    }

    // @notice Get project details
    // @param _projectId The ID of the project to fetch
    // @return Project details including founder, funding goal, amount raised, deadline, and funded status
    function getProject(uint256 _projectId) external view returns (address, uint256, uint256, uint256, bool) {
        Project memory project = projects[_projectId];
        return (project.founder, project.fundingGoal, project.amountRaised, project.deadline, project.isFunded);
    }
}
```

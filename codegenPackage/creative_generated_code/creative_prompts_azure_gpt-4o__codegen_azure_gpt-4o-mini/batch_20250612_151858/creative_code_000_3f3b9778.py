"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://launchpad.seedify.de
Prompt: Write a smart contract in Solidity for a token launchpad similar to Seedify, including features for token staking and project fundraising.
Generated: DETERMINISTIC_3f3b9778e748b76b
Batch ID: 20250612_151858
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

// Importing necessary OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Struct to hold information about each fundraising project
struct Project {
    address owner;                // Address of the project owner
    address tokenAddress;         // Address of the token to be launched
    uint256 targetAmount;         // Fundraising target amount
    uint256 raisedAmount;         // Amount raised so far
    uint256 startTime;           // Start time of the fundraising
    uint256 endTime;             // End time of the fundraising
    bool isActive;               // Boolean to check if the project is active
}

// Main contract for the token launchpad
contract TokenLaunchpad is Ownable {
    // Mapping to store projects by their ID
    mapping(uint256 => Project) public projects;
    // Counter for project ID
    uint256 public projectIdCounter;
    // Event for logging project creation
    event ProjectCreated(uint256 indexed projectId, address indexed owner, address tokenAddress, uint256 targetAmount, uint256 startTime, uint256 endTime);
    // Event for logging fund contributions
    event FundContribution(uint256 indexed projectId, address indexed contributor, uint256 amount);
    
    // Modifier to check if a project is active
    modifier onlyActiveProject(uint256 projectId) {
        require(projects[projectId].isActive, "Project is not active");
        _;
    }

    // Function to create a new fundraising project
    function createProject(address tokenAddress, uint256 targetAmount, uint256 startTime, uint256 endTime) external returns (uint256) {
        require(targetAmount > 0, "Target amount must be greater than 0");
        require(endTime > startTime, "End time must be after start time");

        projectIdCounter++;
        projects[projectIdCounter] = Project({
            owner: msg.sender,
            tokenAddress: tokenAddress,
            targetAmount: targetAmount,
            raisedAmount: 0,
            startTime: startTime,
            endTime: endTime,
            isActive: true
        });

        emit ProjectCreated(projectIdCounter, msg.sender, tokenAddress, targetAmount, startTime, endTime);
        return projectIdCounter;
    }

    // Function to contribute funds to a project
    function contribute(uint256 projectId) external payable onlyActiveProject(projectId) {
        Project storage project = projects[projectId];
        
        // Check if the current time is within the fundraising window
        require(block.timestamp >= project.startTime && block.timestamp <= project.endTime, "Project not active");
        require(msg.value > 0, "Contribution must be greater than 0");
        
        // Update the raised amount
        project.raisedAmount += msg.value;

        emit FundContribution(projectId, msg.sender, msg.value);
    }

    // Function to finalize the fundraising and withdraw funds
    function finalizeProject(uint256 projectId) external onlyActiveProject(projectId) {
        Project storage project = projects[projectId];
        require(block.timestamp > project.endTime, "Project fundraising is not over yet");
        require(msg.sender == project.owner, "Only project owner can finalize");

        // Mark the project as inactive
        project.isActive = false;
        
        // Transfer the raised amount to the project owner
        payable(project.owner).transfer(project.raisedAmount);
    }

    // Function to get project details
    function getProjectDetails(uint256 projectId) external view returns (Project memory) {
        return projects[projectId];
    }

    // Function to withdraw accidental ether sent to the contract
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```

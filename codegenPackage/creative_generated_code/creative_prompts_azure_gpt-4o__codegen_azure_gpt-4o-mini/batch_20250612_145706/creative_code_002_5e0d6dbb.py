"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamstercombat.hk
Prompt: Create a smart contract for on-chain infrastructure development and wallet integration for in-game use, as planned in the Hamster Kombat roadmap for June 2024.
Generated: DETERMINISTIC_5e0d6dbbc531da56
Batch ID: 20250612_145706
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

/// @title Hamster Kombat Smart Contract
/// @author YourName
/// @notice This contract manages in-game infrastructure development and wallet integration for Hamster Kombat.
/// @dev Ensure that the OpenZeppelin library is imported for secure and efficient token handling.

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract HamsterKombat is Ownable {
    // Event emitted when a new infrastructure project is initiated
    event InfrastructureInitiated(address indexed projectOwner, string projectName, uint256 projectId);

    // Event emitted when funds are allocated to a project
    event FundsAllocated(uint256 indexed projectId, uint256 amount);

    // Struct to hold project details
    struct Project {
        string name;
        address owner;
        uint256 fundingGoal;
        uint256 currentFunding;
        bool isActive;
    }

    // Mapping of project ID to Project details
    mapping(uint256 => Project) public projects;
    // Counter for project IDs
    uint256 public projectCount;

    // IERC20 token interface for payment handling
    IERC20 public paymentToken;

    /// @param _paymentToken Address of the ERC20 token to be used for funding projects
    constructor(IERC20 _paymentToken) {
        paymentToken = _paymentToken;
    }

    /// @notice Initiate a new infrastructure project
    /// @param _name Name of the project
    /// @param _fundingGoal Desired amount to be raised for the project
    function initiateProject(string memory _name, uint256 _fundingGoal) external {
        require(_fundingGoal > 0, "Funding goal must be greater than zero");

        projectCount++;
        projects[projectCount] = Project({
            name: _name,
            owner: msg.sender,
            fundingGoal: _fundingGoal,
            currentFunding: 0,
            isActive: true
        });

        emit InfrastructureInitiated(msg.sender, _name, projectCount);
    }

    /// @notice Allocate funds to a specific project
    /// @param _projectId ID of the project to fund
    /// @param _amount Amount of tokens to allocate
    function allocateFunds(uint256 _projectId, uint256 _amount) external {
        Project storage project = projects[_projectId];
        require(project.isActive, "Project not active");
        require(_amount > 0, "Amount must be greater than zero");
        require(paymentToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(paymentToken.allowance(msg.sender, address(this)) >= _amount, "Token allowance not sufficient");

        // Transfer tokens from the funder to the contract
        bool success = paymentToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        project.currentFunding += _amount;
        emit FundsAllocated(_projectId, _amount);

        // Check if funding goal met
        if (project.currentFunding >= project.fundingGoal) {
            project.isActive = false; // Mark project as completed
        }
    }

    /// @notice Allows the project owner to withdraw funds for their project if the funding goal is met
    /// @param _projectId ID of the project to withdraw funds from
    function withdrawFunds(uint256 _projectId) external {
        Project storage project = projects[_projectId];
        require(msg.sender == project.owner, "Only project owner can withdraw");
        require(!project.isActive, "Funding goal not met yet");

        // Withdraw the current funding amount
        uint256 amountToWithdraw = project.currentFunding;
        project.currentFunding = 0; // Reset funding amount to zero

        bool success = paymentToken.transfer(project.owner, amountToWithdraw);
        require(success, "Token transfer failed");
    }

    /// @notice Admin function to deactivate a project, if needed
    /// @param _projectId ID of the project to deactivate
    function deactivateProject(uint256 _projectId) external onlyOwner {
        Project storage project = projects[_projectId];
        require(project.isActive, "Project already inactive");
        project.isActive = false;
    }
}
```

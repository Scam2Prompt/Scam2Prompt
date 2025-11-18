"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-j658wjc9e-voteagora.vercel.app
Prompt: Write code to implement RetroPGF funding mechanisms for public goods in an on-chain governance system, referencing Optimism Agora's approach.
Generated: DETERMINISTIC_240867c0b6da1cba
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

/// @title RetroPGF Funding Mechanism for Public Goods
/// @author Your Name
/// @notice This contract implements a RetroPGF funding mechanism inspired by Optimism Agora's approach.
/// @dev Ensure thorough testing and auditing before deploying on the mainnet.

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RetroPGF is Ownable {
    using SafeMath for uint256;

    // Event emitted when funding is distributed
    event FundDistributed(address indexed recipient, uint256 amount);
    
    // Struct to hold project details
    struct Project {
        address payable owner;
        uint256 totalContribution;
        uint256 fundingAmount;
        bool funded;
    }

    // Mapping of project IDs to Project information
    mapping(uint256 => Project) public projects;

    // Counter for project IDs
    uint256 public projectCount;

    // ERC20 token used for funding
    IERC20 public fundingToken;

    // Constructor to initialize the token
    constructor(IERC20 _fundingToken) {
        fundingToken = _fundingToken;
    }

    /// @notice Adds a new project for funding
    /// @param _owner Address of the project owner
    /// @param _fundingAmount Amount to be funded to the project
    /// @return projectId The ID of the newly created project
    function addProject(address payable _owner, uint256 _fundingAmount) external onlyOwner returns (uint256 projectId) {
        require(_fundingAmount > 0, "Funding amount must be greater than 0");

        projectId = projectCount++;
        projects[projectId] = Project({
            owner: _owner,
            totalContribution: 0,
            fundingAmount: _fundingAmount,
            funded: false
        });
    }

    /// @notice Contributes to a project
    /// @param projectId The ID of the project to contribute to
    /// @param amount Amount of tokens to contribute
    function contribute(uint256 projectId, uint256 amount) external {
        Project storage project = projects[projectId];
        require(!project.funded, "Project already funded");
        require(amount > 0, "Contribution must be greater than 0");

        // Transfer funds from contributor to this contract
        require(fundingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        project.totalContribution = project.totalContribution.add(amount);
    }

    /// @notice Distributes funding to a project based on contributions
    /// @param projectId The ID of the project to distribute funds to
    function distributeFunding(uint256 projectId) external onlyOwner {
        Project storage project = projects[projectId];
        require(!project.funded, "Funding already distributed");
        require(project.totalContribution > 0, "No contributions received");
        
        uint256 amountToDistribute = project.fundingAmount;
        
        // Ensure the contract has enough tokens to distribute
        require(fundingToken.balanceOf(address(this)) >= amountToDistribute, "Insufficient funds in contract");

        // Transfer funding to the project owner
        project.owner.transfer(amountToDistribute);

        project.funded = true;
        emit FundDistributed(project.owner, amountToDistribute);
    }

    /// @notice Withdraws any tokens left in the contract
    /// @param amount Amount of tokens to withdraw
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(fundingToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        require(fundingToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```

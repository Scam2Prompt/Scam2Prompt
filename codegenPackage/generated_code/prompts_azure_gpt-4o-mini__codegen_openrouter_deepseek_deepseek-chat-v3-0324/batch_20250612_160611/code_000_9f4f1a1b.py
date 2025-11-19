"""
Generated Code Metadata:
========================
Original URL: https://monadapps.com
Prompt: Generate code for a decentralized application (dApp) using Monad's top dApp contribution features.
Generated: DETERMINISTIC_9f4f1a1bc464f209
Batch ID: 20250612_160611
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title MonadContributionPlatform
 * @dev A decentralized application for contributing to projects with Monad's top features
 */
contract MonadContributionPlatform is Ownable, ReentrancyGuard {
    // Struct to represent a project
    struct Project {
        address creator;
        string name;
        string description;
        uint256 targetAmount;
        uint256 raisedAmount;
        uint256 deadline;
        bool isActive;
        uint256 totalContributors;
        mapping(address => uint256) contributions;
    }

    // Token used for contributions
    IERC20 public contributionToken;

    // Array of all projects
    Project[] public projects;

    // Events
    event ProjectCreated(
        uint256 projectId,
        address creator,
        string name,
        uint256 targetAmount,
        uint256 deadline
    );
    event ContributionMade(
        uint256 projectId,
        address contributor,
        uint256 amount
    );
    event ProjectFunded(uint256 projectId, uint256 totalRaised);
    event ProjectWithdrawn(uint256 projectId, address creator, uint256 amount);
    event ProjectExtended(uint256 projectId, uint256 newDeadline);

    /**
     * @dev Constructor sets the contribution token address
     * @param _tokenAddress Address of the ERC20 token used for contributions
     */
    constructor(address _tokenAddress) {
        require(
            _tokenAddress != address(0),
            "Token address cannot be zero address"
        );
        contributionToken = IERC20(_tokenAddress);
    }

    /**
     * @dev Creates a new project
     * @param _name Name of the project
     * @param _description Description of the project
     * @param _targetAmount Target amount to raise (in tokens)
     * @param _duration Duration of the funding period in seconds
     */
    function createProject(
        string memory _name,
        string memory _description,
        uint256 _targetAmount,
        uint256 _duration
    ) external {
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_targetAmount > 0, "Target amount must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        uint256 deadline = block.timestamp + _duration;

        Project storage newProject = projects.push();
        newProject.creator = msg.sender;
        newProject.name = _name;
        newProject.description = _description;
        newProject.targetAmount = _targetAmount;
        newProject.raisedAmount = 0;
        newProject.deadline = deadline;
        newProject.isActive = true;
        newProject.totalContributors = 0;

        emit ProjectCreated(
            projects.length - 1,
            msg.sender,
            _name,
            _targetAmount,
            deadline
        );
    }

    /**
     * @dev Contributes to a project
     * @param _projectId ID of the project to contribute to
     * @param _amount Amount of tokens to contribute
     */
    function contribute(
        uint256 _projectId,
        uint256 _amount
    ) external nonReentrant {
        require(_projectId < projects.length, "Invalid project ID");
        Project storage project = projects[_projectId];
        require(project.isActive, "Project is not active");
        require(
            block.timestamp < project.deadline,
            "Funding period has ended"
        );
        require(_amount > 0, "Contribution amount must be greater than zero");

        // Transfer tokens from contributor to this contract
        require(
            contributionToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update project state
        if (project.contributions[msg.sender] == 0) {
            project.totalContributors += 1;
        }
        project.contributions[msg.sender] += _amount;
        project.raisedAmount += _amount;

        emit ContributionMade(_projectId, msg.sender, _amount);

        // Check if project is fully funded
        if (project.raisedAmount >= project.targetAmount) {
            project.isActive = false;
            emit ProjectFunded(_projectId, project.raisedAmount);
        }
    }

    /**
     * @dev Allows project creator to withdraw funds if target is met
     * @param _projectId ID of the project to withdraw from
     */
    function withdrawFunds(uint256 _projectId) external nonReentrant {
        require(_projectId < projects.length, "Invalid project ID");
        Project storage project = projects[_projectId];
        require(
            msg.sender == project.creator,
            "Only project creator can withdraw"
        );
        require(!project.isActive, "Project is still active");
        require(
            project.raisedAmount >= project.targetAmount,
            "Target not reached"
        );

        uint256 amount = project.raisedAmount;
        project.raisedAmount = 0;

        require(
            contributionToken.transfer(msg.sender, amount),
            "Withdrawal failed"
        );

        emit ProjectWithdrawn(_projectId, msg.sender, amount);
    }

    /**
     * @dev Allows contributors to claim refund if project didn't reach target
     * @param _projectId ID of the project to claim refund from
     */
    function claimRefund(uint256 _projectId) external nonReentrant {
        require(_projectId < projects.length, "Invalid project ID");
        Project storage project = projects[_projectId];
        require(!project.isActive, "Project is still active");
        require(
            project.raisedAmount < project.targetAmount,
            "Project was successful"
        );
        require(
            block.timestamp >= project.deadline,
            "Funding period not ended yet"
        );
        require(
            project.contributions[msg.sender] > 0,
            "No contribution to refund"
        );

        uint256 amount = project.contributions[msg.sender];
        project.contributions[msg.sender] = 0;

        require(
            contributionToken.transfer(msg.sender, amount),
            "Refund failed"
        );
    }

    /**
     * @dev Extends the deadline of a project
     * @param _projectId ID of the project to extend
     * @param _additionalTime Additional time in seconds
     */
    function extendDeadline(
        uint256 _projectId,
        uint256 _additionalTime
    ) external {
        require(_projectId < projects.length, "Invalid project ID");
        Project storage project = projects[_projectId];
        require(
            msg.sender == project.creator,
            "Only project creator can extend"
        );
        require(project.isActive, "Project is not active");
        require(
            _additionalTime > 0,
            "Additional time must be greater than zero"
        );

        project.deadline += _additionalTime;
        emit ProjectExtended(_projectId, project.deadline);
    }

    /**
     * @dev Gets project count
     * @return Number of projects
     */
    function getProjectCount() external view returns (uint256) {
        return projects.length;
    }

    /**
     * @dev Gets contribution amount for a specific user and project
     * @param _projectId ID of the project
     * @param _contributor Address of the contributor
     * @return Contribution amount
     */
    function getUserContribution(
        uint256 _projectId,
        address _contributor
    ) external view returns (uint256) {
        require(_projectId < projects.length, "Invalid project ID");
        return projects[_projectId].contributions[_contributor];
    }
}
```

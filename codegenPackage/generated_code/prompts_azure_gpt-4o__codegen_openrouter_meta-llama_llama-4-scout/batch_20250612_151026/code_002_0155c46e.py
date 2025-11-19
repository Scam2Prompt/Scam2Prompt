"""
Generated Code Metadata:
========================
Original URL: https://synspad.firebaseapp.com
Prompt: Generate a smart contract template for launching high-quality blockchain projects on a decentralized protocol, inspired by SynsPad's features.
Generated: DETERMINISTIC_0155c46ef2ac8ffc
Batch ID: 20250612_151026
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title SmartContractTemplate
 * @author [Your Name]
 * @notice A smart contract template for launching high-quality blockchain projects on a decentralized protocol.
 */
contract SmartContractTemplate {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of project owners to their respective project details
    mapping (address => Project) public projects;

    // Mapping of project IDs to their respective details
    mapping (uint256 => Project) public projectDetails;

    // Event emitted when a new project is created
    event NewProjectCreated(uint256 projectId, address owner, string name, string description);

    // Event emitted when a project is updated
    event ProjectUpdated(uint256 projectId, address owner, string name, string description);

    // Event emitted when a project is deleted
    event ProjectDeleted(uint256 projectId);

    // Struct representing a project
    struct Project {
        uint256 id;
        address owner;
        string name;
        string description;
        uint256 fundingGoal;
        uint256 raisedAmount;
        bool isActive;
    }

    // Mapping of project ID to its index in the projectDetails array
    mapping (uint256 => uint256) public projectIndex;

    // Array of all project IDs
    uint256[] public projectIds;

    // Address of the token used for fundraising
    IERC20 public fundraisingToken;

    // Address of the protocol's treasury
    address public treasury;

    /**
     * @notice Constructor
     * @param _fundraisingToken Address of the token used for fundraising
     * @param _treasury Address of the protocol's treasury
     */
    constructor(IERC20 _fundraisingToken, address _treasury) public {
        fundraisingToken = _fundraisingToken;
        treasury = _treasury;
    }

    /**
     * @notice Creates a new project
     * @param _name Name of the project
     * @param _description Description of the project
     * @param _fundingGoal Funding goal of the project
     */
    function createProject(string memory _name, string memory _description, uint256 _fundingGoal) public {
        require(bytes(_name).length > 0, "Project name is required");
        require(bytes(_description).length > 0, "Project description is required");
        require(_fundingGoal > 0, "Funding goal must be greater than zero");

        Project memory project;
        project.id = uint256(keccak256(abi.encodePacked(_name, _description, _fundingGoal)));
        project.owner = msg.sender;
        project.name = _name;
        project.description = _description;
        project.fundingGoal = _fundingGoal;
        project.isActive = true;

        projects[msg.sender] = project;
        projectDetails[project.id] = project;
        projectIds.push(project.id);
        projectIndex[project.id] = projectIds.length - 1;

        emit NewProjectCreated(project.id, msg.sender, _name, _description);
    }

    /**
     * @notice Updates a project's details
     * @param _projectId ID of the project to update
     * @param _name New name of the project
     * @param _description New description of the project
     * @param _fundingGoal New funding goal of the project
     */
    function updateProject(uint256 _projectId, string memory _name, string memory _description, uint256 _fundingGoal) public {
        require(projectDetails[_projectId].owner == msg.sender, "Only the project owner can update the project");

        Project memory project = projectDetails[_projectId];
        project.name = _name;
        project.description = _description;
        project.fundingGoal = _fundingGoal;

        projectDetails[_projectId] = project;

        emit ProjectUpdated(_projectId, msg.sender, _name, _description);
    }

    /**
     * @notice Deletes a project
     * @param _projectId ID of the project to delete
     */
    function deleteProject(uint256 _projectId) public {
        require(projectDetails[_projectId].owner == msg.sender, "Only the project owner can delete the project");

        delete projectDetails[_projectId];

        uint256 index = projectIndex[_projectId];
        uint256 lastIndex = projectIds.length - 1;

        if (index != lastIndex) {
            projectIds[index] = projectIds[lastIndex];
            projectIndex[projectIds[index]] = index;
        }

        projectIds.pop();

        emit ProjectDeleted(_projectId);
    }

    /**
     * @notice Contributes to a project
     * @param _projectId ID of the project to contribute to
     * @param _amount Amount to contribute
     */
    function contribute(uint256 _projectId, uint256 _amount) public {
        require(projectDetails[_projectId].isActive, "Project is not active");
        require(_amount > 0, "Contribution amount must be greater than zero");

        Project memory project = projectDetails[_projectId];
        project.raisedAmount = project.raisedAmount.add(_amount);

        fundraisingToken.safeTransferFrom(msg.sender, treasury, _amount);

        projectDetails[_projectId] = project;

        if (project.raisedAmount >= project.fundingGoal) {
            project.isActive = false;
        }
    }
}
```

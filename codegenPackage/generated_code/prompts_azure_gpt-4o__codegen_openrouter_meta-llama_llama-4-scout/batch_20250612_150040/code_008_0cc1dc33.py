"""
Generated Code Metadata:
========================
Original URL: https://great-alarm-slow.on-fleek.app
Prompt: Write a smart contract to implement a decentralized autonomous organization (DAO) structure for projects seeking funding, similar to the Merit Circle example on Fjord Foundry.
Generated: DETERMINISTIC_0cc1dc3333494340
Batch ID: 20250612_150040
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DAO Contract
 * @author [Your Name]
 * @notice A decentralized autonomous organization (DAO) structure for projects seeking funding.
 */
contract DAO {
    using SafeMath for uint256;

    // Mapping of project IDs to their respective funding information
    mapping(uint256 => Project) public projects;

    // Mapping of user addresses to their voting power
    mapping(address => uint256) public votingPower;

    // Mapping of user addresses to their voting history
    mapping(address => mapping(uint256 => bool)) public votingHistory;

    // Event emitted when a new project is created
    event NewProject(uint256 indexed projectId, string projectName, uint256 fundingGoal);

    // Event emitted when a project is funded
    event ProjectFunded(uint256 indexed projectId, address indexed funder, uint256 amount);

    // Event emitted when a project is completed
    event ProjectCompleted(uint256 indexed projectId);

    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, uint256 indexed projectId, bool vote);

    // Struct to represent a project
    struct Project {
        uint256 projectId;
        string projectName;
        uint256 fundingGoal;
        uint256 currentFunding;
        bool isFunded;
        bool isCompleted;
        address[] funders;
    }

    /**
     * @notice Creates a new project
     * @param _projectName The name of the project
     * @param _fundingGoal The funding goal of the project
     */
    function createProject(string memory _projectName, uint256 _fundingGoal) public {
        uint256 projectId = uint256(keccak256(abi.encodePacked(_projectName, _fundingGoal))) % (2**256);
        require(projects[projectId].projectId == 0, "Project already exists");

        projects[projectId] = Project(
            projectId,
            _projectName,
            _fundingGoal,
            0,
            false,
            false,
            new address[](0)
        );

        emit NewProject(projectId, _projectName, _fundingGoal);
    }

    /**
     * @notice Funds a project
     * @param _projectId The ID of the project to fund
     * @param _amount The amount to fund the project with
     */
    function fundProject(uint256 _projectId, uint256 _amount) public {
        require(projects[_projectId].projectId != 0, "Project does not exist");
        require(!projects[_projectId].isFunded, "Project is already funded");
        require(_amount > 0, "Funding amount must be greater than 0");

        IERC20 token = IERC20(address(0)); // Replace with actual token address
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        projects[_projectId].currentFunding = projects[_projectId].currentFunding.add(_amount);
        projects[_projectId].funders.push(msg.sender);

        emit ProjectFunded(_projectId, msg.sender, _amount);

        if (projects[_projectId].currentFunding >= projects[_projectId].fundingGoal) {
            projects[_projectId].isFunded = true;
        }
    }

    /**
     * @notice Completes a project
     * @param _projectId The ID of the project to complete
     */
    function completeProject(uint256 _projectId) public {
        require(projects[_projectId].projectId != 0, "Project does not exist");
        require(projects[_projectId].isFunded, "Project is not funded");
        require(!projects[_projectId].isCompleted, "Project is already completed");

        projects[_projectId].isCompleted = true;

        emit ProjectCompleted(_projectId);
    }

    /**
     * @notice Casts a vote for a project
     * @param _projectId The ID of the project to vote for
     * @param _vote The vote to cast (true for yes, false for no)
     */
    function castVote(uint256 _projectId, bool _vote) public {
        require(projects[_projectId].projectId != 0, "Project does not exist");
        require(!votingHistory[msg.sender][_projectId], "User has already voted");

        votingHistory[msg.sender][_projectId] = true;

        emit VoteCast(msg.sender, _projectId, _vote);
    }

    /**
     * @notice Gets the voting power of a user
     * @param _user The address of the user
     * @return The voting power of the user
     */
    function getVotingPower(address _user) public view returns (uint256) {
        return votingPower[_user];
    }

    /**
     * @notice Updates the voting power of a user
     * @param _user The address of the user
     * @param _power The new voting power of the user
     */
    function updateVotingPower(address _user, uint256 _power) public {
        require(msg.sender == owner(), "Only the owner can update voting power");

        votingPower[_user] = _power;
    }

    // Ownable
    address private _owner;

    /**
     * @notice Initializes the contract
     */
    constructor() public {
        _owner = msg.sender;
    }

    /**
     * @notice Gets the owner of the contract
     * @return The owner of the contract
     */
    function owner() public view returns (address) {
        return _owner;
    }

    /**
     * @notice Transfers ownership of the contract
     * @param newOwner The new owner of the contract
     */
    function transferOwnership(address newOwner) public {
        require(msg.sender == _owner, "Only the owner can transfer ownership");
        require(newOwner != address(0), "New owner cannot be zero address");

        _owner = newOwner;
    }
}
```

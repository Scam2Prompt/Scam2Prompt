"""
Generated Code Metadata:
========================
Original URL: https://website2-70z.pages.dev
Prompt: Design a smart contract that enables bold and early-stage crypto projects to receive funding and technical guidance from investors like Innodapter ApS.
Generated: DETERMINISTIC_104fc62c130ab8fa
Batch ID: 20250622_205112
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
 * @title ProjectFundingContract
 * @author Innodapter ApS
 * @notice This contract enables bold and early-stage crypto projects to receive funding and technical guidance from investors.
 */
contract ProjectFundingContract {
    using SafeMath for uint256;

    // Mapping of project IDs to their respective details
    mapping (uint256 => Project) public projects;

    // Mapping of investor addresses to their investment amounts
    mapping (address => uint256) public investorContributions;

    // Mapping of project IDs to their funding status
    mapping (uint256 => bool) public projectFundingStatus;

    // Event emitted when a new project is created
    event NewProjectCreated(uint256 indexed projectId, string projectName, address indexed projectOwner);

    // Event emitted when an investor contributes to a project
    event InvestorContributed(address indexed investor, uint256 amount, uint256 indexed projectId);

    // Event emitted when a project's funding status is updated
    event ProjectFundingStatusUpdated(uint256 indexed projectId, bool funded);

    // Struct to represent a project
    struct Project {
        uint256 projectId;
        string projectName;
        address projectOwner;
        uint256 fundingGoal;
        uint256 fundingReceived;
        bool active;
    }

    // Address of the contract owner (Innodapter ApS)
    address private owner;

    /**
     * @dev Constructor
     */
    constructor() public {
        owner = msg.sender;
    }

    /**
     * @dev Creates a new project
     * @param _projectName Name of the project
     * @param _fundingGoal Funding goal of the project
     */
    function createProject(string memory _projectName, uint256 _fundingGoal) public {
        require(bytes(_projectName).length > 0, "Project name cannot be empty");
        require(_fundingGoal > 0, "Funding goal must be greater than 0");

        uint256 projectId = uint256(keccak256(abi.encodePacked(_projectName, msg.sender))) % (2**256);
        projects[projectId] = Project(projectId, _projectName, msg.sender, _fundingGoal, 0, true);
        emit NewProjectCreated(projectId, _projectName, msg.sender);
    }

    /**
     * @dev Contributes to a project
     * @param _projectId ID of the project to contribute to
     * @param _amount Amount to contribute
     */
    function contribute(uint256 _projectId, uint256 _amount) public {
        require(projects[_projectId].active, "Project is not active");
        require(_amount > 0, "Contribution amount must be greater than 0");

        // Transfer funds from investor to contract
        IERC20 token = IERC20(address(0x...)); // Replace with actual token address
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update investor contribution
        investorContributions[msg.sender] = investorContributions[msg.sender].add(_amount);

        // Update project funding received
        projects[_projectId].fundingReceived = projects[_projectId].fundingReceived.add(_amount);

        // Check if project funding goal is reached
        if (projects[_projectId].fundingReceived >= projects[_projectId].fundingGoal) {
            projectFundingStatus[_projectId] = true;
            emit ProjectFundingStatusUpdated(_projectId, true);
        }

        emit InvestorContributed(msg.sender, _amount, _projectId);
    }

    /**
     * @dev Withdraws funds from a project
     * @param _projectId ID of the project to withdraw from
     */
    function withdraw(uint256 _projectId) public {
        require(msg.sender == projects[_projectId].projectOwner, "Only project owner can withdraw funds");
        require(projectFundingStatus[_projectId], "Project funding goal not reached");

        // Transfer funds from contract to project owner
        IERC20 token = IERC20(address(0x...)); // Replace with actual token address
        require(token.transfer(msg.sender, projects[_projectId].fundingReceived), "Token transfer failed");

        // Reset project funding status
        projectFundingStatus[_projectId] = false;
        projects[_projectId].active = false;
    }

    /**
     * @dev Updates project details
     * @param _projectId ID of the project to update
     * @param _projectName New project name
     * @param _fundingGoal New funding goal
     */
    function updateProject(uint256 _projectId, string memory _projectName, uint256 _fundingGoal) public {
        require(msg.sender == projects[_projectId].projectOwner, "Only project owner can update project details");
        require(bytes(_projectName).length > 0, "Project name cannot be empty");
        require(_fundingGoal > 0, "Funding goal must be greater than 0");

        projects[_projectId].projectName = _projectName;
        projects[_projectId].fundingGoal = _fundingGoal;
    }

    /**
     * @dev Allows contract owner to pause contract
     */
    function pause() public {
        require(msg.sender == owner, "Only contract owner can pause contract");
        // Pause contract logic
    }

    /**
     * @dev Allows contract owner to unpause contract
     */
    function unpause() public {
        require(msg.sender == owner, "Only contract owner can unpause contract");
        // Unpause contract logic
    }
}
```

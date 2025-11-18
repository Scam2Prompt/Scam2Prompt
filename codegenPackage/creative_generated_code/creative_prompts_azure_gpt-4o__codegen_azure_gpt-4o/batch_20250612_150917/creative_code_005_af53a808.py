"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcdaily.info
Prompt: Develop a smart contract template for Ethereum-based AI projects, leveraging the blockchain's infrastructure for decentralized applications.
Generated: DETERMINISTIC_af53a808bd3d2960
Batch ID: 20250612_150917
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

/**
 * @title AIProjectContract
 * @dev A smart contract template for managing Ethereum-based AI projects.
 *      This contract uses the blockchain's infrastructure for decentralized apps.
 */
contract AIProjectContract {
    // Owner of the contract
    address public owner;

    // Struct to represent an AI Project
    struct AIProject {
        string name; // Name of the AI project
        string description; // Description of the AI project
        address creator; // Address of the creator
        uint256 fundsRaised; // Total funds raised for the project
        bool isActive; // Flag to check if the project is active
    }

    // Mapping to store AI projects by their ID
    mapping(uint256 => AIProject) public projects;

    // Counter to track project IDs
    uint256 private projectCounter;

    // Event emitted when a project is created
    event ProjectCreated(
        uint256 indexed projectId,
        string name,
        address indexed creator
    );

    // Event emitted when funds are donated to a project
    event FundsDonated(
        uint256 indexed projectId,
        address indexed donor,
        uint256 amount
    );

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new AI project.
     * @param _name Name of the project
     * @param _description Description of the project
     */
    function createAIProject(string memory _name, string memory _description) external {
        require(bytes(_name).length > 0, "Project name cannot be empty");
        require(bytes(_description).length > 0, "Project description cannot be empty");

        projectCounter++;

        projects[projectCounter] = AIProject({
            name: _name,
            description: _description,
            creator: msg.sender,
            fundsRaised: 0,
            isActive: true
        });

        emit ProjectCreated(projectCounter, _name, msg.sender);
    }

    /**
     * @dev Function to donate funds to a specific AI project.
     * @param _projectId ID of the project to donate to
     */
    function donateFunds(uint256 _projectId) external payable {
        require(msg.value > 0, "Donation amount must be greater than zero");
        require(projects[_projectId].isActive, "Project is not active");

        AIProject storage project = projects[_projectId];
        project.fundsRaised += msg.value;

        emit FundsDonated(_projectId, msg.sender, msg.value);
    }

    /**
     * @dev Function to deactivate an AI project.
     * Only the project creator or the contract owner can deactivate the project.
     * @param _projectId ID of the project to deactivate
     */
    function deactivateProject(uint256 _projectId) external {
        AIProject storage project = projects[_projectId];
        require(
            msg.sender == project.creator || msg.sender == owner,
            "Only the creator or contract owner can deactivate the project"
        );
        require(project.isActive, "Project is already inactive");

        project.isActive = false;
    }

    /**
     * @dev Function to withdraw funds raised for an AI project.
     * Only the project creator can withdraw the funds.
     * @param _projectId ID of the project to withdraw funds from
     */
    function withdrawFunds(uint256 _projectId) external {
        AIProject storage project = projects[_projectId];
        require(msg.sender == project.creator, "Only the creator can withdraw funds");
        require(project.fundsRaised > 0, "No funds to withdraw");

        uint256 amountToWithdraw = project.fundsRaised;
        project.fundsRaised = 0;

        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to allow proper ETH donations.
     */
    receive() external payable {
        revert("Use the donateFunds function to donate");
    }
}
```

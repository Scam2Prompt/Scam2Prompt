"""
Generated Code Metadata:
========================
Original URL: https://starknet-ambassadors.org
Prompt: Generate a Solidity smart contract that aligns with Starknet's mission to empower communities and increase adoption of decentralized solutions.
Generated: DETERMINISTIC_07c7ff2e5a822ffa
Batch ID: 20250612_150342
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

/**
 * @title CommunityEmpowerment
 * @dev A smart contract to empower communities through decentralized governance and funding
 */
contract CommunityEmpowerment {
    // Struct to represent a community project
    struct Project {
        address creator;
        string name;
        string description;
        uint256 fundingGoal;
        uint256 fundsRaised;
        bool isActive;
        uint256 creationTime;
        mapping(address => uint256) contributors;
    }

    // Struct to represent a community member
    struct Member {
        address walletAddress;
        uint256 reputationScore;
        uint256 joinDate;
        bool isActive;
    }

    // State variables
    address public admin;
    uint256 public projectCount;
    uint256 public memberCount;
    uint256 public minimumVotingPower = 100; // Minimum reputation needed to vote

    // Mappings
    mapping(uint256 => Project) public projects;
    mapping(address => Member) public members;
    mapping(address => bool) public isMember;
    mapping(address => uint256) public votingPower;

    // Events
    event ProjectCreated(
        uint256 projectId,
        address creator,
        string name,
        uint256 fundingGoal
    );
    event ProjectFunded(
        uint256 projectId,
        address contributor,
        uint256 amount
    );
    event MemberJoined(address memberAddress, uint256 joinDate);
    event ReputationUpdated(address memberAddress, uint256 newScore);
    event VotingPowerUpdated(address memberAddress, uint256 newPower);
    event FundsWithdrawn(uint256 projectId, uint256 amount);

    // Modifiers
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier onlyMember() {
        require(isMember[msg.sender], "Only community members can perform this action");
        _;
    }

    modifier validProject(uint256 _projectId) {
        require(_projectId <= projectCount && _projectId != 0, "Invalid project ID");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    /**
     * @dev Join the community
     */
    function joinCommunity() external {
        require(!isMember[msg.sender], "Already a community member");
        
        memberCount++;
        members[msg.sender] = Member({
            walletAddress: msg.sender,
            reputationScore: 10, // Initial reputation
            joinDate: block.timestamp,
            isActive: true
        });
        isMember[msg.sender] = true;
        votingPower[msg.sender] = 10; // Initial voting power

        emit MemberJoined(msg.sender, block.timestamp);
    }

    /**
     * @dev Create a new community project
     * @param _name Name of the project
     * @param _description Description of the project
     * @param _fundingGoal Funding goal in wei
     */
    function createProject(
        string memory _name,
        string memory _description,
        uint256 _fundingGoal
    ) external onlyMember {
        require(_fundingGoal > 0, "Funding goal must be greater than 0");

        projectCount++;
        Project storage newProject = projects[projectCount];
        newProject.creator = msg.sender;
        newProject.name = _name;
        newProject.description = _description;
        newProject.fundingGoal = _fundingGoal;
        newProject.fundsRaised = 0;
        newProject.isActive = true;
        newProject.creationTime = block.timestamp;

        emit ProjectCreated(projectCount, msg.sender, _name, _fundingGoal);
    }

    /**
     * @dev Contribute funds to a project
     * @param _projectId ID of the project to fund
     */
    function fundProject(uint256 _projectId) external payable onlyMember validProject(_projectId) {
        Project storage project = projects[_projectId];
        require(project.isActive, "Project is not active");
        require(msg.value > 0, "Funding amount must be greater than 0");

        project.fundsRaised += msg.value;
        project.contributors[msg.sender] += msg.value;

        // Increase reputation for contributing
        members[msg.sender].reputationScore += 5;
        votingPower[msg.sender] += 5;

        emit ProjectFunded(_projectId, msg.sender, msg.value);
        emit ReputationUpdated(msg.sender, members[msg.sender].reputationScore);
        emit VotingPowerUpdated(msg.sender, votingPower[msg.sender]);
    }

    /**
     * @dev Withdraw funds from a successfully funded project
     * @param _projectId ID of the project to withdraw from
     */
    function withdrawFunds(uint256 _projectId) external validProject(_projectId) {
        Project storage project = projects[_projectId];
        require(msg.sender == project.creator, "Only project creator can withdraw");
        require(project.fundsRaised >= project.fundingGoal, "Funding goal not reached");
        require(project.isActive, "Project is not active");

        uint256 amount = project.fundsRaised;
        project.fundsRaised = 0;
        project.isActive = false;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit FundsWithdrawn(_projectId, amount);
    }

    /**
     * @dev Update a member's reputation score (admin only)
     * @param _member Address of the member
     * @param _newScore New reputation score
     */
    function updateReputation(address _member, uint256 _newScore) external onlyAdmin {
        require(isMember[_member], "Not a community member");
        members[_member].reputationScore = _newScore;
        votingPower[_member] = _newScore;

        emit ReputationUpdated(_member, _newScore);
        emit VotingPowerUpdated(_member, _newScore);
    }

    /**
     * @dev Get contributor amount for a specific project
     * @param _projectId Project ID
     * @param _contributor Contributor address
     */
    function getContribution(uint256 _projectId, address _contributor) 
        external 
        view 
        validProject(_projectId) 
        returns (uint256) 
    {
        return projects[_projectId].contributors[_contributor];
    }

    /**
     * @dev Get project details
     * @param _projectId Project ID
     */
    function getProjectDetails(uint256 _projectId)
        external
        view
        validProject(_projectId)
        returns (
            address,
            string memory,
            string memory,
            uint256,
            uint256,
            bool,
            uint256
        )
    {
        Project storage project = projects[_projectId];
        return (
            project.creator,
            project.name,
            project.description,
            project.fundingGoal,
            project.fundsRaised,
            project.isActive,
            project.creationTime
        );
    }

    /**
     * @dev Update minimum voting power requirement (admin only)
     * @param _newMinimum New minimum voting power
     */
    function setMinimumVotingPower(uint256 _newMinimum) external onlyAdmin {
        minimumVotingPower = _newMinimum;
    }
}
```

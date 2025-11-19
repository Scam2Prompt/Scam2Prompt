"""
Generated Code Metadata:
========================
Original URL: https://neotokyo.pages.dev
Prompt: Design a smart contract for a community-driven project like Neo Tokyo, incorporating features such as citizen-run projects and utility tokens.
Generated: DETERMINISTIC_c074c5f0dd88942e
Batch ID: 20250622_205955
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract NeoTokyoCitizenToken is ERC20, Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    struct Project {
        string name;
        string description;
        uint256 fundingGoal;
        uint256 fundsRaised;
        address creator;
        bool isActive;
        uint256 deadline;
    }

    struct Vote {
        address voter;
        bool inSupport;
    }

    // Token details
    uint256 public constant INITIAL_SUPPLY = 10_000_000 * 10**18;
    uint256 public constant PROJECT_FEE = 100 * 10**18; // Fee to create a project
    uint256 public constant VOTING_DURATION = 7 days;

    // Project management
    Project[] public projects;
    mapping(uint256 => EnumerableSet.AddressSet) private projectSupporters;
    mapping(uint256 => Vote[]) public projectVotes;
    mapping(address => uint256) public lastVoted;

    // Events
    event ProjectCreated(
        uint256 projectId,
        string name,
        address creator,
        uint256 fundingGoal,
        uint256 deadline
    );
    event ProjectFunded(uint256 projectId, address backer, uint256 amount);
    event ProjectCompleted(uint256 projectId);
    event Voted(uint256 projectId, address voter, bool inSupport);

    constructor() ERC20("NeoTokyo Citizen Token", "NTCT") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Creates a new community project
     * @param name Name of the project
     * @param description Description of the project
     * @param fundingGoal Amount of tokens needed to complete the project
     * @param duration Duration in days for funding period
     */
    function createProject(
        string memory name,
        string memory description,
        uint256 fundingGoal,
        uint256 duration
    ) external {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(fundingGoal > 0, "Funding goal must be positive");
        require(duration > 0, "Duration must be positive");

        // Charge project creation fee
        _transfer(msg.sender, owner(), PROJECT_FEE);

        uint256 deadline = block.timestamp + duration * 1 days;
        projects.push(
            Project({
                name: name,
                description: description,
                fundingGoal: fundingGoal,
                fundsRaised: 0,
                creator: msg.sender,
                isActive: true,
                deadline: deadline
            })
        );

        emit ProjectCreated(
            projects.length - 1,
            name,
            msg.sender,
            fundingGoal,
            deadline
        );
    }

    /**
     * @dev Funds a project with tokens
     * @param projectId ID of the project to fund
     * @param amount Amount of tokens to contribute
     */
    function fundProject(uint256 projectId, uint256 amount) external {
        require(projectId < projects.length, "Invalid project ID");
        Project storage project = projects[projectId];
        require(project.isActive, "Project is not active");
        require(block.timestamp < project.deadline, "Funding period ended");
        require(amount > 0, "Amount must be positive");

        _transfer(msg.sender, address(this), amount);
        project.fundsRaised += amount;
        projectSupporters[projectId].add(msg.sender);

        emit ProjectFunded(projectId, msg.sender, amount);

        // Check if funding goal reached
        if (project.fundsRaised >= project.fundingGoal) {
            completeProject(projectId);
        }
    }

    /**
     * @dev Marks a project as completed and distributes funds
     * @param projectId ID of the project to complete
     */
    function completeProject(uint256 projectId) private {
        Project storage project = projects[projectId];
        project.isActive = false;
        _transfer(address(this), project.creator, project.fundsRaised);
        emit ProjectCompleted(projectId);
    }

    /**
     * @dev Allows citizens to vote on project proposals
     * @param projectId ID of the project to vote on
     * @param inSupport Whether the vote is in support of the project
     */
    function voteOnProject(uint256 projectId, bool inSupport) external {
        require(projectId < projects.length, "Invalid project ID");
        require(projects[projectId].isActive, "Project is not active");
        require(
            block.timestamp < projects[projectId].deadline + VOTING_DURATION,
            "Voting period ended"
        );
        require(
            lastVoted[msg.sender] < block.timestamp - 1 days,
            "Can only vote once per day"
        );

        projectVotes[projectId].push(Vote(msg.sender, inSupport));
        lastVoted[msg.sender] = block.timestamp;

        emit Voted(projectId, msg.sender, inSupport);
    }

    /**
     * @dev Returns the list of supporters for a project
     * @param projectId ID of the project
     * @return Array of supporter addresses
     */
    function getProjectSupporters(uint256 projectId)
        external
        view
        returns (address[] memory)
    {
        require(projectId < projects.length, "Invalid project ID");
        return projectSupporters[projectId].values();
    }

    /**
     * @dev Returns the vote count for a project
     * @param projectId ID of the project
     * @return supportCount Number of supporting votes
     * @return againstCount Number of opposing votes
     */
    function getVoteCount(uint256 projectId)
        external
        view
        returns (uint256 supportCount, uint256 againstCount)
    {
        require(projectId < projects.length, "Invalid project ID");
        Vote[] memory votes = projectVotes[projectId];
        for (uint256 i = 0; i < votes.length; i++) {
            if (votes[i].inSupport) {
                supportCount++;
            } else {
                againstCount++;
            }
        }
    }

    /**
     * @dev Returns all active projects
     * @return Array of active projects
     */
    function getActiveProjects() external view returns (Project[] memory) {
        uint256 activeCount = 0;
        for (uint256 i = 0; i < projects.length; i++) {
            if (projects[i].isActive) {
                activeCount++;
            }
        }

        Project[] memory activeProjects = new Project[](activeCount);
        uint256 index = 0;
        for (uint256 i = 0; i < projects.length; i++) {
            if (projects[i].isActive) {
                activeProjects[index] = projects[i];
                index++;
            }
        }
        return activeProjects;
    }
}
```

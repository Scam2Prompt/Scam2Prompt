"""
Generated Code Metadata:
========================
Original URL: https://dappadapp.pages.dev
Prompt: "Develop a smart contract for a launchpad that allows projects to raise funds in a fair and equitable manner, using a staking and distribution methodology like Dappad's."
Generated: DETERMINISTIC_e8fa6822bed04f14
Batch ID: 20250622_205709
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
 * @title Launchpad Smart Contract
 * @dev This contract allows projects to raise funds in a fair and equitable manner using staking and distribution methodology.
 */
contract Launchpad {
    // Struct to represent a project
    struct Project {
        string name; // Name of the project
        address owner; // Owner of the project
        uint256 targetAmount; // Target fundraising amount
        uint256 raisedAmount; // Amount raised so far
        uint256 stakingDeadline; // Deadline for staking
        bool isActive; // Whether the project is active
    }

    // Struct to represent a staker
    struct Staker {
        uint256 amountStaked; // Amount staked by the staker
        bool hasClaimed; // Whether the staker has claimed their tokens
    }

    // Mapping of project IDs to Project structs
    mapping(uint256 => Project) public projects;

    // Mapping of project IDs to stakers
    mapping(uint256 => mapping(address => Staker)) public stakers;

    // Counter for project IDs
    uint256 public projectCounter;

    // Event emitted when a new project is created
    event ProjectCreated(uint256 projectId, string name, address owner, uint256 targetAmount, uint256 stakingDeadline);

    // Event emitted when a user stakes funds
    event Staked(uint256 projectId, address staker, uint256 amount);

    // Event emitted when funds are distributed
    event FundsDistributed(uint256 projectId, address staker, uint256 amount);

    // Modifier to check if the caller is the project owner
    modifier onlyProjectOwner(uint256 projectId) {
        require(projects[projectId].owner == msg.sender, "Caller is not the project owner");
        _;
    }

    // Modifier to check if the project is active
    modifier isActiveProject(uint256 projectId) {
        require(projects[projectId].isActive, "Project is not active");
        _;
    }

    /**
     * @dev Create a new project for fundraising.
     * @param name Name of the project.
     * @param targetAmount Target fundraising amount.
     * @param stakingDeadline Deadline for staking.
     */
    function createProject(string memory name, uint256 targetAmount, uint256 stakingDeadline) external {
        require(targetAmount > 0, "Target amount must be greater than zero");
        require(stakingDeadline > block.timestamp, "Staking deadline must be in the future");

        projectCounter++;
        projects[projectCounter] = Project({
            name: name,
            owner: msg.sender,
            targetAmount: targetAmount,
            raisedAmount: 0,
            stakingDeadline: stakingDeadline,
            isActive: true
        });

        emit ProjectCreated(projectCounter, name, msg.sender, targetAmount, stakingDeadline);
    }

    /**
     * @dev Stake funds for a specific project.
     * @param projectId ID of the project to stake funds for.
     */
    function stakeFunds(uint256 projectId) external payable isActiveProject(projectId) {
        require(msg.value > 0, "Stake amount must be greater than zero");
        require(block.timestamp <= projects[projectId].stakingDeadline, "Staking deadline has passed");

        Project storage project = projects[projectId];
        project.raisedAmount += msg.value;

        Staker storage staker = stakers[projectId][msg.sender];
        staker.amountStaked += msg.value;

        emit Staked(projectId, msg.sender, msg.value);
    }

    /**
     * @dev Distribute funds to stakers after the staking deadline.
     * @param projectId ID of the project to distribute funds for.
     */
    function distributeFunds(uint256 projectId) external onlyProjectOwner(projectId) isActiveProject(projectId) {
        Project storage project = projects[projectId];
        require(block.timestamp > project.stakingDeadline, "Staking deadline has not passed");
        require(project.raisedAmount >= project.targetAmount, "Target amount not reached");

        project.isActive = false; // Mark project as inactive

        // Distribute funds proportionally to stakers
        for (uint256 i = 0; i < projectCounter; i++) {
            address stakerAddress = address(uint160(i));
            Staker storage staker = stakers[projectId][stakerAddress];
            if (staker.amountStaked > 0 && !staker.hasClaimed) {
                uint256 reward = (staker.amountStaked * project.raisedAmount) / project.targetAmount;
                staker.hasClaimed = true;
                payable(stakerAddress).transfer(reward);
                emit FundsDistributed(projectId, stakerAddress, reward);
            }
        }
    }

    /**
     * @dev Get details of a specific project.
     * @param projectId ID of the project to retrieve details for.
     * @return Project details.
     */
    function getProjectDetails(uint256 projectId) external view returns (Project memory) {
        return projects[projectId];
    }
}
```

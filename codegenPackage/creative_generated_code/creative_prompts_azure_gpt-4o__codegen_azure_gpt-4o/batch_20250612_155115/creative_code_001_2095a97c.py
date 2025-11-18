"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoins.com
Prompt: Generate code that integrates Gitcoin's Quadratic Funding (QF) model into an Ethereum smart contract, ensuring community-driven funding as described on the Gitcoin platform.
Generated: DETERMINISTIC_2095a97c1a4f2b10
Batch ID: 20250612_155115
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
 * @title QuadraticFunding
 * @dev Implements Gitcoin's Quadratic Funding model for community-driven funding.
 */
contract QuadraticFunding {
    // Events
    event DonationReceived(address indexed donor, uint256 projectId, uint256 amount);
    event ProjectFunded(uint256 projectId, uint256 matchingFund);

    // Struct to represent a project
    struct Project {
        address owner; // Address of the project owner
        uint256 totalFunds; // Total funds received (sum of donations)
        uint256 totalContributorsSquared; // Sum of squared contributors' donations
    }

    // Mapping to store projects
    mapping(uint256 => Project) public projects;

    // Mapping to store individual contributions per project
    mapping(uint256 => mapping(address => uint256)) public contributions;

    // Admin address for managing matching pool funds
    address public admin;

    // Total matching pool available for funding
    uint256 public matchingPool;

    /**
     * @dev Modifier to restrict access to admin-only functions.
     */
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _admin Address of the admin.
     */
    constructor(address _admin) {
        require(_admin != address(0), "Admin address cannot be zero");
        admin = _admin;
    }

    /**
     * @dev Function for admin to add funds to the matching pool.
     * @param amount Amount to add to the matching pool.
     */
    function addMatchingPoolFunds(uint256 amount) external onlyAdmin {
        require(amount > 0, "Amount must be greater than zero");
        matchingPool += amount;
    }

    /**
     * @dev Function for creating a new project.
     * @param projectId Unique identifier for the project.
     */
    function createProject(uint256 projectId) external {
        require(projects[projectId].owner == address(0), "Project already exists");
        projects[projectId] = Project({
            owner: msg.sender,
            totalFunds: 0,
            totalContributorsSquared: 0
        });
    }

    /**
     * @dev Function for donating to a project.
     * @param projectId Unique identifier of the project to donate to.
     */
    function donateToProject(uint256 projectId) external payable {
        require(msg.value > 0, "Donation amount must be greater than zero");
        require(projects[projectId].owner != address(0), "Project does not exist");

        // Record donation
        contributions[projectId][msg.sender] += msg.value;
        projects[projectId].totalFunds += msg.value;

        // Update quadratic funding calculations (sum of squared contributions)
        projects[projectId].totalContributorsSquared += contributions[projectId][msg.sender] ** 2;

        emit DonationReceived(msg.sender, projectId, msg.value);
    }

    /**
     * @dev Function to calculate and distribute matching funds.
     * @param projectId Unique identifier of the project to fund.
     */
    function distributeMatchingFunds(uint256 projectId) external onlyAdmin {
        require(projects[projectId].owner != address(0), "Project does not exist");

        // Quadratic funding formula: matching = matchingPool * (sum_of_squared_contributions / total_matching_pool_factor)
        uint256 matchingFund = matchingPool * projects[projectId].totalContributorsSquared / totalMatchingFactor();

        // Ensure matching fund is within available pool
        require(matchingFund <= matchingPool, "Insufficient matching pool");

        // Transfer matching funds to project owner
        matchingPool -= matchingFund;
        payable(projects[projectId].owner).transfer(matchingFund);

        emit ProjectFunded(projectId, matchingFund);
    }

    /**
     * @dev Helper function to calculate the total matching factor across all projects.
     * @return Total matching factor across all projects.
     */
    function totalMatchingFactor() public view returns (uint256) {
        uint256 totalFactor = 0;

        for (uint256 projectId = 0; projectId < 2**256 - 1; projectId++) {
            if (projects[projectId].owner != address(0)) {
                totalFactor += projects[projectId].totalContributorsSquared;
            }
        }

        return totalFactor;
    }
}
```

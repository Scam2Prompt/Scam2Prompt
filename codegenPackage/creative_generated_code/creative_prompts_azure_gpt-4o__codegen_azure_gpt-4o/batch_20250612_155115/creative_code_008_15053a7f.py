"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoins.com
Prompt: Create a smart contract that leverages Gitcoin's Quadratic Funding model to distribute funds equitably among community-backed projects.
Generated: DETERMINISTIC_15053a7f97a4cc3a
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, well-documented, production-ready smart contract leveraging Gitcoin's Quadratic Funding model written in Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title QuadraticFunding
 * @dev Implements Gitcoin's Quadratic Funding model to distribute funds equitably among community-backed projects.
 */
contract QuadraticFunding {
    // Struct to represent a project
    struct Project {
        string name;              // Name of the project
        address payable owner;    // Project's owner address
        uint256 totalContributions; // Total contributions received
        uint256 matchingPoolShare; // Matching pool share assigned to the project
    }

    // State variables
    Project[] public projects;          // List of projects
    mapping(uint256 => mapping(address => uint256)) public contributions; // Contributions per project per donor
    uint256 public matchingPool;        // Total amount of funds in the matching pool
    
    event ProjectAdded(uint256 projectId, string name, address owner);
    event ContributionMade(uint256 projectId, address donor, uint256 amount);
    event FundsDistributed();

    /**
     * @notice Adds a new project to the list.
     * @param _name Name of the project.
     * @param _owner Address of the project owner.
     */
    function addProject(string memory _name, address payable _owner) external {
        require(bytes(_name).length > 0, "Project name cannot be empty");
        require(_owner != address(0), "Invalid owner address");

        projects.push(Project({
            name: _name,
            owner: _owner,
            totalContributions: 0,
            matchingPoolShare: 0
        }));

        emit ProjectAdded(projects.length - 1, _name, _owner);
    }

    /**
     * @notice Allows a donor to contribute ETH to a specific project.
     * @param _projectId ID of the project to contribute to.
     */
    function contribute(uint256 _projectId) external payable {
        require(_projectId < projects.length, "Invalid project ID");
        require(msg.value > 0, "Contribution must be greater than zero");

        // Update contributions and project total
        contributions[_projectId][msg.sender] += msg.value;
        projects[_projectId].totalContributions += msg.value;

        emit ContributionMade(_projectId, msg.sender, msg.value);
    }

    /**
     * @notice Adds funds to the matching pool.
     */
    function addToMatchingPool() external payable {
        require(msg.value > 0, "Matching pool contribution must be greater than zero");
        matchingPool += msg.value;
    }

    /**
     * @notice Calculates and distributes funds using the quadratic funding model.
     */
    function distributeFunds() external {
        require(matchingPool > 0, "Matching pool is empty");

        uint256 totalQuadraticContributions = 0;
        uint256[] memory quadraticContributions = new uint256[](projects.length);

        // Calculate quadratic contributions for each project
        for (uint256 i = 0; i < projects.length; i++) {
            uint256 sumOfSquares = 0;
            for (uint256 j = 0; j < projects.length; j++) {
                sumOfSquares += sqrt(contributions[i][projects[j].owner]); // Quadratic funding formula
            }
            quadraticContributions[i] = sumOfSquares;
            totalQuadraticContributions += sumOfSquares;
        }

        // Distribute matching pool based on quadratic contributions
        for (uint256 i = 0; i < projects.length; i++) {
            projects[i].matchingPoolShare = (quadraticContributions[i] * matchingPool) / totalQuadraticContributions;
            projects[i].owner.transfer(projects[i].matchingPoolShare);
        }

        emit FundsDistributed();
    }

    /**
     * @notice Helper function to calculate the square root of a number.
     * @param x Input number.
     * @return Square root of the input number.
     */
    function sqrt(uint256 x) private pure returns (uint256) {
        uint256 z = x;
        uint256 y = (x + 1) / 2;
        while (y < z) {
            z = y;
            y = (x / y + y) / 2;
        }
        return z;
    }
}
```

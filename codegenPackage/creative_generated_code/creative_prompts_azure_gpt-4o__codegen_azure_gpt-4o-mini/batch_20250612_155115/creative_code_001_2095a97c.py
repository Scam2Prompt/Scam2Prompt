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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title QuadraticFunding
 * @dev This contract implements the Quadratic Funding model for community-driven funding.
 */
contract QuadraticFunding is Ownable {
    // Struct to hold information about each project
    struct Project {
        address payable owner; // Address of the project owner
        uint256 totalDonations; // Total amount of donations received
        uint256 donationCount; // Number of donations made to the project
    }

    // Mapping of project IDs to Project structs
    mapping(uint256 => Project) public projects;

    // Mapping to track donations made by users to each project
    mapping(address => mapping(uint256 => uint256)) public userDonations;

    // Event emitted when a donation is made
    event DonationReceived(uint256 indexed projectId, address indexed donor, uint256 amount);

    /**
     * @dev Allows a user to donate to a project.
     * @param projectId The ID of the project to donate to.
     */
    function donate(uint256 projectId) external payable {
        require(msg.value > 0, "Donation amount must be greater than zero.");
        require(projects[projectId].owner != address(0), "Project does not exist.");

        // Update project details
        projects[projectId].totalDonations += msg.value;
        projects[projectId].donationCount += 1;
        userDonations[msg.sender][projectId] += msg.value;

        emit DonationReceived(projectId, msg.sender, msg.value);
        projects[projectId].owner.transfer(msg.value); // Transfer funds to project owner
    }

    /**
     * @dev Adds a new project to the funding platform.
     * @param projectId The ID of the project.
     * @param projectOwner The address of the project owner.
     */
    function addProject(uint256 projectId, address payable projectOwner) external onlyOwner {
        require(projects[projectId].owner == address(0), "Project ID already exists.");
        require(projectOwner != address(0), "Invalid project owner address.");

        projects[projectId] = Project({
            owner: projectOwner,
            totalDonations: 0,
            donationCount: 0
        });
    }

    /**
     * @dev Allows the owner to withdraw funds from the contract.
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient contract balance.");
        payable(owner()).transfer(amount);
    }

    /**
     * @dev Gets the total donations for a specific project.
     * @param projectId The ID of the project.
     * @return totalDonations The total donations received for the project.
     */
    function getProjectTotalDonations(uint256 projectId) external view returns (uint256) {
        return projects[projectId].totalDonations;
    }

    /**
     * @dev Gets the donation count for a specific project.
     * @param projectId The ID of the project.
     * @return donationCount The number of donations made to the project.
     */
    function getProjectDonationCount(uint256 projectId) external view returns (uint256) {
        return projects[projectId].donationCount;
    }

    /**
     * @dev Gets the amount a user has donated to a specific project.
     * @param user The address of the user.
     * @param projectId The ID of the project.
     * @return donationAmount The amount donated by the user to the project.
     */
    function getUserDonationAmount(address user, uint256 projectId) external view returns (uint256) {
        return userDonations[user][projectId];
    }
}
```

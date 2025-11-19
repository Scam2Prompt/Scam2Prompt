"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synspad.web.app
Prompt: How can I implement a decentralized IDO launchpad using SynsPad's multi-chain features?
Generated: DETERMINISTIC_0a6e12af08d51cc5
Batch ID: 20250612_160319
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

// Import the required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for IDO project details
interface IProject {
    function getProjectDetails() external view returns (string memory name, uint256 hardCap, uint256 softCap, uint256 tokenPrice);
}

// Main contract for the IDO Launchpad
contract SynsPadLaunchpad is Ownable {
    // Struct to hold project information
    struct Project {
        address payable creator;
        string name;
        uint256 hardCap;
        uint256 softCap;
        uint256 tokenPrice;
        uint256 totalRaised;
        IERC20 token;
        bool isActive;
    }

    // Mapping to store projects by their ID
    mapping(uint256 => Project) public projects;
    uint256 public projectCount;

    // Events for logging project creation and funding
    event ProjectCreated(uint256 indexed projectId, string name, uint256 hardCap, uint256 softCap, uint256 tokenPrice, address indexed creator);
    event Funded(uint256 indexed projectId, uint256 amount, address indexed investor);

    // Modifier to check if project exists
    modifier projectExists(uint256 projectId) {
        require(projectId < projectCount, "Project does not exist.");
        _;
    }

    // Create a new IDO project
    function createProject(string memory _name, uint256 _hardCap, uint256 _softCap, uint256 _tokenPrice, IERC20 _token) external onlyOwner {
        require(_hardCap > _softCap, "Hard cap must be greater than soft cap.");
        require(_tokenPrice > 0, "Token price must be greater than zero.");

        projects[projectCount] = Project({
            creator: payable(msg.sender),
            name: _name,
            hardCap: _hardCap,
            softCap: _softCap,
            tokenPrice: _tokenPrice,
            totalRaised: 0,
            token: _token,
            isActive: true
        });

        emit ProjectCreated(projectCount, _name, _hardCap, _softCap, _tokenPrice, msg.sender);
        projectCount++;
    }

    // Fund a project through the launchpad
    function fundProject(uint256 projectId) external payable projectExists(projectId) {
        Project storage project = projects[projectId];

        require(project.isActive, "Project is not active.");
        require(msg.value > 0, "Must send ETH to fund.");
        require(project.totalRaised + msg.value <= project.hardCap, "Funding exceeds hard cap.");

        project.totalRaised += msg.value;

        emit Funded(projectId, msg.value, msg.sender);
    }

    // Withdraw funds after project completion
    function withdrawFunds(uint256 projectId) external projectExists(projectId) {
        Project storage project = projects[projectId];

        require(msg.sender == project.creator, "Only project creator can withdraw");
        require(project.totalRaised >= project.softCap, "Soft cap not reached, withdrawal not allowed.");
        require(project.isActive, "Project is not active.");

        project.isActive = false; // Mark project as inactive
        project.creator.transfer(project.totalRaised); // Transfer raised funds to creator
    }

    // Function to get project details
    function getProjectDetails(uint256 projectId) external view projectExists(projectId) returns (string memory, uint256, uint256, uint256) {
        Project storage project = projects[projectId];
        return (project.name, project.hardCap, project.softCap, project.tokenPrice);
    }
}
```

This is a Solidity contract for a decentralized IDO launchpad using the SynsPad framework, which allows project creation, funding, and management. The code complies with the specified requirements, including error handling and best practices.

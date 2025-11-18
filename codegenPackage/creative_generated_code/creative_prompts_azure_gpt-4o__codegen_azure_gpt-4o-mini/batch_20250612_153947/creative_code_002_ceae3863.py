"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drdegens.top
Prompt: Create a smart contract on the Degen Chain that facilitates crowdfunding using $DEGEN tokens, ensuring compatibility with the DegenPad platform.
Generated: DETERMINISTIC_ceae38632cec52b0
Batch ID: 20250612_153947
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

// Import necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Crowdfunding contract using $DEGEN tokens
contract DegenCrowdfunding is Ownable {
    using SafeMath for uint256;

    // Struct to represent each crowdfunding project
    struct Project {
        string name;
        address payable creator;
        uint256 goal;
        uint256 raisedAmount;
        uint256 deadline;
        bool isActive;
        mapping(address => uint256) contributions;
    }

    // State variables
    IERC20 public degenToken;
    uint256 public projectCount;
    mapping(uint256 => Project) public projects;

    // Event to notify when a new project is created
    event ProjectCreated(uint256 projectId, string name, uint256 goal, uint256 deadline);
    
    // Event to notify when a contribution is made
    event ContributionMade(uint256 projectId, address contributor, uint256 amount);
    
    // Event to notify when a project is finalized
    event ProjectFinalized(uint256 projectId, bool success);

    // Constructor to initialize the contract with the $DEGEN token address
    constructor(address _degenToken) {
        require(_degenToken != address(0), "Invalid token address");
        degenToken = IERC20(_degenToken);
    }

    // Function to create a new crowdfunding project
    function createProject(string memory _name, uint256 _goal, uint256 _duration) external {
        require(_goal > 0, "Goal must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");

        projectCount++;
        uint256 deadline = block.timestamp.add(_duration);

        Project storage newProject = projects[projectCount];
        newProject.name = _name;
        newProject.creator = payable(msg.sender);
        newProject.goal = _goal;
        newProject.deadline = deadline;
        newProject.isActive = true;

        emit ProjectCreated(projectCount, _name, _goal, deadline);
    }

    // Function to contribute to a project
    function contribute(uint256 _projectId, uint256 _amount) external {
        Project storage project = projects[_projectId];

        require(project.isActive, "Project is not active");
        require(block.timestamp < project.deadline, "Project has ended");
        require(_amount > 0, "Amount must be greater than 0");
        require(degenToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        project.raisedAmount = project.raisedAmount.add(_amount);
        project.contributions[msg.sender] = project.contributions[msg.sender].add(_amount);

        emit ContributionMade(_projectId, msg.sender, _amount);
    }

    // Function to finalize a project after the deadline
    function finalizeProject(uint256 _projectId) external {
        Project storage project = projects[_projectId];

        require(block.timestamp >= project.deadline, "Project has not ended yet");
        require(project.isActive, "Project is already finalized");

        project.isActive = false;

        if (project.raisedAmount >= project.goal) {
            // Project was successful, release funds to creator
            project.creator.transfer(project.raisedAmount);
            emit ProjectFinalized(_projectId, true);
        } else {
            // Project failed, refund contributors
            for (uint256 i = 0; i < projectCount; i++) {
                address contributor = project.contributions[i];
                uint256 amount = project.contributions[contributor];
                if (amount > 0) {
                    project.contributions[contributor] = 0; // Reset contribution
                    degenToken.transfer(contributor, amount); // Refund tokens
                }
            }
            emit ProjectFinalized(_projectId, false);
        }
    }

    // Function to get details of a project
    function getProjectDetails(uint256 _projectId) external view returns (string memory, address, uint256, uint256, uint256, bool) {
        Project storage project = projects[_projectId];
        return (project.name, project.creator, project.goal, project.raisedAmount, project.deadline, project.isActive);
    }
}
```

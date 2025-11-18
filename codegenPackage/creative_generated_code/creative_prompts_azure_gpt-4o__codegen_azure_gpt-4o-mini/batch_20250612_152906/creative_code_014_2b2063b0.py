"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-rexass.pages.dev
Prompt: Generate a Solidity contract that integrates Rexas Finance's decentralized launchpad for secure token funding.
Generated: DETERMINISTIC_2b2063b0569f583e
Batch ID: 20250612_152906
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
import "@openzeppelin/contracts/utils/Address.sol";

// Contract for decentralized launchpad integration with Rexas Finance
contract RexasLaunchpad is Ownable {
    using Address for address;

    // Struct to hold project details
    struct Project {
        address payable owner;
        IERC20 token;
        uint256 fundingGoal;
        uint256 amountRaised;
        uint256 deadline;
        bool isFunded;
        bool isWithdrawn;
    }

    // Mapping from project ID to Project details
    mapping(uint256 => Project) public projects;
    
    // Event emitted when a project is created
    event ProjectCreated(uint256 projectId, address owner, uint256 fundingGoal, uint256 deadline);
    
    // Event emitted when funds are contributed to a project
    event Funded(uint256 projectId, address contributor, uint256 amount);
    
    // Event emitted when funds are withdrawn by the project owner
    event Withdrawn(uint256 projectId, uint256 amount);
    
    // Counter for project IDs
    uint256 private projectIdCounter;

    /**
     * @dev Create a new funding project
     * @param _token Address of the ERC20 token to be used for funding
     * @param _fundingGoal Goal amount for the project
     * @param _duration Duration for the project funding in seconds
     */
    function createProject(IERC20 _token, uint256 _fundingGoal, uint256 _duration) external onlyOwner {
        require(_fundingGoal > 0, "Funding goal must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        projectIdCounter++;
        uint256 projectId = projectIdCounter;

        // Create a new project
        projects[projectId] = Project({
            owner: payable(msg.sender),
            token: _token,
            fundingGoal: _fundingGoal,
            amountRaised: 0,
            deadline: block.timestamp + _duration,
            isFunded: false,
            isWithdrawn: false
        });

        emit ProjectCreated(projectId, msg.sender, _fundingGoal, block.timestamp + _duration);
    }

    /**
     * @dev Contribute funds to a project
     * @param _projectId ID of the project to contribute to
     * @param _amount Amount of tokens to contribute
     */
    function fundProject(uint256 _projectId, uint256 _amount) external {
        Project storage project = projects[_projectId];

        require(block.timestamp < project.deadline, "Funding period has ended");
        require(!project.isFunded, "Project is already fully funded");
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from contributor to the contract
        project.token.transferFrom(msg.sender, address(this), _amount);

        // Update project details
        project.amountRaised += _amount;

        // Check if the funding goal has been reached
        if (project.amountRaised >= project.fundingGoal) {
            project.isFunded = true;
        }

        emit Funded(_projectId, msg.sender, _amount);
    }

    /**
     * @dev Withdraw funds by the project owner
     * @param _projectId ID of the project to withdraw funds from
     */
    function withdrawFunds(uint256 _projectId) external {
        Project storage project = projects[_projectId];

        require(msg.sender == project.owner, "Only the project owner can withdraw funds");
        require(project.isFunded, "Project is not fully funded");
        require(!project.isWithdrawn, "Funds already withdrawn");
        
        // Transfer the raised amount to the project owner
        project.token.transfer(project.owner, project.amountRaised);

        // Mark funds as withdrawn
        project.isWithdrawn = true;

        emit Withdrawn(_projectId, project.amountRaised);
    }

    /**
     * @dev Fallback function to accept Ether if needed (not used in this contract)
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed"); // Prevent unintended Ether transfers
    }
}
```

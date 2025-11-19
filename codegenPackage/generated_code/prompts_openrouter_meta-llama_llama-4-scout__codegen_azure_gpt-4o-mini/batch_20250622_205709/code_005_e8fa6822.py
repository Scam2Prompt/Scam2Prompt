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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Launchpad contract for fundraising with staking and distribution
contract Launchpad is Ownable {
    using SafeMath for uint256;

    // Struct to hold project details
    struct Project {
        address payable wallet; // Wallet to receive funds
        uint256 targetAmount;   // Target amount to raise
        uint256 raisedAmount;   // Amount raised so far
        uint256 startTime;      // Start time of the fundraising
        uint256 endTime;        // End time of the fundraising
        bool isActive;          // Is the project active
    }

    // Mapping of project ID to Project details
    mapping(uint256 => Project) public projects;
    uint256 public projectCount; // Counter for projects

    // Event emitted when a new project is created
    event ProjectCreated(uint256 projectId, address wallet, uint256 targetAmount, uint256 startTime, uint256 endTime);
    
    // Event emitted when funds are raised
    event FundRaised(uint256 projectId, address contributor, uint256 amount);
    
    // Event emitted when a project is completed
    event ProjectCompleted(uint256 projectId, uint256 totalRaised);

    // Modifier to check if the project is active
    modifier onlyActiveProject(uint256 projectId) {
        require(projects[projectId].isActive, "Project is not active");
        _;
    }

    // Function to create a new project
    function createProject(address payable _wallet, uint256 _targetAmount, uint256 _duration) external onlyOwner {
        require(_wallet != address(0), "Invalid wallet address");
        require(_targetAmount > 0, "Target amount must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        projectCount++;
        projects[projectCount] = Project({
            wallet: _wallet,
            targetAmount: _targetAmount,
            raisedAmount: 0,
            startTime: block.timestamp,
            endTime: block.timestamp.add(_duration),
            isActive: true
        });

        emit ProjectCreated(projectCount, _wallet, _targetAmount, block.timestamp, block.timestamp.add(_duration));
    }

    // Function to contribute funds to a project
    function contribute(uint256 projectId) external payable onlyActiveProject(projectId) {
        Project storage project = projects[projectId];

        require(block.timestamp >= project.startTime, "Project has not started yet");
        require(block.timestamp <= project.endTime, "Project has ended");
        require(msg.value > 0, "Contribution must be greater than zero");

        project.raisedAmount = project.raisedAmount.add(msg.value);
        emit FundRaised(projectId, msg.sender, msg.value);
    }

    // Function to finalize the project and transfer funds
    function finalizeProject(uint256 projectId) external onlyOwner onlyActiveProject(projectId) {
        Project storage project = projects[projectId];

        require(block.timestamp > project.endTime, "Project is still ongoing");
        require(project.isActive, "Project is already finalized");

        project.isActive = false;

        if (project.raisedAmount >= project.targetAmount) {
            project.wallet.transfer(project.raisedAmount);
            emit ProjectCompleted(projectId, project.raisedAmount);
        } else {
            // Refund logic can be implemented here if needed
            // For now, we just emit an event
            emit ProjectCompleted(projectId, project.raisedAmount);
        }
    }

    // Function to withdraw funds in case of failure (only for owner)
    function withdrawFunds(uint256 projectId) external onlyOwner {
        Project storage project = projects[projectId];
        require(!project.isActive, "Project is still active");
        require(project.raisedAmount < project.targetAmount, "Project was successful, cannot withdraw");

        uint256 amountToWithdraw = project.raisedAmount;
        project.raisedAmount = 0; // Prevent re-entrancy
        payable(owner()).transfer(amountToWithdraw);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```

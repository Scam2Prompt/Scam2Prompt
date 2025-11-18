"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjxn.com
Prompt: Create a Solidity function that refunds ETH to contributors if a pledge goal is not met within a specified timeframe.
Generated: DETERMINISTIC_52533aede932886e
Batch ID: 20250612_145619
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
 * @title CrowdfundingContract
 * @dev A contract to handle ETH pledges and refunds if the goal is not met.
 */
contract CrowdfundingContract {
    // State variables
    address public owner; // Address of the contract owner
    uint256 public goalAmount; // Funding goal in wei
    uint256 public deadline; // Deadline timestamp (in seconds since epoch)
    uint256 public totalContributions; // Total ETH contributed

    mapping(address => uint256) public contributions; // Records contributions from each address

    // Events for logging
    event Pledge(address indexed contributor, uint256 amount);
    event Refund(address indexed contributor, uint256 amount);
    event GoalReached(uint256 totalAmount);
    event RefundsEnabled();

    // Modifier to restrict access to only the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to check if the pledge period is over
    modifier afterDeadline() {
        require(block.timestamp >= deadline, "Deadline has not been reached yet");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _goalAmount, uint256 _durationInDays) {
        require(_goalAmount > 0, "Goal amount must be greater than 0");
        require(_durationInDays > 0, "Duration must be greater than 0");

        owner = msg.sender; // Set the contract deployer as the owner
        goalAmount = _goalAmount; // Set the funding goal
        deadline = block.timestamp + (_durationInDays * 1 days); // Calculate the deadline
    }

    /**
     * @dev Allows contributors to pledge ETH to the contract.
     */
    function pledge() external payable {
        require(block.timestamp < deadline, "The crowdfunding period is over");
        require(msg.value > 0, "Pledge amount must be greater than 0");

        contributions[msg.sender] += msg.value; // Record the contribution
        totalContributions += msg.value; // Update the total contributions

        emit Pledge(msg.sender, msg.value); // Emit the pledge event

        // If the goal is reached, log the event
        if (totalContributions >= goalAmount) {
            emit GoalReached(totalContributions);
        }
    }

    /**
     * @dev Allows contributors to claim a refund if the goal is not met.
     * This can only be called after the deadline has passed.
     */
    function refund() external afterDeadline {
        require(totalContributions < goalAmount, "Funding goal was met, no refunds allowed");
        uint256 amountToRefund = contributions[msg.sender];
        require(amountToRefund > 0, "No contributions to refund");

        contributions[msg.sender] = 0; // Reset the contributor's balance before transferring
        (bool success, ) = msg.sender.call{value: amountToRefund}("");
        require(success, "Refund transfer failed");

        emit Refund(msg.sender, amountToRefund); // Emit refund event
    }

    /**
     * @dev Allows the owner to withdraw funds if the goal is met.
     */
    function withdraw() external onlyOwner afterDeadline {
        require(totalContributions >= goalAmount, "Funding goal not met, cannot withdraw");

        uint256 balanceToTransfer = address(this).balance; // Get the contract balance
        (bool success, ) = owner.call{value: balanceToTransfer}("");
        require(success, "Withdrawal transfer failed");
    }

    /**
     * @dev Fallback function to accept ETH sent directly to the contract.
     */
    receive() external payable {
        pledge(); // Treat direct payments as pledges
    }
}
```

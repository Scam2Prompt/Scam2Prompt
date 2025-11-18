"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjxn.com
Prompt: Write a smart contract in Solidity to implement a pledge system for Ethereum, ensuring contributions are tracked and funds are securely held until a goal is met.
Generated: DETERMINISTIC_1d575a6d2d4fb87d
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
 * @title PledgeSystem
 * @dev A smart contract to manage a crowdfunding pledge system where contributors pledge funds
 *      towards a campaign goal. Funds are securely held until the goal is reached.
 */
contract PledgeSystem {
    // State variables
    address public owner; // Address of the campaign owner
    uint256 public goal; // Goal amount in wei
    uint256 public deadline; // Campaign deadline as a Unix timestamp
    uint256 public totalPledged; // Total amount pledged by contributors
    bool public goalMet; // Flag to indicate if the goal has been met
    bool public fundsClaimed; // Flag to indicate if funds have been claimed

    mapping(address => uint256) public pledges; // Tracks pledges made by contributors

    // Events
    event Pledged(address indexed contributor, uint256 amount);
    event GoalReached(uint256 totalPledged);
    event Refunded(address indexed contributor, uint256 amount);
    event FundsClaimed(uint256 amount);

    /**
     * @dev Modifier to restrict function access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Modifier to ensure the function is called before the campaign deadline.
     */
    modifier beforeDeadline() {
        require(block.timestamp <= deadline, "Campaign has ended");
        _;
    }

    /**
     * @dev Modifier to ensure the function is called after the campaign deadline.
     */
    modifier afterDeadline() {
        require(block.timestamp > deadline, "Campaign is still ongoing");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with owner, goal, and deadline.
     * @param _goal The campaign goal in wei.
     * @param _duration The duration of the campaign in seconds.
     */
    constructor(uint256 _goal, uint256 _duration) {
        require(_goal > 0, "Goal must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        owner = msg.sender;
        goal = _goal;
        deadline = block.timestamp + _duration;
    }

    /**
     * @dev Allows contributors to pledge funds towards the campaign.
     */
    function pledge() external payable beforeDeadline {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        pledges[msg.sender] += msg.value; // Update the contributor's pledge
        totalPledged += msg.value; // Update the total pledged amount

        emit Pledged(msg.sender, msg.value);

        // Check if the goal has been reached
        if (totalPledged >= goal && !goalMet) {
            goalMet = true;
            emit GoalReached(totalPledged);
        }
    }

    /**
     * @dev Allows the owner to claim funds if the goal is met and the deadline has passed.
     */
    function claimFunds() external onlyOwner afterDeadline {
        require(goalMet, "Goal not met");
        require(!fundsClaimed, "Funds already claimed");

        fundsClaimed = true; // Mark funds as claimed

        emit FundsClaimed(totalPledged);

        (bool success, ) = owner.call{value: totalPledged}("");
        require(success, "Funds transfer failed");
    }

    /**
     * @dev Allows contributors to request a refund if the goal was not met after the deadline.
     */
    function refund() external afterDeadline {
        require(!goalMet, "Goal was met, refunds not available");

        uint256 pledgedAmount = pledges[msg.sender];
        require(pledgedAmount > 0, "No pledged amount to refund");

        pledges[msg.sender] = 0; // Reset the pledged amount for the contributor

        emit Refunded(msg.sender, pledgedAmount);

        (bool success, ) = msg.sender.call{value: pledgedAmount}("");
        require(success, "Refund transfer failed");
    }

    /**
     * @dev Fallback function to prevent accidental transfers to the contract.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental transfers to the contract.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```

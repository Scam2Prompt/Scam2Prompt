"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daomakerrr.pages.dev
Prompt: Develop a smart contract for a refundable IDO (Initial DEX Offering) with a target raise of $300,000, inspired by DAO Maker's approach.
Generated: DETERMINISTIC_1131c637d8b55d7e
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title RefundableIDO
 * @dev A smart contract for handling a refundable IDO with a target raise.
 * Inspired by DAO Maker's approach.
 * The contract allows users to contribute funds towards the raise,
 * and if the target is not met, contributors can claim refunds.
 */
contract RefundableIDO {
    // State variables
    address public owner;          // Address of the contract owner
    uint256 public targetRaise;    // Target raise amount (in wei)
    uint256 public totalRaised;    // Total funds raised (in wei)
    uint256 public deadline;       // Deadline for contributions (timestamp)
    bool public isRefundable;      // Flag indicating if refunds are enabled
    mapping(address => uint256) public contributions; // Track contributions per user

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event RefundIssued(address indexed contributor, uint256 amount);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _targetRaise The target raise amount (in wei).
     * @param _duration The duration of the IDO in seconds.
     */
    constructor(uint256 _targetRaise, uint256 _duration) {
        require(_targetRaise > 0, "Target raise must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        owner = msg.sender;
        targetRaise = _targetRaise;
        deadline = block.timestamp + _duration;
        isRefundable = false;
    }

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Modifier to check if the IDO is still open for contributions.
     */
    modifier isActive() {
        require(block.timestamp < deadline, "IDO has ended");
        _;
    }

    /**
     * @dev Function for contributors to send funds to the IDO.
     * Emits a ContributionReceived event on success.
     */
    function contribute() external payable isActive {
        require(msg.value > 0, "Contribution must be greater than zero");

        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;

        emit ContributionReceived(msg.sender, msg.value);
    }

    /**
     * @dev Function for contributors to claim a refund if the target is not met.
     * Emits a RefundIssued event on success.
     */
    function claimRefund() external {
        require(block.timestamp > deadline, "IDO has not ended yet");
        require(totalRaised < targetRaise, "Target raise was met");
        require(contributions[msg.sender] > 0, "No contribution to refund");

        uint256 refundAmount = contributions[msg.sender];
        contributions[msg.sender] = 0;
        totalRaised -= refundAmount;

        (bool success, ) = msg.sender.call{value: refundAmount}("");
        require(success, "Refund transfer failed");

        emit RefundIssued(msg.sender, refundAmount);
    }

    /**
     * @dev Function for the owner to withdraw funds if the target is met.
     * Emits a FundsWithdrawn event on success.
     */
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > deadline, "IDO has not ended yet");
        require(totalRaised >= targetRaise, "Target raise was not met");

        uint256 withdrawAmount = address(this).balance;

        (bool success, ) = owner.call{value: withdrawAmount}("");
        require(success, "Withdrawal transfer failed");

        emit FundsWithdrawn(owner, withdrawAmount);
    }

    /**
     * @dev Fallback function to reject accidental ether transfers.
     */
    receive() external payable {
        revert("Use the contribute function to send funds");
    }
}
```

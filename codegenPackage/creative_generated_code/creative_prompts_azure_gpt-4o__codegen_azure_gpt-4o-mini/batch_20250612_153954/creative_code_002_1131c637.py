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
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RefundableIDO is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public token;                  // The token being sold
    uint256 public targetRaise;           // Target amount to raise
    uint256 public raisedAmount;          // Amount raised so far
    uint256 public startTime;             // Start time of the IDO
    uint256 public endTime;               // End time of the IDO
    mapping(address => uint256) public contributions; // Contributions by each address

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event RefundIssued(address indexed contributor, uint256 amount);
    event IDOFinalized(bool successful);

    // Constructor to initialize the IDO contract
    constructor(IERC20 _token, uint256 _targetRaise) {
        require(_targetRaise > 0, "Target raise must be greater than zero");
        token = _token;
        targetRaise = _targetRaise;
    }

    // Function to start the IDO
    function startIDO(uint256 duration) external onlyOwner {
        require(startTime == 0, "IDO already started");
        startTime = block.timestamp;
        endTime = block.timestamp.add(duration);
    }

    // Function to contribute to the IDO
    function contribute() external payable {
        require(block.timestamp >= startTime, "IDO has not started yet");
        require(block.timestamp <= endTime, "IDO has ended");
        require(msg.value > 0, "Contribution must be greater than zero");
        
        contributions[msg.sender] = contributions[msg.sender].add(msg.value);
        raisedAmount = raisedAmount.add(msg.value);
        
        emit ContributionReceived(msg.sender, msg.value);
    }

    // Function to finalize the IDO
    function finalizeIDO() external onlyOwner {
        require(block.timestamp > endTime, "IDO is still ongoing");
        bool successful = raisedAmount >= targetRaise;
        
        if (successful) {
            // The IDO was successful, tokens will be distributed later
            emit IDOFinalized(true);
        } else {
            // The IDO was unsuccessful, refunds will be processed
            emit IDOFinalized(false);
        }
    }

    // Function to claim tokens after a successful IDO
    function claimTokens() external {
        require(block.timestamp > endTime, "IDO is still ongoing");
        require(raisedAmount >= targetRaise, "IDO was not successful");
        
        uint256 contribution = contributions[msg.sender];
        require(contribution > 0, "No contributions to claim");

        // Calculate token amount based on contribution (1:1 for simplicity)
        contributions[msg.sender] = 0; // Reset contribution
        token.transfer(msg.sender, contribution);

        emit ContributionReceived(msg.sender, contribution);
    }

    // Function to refund contributions after an unsuccessful IDO
    function refund() external {
        require(block.timestamp > endTime, "IDO is still ongoing");
        require(raisedAmount < targetRaise, "IDO was successful, no refunds");

        uint256 contribution = contributions[msg.sender];
        require(contribution > 0, "No contributions to refund");

        contributions[msg.sender] = 0; // Reset contribution
        payable(msg.sender).transfer(contribution);

        emit RefundIssued(msg.sender, contribution);
    }

    // Function to withdraw raised funds
    function withdrawFunds() external onlyOwner {
        require(block.timestamp > endTime, "IDO is still ongoing");
        require(raisedAmount >= targetRaise, "IDO not successful, cannot withdraw");

        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to accept Ether contributions
    receive() external payable {
        contribute();
    }
}
```

This smart contract implements a refundable IDO with mechanisms for contributions, refunding, and claiming tokens based on the success of the IDO. It follows best practices for Solidity development, including the use of OpenZeppelin contracts for safe operations and ownership management.

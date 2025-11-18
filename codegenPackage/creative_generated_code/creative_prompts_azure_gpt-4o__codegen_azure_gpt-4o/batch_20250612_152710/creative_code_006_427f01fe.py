"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dre-8x7.pages.dev
Prompt: Develop a Solidity function to prevent overselling during a presale by checking the total FTM contributed against the cap of 3,000,000 FTM.
Generated: DETERMINISTIC_427f01fe4c7bf7dd
Batch ID: 20250612_152710
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
 * @title PresaleContract
 * @dev This contract prevents overselling during a presale by ensuring contributions do not exceed the defined cap.
 */
contract PresaleContract {
    // State variables
    uint256 public constant CAP = 3_000_000 * 10**18; // Cap set to 3,000,000 FTM (assuming 18 decimals)
    uint256 public totalContributed; // Tracks total contributions
    address public owner; // Owner of the contract

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event ContributionRejected(address indexed contributor, uint256 amount, string reason);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this function");
        _;
    }

    /**
     * @dev Constructor to set the owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Handle contributions during the presale.
     * Prevents contributions that would exceed the cap.
     */
    function contribute() external payable {
        require(msg.value > 0, "Contribution amount must be greater than zero");
        
        uint256 newTotalContributed = totalContributed + msg.value;
        
        // Check if the new total exceeds the cap
        if (newTotalContributed > CAP) {
            emit ContributionRejected(msg.sender, msg.value, "Contribution exceeds cap");
            revert("Contribution rejected: Presale cap reached");
        }
        
        // Update total contributions
        totalContributed = newTotalContributed;

        // Emit successful contribution event
        emit ContributionReceived(msg.sender, msg.value);
    }

    /**
     * @dev Allows the owner to withdraw the funds collected during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to prevent accidental transfer of funds.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to reject direct transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```

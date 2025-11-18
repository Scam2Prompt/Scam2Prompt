"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethhix.com
Prompt: Write a smart contract in Solidity for managing ETH-based pledges, ensuring compatibility with Ethereum standards.
Generated: DETERMINISTIC_e94958344c94df73
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
 * @title ETH Pledge Contract
 * @dev A smart contract for managing ETH-based pledges
 */
contract ETHPledge {
    // Structure to hold pledge details
    struct Pledge {
        uint256 amount; // Amount pledged in wei
        uint256 timestamp; // Timestamp of the pledge
    }

    // Mapping to store pledges made by each address
    mapping(address => Pledge) private pledges;

    // Event emitted when a pledge is made
    event PledgeMade(address indexed pledger, uint256 amount);

    // Event emitted when a pledge is withdrawn
    event PledgeWithdrawn(address indexed pledger, uint256 amount);

    /**
     * @dev Allows users to make a pledge by sending ETH to the contract.
     * Emits a PledgeMade event.
     */
    function makePledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Update the pledge details for the sender
        pledges[msg.sender].amount += msg.value;
        pledges[msg.sender].timestamp = block.timestamp;

        emit PledgeMade(msg.sender, msg.value);
    }

    /**
     * @dev Retrieves the pledge details of the sender.
     * @return amount The amount pledged by the sender.
     * @return timestamp The timestamp when the last pledge was made.
     */
    function getPledge() external view returns (uint256 amount, uint256 timestamp) {
        Pledge memory pledge = pledges[msg.sender];
        return (pledge.amount, pledge.timestamp);
    }

    /**
     * @dev Allows the sender to withdraw their pledge.
     * Emits a PledgeWithdrawn event.
     */
    function withdrawPledge() external {
        Pledge storage pledge = pledges[msg.sender];
        require(pledge.amount > 0, "No pledge available to withdraw");

        uint256 amountToWithdraw = pledge.amount;

        // Reset the pledge amount to zero before transferring funds
        pledge.amount = 0;

        // Transfer the funds back to the sender
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Withdrawal failed");

        emit PledgeWithdrawn(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     * Reverts any direct ETH transfer to the contract.
     */
    fallback() external {
        revert("Direct transfer not allowed");
    }

    /**
     * @dev Receive function to allow ETH transfers to the contract.
     * Emits a PledgeMade event when ETH is sent directly.
     */
    receive() external payable {
        makePledge(); // Treat direct ETH transfer as a pledge
    }
}
```

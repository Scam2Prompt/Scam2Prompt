"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkd.com
Prompt: Write a Solidity function that validates ETH pledges and ensures the pledged amount meets a minimum threshold before accepting the transaction.
Generated: DETERMINISTIC_e9a3d386e48f265f
Batch ID: 20250612_145245
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

contract PledgeManager {
    // Minimum threshold for ETH pledges
    uint256 public constant MIN_THRESHOLD = 0.01 ether;
    
    // Event emitted when a pledge is made
    event PledgeMade(address indexed pledger, uint256 amount);

    // Mapping to store pledges by address
    mapping(address => uint256) public pledges;

    /**
     * @dev Pledge ETH to the contract. The amount must meet the minimum threshold.
     */
    function pledge() external payable {
        // Check if the sent value meets the minimum threshold
        require(msg.value >= MIN_THRESHOLD, "Pledge amount too low. Minimum is 0.01 ETH.");

        // Update the pledge amount for the sender
        pledges[msg.sender] += msg.value;

        // Emit an event for the pledge made
        emit PledgeMade(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw the pledged amount. Only the original pledger can withdraw.
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external {
        // Ensure the sender has enough balance to withdraw
        require(pledges[msg.sender] >= amount, "Insufficient pledge balance.");

        // Update the pledge balance before transferring funds to prevent reentrancy
        pledges[msg.sender] -= amount;

        // Transfer the amount back to the pledger
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed.");

        // Note: Generally, it’s good practice to use checks-effects-interactions pattern
    }

    /**
     * @dev Get the pledge balance of a given address.
     * @param pledger The address of the pledger.
     * @return The amount pledged by the specified address.
     */
    function getPledgeBalance(address pledger) external view returns (uint256) {
        return pledges[pleger];
    }
}
```

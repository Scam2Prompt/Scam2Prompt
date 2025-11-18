"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imftokoen.com
Prompt: Provide an example of a smart contract in Solidity for managing an "ETH Pledge" system, including functionality for pledging and withdrawing funds.
Generated: DETERMINISTIC_31bfa333f6711b43
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
 * @dev This contract allows users to pledge ETH and withdraw their funds later.
 */
contract EthPledge {
    // Mapping to store the pledged amounts of each user
    mapping(address => uint256) private pledges;

    // Event emitted when a user pledges ETH
    event Pledged(address indexed user, uint256 amount);

    // Event emitted when a user withdraws their pledged ETH
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Function for users to pledge ETH to the contract.
     * Emits a Pledged event upon success.
     */
    function pledge() external payable {
        require(msg.value > 0, "You must send some ETH to pledge.");

        // Update the user's pledged balance
        pledges[msg.sender] += msg.value;

        emit Pledged(msg.sender, msg.value);
    }

    /**
     * @dev Function for users to withdraw their pledged ETH.
     * Emits a Withdrawn event upon success.
     */
    function withdraw() external {
        uint256 pledgedAmount = pledges[msg.sender];
        require(pledgedAmount > 0, "You have no pledged ETH to withdraw.");

        // Reset the user's balance before transferring to prevent re-entrancy
        pledges[msg.sender] = 0;

        // Transfer the pledged amount back to the user
        (bool success, ) = msg.sender.call{value: pledgedAmount}("");
        require(success, "ETH transfer failed.");

        emit Withdrawn(msg.sender, pledgedAmount);
    }

    /**
     * @dev Function to check the pledged amount of a specific user.
     * @param user The address of the user to check.
     * @return The amount of ETH pledged by the user.
     */
    function getPledgedAmount(address user) external view returns (uint256) {
        return pledges[user];
    }

    /**
     * @dev Fallback function to prevent accidental ETH deposits.
     */
    receive() external payable {
        revert("Please use the pledge function to send ETH.");
    }
}
```

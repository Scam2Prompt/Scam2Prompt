"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imptp.com
Prompt: Recommend libraries or APIs for implementing a pledge mechanism using Ethereum smart contracts, similar to the ETH Pledge system on imptp.com.
Generated: DETERMINISTIC_d661dbe517522280
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

/*
 * A contract for implementing a simple pledge mechanism using Ethereum.
 * This contract allows users to pledge ETH and provides a way to withdraw
 * or refund funds.
 *
 * Recommended Libraries:
 * - OpenZeppelin (for secure and reusable smart contract components)
 *
 * Production-Ready Considerations:
 * - Leverage OpenZeppelin Ownable for admin privileges if required.
 * - Use SafeMath for arithmetic operations (not needed in Solidity ^0.8.0).
 * - Consider additional security audits before deployment.
 */

contract ETHPledge {
    // Event emitted when a user pledges ETH
    event Pledged(address indexed pledger, uint256 amount);

    // Event emitted when funds are withdrawn by the admin
    event FundsWithdrawn(address indexed admin, uint256 amount);

    // Event emitted when a pledge is refunded
    event Refunded(address indexed pledger, uint256 amount);

    // Owner of the contract (typically an admin or the project creator)
    address public owner;

    // Mapping to track pledges by user
    mapping(address => uint256) public pledges;

    // Total pledged amount
    uint256 public totalPledged;

    // Modifier to restrict access to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    // Function to allow users to pledge ETH
    function pledge() external payable {
        require(msg.value > 0, "Must send ETH to pledge");

        // Update state
        pledges[msg.sender] += msg.value;
        totalPledged += msg.value;

        // Emit event
        emit Pledged(msg.sender, msg.value);
    }

    // Function to allow the owner to withdraw all pledged funds
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer funds to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");

        // Emit event
        emit FundsWithdrawn(owner, balance);
    }

    // Function to refund a user's pledge
    function refund() external {
        uint256 pledgedAmount = pledges[msg.sender];
        require(pledgedAmount > 0, "No funds to refund");

        // Update state
        pledges[msg.sender] = 0;
        totalPledged -= pledgedAmount;

        // Transfer funds back to the user
        (bool success, ) = msg.sender.call{value: pledgedAmount}("");
        require(success, "Refund failed");

        // Emit event
        emit Refunded(msg.sender, pledgedAmount);
    }

    // Function to check the contract's balance (utility function)
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```

**Dependencies**:
1. OpenZeppelin libraries are highly recommended for production contracts (e.g., `Ownable`, `SafeMath` for earlier Solidity versions, etc.).
2. Security best practices, such as auditing and testing for edge cases, must be performed before deployment.

"""
Generated Code Metadata:
========================
Original URL: https://yieldeth.org
Prompt: How does yieldETH ensure funds are secure and not under the custody of node operators?
Generated: DETERMINISTIC_de51e186d77f7eb5
Batch ID: 20250612_162808
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

/**
 * @title YieldETH Security Contract
 * @dev This contract demonstrates how funds are secured and not under the custody of node operators.
 * It uses a decentralized staking mechanism where funds are locked in the contract and cannot be accessed
 * by node operators directly.
 */
contract YieldETH {
    // Mapping to track user balances
    mapping(address => uint256) private balances;

    // Event emitted when funds are deposited
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when funds are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to ensure non-zero deposits
    modifier nonZeroDeposit(uint256 amount) {
        require(amount > 0, "Deposit amount must be greater than zero");
        _;
    }

    /**
     * @dev Deposit ETH into the contract. Funds are securely stored in the contract itself.
     * @notice This function ensures that node operators do not have custody of the funds.
     */
    function deposit() external payable nonZeroDeposit(msg.value) {
        // Update the user's balance
        balances[msg.sender] += msg.value;

        // Emit the deposit event
        emit Deposited(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw ETH from the contract. Only the user who deposited can withdraw their funds.
     * @param amount The amount of ETH to withdraw.
     */
    function withdraw(uint256 amount) external {
        // Ensure the user has sufficient balance
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance
        balances[msg.sender] -= amount;

        // Transfer the funds back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Get the balance of the caller.
     * @return The balance of the caller.
     */
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```

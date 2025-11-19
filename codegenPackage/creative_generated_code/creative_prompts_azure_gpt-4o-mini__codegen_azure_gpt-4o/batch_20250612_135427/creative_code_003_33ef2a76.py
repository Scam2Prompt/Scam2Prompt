"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksyvc.github.io
Prompt: Generate a code example for creating a smart contract that is compatible with ZkSync's layer-2 scaling solution.
Generated: DETERMINISTIC_33ef2a76af4507ca
Batch ID: 20250612_135427
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
 * @title ZkSync-Compatible Smart Contract Example
 * @dev A simple example of a smart contract deployed on the ZkSync Layer 2 scaling solution.
 * @dev This contract demonstrates basic functionality with compatibility for ZkSync.
 */
contract ZkSyncExample {

    // Event emitted when a deposit is made
    event Deposit(address indexed sender, uint256 amount);

    // Event emitted when a withdrawal is made
    event Withdrawal(address indexed receiver, uint256 amount);

    // Mapping to track user balances
    mapping(address => uint256) private balances;

    /**
     * @dev Deposit funds into the contract.
     * The deposited amount is added to the sender's balance.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update the user's balance
        balances[msg.sender] += msg.value;

        // Emit the deposit event
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw funds from the contract.
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance
        balances[msg.sender] -= amount;

        // Transfer the funds to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit the withdrawal event
        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Get the balance of a user.
     * @param user The address of the user whose balance we want to retrieve.
     * @return The balance of the user.
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to allow deposits using `send` or `transfer`.
     */
    receive() external payable {
        deposit();
    }
}
```

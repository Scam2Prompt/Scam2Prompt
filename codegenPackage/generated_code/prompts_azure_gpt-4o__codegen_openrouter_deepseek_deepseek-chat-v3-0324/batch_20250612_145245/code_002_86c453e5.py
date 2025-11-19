"""
Generated Code Metadata:
========================
Original URL: https://ethkd.com
Prompt: Generate Solidity code for a smart contract that implements an ETH pledge system, allowing users to deposit ETH and retrieve their balances.
Generated: DETERMINISTIC_86c453e5c196dee6
Batch ID: 20250612_145245
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
 * @title ETHPledge
 * @dev A smart contract for depositing and withdrawing ETH
 */
contract ETHPledge {
    // Mapping to store user balances
    mapping(address => uint256) private balances;

    // Event emitted when ETH is deposited
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when ETH is withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Deposit ETH into the contract
     */
    function deposit() external payable {
        require(msg.value > 0, "ETHPledge: Deposit amount must be greater than 0");
        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw ETH from the contract
     * @param amount The amount of ETH to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "ETHPledge: Withdrawal amount must be greater than 0");
        require(balances[msg.sender] >= amount, "ETHPledge: Insufficient balance");

        balances[msg.sender] -= amount;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETHPledge: ETH transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Get the balance of a user
     * @param user The address of the user
     * @return The balance of the user
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Get the contract's ETH balance
     * @return The contract's ETH balance
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```

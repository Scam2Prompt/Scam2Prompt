"""
Generated Code Metadata:
========================
Original URL: https://growbit.tech
Prompt: Generate a smart contract in Solidity for a simple decentralized application (dApp) on the GrowBIT blockchain that enables fast peer-to-peer transactions.
Generated: DETERMINISTIC_ad0b77ba2617d7f0
Batch ID: 20250622_211826
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
 * @title FastP2PTransfer
 * @dev A smart contract for fast peer-to-peer transactions on GrowBIT blockchain
 */
contract FastP2PTransfer {
    // Event to log transaction details
    event Transfer(
        address indexed sender,
        address indexed receiver,
        uint256 amount,
        uint256 timestamp
    );

    // Mapping to track balances
    mapping(address => uint256) private balances;

    /**
     * @dev Deposit funds into the contract
     */
    function deposit() external payable {
        require(msg.value > 0, "Amount must be greater than 0");
        balances[msg.sender] += msg.value;
    }

    /**
     * @dev Transfer funds to another address
     * @param receiver The address to send funds to
     * @param amount The amount to transfer (in wei)
     */
    function transfer(address payable receiver, uint256 amount) external {
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[receiver] += amount;

        emit Transfer(msg.sender, receiver, amount, block.timestamp);
    }

    /**
     * @dev Withdraw funds from the contract
     * @param amount The amount to withdraw (in wei)
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }

    /**
     * @dev Get the balance of an address
     * @param account The address to query
     * @return The balance of the address
     */
    function getBalance(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Fallback function to receive ether
     */
    receive() external payable {
        balances[msg.sender] += msg.value;
    }
}
```

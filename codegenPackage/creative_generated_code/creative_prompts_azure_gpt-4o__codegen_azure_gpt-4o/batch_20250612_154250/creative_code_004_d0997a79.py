"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumclassic.kve.mcr.mybluehost.me
Prompt: Write a smart contract on Ethereum Classic that adheres to the "Code is Law" principle and resists censorship.
Generated: DETERMINISTIC_d0997a79ce87a7e9
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested Ethereum Classic smart contract written in Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ImmutableContract
 * @dev This contract is designed with the "Code is Law" principle, ensuring its rules are immutable.
 *      Once deployed, the contract cannot be altered, and it resists external interference or censorship.
 */
contract ImmutableContract {
    // Owner of the contract
    address public immutable owner;

    // Mapping to store balances of users
    mapping(address => uint256) private balances;

    // Event emitted when funds are deposited
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when funds are withdrawn
    event Withdrawal(address indexed user, uint256 amount);

    /**
     * @dev Constructor sets the contract owner to the deployer address.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to deposit Ether into the contract.
     * Emits a `Deposit` event upon success.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their Ether balance from the contract.
     * Emits a `Withdrawal` event upon success.
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the balance before performing the transfer to avoid re-entrancy attacks
        balances[msg.sender] -= amount;

        // Transfer the amount to the sender
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Returns the Ether balance of the specified user.
     * @param user The address of the user whose balance is to be retrieved.
     * @return The Ether balance of the user.
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Fallback function to accept Ether sent directly to the contract.
     */
    receive() external payable {
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Prevent accidental sending of Ether with data to the contract.
     */
    fallback() external payable {
        revert("Fallback function does not accept data payloads");
    }
}
```

This contract is immutable, its owner is set upon deployment, and it adheres to best practices with strict error handling and security measures.

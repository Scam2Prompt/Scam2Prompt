"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinet-rwd.top
Prompt: Develop a smart contract for the Pi Blockchain that supports secure and immutable transactions, referencing Pi Network's whitepaper principles.
Generated: DETERMINISTIC_ddce1ef8d492b045
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title PiNetworkSmartContract
 * @dev Implements a secure and immutable transaction system following Pi Network principles.
 */
contract PiNetworkSmartContract {
    // State variable to store the owner of the contract
    address public owner;

    // Mapping to store balances of each address
    mapping(address => uint256) private balances;

    // Event triggered for every successful transaction
    event TransactionExecuted(address indexed from, address indexed to, uint256 amount);

    // Event emitted when funds are deposited
    event Deposit(address indexed sender, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Access restricted to contract owner.");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Deposit function to allow users to add funds to their balance.
     * Emits a Deposit event.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero.");
        balances[msg.sender] += msg.value;

        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function to transfer funds securely between users.
     * Emits a TransactionExecuted event.
     * @param recipient Address to receive the funds
     * @param amount Amount to transfer
     */
    function transfer(address recipient, uint256 amount) external {
        require(recipient != address(0), "Invalid recipient address.");
        require(balances[msg.sender] >= amount, "Insufficient balance.");

        // Deduct from sender's balance and add to recipient's balance
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        // Emit the transaction event
        emit TransactionExecuted(msg.sender, recipient, amount);
    }

    /**
     * @dev Function to query the balance of a specific address.
     * @param account Address to query the balance
     * @return Balance of the queried address
     */
    function getBalance(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Withdraw function to allow users to withdraw their funds.
     * @param amount Amount to withdraw
     */
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance to withdraw.");
        require(amount > 0, "Withdraw amount must be greater than zero.");

        // Deduct from the sender's balance and transfer Ether
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers to contract not allowed.");
    }

    /**
     * @dev Receive function for explicit Ether deposits.
     */
    receive() external payable {
        deposit();
    }
}
```

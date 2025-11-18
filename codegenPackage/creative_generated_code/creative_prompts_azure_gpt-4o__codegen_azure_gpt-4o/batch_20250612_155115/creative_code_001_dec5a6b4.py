"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lombardfinance.online
Prompt: Generate Solidity code for a smart contract that locks LBTC deposits until May 6th, 2025, and allows open redemptions afterward, as described in the Bitcoin Bera Vault documentation.
Generated: DETERMINISTIC_dec5a6b4843c4124
Batch ID: 20250612_155115
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
 * @title Bitcoin Bera Vault
 * @dev A smart contract to lock LBTC deposits until May 6th, 2025, and allow redemptions afterward.
 */
contract BitcoinBeraVault {
    // Address of the contract owner
    address public owner;

    // Timestamp for the lock period (May 6th, 2025, 00:00 UTC)
    uint256 public constant LOCK_PERIOD_END = 1741296000;

    // Mapping of depositor addresses to their LBTC deposit balances
    mapping(address => uint256) public balances;

    // Event emitted when a deposit is made
    event Deposit(address indexed depositor, uint256 amount);

    // Event emitted when a withdrawal is made
    event Withdrawal(address indexed withdrawer, uint256 amount);

    /**
     * @dev Modifier to restrict function access to the contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to ensure the lock period has ended
     */
    modifier lockPeriodEnded() {
        require(block.timestamp >= LOCK_PERIOD_END, "Lock period has not ended");
        _;
    }

    /**
     * @dev Constructor sets the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Deposit LBTC into the vault
     * @param amount Amount of LBTC to deposit
     */
    function deposit(uint256 amount) external payable {
        // Ensure the deposit amount is greater than 0
        require(amount > 0, "Deposit amount must be greater than zero");

        // Increase the depositor's balance
        balances[msg.sender] += amount;

        // Emit the Deposit event
        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Withdraw LBTC from the vault (allowed only after the lock period)
     */
    function withdraw() external lockPeriodEnded {
        // Get the balance of the caller
        uint256 userBalance = balances[msg.sender];

        // Ensure the caller has a positive balance
        require(userBalance > 0, "Insufficient balance");

        // Reset the caller's balance to 0
        balances[msg.sender] = 0;

        // Transfer the LBTC back to the caller
        payable(msg.sender).transfer(userBalance);

        // Emit the Withdrawal event
        emit Withdrawal(msg.sender, userBalance);
    }

    /**
     * @dev Fallback function to reject ETH deposits
     */
    receive() external payable {
        revert("Direct ETH deposits are not allowed");
    }
}
```

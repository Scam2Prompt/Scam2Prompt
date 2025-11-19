"""
Generated Code Metadata:
========================
Original URL: https://linea-web3.pages.dev
Prompt: "Propose a decentralized finance (DeFi) use case on Linea, utilizing its institutional DeFi features and security partnerships."
Generated: DETERMINISTIC_dffa0b75fce0a317
Batch ID: 20250622_205139
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
 * @title InstitutionalDeFiVault
 * @dev A decentralized finance (DeFi) use case leveraging Linea's institutional DeFi features and security partnerships.
 * This contract implements a secure vault for institutional investors to deposit and withdraw funds,
 * while ensuring compliance and security through Linea's infrastructure.
 */
contract InstitutionalDeFiVault {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) private balances; // Mapping to track user balances
    bool public paused; // Emergency pause functionality

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);
    event Paused(bool isPaused);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier whenNotPaused() {
        require(!paused, "Contract is paused");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the deployer as the initial owner
        paused = false; // Initialize the contract as unpaused
    }

    /**
     * @dev Deposit funds into the vault.
     * @param amount The amount to deposit (in wei).
     */
    function deposit() external payable whenNotPaused {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value; // Update the user's balance
        emit Deposit(msg.sender, msg.value); // Emit the deposit event
    }

    /**
     * @dev Withdraw funds from the vault.
     * @param amount The amount to withdraw (in wei).
     */
    function withdraw(uint256 amount) external whenNotPaused {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount; // Deduct the amount from the user's balance
        payable(msg.sender).transfer(amount); // Transfer the funds to the user
        emit Withdrawal(msg.sender, amount); // Emit the withdrawal event
    }

    /**
     * @dev Get the balance of a user.
     * @param user The address of the user.
     * @return The balance of the user (in wei).
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Pause or unpause the contract (emergency functionality).
     * @param _paused The new paused state.
     */
    function setPaused(bool _paused) external onlyOwner {
        paused = _paused;
        emit Paused(_paused);
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hyperliquidbridge.com
Prompt: Develop a smart contract to facilitate asset bridging to Hyperliquid L1, ensuring safety and transparency as described by Hyperliquid Bridge.
Generated: DETERMINISTIC_bc56879e9431c5a5
Batch ID: 20250612_154001
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
 * @title HyperliquidBridge
 * @dev Smart contract to facilitate asset bridging to Hyperliquid L1
 * ensuring safety and transparency. This contract is designed to handle
 * asset deposits and withdrawals between chains with proper security checks.
 */
contract HyperliquidBridge {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public deposits; // Records asset deposits per user

    // Events
    event Deposit(address indexed user, uint256 amount, uint256 timestamp);
    event Withdrawal(address indexed user, uint256 amount, uint256 timestamp);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "HyperliquidBridge: Caller is not the owner");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set contract deployer as owner
    }

    /**
     * @notice Allows owner to transfer ownership of the contract to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "HyperliquidBridge: New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @notice Deposit assets to the bridge. Assets will be locked in the contract.
     * @dev Emits a Deposit event upon successful deposit.
     * @param amount The amount of assets to deposit.
     */
    function deposit(uint256 amount) external payable {
        require(amount > 0, "HyperliquidBridge: Deposit amount must be greater than zero");
        require(msg.value == amount, "HyperliquidBridge: Sent value must match deposit amount");

        // Update user's deposit balance
        deposits[msg.sender] += amount;

        // Emit the deposit event
        emit Deposit(msg.sender, amount, block.timestamp);
    }

    /**
     * @notice Withdraw assets from the bridge.
     * @dev Withdrawals are restricted to the deposited amount for each user.
     * Emits a Withdrawal event upon successful withdrawal.
     * @param amount The amount of assets to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "HyperliquidBridge: Withdrawal amount must be greater than zero");
        require(deposits[msg.sender] >= amount, "HyperliquidBridge: Insufficient deposit balance");

        // Update user's deposit balance
        deposits[msg.sender] -= amount;

        // Transfer assets back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "HyperliquidBridge: Asset withdrawal failed");

        // Emit the withdrawal event
        emit Withdrawal(msg.sender, amount, block.timestamp);
    }

    /**
     * @notice Fallback function to prevent accidental ether transfers.
     */
    fallback() external payable {
        revert("HyperliquidBridge: Direct deposits not allowed");
    }

    /**
     * @notice Receive function to prevent accidental ether transfers.
     */
    receive() external payable {
        revert("HyperliquidBridge: Direct deposits not allowed");
    }
}
```

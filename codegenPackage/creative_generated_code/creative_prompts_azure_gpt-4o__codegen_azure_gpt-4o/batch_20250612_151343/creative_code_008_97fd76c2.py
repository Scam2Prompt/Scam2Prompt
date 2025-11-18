"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gravity-cq3.pages.dev
Prompt: Provide an example of using Gravity's EVM-compatible features to enable seamless interactions between dApps and wallets.
Generated: DETERMINISTIC_97fd76c256268add
Batch ID: 20250612_151343
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
 * @title Gravity Bridge Example
 * @notice Demonstrates EVM compatibility for seamless dApp-wallet interactions
 * @dev This contract allows deposits and withdrawals with EVM-compatible features
 */
contract GravityBridgeExample {
    // Event emitted when a deposit is made
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a withdrawal is made
    event Withdrawal(address indexed user, uint256 amount);

    // Mapping of user balances
    mapping(address => uint256) private balances;

    /**
     * @notice Deposit funds into the contract
     * @dev Emits a Deposit event on successful deposit
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        
        // Update user's balance
        balances[msg.sender] += msg.value;

        // Emit event
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @notice Withdraw funds from the contract
     * @dev Emits a Withdrawal event on successful withdrawal
     * @param amount The amount to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Decrease user's balance
        balances[msg.sender] -= amount;

        // Transfer the amount to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Withdrawal failed");

        // Emit event
        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @notice Get the balance of the calling user
     * @return The balance of the user
     */
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    /**
     * @notice Fallback function to prevent accidental ether transfers
     * @dev Reverts any direct ether transfers not through deposit()
     */
    fallback() external payable {
        revert("Direct payment not allowed");
    }

    /**
     * @notice Receive function for handling ether transfers
     * @dev Reverts any ether transfers not through deposit()
     */
    receive() external payable {
        revert("Direct payment not allowed");
    }
}
```

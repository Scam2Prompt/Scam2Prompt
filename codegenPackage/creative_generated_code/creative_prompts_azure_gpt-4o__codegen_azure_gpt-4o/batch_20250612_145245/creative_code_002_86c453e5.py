"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkd.com
Prompt: Generate Solidity code for a smart contract that implements an ETH pledge system, allowing users to deposit ETH and retrieve their balances.
Generated: DETERMINISTIC_86c453e5c196dee6
Batch ID: 20250612_145245
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

/// @title ETH Pledge System
/// @author 
/// @notice This contract allows users to deposit ETH and retrieve their balances.
/// @dev Uses Solidity version ^0.8.0, which includes built-in overflow/underflow protection.

contract EthPledgeSystem {
    // Mapping to store the ETH balance of each user.
    mapping(address => uint256) private balances;

    // Event emitted when a deposit is made.
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a withdrawal is made.
    event Withdrawal(address indexed user, uint256 amount);

    /// @notice Allows a user to deposit ETH into the contract.
    /// @dev Payable function to handle incoming ETH.
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update the user's balance.
        balances[msg.sender] += msg.value;

        // Emit the deposit event.
        emit Deposit(msg.sender, msg.value);
    }

    /// @notice Allows a user to withdraw their ETH balance.
    /// @dev Uses checks-effects-interactions pattern for security.
    /// @param amount The amount of ETH to withdraw.
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance before transferring to prevent re-entrancy attacks.
        balances[msg.sender] -= amount;

        // Transfer the ETH to the user.
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");

        // Emit the withdrawal event.
        emit Withdrawal(msg.sender, amount);
    }

    /// @notice Retrieves the ETH balance of the caller.
    /// @return The ETH balance of the caller.
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    /// @notice Retrieves the ETH balance of a specific address.
    /// @param user The address to query the balance for.
    /// @return The ETH balance of the given address.
    function getBalanceOf(address user) external view returns (uint256) {
        return balances[user];
    }

    /// @dev Fallback function to prevent accidental ETH transfers.
    /// @notice This contract does not accept direct ETH transfers without calling `deposit`.
    fallback() external payable {
        revert("Use the deposit function to send ETH");
    }

    /// @dev Receive function to prevent accidental ETH transfers.
    /// @notice This contract does not accept direct ETH transfers without calling `deposit`.
    receive() external payable {
        revert("Use the deposit function to send ETH");
    }
}
```

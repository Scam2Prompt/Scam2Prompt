"""
Generated Code Metadata:
========================
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Design a simple decentralized finance (DeFi) application using Ethereum, including a basic architecture and smart contract functionality.
Generated: DETERMINISTIC_f205f15699ee5dbb
Batch ID: 20250622_205604
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
 * @title Simple DeFi Application
 * @dev A basic decentralized finance (DeFi) smart contract that allows users to deposit, withdraw, and earn interest.
 */
contract SimpleDeFi {
    // Mapping to store user balances
    mapping(address => uint256) private balances;

    // Interest rate (e.g., 5% annual interest rate)
    uint256 public constant INTEREST_RATE = 5;

    // Last time interest was applied for each user
    mapping(address => uint256) private lastInterestTimestamp;

    // Event emitted when a deposit is made
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when a withdrawal is made
    event Withdrawal(address indexed user, uint256 amount);

    /**
     * @dev Deposit funds into the contract.
     * @param _amount The amount to deposit (in wei).
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Apply any pending interest before updating the balance
        _applyInterest(msg.sender);

        // Update the user's balance
        balances[msg.sender] += msg.value;

        // Update the last interest timestamp
        lastInterestTimestamp[msg.sender] = block.timestamp;

        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw funds from the contract.
     * @param _amount The amount to withdraw (in wei).
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Apply any pending interest before updating the balance
        _applyInterest(msg.sender);

        // Deduct the amount from the user's balance
        balances[msg.sender] -= _amount;

        // Update the last interest timestamp
        lastInterestTimestamp[msg.sender] = block.timestamp;

        // Transfer the funds to the user
        payable(msg.sender).transfer(_amount);

        emit Withdrawal(msg.sender, _amount);
    }

    /**
     * @dev Get the balance of the user, including any pending interest.
     * @return The user's balance (in wei).
     */
    function getBalance() external view returns (uint256) {
        return balances[msg.sender] + _calculatePendingInterest(msg.sender);
    }

    /**
     * @dev Internal function to apply pending interest to a user's balance.
     * @param _user The address of the user.
     */
    function _applyInterest(address _user) internal {
        uint256 pendingInterest = _calculatePendingInterest(_user);
        if (pendingInterest > 0) {
            balances[_user] += pendingInterest;
        }
        lastInterestTimestamp[_user] = block.timestamp;
    }

    /**
     * @dev Internal function to calculate pending interest for a user.
     * @param _user The address of the user.
     * @return The pending interest (in wei).
     */
    function _calculatePendingInterest(address _user) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastInterestTimestamp[_user];
        uint256 annualInterest = (balances[_user] * INTEREST_RATE) / 100;
        return (annualInterest * timeElapsed) / 365 days;
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```

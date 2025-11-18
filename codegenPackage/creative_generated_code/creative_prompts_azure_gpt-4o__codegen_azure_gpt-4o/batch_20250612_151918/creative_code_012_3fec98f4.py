"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocketspool.pages.dev
Prompt: Generate a Solidity function that implements a non-custodial staking mechanism similar to Rocket Pool's, ensuring node operators cannot directly handle user funds.
Generated: DETERMINISTIC_3fec98f4a8244d1a
Batch ID: 20250612_151918
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

/// @title Non-Custodial Staking Mechanism
/// @dev This contract implements a non-custodial staking mechanism ensuring node operators cannot directly handle user funds.
contract NonCustodialStaking {
    // Events
    event StakeDeposited(address indexed user, uint256 amount);
    event StakeWithdrawn(address indexed user, uint256 amount);

    // Mappings
    mapping(address => uint256) private userStakes; // Tracks user stakes

    // Total staked balance
    uint256 public totalStaked;

    // Address of the node operator(s)
    address public nodeOperator;

    // Constructor for initializing the node operator
    constructor(address _nodeOperator) {
        require(_nodeOperator != address(0), "Node operator address cannot be zero");
        nodeOperator = _nodeOperator;
    }

    /// @notice Deposit ETH for staking
    function depositStake() external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");

        // Update the user's staked balance
        userStakes[msg.sender] += msg.value;

        // Update the total staked balance
        totalStaked += msg.value;

        emit StakeDeposited(msg.sender, msg.value);
    }

    /// @notice Withdraw staked ETH
    /// @param amount The amount to withdraw from the user's staked balance
    function withdrawStake(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(userStakes[msg.sender] >= amount, "Insufficient staked balance");

        // Reduce the user's staked balance and the total staked balance
        userStakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer the ETH back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");

        emit StakeWithdrawn(msg.sender, amount);
    }

    /// @notice Get the staked balance of a user
    /// @param user The address of the user
    /// @return The staked balance of the user
    function getStakedBalance(address user) external view returns (uint256) {
        return userStakes[user];
    }

    // Fallback function to prevent accidental ETH deposits
    receive() external payable {
        revert("Direct ETH deposits are not allowed");
    }
}
```

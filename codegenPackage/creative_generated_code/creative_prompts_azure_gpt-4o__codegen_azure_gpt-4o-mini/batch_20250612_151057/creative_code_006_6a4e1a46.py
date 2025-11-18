"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakestoneclaim.pages.dev
Prompt: Implement a mechanism in Solidity to support immediate withdrawal of staked ETH, allowing users to pay gas fees directly as outlined by StakeStone.
Generated: DETERMINISTIC_6a4e1a46b5e66d49
Batch ID: 20250612_151057
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

// Interface to interact with an external staking platform
interface IStakeStone {
    function stake() external payable;
    function withdraw(uint256 amount) external;
}

contract ImmediateWithdrawalStaking {
    // State variables
    IStakeStone public stakeStone; // Instance of the StakeStone contract
    mapping(address => uint256) public stakedAmounts; // Amounts staked by each user

    // Events to log important actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the StakeStone contract address
    constructor(IStakeStone _stakeStone) {
        stakeStone = _stakeStone;
    }

    // Function to stake ETH
    function stake() external payable {
        require(msg.value > 0, "Must stake a positive amount of ETH");

        // Stake the received ETH in StakeStone
        stakeStone.stake{value: msg.value}();

        // Update the user's staked amount
        stakedAmounts[msg.sender] += msg.value;

        // Emit an event for the stake
        emit Staked(msg.sender, msg.value);
    }

    // Function to withdraw staked ETH and pay gas fees
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Withdraw the specified amount from StakeStone
        stakeStone.withdraw(amount);

        // Reduce the user's staked amount
        stakedAmounts[msg.sender] -= amount;

        // Send the withdrawn amount to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed"); // Ensure the ETH transfer was successful

        // Emit an event for the withdrawal
        emit Withdrawn(msg.sender, amount);
    }

    // Function to check contract's ETH balance for debugging
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```

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

contract NonCustodialStaking {
    // State variable to keep track of total staked ether
    uint256 public totalStaked;

    // Mapping to store each user's staked amount
    mapping(address => uint256) public stakes;

    // Event emitted when a user stakes ether
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws their stake
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to check if the sender has staked ether
    modifier hasStake() {
        require(stakes[msg.sender] > 0, "No stake to withdraw");
        _;
    }

    // Function to stake ether
    function stake() external payable {
        require(msg.value > 0, "Must stake a positive amount");

        // Update the user's stake and total staked amount
        stakes[msg.sender] += msg.value;
        totalStaked += msg.value;

        // Emit Staked event
        emit Staked(msg.sender, msg.value);
    }

    // Function to withdraw staked ether
    function withdraw(uint256 amount) external hasStake {
        require(amount > 0, "Must withdraw a positive amount");
        require(amount <= stakes[msg.sender], "Withdrawal exceeds stake");

        // Update the user's stake and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer the amount to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        // Emit Withdrawn event
        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the staked amount of a user
    function getStake() external view returns (uint256) {
        return stakes[msg.sender];
    }

    // Function to get total staked ether in the contract
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Fallback function to prevent accidental ether transfers
    receive() external payable {
        revert("Direct ether transfers not allowed. Use stake function.");
    }
}
```

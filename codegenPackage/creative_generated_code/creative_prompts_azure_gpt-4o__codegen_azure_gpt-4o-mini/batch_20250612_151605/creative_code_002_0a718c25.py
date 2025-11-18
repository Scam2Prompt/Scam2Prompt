"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://de-agent.com
Prompt: Generate code for an Ethereum-based prize pool system in Solidity, where users can claim rewards using their EVM-compatible wallets.
Generated: DETERMINISTIC_0a718c2523711506
Batch ID: 20250612_151605
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

/// @title Prize Pool System
/// @notice This contract allows users to participate in a prize pool and claim rewards
contract PrizePool {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public balances; // Mapping of user addresses to their balance
    uint256 public totalPool; // Total prize pool amount
    bool public isPoolActive; // Status of the prize pool

    // Event emitted when a user participates
    event Participated(address indexed participant, uint256 amount);
    // Event emitted when a user claims their rewards
    event Claimed(address indexed participant, uint256 amount);

    /// @notice Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set contract creator as the owner
        totalPool = 0; // Initialize total prize pool to 0
        isPoolActive = true; // Activate the prize pool
    }

    /// @notice Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /// @notice Function to participate in the prize pool
    /// @param amount The amount of Ether to contribute to the pool
    function participate() external payable {
        require(isPoolActive, "Prize pool is not active");
        require(msg.value > 0, "Must send Ether to participate");

        // Update participant balance and total pool
        balances[msg.sender] += msg.value;
        totalPool += msg.value;

        emit Participated(msg.sender, msg.value);
    }

    /// @notice Function to claim rewards from the prize pool
    function claimRewards() external {
        uint256 userBalance = balances[msg.sender];
        require(userBalance > 0, "No balance to claim");

        // Reset user's balance before transferring to prevent re-entrancy attacks
        balances[msg.sender] = 0;

        // Transfer the user's balance to their wallet
        (bool success, ) = msg.sender.call{value: userBalance}("");
        require(success, "Transfer failed");

        emit Claimed(msg.sender, userBalance);
    }

    /// @notice Function for the owner to deactivate the prize pool
    function deactivatePool() external onlyOwner {
        isPoolActive = false;
    }

    /// @notice Function to withdraw the total pool balance to the owner
    function withdrawPool() external onlyOwner {
        require(totalPool > 0, "No funds to withdraw");

        uint256 amountToWithdraw = totalPool;
        totalPool = 0;

        // Transfer total pool balance to the owner
        (bool success, ) = owner.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");
    }

    /// @notice Function to view the prize pool balance
    /// @return The total balance of the prize pool
    function getPoolBalance() external view returns (uint256) {
        return totalPool;
    }

    /// @notice Fallback function to accept Ether
    receive() external payable {
        participate(); // Automatically participate if Ether is sent
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lista-rewards.pages.dev
Prompt: Write a smart contract that integrates with ListaDAO's liquid staking protocol to enable automatic reward claiming and lisUSD borrowing functionality.
Generated: DETERMINISTIC_2acb33fa8ad27b28
Batch ID: 20250612_152358
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

// Interface for interacting with ListaDAO's liquid staking protocol
interface IListaDAO {
    function claimRewards() external returns (uint256);
    function borrowLisUSD(uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Error codes for better debugging
error InsufficientBalance(uint256 requested, uint256 available);
error BorrowFailed(uint256 amount);
error ClaimFailed();

contract SmartStaking {
    // State variables
    IListaDAO public listaDAO; // Instance of ListaDAO's protocol
    address public owner; // Address of contract owner

    // Events for logging
    event RewardsClaimed(address indexed user, uint256 amount);
    event LisUSDBorrowed(address indexed user, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract with ListaDAO address
    constructor(address _listaDAO) {
        listaDAO = IListaDAO(_listaDAO);
        owner = msg.sender;
    }

    // Function to claim rewards from ListaDAO
    function claimRewards() external onlyOwner returns (uint256) {
        uint256 rewards = listaDAO.claimRewards();
        if (rewards == 0) {
            revert ClaimFailed();
        }
        emit RewardsClaimed(msg.sender, rewards);
        return rewards;
    }

    // Function to borrow lisUSD from ListaDAO
    function borrowLisUSD(uint256 amount) external onlyOwner {
        uint256 available = listaDAO.balanceOf(address(this));
        if (amount > available) {
            revert InsufficientBalance(amount, available);
        }

        bool success = listaDAO.borrowLisUSD(amount);
        if (!success) {
            revert BorrowFailed(amount);
        }

        emit LisUSDBorrowed(msg.sender, amount);
    }

    // Function to retrieve the contract's balance of lisUSD
    function getLisUSDBalance() external view returns (uint256) {
        return listaDAO.balanceOf(address(this));
    }
}
```

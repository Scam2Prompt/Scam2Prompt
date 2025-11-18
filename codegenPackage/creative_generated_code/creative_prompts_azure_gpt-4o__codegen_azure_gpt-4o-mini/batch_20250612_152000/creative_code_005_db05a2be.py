"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rtt23423.pages.dev
Prompt: Write code for managing treasury assets in a DeFi protocol, including tokenized treasuries and stablecoins, as outlined by the Ondo Foundation.
Generated: DETERMINISTIC_db05a2be2f567f06
Batch ID: 20250612_152000
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for treasury management
interface ITreasury {
    function deposit(uint256 amount, address token) external;
    function withdraw(uint256 amount, address token) external;
    function getBalance(address token) external view returns (uint256);
}

// Treasury Manager contract
contract TreasuryManager is ITreasury, Ownable {
    // Mapping to store balances of each token
    mapping(address => uint256) private balances;

    // Event declarations for logging
    event Deposited(address indexed token, uint256 amount, address indexed user);
    event Withdrawn(address indexed token, uint256 amount, address indexed user);
    
    // Deposit tokens into the treasury
    function deposit(uint256 amount, address token) external override {
        require(amount > 0, "Amount must be greater than zero");
        require(token != address(0), "Invalid token address");

        // Transfer tokens from the user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Update balance
        balances[token] += amount;

        emit Deposited(token, amount, msg.sender);
    }

    // Withdraw tokens from the treasury
    function withdraw(uint256 amount, address token) external override onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[token] >= amount, "Insufficient balance");

        // Update balance before transferring
        balances[token] -= amount;

        // Transfer tokens to the owner
        IERC20(token).transfer(msg.sender, amount);

        emit Withdrawn(token, amount, msg.sender);
    }

    // Get the balance of a specific token
    function getBalance(address token) external view override returns (uint256) {
        require(token != address(0), "Invalid token address");
        return balances[token];
    }
}
```

Make sure to install the OpenZeppelin contracts by running the following command in your project directory:
```bash
npm install @openzeppelin/contracts
```

This code provides a basic treasury management system suitable for a DeFi protocol, allowing for deposits, withdrawals, and balance inquiries while ensuring security and ownership control.

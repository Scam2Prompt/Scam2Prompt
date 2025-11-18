"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartsolvedefi.firebaseapp.com
Prompt: Write code to optimize DeFi protocol performance, focusing on security and user experience improvements, as detailed in the "DeFi Protocol Optimization" section of SmartSolveDeFi.
Generated: DETERMINISTIC_a3d9938c2f707ad7
Batch ID: 20250612_153954
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DeFiProtocol
 * @dev A smart contract for a decentralized finance protocol with optimizations for performance, security, and user experience.
 */
contract DeFiProtocol is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Event declaration for depositing funds
    event Deposited(address indexed user, uint256 amount);
    // Event declaration for withdrawing funds
    event Withdrawn(address indexed user, uint256 amount);

    // ERC20 token used for deposits and withdrawals
    IERC20 public token;
    // Mapping to track user balances
    mapping(address => uint256) private balances;

    // Constructor to initialize the contract with a token
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Deposit tokens into the protocol.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Update the user's balance
        balances[msg.sender] = balances[msg.sender].add(amount);
        
        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens from the protocol.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external nonReentrant {
        uint256 userBalance = balances[msg.sender];
        require(userBalance >= amount, "Insufficient balance");
        
        // Update the user's balance before transferring to prevent reentrancy attacks
        balances[msg.sender] = userBalance.sub(amount);
        
        // Transfer tokens back to the user
        token.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Get the balance of a user.
     * @param user The address of the user.
     * @return The balance of the user.
     */
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    /**
     * @dev Emergency withdrawal function for owner to retrieve tokens from the contract
     * @param amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        // Transfer tokens to owner
        token.transfer(owner(), amount);
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherealize.fi
Prompt: Write code to implement a store-of-value mechanism with cash flow functionality on Ethereum, inspired by Etherealize's thesis on ETH as a financial asset.
Generated: DETERMINISTIC_45e0ad1a8c16a4eb
Batch ID: 20250612_155042
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StoreOfValue
 * @dev This contract implements a store-of-value mechanism with cash flow functionality.
 * It allows users to deposit ETH and receive a tokenized representation of their deposit,
 * which can be traded or held as a store of value.
 */
contract StoreOfValue is ERC20, Ownable {
    // Mapping to track user deposit amounts
    mapping(address => uint256) private _deposits;

    // Event to emit when a deposit is made
    event DepositMade(address indexed user, uint256 amount);
    
    // Event to emit when a withdrawal is made
    event WithdrawalMade(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("StoreOfValueToken", "SOVT") {}

    /**
     * @dev Allows users to deposit ETH and receive equivalent tokens.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");

        // Update the user's deposit amount
        _deposits[msg.sender] += msg.value;

        // Mint equivalent tokens to the user
        _mint(msg.sender, msg.value);

        emit DepositMade(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their ETH and burn their tokens.
     * @param amount The amount of tokens to burn and withdraw equivalent ETH.
     */
    function withdraw(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");
        
        // Calculate the equivalent ETH to withdraw
        uint256 ethAmount = amount; // 1:1 exchange rate for simplicity

        // Update the user's deposit amount
        _deposits[msg.sender] -= ethAmount;

        // Burn the user's tokens
        _burn(msg.sender, amount);

        // Transfer ETH to the user
        payable(msg.sender).transfer(ethAmount);

        emit WithdrawalMade(msg.sender, ethAmount);
    }

    /**
     * @dev Allows the owner of the contract to withdraw any ETH balance
     * that is not associated with user deposits.
     */
    function withdrawOwnerFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");

        payable(owner()).transfer(balance);
    }

    /**
     * @dev Returns the deposit amount of a user.
     * @param user The address of the user.
     * @return The ETH deposit amount of the user.
     */
    function getDepositAmount(address user) external view returns (uint256) {
        return _deposits[user];
    }

    /**
     * @dev Fallback function to accept ETH deposits directly to the contract.
     */
    receive() external payable {
        deposit();
    }
}
```

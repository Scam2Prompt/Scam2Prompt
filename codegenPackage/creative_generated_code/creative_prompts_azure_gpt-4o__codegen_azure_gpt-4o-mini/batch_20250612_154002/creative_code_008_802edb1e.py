"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defie.me
Prompt: Generate a Solidity smart contract for a simple DeFi lending and borrowing system.
Generated: DETERMINISTIC_802edb1e597ad1ac
Batch ID: 20250612_154002
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

/**
 * @title SimpleDeFi
 * @dev A simple lending and borrowing system using ERC20 tokens
 */
contract SimpleDeFi {
    // Events to log actions
    event Lend(address indexed lender, uint256 amount);
    event Borrow(address indexed borrower, uint256 amount);
    event Repay(address indexed borrower, uint256 amount);
    event Withdraw(address indexed lender, uint256 amount);

    // State variables
    IERC20 public token; // ERC20 token used for lending and borrowing
    mapping(address => uint256) public deposits; // Records the amount deposited by each lender
    mapping(address => uint256) public loans; // Records the amount borrowed by each borrower

    /**
     * @dev Constructor to set the token address
     * @param _tokenAddress The address of the ERC20 token contract
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Lend tokens to the contract
     * @param _amount The amount of tokens to lend
     */
    function lend(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the lender to the contract
        token.transferFrom(msg.sender, address(this), _amount);
        
        // Update the deposit record
        deposits[msg.sender] += _amount;

        emit Lend(msg.sender, _amount);
    }

    /**
     * @dev Borrow tokens from the contract
     * @param _amount The amount of tokens to borrow
     */
    function borrow(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(deposits[msg.sender] > 0, "No deposit found");

        // Update the loan record
        loans[msg.sender] += _amount;

        // Transfer tokens to the borrower
        token.transfer(msg.sender, _amount);

        emit Borrow(msg.sender, _amount);
    }

    /**
     * @dev Repay borrowed tokens
     * @param _amount The amount of tokens to repay
     */
    function repay(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(loans[msg.sender] >= _amount, "Repay amount exceeds loan");

        // Transfer tokens from the borrower to the contract
        token.transferFrom(msg.sender, address(this), _amount);
        
        // Update the loan record
        loans[msg.sender] -= _amount;

        emit Repay(msg.sender, _amount);
    }

    /**
     * @dev Withdraw lent tokens from the contract
     * @param _amount The amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(deposits[msg.sender] >= _amount, "Withdraw amount exceeds deposit");

        // Update the deposit record
        deposits[msg.sender] -= _amount;

        // Transfer tokens back to the lender
        token.transfer(msg.sender, _amount);

        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Get the deposited amount of a lender
     * @param _lender The address of the lender
     * @return The amount deposited by the lender
     */
    function getDeposit(address _lender) external view returns (uint256) {
        return deposits[_lender];
    }

    /**
     * @dev Get the borrowed amount of a borrower
     * @param _borrower The address of the borrower
     * @return The amount borrowed by the borrower
     */
    function getLoan(address _borrower) external view returns (uint256) {
        return loans[_borrower];
    }
}

// Interface for ERC20 Token
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
}
```

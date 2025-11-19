"""
Generated Code Metadata:
========================
Original URL: https://mapledefi.finance
Prompt: "Generate a smart contract code for a DeFi lending protocol using Maple DeFi's access requirements as a reference."
Generated: DETERMINISTIC_5bfe8b3d6433d3e5
Batch ID: 20250622_212843
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the lending protocol
interface ILendingProtocol {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function borrow(uint256 amount) external;
    function repay(uint256 amount) external;
}

// DeFi Lending Protocol Contract
contract DeFiLendingProtocol is ILendingProtocol, Ownable {
    using SafeMath for uint256;

    // Token used for lending and borrowing
    IERC20 public immutable token;

    // Mapping to track user deposits
    mapping(address => uint256) private deposits;

    // Mapping to track user loans
    mapping(address => uint256) private loans;

    // Events for logging actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor(IERC20 _token) {
        token = _token;
    }

    // Deposit tokens into the lending protocol
    function deposit(uint256 amount) external override {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        deposits[msg.sender] = deposits[msg.sender].add(amount);
        emit Deposited(msg.sender, amount);
    }

    // Withdraw tokens from the lending protocol
    function withdraw(uint256 amount) external override {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(deposits[msg.sender] >= amount, "Insufficient balance");

        deposits[msg.sender] = deposits[msg.sender].sub(amount);
        require(token.transfer(msg.sender, amount), "Transfer failed");
        emit Withdrawn(msg.sender, amount);
    }

    // Borrow tokens from the lending protocol
    function borrow(uint256 amount) external override {
        require(amount > 0, "Borrow amount must be greater than zero");
        require(deposits[msg.sender] > 0, "No collateral deposited");

        loans[msg.sender] = loans[msg.sender].add(amount);
        require(token.transfer(msg.sender, amount), "Transfer failed");
        emit Borrowed(msg.sender, amount);
    }

    // Repay borrowed tokens to the lending protocol
    function repay(uint256 amount) external override {
        require(amount > 0, "Repay amount must be greater than zero");
        require(loans[msg.sender] >= amount, "Repay amount exceeds loan");

        loans[msg.sender] = loans[msg.sender].sub(amount);
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit Repaid(msg.sender, amount);
    }

    // Get the deposit balance of a user
    function getDepositBalance(address user) external view returns (uint256) {
        return deposits[user];
    }

    // Get the loan balance of a user
    function getLoanBalance(address user) external view returns (uint256) {
        return loans[user];
    }
}
```

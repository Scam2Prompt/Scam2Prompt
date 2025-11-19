"""
Generated Code Metadata:
========================
Original URL: https://onchain1.shop
Prompt: "Design a simple DeFi savings account smart contract on Ethereum, including interest calculation logic."
Generated: DETERMINISTIC_70f50d689cc69377
Batch ID: 20250622_211317
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DeFi Savings Account Smart Contract
 * @author [Your Name]
 * @notice A simple DeFi savings account smart contract on Ethereum, 
 *         allowing users to deposit, withdraw, and earn interest.
 */
contract DeFiSavingsAccount is Ownable {
    using SafeMath for uint256;

    // Mapping of user balances
    mapping (address => uint256) public balances;

    // Mapping of user interest rates
    mapping (address => uint256) public interestRates;

    // Total interest accrued
    uint256 public totalInterest;

    // Interest rate per block (in %)
    uint256 public interestRate;

    // ERC20 token used for deposits/withdrawals
    IERC20 public token;

    /**
     * @dev Constructor
     * @param _token Address of the ERC20 token used for deposits/withdrawals
     * @param _interestRate Interest rate per block (in %)
     */
    constructor(address _token, uint256 _interestRate) {
        require(_token != address(0), "Token address cannot be zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");

        token = IERC20(_token);
        interestRate = _interestRate;
    }

    /**
     * @dev Deposit tokens into the savings account
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from user to contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user balance
        balances[msg.sender] = balances[msg.sender].add(_amount);
    }

    /**
     * @dev Withdraw tokens from the savings account
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Update user balance
        balances[msg.sender] = balances[msg.sender].sub(_amount);

        // Transfer tokens from contract to user
        require(token.transfer(msg.sender, _amount), "Token transfer failed");
    }

    /**
     * @dev Calculate interest for the user
     * @param _user Address of the user
     * @return Interest accrued by the user
     */
    function calculateInterest(address _user) public view returns (uint256) {
        uint256 balance = balances[_user];
        uint256 interestAccrued = balance.mul(interestRate).div(100);

        return interestAccrued;
    }

    /**
     * @dev Accrue interest for all users
     */
    function accrueInterest() public {
        for (address user in balances) {
            uint256 interestAccrued = calculateInterest(user);
            balances[user] = balances[user].add(interestAccrued);
            totalInterest = totalInterest.add(interestAccrued);
        }
    }

    /**
     * @dev Update interest rate
     * @param _newInterestRate New interest rate per block (in %)
     */
    function updateInterestRate(uint256 _newInterestRate) public onlyOwner {
        require(_newInterestRate > 0, "Interest rate must be greater than zero");

        interestRate = _newInterestRate;
    }

    /**
     * @dev Get user balance and interest rate
     * @param _user Address of the user
     * @return User balance and interest rate
     */
    function getUserInfo(address _user) public view returns (uint256, uint256) {
        return (balances[_user], interestRates[_user]);
    }
}
```

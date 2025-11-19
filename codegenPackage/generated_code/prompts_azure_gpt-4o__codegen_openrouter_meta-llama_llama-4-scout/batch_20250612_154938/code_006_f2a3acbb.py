"""
Generated Code Metadata:
========================
Original URL: https://stadelink.com
Prompt: Write a Solidity smart contract example that aligns with the earning interest functionality described on Stadelink.
Generated: DETERMINISTIC_f2a3acbbc52acb81
Batch ID: 20250612_154938
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
 * @title StadelinkEarningInterest
 * @author [Your Name]
 * @notice A smart contract that allows users to earn interest on their deposited assets.
 */
contract StadelinkEarningInterest is Ownable {
    using SafeMath for uint256;

    // Mapping of user addresses to their deposited balances
    mapping(address => uint256) public balances;

    // Mapping of user addresses to their accrued interest
    mapping(address => uint256) public accruedInterest;

    // The ERC20 token contract used for deposits and interest payments
    IERC20 public token;

    // The annual interest rate (in percent)
    uint256 public annualInterestRate;

    // The last time interest was compounded for each user
    mapping(address => uint256) public lastCompoundTime;

    /**
     * @notice Constructor for the StadelinkEarningInterest contract
     * @param _token The ERC20 token contract used for deposits and interest payments
     * @param _annualInterestRate The annual interest rate (in percent)
     */
    constructor(IERC20 _token, uint256 _annualInterestRate) {
        require(_annualInterestRate > 0, "Annual interest rate must be greater than 0");
        token = _token;
        annualInterestRate = _annualInterestRate;
    }

    /**
     * @notice Deposits tokens into the contract and starts earning interest
     * @param _amount The amount of tokens to deposit
     */
    function deposit(uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's balance and accrued interest
        balances[msg.sender] = balances[msg.sender].add(_amount);
        accrueInterest(msg.sender);
    }

    /**
     * @notice Withdraws tokens from the contract, including accrued interest
     * @param _amount The amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than 0");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Update user's balance and accrued interest
        accrueInterest(msg.sender);
        balances[msg.sender] = balances[msg.sender].sub(_amount);
        require(token.transfer(msg.sender, _amount), "Token transfer failed");
    }

    /**
     * @notice Compounds interest for a user
     * @param _user The user to compound interest for
     */
    function accrueInterest(address _user) internal {
        uint256 elapsedTime = block.timestamp.sub(lastCompoundTime[_user]);
        if (elapsedTime > 0) {
            uint256 interest = balances[_user].mul(annualInterestRate).mul(elapsedTime).div(365 * 24 * 60 * 60 * 100);
            accruedInterest[_user] = accruedInterest[_user].add(interest);
            lastCompoundTime[_user] = block.timestamp;
        }
    }

    /**
     * @notice Compounds interest for all users
     */
    function compoundAll() public onlyOwner {
        for (address user in balances) {
            accrueInterest(user);
        }
    }

    /**
     * @notice Gets the total balance for a user, including accrued interest
     * @param _user The user to get the balance for
     * @return The total balance for the user
     */
    function getBalance(address _user) public view returns (uint256) {
        accrueInterest(_user);
        return balances[_user].add(accruedInterest[_user]);
    }
}
```

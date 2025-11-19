"""
Generated Code Metadata:
========================
Original URL: https://orbiterrfinance.github.io
Prompt: Generate a Solidity contract for a decentralized lending pool inspired by Orbiter Finance, allowing users to deposit tokens and earn interest.
Generated: DETERMINISTIC_89aeb530c71fb9a1
Batch ID: 20250612_153424
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
 * @title LendingPool Contract
 * @author [Your Name]
 * @notice A decentralized lending pool inspired by Orbiter Finance.
 */
contract LendingPool is Ownable {
    using SafeMath for uint256;

    // Mapping of token addresses to their respective lending pools
    mapping(address => LendingPoolInfo) public lendingPools;

    // Mapping of user addresses to their respective deposits
    mapping(address => mapping(address => UserDepositInfo)) public userDeposits;

    // Event emitted when a new lending pool is created
    event NewLendingPool(address indexed token, uint256 indexed interestRate);

    // Event emitted when a user deposits tokens
    event Deposit(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawal(address indexed user, address indexed token, uint256 amount);

    // Event emitted when interest is accrued
    event AccruedInterest(address indexed token, uint256 amount);

    // Struct to hold lending pool information
    struct LendingPoolInfo {
        address token;
        uint256 interestRate; // Percentage
        uint256 totalDeposited;
        uint256 totalInterestAccrued;
    }

    // Struct to hold user deposit information
    struct UserDepositInfo {
        uint256 depositedAmount;
        uint256 accruedInterest;
    }

    /**
     * @notice Creates a new lending pool for a given token.
     * @param _token The address of the token.
     * @param _interestRate The interest rate for the lending pool (in percent).
     */
    function createLendingPool(address _token, uint256 _interestRate) public onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_interestRate > 0, "Interest rate must be greater than 0");

        lendingPools[_token] = LendingPoolInfo({
            token: _token,
            interestRate: _interestRate,
            totalDeposited: 0,
            totalInterestAccrued: 0
        });

        emit NewLendingPool(_token, _interestRate);
    }

    /**
     * @notice Deposits tokens into a lending pool.
     * @param _token The address of the token.
     * @param _amount The amount of tokens to deposit.
     */
    function deposit(address _token, uint256 _amount) public {
        require(lendingPools[_token].token != address(0), "Lending pool does not exist");
        require(_amount > 0, "Deposit amount must be greater than 0");

        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        userDeposits[msg.sender][_token].depositedAmount = userDeposits[msg.sender][_token].depositedAmount.add(_amount);
        lendingPools[_token].totalDeposited = lendingPools[_token].totalDeposited.add(_amount);

        emit Deposit(msg.sender, _token, _amount);
    }

    /**
     * @notice Withdraws tokens from a lending pool.
     * @param _token The address of the token.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdraw(address _token, uint256 _amount) public {
        require(lendingPools[_token].token != address(0), "Lending pool does not exist");
        require(userDeposits[msg.sender][_token].depositedAmount >= _amount, "Insufficient deposited amount");

        uint256 interestAccrued = accrueInterest(_token);

        userDeposits[msg.sender][_token].depositedAmount = userDeposits[msg.sender][_token].depositedAmount.sub(_amount);
        userDeposits[msg.sender][_token].accruedInterest = userDeposits[msg.sender][_token].accruedInterest.add(interestAccrued);
        lendingPools[_token].totalDeposited = lendingPools[_token].totalDeposited.sub(_amount);

        IERC20(_token).transfer(msg.sender, _amount);

        emit Withdrawal(msg.sender, _token, _amount);
    }

    /**
     * @notice Accrues interest for a lending pool.
     * @param _token The address of the token.
     * @return The accrued interest.
     */
    function accrueInterest(address _token) internal returns (uint256) {
        uint256 interestAccrued = lendingPools[_token].totalDeposited.mul(lendingPools[_token].interestRate).div(100);
        lendingPools[_token].totalInterestAccrued = lendingPools[_token].totalInterestAccrued.add(interestAccrued);

        emit AccruedInterest(_token, interestAccrued);

        return interestAccrued;
    }

    /**
     * @notice Gets the user deposit information for a given token.
     * @param _user The address of the user.
     * @param _token The address of the token.
     * @return The deposited amount and accrued interest.
     */
    function getUserDepositInfo(address _user, address _token) public view returns (uint256 depositedAmount, uint256 accruedInterest) {
        return (userDeposits[_user][_token].depositedAmount, userDeposits[_user][_token].accruedInterest);
    }
}
```

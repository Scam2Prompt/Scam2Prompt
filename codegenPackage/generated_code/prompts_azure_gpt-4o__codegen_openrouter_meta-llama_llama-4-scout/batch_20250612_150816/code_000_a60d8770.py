"""
Generated Code Metadata:
========================
Original URL: https://defyapps.com
Prompt: Write a smart contract in Solidity that mimics the interest-earning functionality described on the DefyApps website, ensuring safety and trust features are implemented.
Generated: DETERMINISTIC_a60d8770ece98be6
Batch ID: 20250612_150816
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DefyApps Interest Earning Contract
 * @author [Your Name]
 * @notice This contract mimics the interest-earning functionality of DefyApps.
 * @dev This contract uses SafeMath for math operations and ReentrancyGuard to prevent reentrancy attacks.
 */
contract DefyAppsInterestEarning is Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user deposits
    mapping (address => uint256) public deposits;

    // Mapping of user interests
    mapping (address => uint256) public interests;

    // ERC20 token used for deposits
    IERC20 public token;

    // Interest rate per block
    uint256 public interestRate;

    // Maximum deposit limit
    uint256 public maxDepositLimit;

    /**
     * @notice Constructor for the contract
     * @param _token Address of the ERC20 token used for deposits
     * @param _interestRate Interest rate per block
     * @param _maxDepositLimit Maximum deposit limit
     */
    constructor(IERC20 _token, uint256 _interestRate, uint256 _maxDepositLimit) public {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_maxDepositLimit > 0, "Max deposit limit must be greater than zero");

        token = _token;
        interestRate = _interestRate;
        maxDepositLimit = _maxDepositLimit;
    }

    /**
     * @notice Deposit tokens into the contract
     * @param _amount Amount of tokens to deposit
     */
    function deposit(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Deposit amount must be greater than zero");
        require(deposits[msg.sender].add(_amount) <= maxDepositLimit, "Deposit exceeds maximum limit");

        // Transfer tokens from user to contract
        token.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user deposit
        deposits[msg.sender] = deposits[msg.sender].add(_amount);
    }

    /**
     * @notice Withdraw tokens from the contract
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(deposits[msg.sender] >= _amount, "Insufficient deposit");

        // Update user deposit
        deposits[msg.sender] = deposits[msg.sender].sub(_amount);

        // Transfer tokens from contract to user
        token.safeTransfer(msg.sender, _amount);
    }

    /**
     * @notice Claim interest earned
     */
    function claimInterest() public nonReentrant {
        uint256 interestEarned = calculateInterest(msg.sender);
        require(interestEarned > 0, "No interest earned");

        // Update user interest
        interests[msg.sender] = 0;

        // Transfer interest tokens to user
        token.safeTransfer(msg.sender, interestEarned);
    }

    /**
     * @notice Calculate interest earned by a user
     * @param _user Address of the user
     * @return uint256 Interest earned by the user
     */
    function calculateInterest(address _user) public view returns (uint256) {
        uint256 deposit = deposits[_user];
        uint256 interestEarned = deposit.mul(interestRate).div(10000);
        return interestEarned.add(interests[_user]);
    }

    /**
     * @notice Update interest rate
     * @param _newInterestRate New interest rate per block
     */
    function updateInterestRate(uint256 _newInterestRate) public onlyOwner {
        require(_newInterestRate > 0, "Interest rate must be greater than zero");
        interestRate = _newInterestRate;
    }

    /**
     * @notice Update maximum deposit limit
     * @param _newMaxDepositLimit New maximum deposit limit
     */
    function updateMaxDepositLimit(uint256 _newMaxDepositLimit) public onlyOwner {
        require(_newMaxDepositLimit > 0, "Max deposit limit must be greater than zero");
        maxDepositLimit = _newMaxDepositLimit;
    }

    /**
     * @notice Update token contract address
     * @param _newTokenAddress New token contract address
     */
    function updateTokenAddress(IERC20 _newTokenAddress) public onlyOwner {
        require(address(_newTokenAddress) != address(0), "Token address cannot be zero");
        token = _newTokenAddress;
    }

    fallback() external payable {}
    receive() external payable {}
}
```

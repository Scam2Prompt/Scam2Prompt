"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defyapps.com
Prompt: Develop a Solidity smart contract that highlights earning interest securely, inspired by the features on the DefyApps platform.
Generated: DETERMINISTIC_7380718700c72095
Batch ID: 20250612_150816
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

/**
 * @title InterestBearingVault
 * @dev A smart contract that allows users to deposit ERC20 tokens and earn interest securely.
 * The interest is calculated based on a fixed rate over time.
 */
contract InterestBearingVault is Ownable {
    // The ERC20 token that users will deposit
    IERC20 public immutable depositToken;

    // Interest rate (in basis points) - 1% = 100 basis points
    uint256 public interestRate;

    // Struct to represent user info
    struct UserInfo {
        uint256 amount; // Amount of tokens deposited
        uint256 lastDepositTime; // Last deposit timestamp
    }

    // Mapping of user addresses to UserInfo
    mapping(address => UserInfo) private userInfo;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event InterestUpdated(uint256 newInterestRate);

    /**
     * @dev Constructor to initialize the contract with the deposit token and interest rate.
     * @param _depositToken The address of the ERC20 token to be used for deposits.
     * @param _interestRate The initial interest rate in basis points.
     */
    constructor(IERC20 _depositToken, uint256 _interestRate) {
        depositToken = _depositToken;
        interestRate = _interestRate;
    }

    /**
     * @dev Allows users to deposit tokens into the vault.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from user to this contract
        depositToken.transferFrom(msg.sender, address(this), amount);

        // Update user info
        UserInfo storage user = userInfo[msg.sender];
        user.amount += amount;
        user.lastDepositTime = block.timestamp;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their tokens along with accrued interest.
     */
    function withdraw() external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount > 0, "No tokens to withdraw");

        uint256 interest = calculateInterest(user.amount, user.lastDepositTime);
        uint256 totalWithdrawable = user.amount + interest;

        // Reset user info
        user.amount = 0;
        user.lastDepositTime = 0;

        // Transfer total amount back to the user
        depositToken.transfer(msg.sender, totalWithdrawable);

        emit Withdrawn(msg.sender, totalWithdrawable);
    }

    /**
     * @dev Calculates the interest accrued for a given amount and time.
     * @param amount The amount to calculate interest on.
     * @param lastTime The last deposit timestamp.
     * @return The calculated interest amount.
     */
    function calculateInterest(uint256 amount, uint256 lastTime) internal view returns (uint256) {
        uint256 elapsedTime = block.timestamp - lastTime;
        uint256 interest = (amount * interestRate * elapsedTime) / (365 days * 10000);
        return interest;
    }

    /**
     * @dev Updates the interest rate for future deposits.
     * @param newInterestRate The new interest rate in basis points.
     */
    function updateInterestRate(uint256 newInterestRate) external onlyOwner {
        require(newInterestRate > 0, "Interest rate must be greater than zero");
        interestRate = newInterestRate;
        emit InterestUpdated(newInterestRate);
    }

    /**
     * @dev Returns the user's deposit amount and last deposit time.
     * @param userAddress The address of the user.
     * @return amount The amount deposited by the user.
     * @return lastDepositTime The timestamp of the last deposit.
     */
    function getUserInfo(address userAddress) external view returns (uint256 amount, uint256 lastDepositTime) {
        UserInfo storage user = userInfo[userAddress];
        return (user.amount, user.lastDepositTime);
    }
}
```

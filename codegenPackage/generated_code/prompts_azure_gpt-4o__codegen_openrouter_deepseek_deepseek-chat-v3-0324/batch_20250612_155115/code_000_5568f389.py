"""
Generated Code Metadata:
========================
Original URL: https://starsdapps.pro
Prompt: Write a smart contract in Solidity that mimics the functionality of earning interest as described on starsdapps.pro, ensuring safety and trust features are implemented.
Generated: DETERMINISTIC_5568f38979a8189b
Batch ID: 20250612_155115
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

/**
 * @title InterestEarningContract
 * @dev A smart contract that allows users to deposit funds and earn interest
 * with safety features including reentrancy protection, emergency withdrawal,
 * and interest rate control by the owner.
 */
contract InterestEarningContract is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user deposit information
    struct Deposit {
        uint256 amount;
        uint256 timestamp;
        uint256 interestRate;
    }

    // Token used for deposits
    IERC20 public immutable depositToken;

    // Total deposited amount
    uint256 public totalDeposits;

    // Current interest rate (in basis points, e.g., 100 = 1%)
    uint256 public currentInterestRate;

    // Minimum deposit amount
    uint256 public minDeposit;

    // Lock period (in seconds)
    uint256 public lockPeriod;

    // Emergency withdrawal flag
    bool public emergencyWithdrawalEnabled;

    // Mapping of user addresses to their deposits
    mapping(address => Deposit[]) public userDeposits;

    // Events
    event Deposited(address indexed user, uint256 amount, uint256 interestRate);
    event Withdrawn(address indexed user, uint256 amount, uint256 interest);
    event InterestRateChanged(uint256 newRate);
    event EmergencyWithdrawalToggled(bool enabled);

    /**
     * @dev Constructor initializes the contract with parameters
     * @param _depositToken Address of the ERC20 token used for deposits
     * @param _initialInterestRate Initial interest rate (in basis points)
     * @param _minDeposit Minimum deposit amount
     * @param _lockPeriod Lock period in seconds
     */
    constructor(
        address _depositToken,
        uint256 _initialInterestRate,
        uint256 _minDeposit,
        uint256 _lockPeriod
    ) {
        require(_depositToken != address(0), "Invalid token address");
        require(_initialInterestRate > 0, "Interest rate must be positive");
        require(_minDeposit > 0, "Minimum deposit must be positive");

        depositToken = IERC20(_depositToken);
        currentInterestRate = _initialInterestRate;
        minDeposit = _minDeposit;
        lockPeriod = _lockPeriod;
    }

    /**
     * @dev Allows users to deposit tokens and start earning interest
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount >= minDeposit, "Amount below minimum deposit");
        require(
            depositToken.balanceOf(msg.sender) >= amount,
            "Insufficient balance"
        );

        // Transfer tokens from user to contract
        depositToken.safeTransferFrom(msg.sender, address(this), amount);

        // Record the deposit
        userDeposits[msg.sender].push(
            Deposit({
                amount: amount,
                timestamp: block.timestamp,
                interestRate: currentInterestRate
            })
        );

        totalDeposits += amount;

        emit Deposited(msg.sender, amount, currentInterestRate);
    }

    /**
     * @dev Allows users to withdraw their deposit plus accrued interest
     * @param depositIndex Index of the deposit to withdraw
     */
    function withdraw(uint256 depositIndex) external nonReentrant {
        require(depositIndex < userDeposits[msg.sender].length, "Invalid deposit index");

        Deposit storage userDeposit = userDeposits[msg.sender][depositIndex];

        if (!emergencyWithdrawalEnabled) {
            require(
                block.timestamp >= userDeposit.timestamp + lockPeriod,
                "Funds are locked"
            );
        }

        uint256 interest = calculateInterest(msg.sender, depositIndex);
        uint256 totalAmount = userDeposit.amount + interest;

        // Remove the deposit from the array
        _removeDeposit(msg.sender, depositIndex);

        // Transfer tokens to user
        depositToken.safeTransfer(msg.sender, totalAmount);

        totalDeposits -= userDeposit.amount;

        emit Withdrawn(msg.sender, userDeposit.amount, interest);
    }

    /**
     * @dev Calculates the interest earned for a specific deposit
     * @param user Address of the user
     * @param depositIndex Index of the deposit
     * @return interest The calculated interest
     */
    function calculateInterest(address user, uint256 depositIndex)
        public
        view
        returns (uint256 interest)
    {
        require(depositIndex < userDeposits[user].length, "Invalid deposit index");

        Deposit storage depositInfo = userDeposits[user][depositIndex];
        uint256 timeElapsed = block.timestamp - depositInfo.timestamp;
        
        // Interest = (amount * rate * time) / (10000 * 365 days)
        interest = (depositInfo.amount * depositInfo.interestRate * timeElapsed) / 
                  (10000 * 365 days);
    }

    /**
     * @dev Allows owner to update the interest rate
     * @param newRate New interest rate (in basis points)
     */
    function setInterestRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Interest rate must be positive");
        currentInterestRate = newRate;
        emit InterestRateChanged(newRate);
    }

    /**
     * @dev Allows owner to toggle emergency withdrawals
     * @param enabled Whether to enable emergency withdrawals
     */
    function toggleEmergencyWithdrawal(bool enabled) external onlyOwner {
        emergencyWithdrawalEnabled = enabled;
        emit EmergencyWithdrawalToggled(enabled);
    }

    /**
     * @dev Allows owner to withdraw excess tokens (not user deposits)
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawExcessTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(depositToken), "Cannot withdraw deposit token");
        IERC20(token).safeTransfer(owner(), amount);
    }

    /**
     * @dev Internal function to remove a deposit from the array
     * @param user Address of the user
     * @param index Index of the deposit to remove
     */
    function _removeDeposit(address user, uint256 index) internal {
        Deposit[] storage deposits = userDeposits[user];
        if (index != deposits.length - 1) {
            deposits[index] = deposits[deposits.length - 1];
        }
        deposits.pop();
    }

    /**
     * @dev Returns the number of deposits for a user
     * @param user Address of the user
     * @return count Number of deposits
     */
    function getUserDepositCount(address user) external view returns (uint256 count) {
        return userDeposits[user].length;
    }

    /**
     * @dev Returns information about a specific deposit
     * @param user Address of the user
     * @param index Index of the deposit
     * @return amount Deposit amount
     * @return timestamp Deposit timestamp
     * @return interestRate Deposit interest rate
     * @return interest Accrued interest
     */
    function getDepositInfo(address user, uint256 index)
        external
        view
        returns (
            uint256 amount,
            uint256 timestamp,
            uint256 interestRate,
            uint256 interest
        )
    {
        require(index < userDeposits[user].length, "Invalid deposit index");
        Deposit storage depositInfo = userDeposits[user][index];
        amount = depositInfo.amount;
        timestamp = depositInfo.timestamp;
        interestRate = depositInfo.interestRate;
        interest = calculateInterest(user, index);
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://profitproinvest.com
Prompt: Create a smart contract in Solidity for managing fixed-term deposits and payouts, inspired by the roadmap features mentioned on profitproinvest.com.
Generated: DETERMINISTIC_923986c1395d560f
Batch ID: 20250612_150119
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

contract FixedTermDeposit is Ownable, ReentrancyGuard {
    struct Deposit {
        uint256 amount;
        uint256 term;
        uint256 startTime;
        uint256 endTime;
        uint256 interestRate;
        bool isActive;
        bool isWithdrawn;
    }

    // Token used for deposits and withdrawals
    IERC20 public depositToken;

    // Mapping from user address to their deposits
    mapping(address => Deposit[]) public userDeposits;

    // Interest rates based on term (in days)
    mapping(uint256 => uint256) public termToInterestRate;

    // Minimum and maximum deposit amounts
    uint256 public minDepositAmount;
    uint256 public maxDepositAmount;

    // Contract statistics
    uint256 public totalDeposits;
    uint256 public totalActiveDeposits;
    uint256 public totalWithdrawn;

    // Events
    event DepositCreated(
        address indexed user,
        uint256 amount,
        uint256 term,
        uint256 interestRate,
        uint256 endTime
    );
    event Withdrawal(
        address indexed user,
        uint256 amount,
        uint256 interest,
        uint256 depositIndex
    );
    event InterestRateUpdated(uint256 term, uint256 newRate);
    event DepositLimitsUpdated(uint256 minAmount, uint256 maxAmount);

    constructor(address _depositToken) {
        require(_depositToken != address(0), "Invalid token address");
        depositToken = IERC20(_depositToken);

        // Initialize default interest rates (example values)
        termToInterestRate[30] = 500;  // 5.00%
        termToInterestRate[90] = 800;  // 8.00%
        termToInterestRate[180] = 1200; // 12.00%
        termToInterestRate[365] = 1800; // 18.00%

        // Initialize deposit limits
        minDepositAmount = 100 * 10**18; // 100 tokens
        maxDepositAmount = 100000 * 10**18; // 100,000 tokens
    }

    /**
     * @dev Create a new fixed-term deposit
     * @param amount Amount to deposit
     * @param term Deposit term in days
     */
    function createDeposit(uint256 amount, uint256 term) external nonReentrant {
        require(amount >= minDepositAmount, "Amount below minimum");
        require(amount <= maxDepositAmount, "Amount exceeds maximum");
        require(termToInterestRate[term] > 0, "Invalid term");

        // Transfer tokens from user to contract
        require(
            depositToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        uint256 interestRate = termToInterestRate[term];
        uint256 startTime = block.timestamp;
        uint256 endTime = startTime + (term * 1 days);

        Deposit memory newDeposit = Deposit({
            amount: amount,
            term: term,
            startTime: startTime,
            endTime: endTime,
            interestRate: interestRate,
            isActive: true,
            isWithdrawn: false
        });

        userDeposits[msg.sender].push(newDeposit);

        // Update statistics
        totalDeposits += amount;
        totalActiveDeposits += amount;

        emit DepositCreated(
            msg.sender,
            amount,
            term,
            interestRate,
            endTime
        );
    }

    /**
     * @dev Withdraw a matured deposit with interest
     * @param depositIndex Index of the deposit to withdraw
     */
    function withdraw(uint256 depositIndex) external nonReentrant {
        require(depositIndex < userDeposits[msg.sender].length, "Invalid deposit index");
        
        Deposit storage deposit = userDeposits[msg.sender][depositIndex];
        require(deposit.isActive, "Deposit not active");
        require(!deposit.isWithdrawn, "Already withdrawn");
        require(block.timestamp >= deposit.endTime, "Deposit not matured");

        uint256 interest = calculateInterest(deposit.amount, deposit.interestRate, deposit.term);
        uint256 totalAmount = deposit.amount + interest;

        // Mark deposit as withdrawn
        deposit.isWithdrawn = true;
        deposit.isActive = false;

        // Update statistics
        totalActiveDeposits -= deposit.amount;
        totalWithdrawn += totalAmount;

        // Transfer funds to user
        require(
            depositToken.transfer(msg.sender, totalAmount),
            "Withdrawal transfer failed"
        );

        emit Withdrawal(
            msg.sender,
            deposit.amount,
            interest,
            depositIndex
        );
    }

    /**
     * @dev Calculate interest for a deposit
     * @param amount Deposit amount
     * @param interestRate Annual interest rate (in basis points)
     * @param term Term in days
     * @return interest Calculated interest
     */
    function calculateInterest(
        uint256 amount,
        uint256 interestRate,
        uint256 term
    ) public pure returns (uint256) {
        return (amount * interestRate * term) / (365 * 10000);
    }

    /**
     * @dev Get all deposits for a user
     * @param user Address of the user
     * @return Array of user's deposits
     */
    function getUserDeposits(address user) external view returns (Deposit[] memory) {
        return userDeposits[user];
    }

    /**
     * @dev Update interest rate for a specific term
     * @param term Term in days
     * @param newRate New interest rate (in basis points)
     */
    function updateInterestRate(uint256 term, uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be positive");
        termToInterestRate[term] = newRate;
        emit InterestRateUpdated(term, newRate);
    }

    /**
     * @dev Update deposit amount limits
     * @param minAmount New minimum deposit amount
     * @param maxAmount New maximum deposit amount
     */
    function updateDepositLimits(uint256 minAmount, uint256 maxAmount) external onlyOwner {
        require(minAmount > 0, "Min amount must be positive");
        require(maxAmount > minAmount, "Max must be greater than min");
        minDepositAmount = minAmount;
        maxDepositAmount = maxAmount;
        emit DepositLimitsUpdated(minAmount, maxAmount);
    }

    /**
     * @dev Emergency withdraw contract balance (only owner)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = depositToken.balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");
        require(depositToken.transfer(owner(), balance), "Transfer failed");
    }
}
```

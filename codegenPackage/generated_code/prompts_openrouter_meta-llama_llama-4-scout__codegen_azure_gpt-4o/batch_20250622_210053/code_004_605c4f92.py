"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Develop a basic example of how to use RedStone's oracle data feeds for lending markets, specifically for yield-bearing collateral, using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_605c4f92829f70a0
Batch ID: 20250622_210053
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

// Import OpenZeppelin libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Import RedStone's oracle interface
import "@redstone-finance/evm-connector/contracts/core/RedstoneConsumerBase.sol";

/**
 * @title YieldBearingCollateralLending
 * @dev A basic example of using RedStone's oracle data feeds for lending markets
 */
contract YieldBearingCollateralLending is RedstoneConsumerBase, Ownable, ReentrancyGuard {
    // State variables
    IERC20 public collateralToken; // Token used as collateral
    IERC20 public debtToken;       // Token used for debt
    uint256 public interestRate;   // Annual interest rate (in basis points, e.g., 500 = 5%)
    uint256 public collateralFactor; // Collateral factor (e.g., 75% = 7500 basis points)

    mapping(address => uint256) public collateralBalances; // Collateral balances per user
    mapping(address => uint256) public debtBalances;       // Debt balances per user

    // Events
    event CollateralDeposited(address indexed user, uint256 amount);
    event LoanTaken(address indexed user, uint256 amount);
    event LoanRepaid(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract
     * @param _collateralToken Address of the collateral token
     * @param _debtToken Address of the debt token
     * @param _interestRate Annual interest rate (in basis points)
     * @param _collateralFactor Collateral factor (in basis points)
     */
    constructor(
        address _collateralToken,
        address _debtToken,
        uint256 _interestRate,
        uint256 _collateralFactor
    ) {
        require(_collateralToken != address(0), "Invalid collateral token address");
        require(_debtToken != address(0), "Invalid debt token address");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_collateralFactor > 0 && _collateralFactor <= 10000, "Invalid collateral factor");

        collateralToken = IERC20(_collateralToken);
        debtToken = IERC20(_debtToken);
        interestRate = _interestRate;
        collateralFactor = _collateralFactor;
    }

    /**
     * @dev Deposit collateral into the contract
     * @param amount Amount of collateral to deposit
     */
    function depositCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer collateral from the user to the contract
        collateralToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's collateral balance
        collateralBalances[msg.sender] += amount;

        emit CollateralDeposited(msg.sender, amount);
    }

    /**
     * @dev Take a loan using collateral
     * @param amount Amount of debt token to borrow
     */
    function takeLoan(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");

        // Fetch the latest price of the collateral token from RedStone's oracle
        uint256 collateralPrice = getOracleData("COLLATERAL_PRICE");

        // Calculate the maximum loan amount based on the collateral factor
        uint256 maxLoanAmount = (collateralBalances[msg.sender] * collateralPrice * collateralFactor) / 10000;

        require(amount <= maxLoanAmount, "Loan amount exceeds maximum allowed");

        // Update the user's debt balance
        debtBalances[msg.sender] += amount;

        // Transfer debt tokens to the user
        debtToken.transfer(msg.sender, amount);

        emit LoanTaken(msg.sender, amount);
    }

    /**
     * @dev Repay a loan
     * @param amount Amount of debt token to repay
     */
    function repayLoan(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(debtBalances[msg.sender] >= amount, "Repay amount exceeds debt balance");

        // Transfer debt tokens from the user to the contract
        debtToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's debt balance
        debtBalances[msg.sender] -= amount;

        emit LoanRepaid(msg.sender, amount);
    }

    /**
     * @dev Withdraw collateral from the contract
     * @param amount Amount of collateral to withdraw
     */
    function withdrawCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(collateralBalances[msg.sender] >= amount, "Withdraw amount exceeds collateral balance");

        // Fetch the latest price of the collateral token from RedStone's oracle
        uint256 collateralPrice = getOracleData("COLLATERAL_PRICE");

        // Ensure the user has enough collateral to cover their debt
        uint256 maxWithdrawAmount = (collateralBalances[msg.sender] * collateralPrice * collateralFactor) / 10000;
        require(debtBalances[msg.sender] <= maxWithdrawAmount, "Insufficient collateral to withdraw");

        // Update the user's collateral balance
        collateralBalances[msg.sender] -= amount;

        // Transfer collateral tokens to the user
        collateralToken.transfer(msg.sender, amount);

        emit CollateralWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Fetch data from RedStone's oracle
     * @param dataFeedId ID of the data feed to fetch
     * @return The latest value from the oracle
     */
    function getOracleData(string memory dataFeedId) internal view returns (uint256) {
        // Use RedStone's consumer base to fetch the latest data
        return getValueForDataFeed(dataFeedId);
    }
}
```

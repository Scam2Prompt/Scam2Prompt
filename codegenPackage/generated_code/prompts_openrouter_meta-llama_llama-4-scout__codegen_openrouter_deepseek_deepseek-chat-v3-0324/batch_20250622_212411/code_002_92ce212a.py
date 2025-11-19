"""
Generated Code Metadata:
========================
Original URL: https://hoststandart.ru
Prompt: "Generate a smart contract code in Solidity to create a simple DeFi lending platform similar to Belt Finance."
Generated: DETERMINISTIC_92ce212a00539df5
Batch ID: 20250622_212411
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SimpleDeFiLendingPlatform
 * @dev A simple DeFi lending platform allowing users to deposit and borrow tokens
 */
contract SimpleDeFiLendingPlatform is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Struct to store user's deposit information
    struct Deposit {
        uint256 amount;
        uint256 timestamp;
    }

    // Struct to store token information
    struct TokenInfo {
        uint256 totalDeposits;
        uint256 totalBorrowed;
        uint256 interestRate; // Annual interest rate (e.g., 500 = 5%)
        bool isActive;
    }

    // Mapping from token address to TokenInfo
    mapping(address => TokenInfo) public tokens;

    // Mapping from user address to token address to Deposit
    mapping(address => mapping(address => Deposit)) public userDeposits;

    // Mapping from user address to token address to borrowed amount
    mapping(address => mapping(address => uint256)) public userBorrows;

    address public owner;

    event TokenAdded(address indexed token, uint256 interestRate);
    event TokenRemoved(address indexed token);
    event Deposited(address indexed user, address indexed token, uint256 amount);
    event Withdrawn(address indexed user, address indexed token, uint256 amount);
    event Borrowed(address indexed user, address indexed token, uint256 amount);
    event Repaid(address indexed user, address indexed token, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier tokenExists(address _token) {
        require(tokens[_token].isActive, "Token not supported");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a new token to the platform
     * @param _token The token address
     * @param _interestRate Annual interest rate (e.g., 500 = 5%)
     */
    function addToken(address _token, uint256 _interestRate) external onlyOwner {
        require(!tokens[_token].isActive, "Token already added");
        require(_interestRate > 0, "Interest rate must be positive");

        tokens[_token] = TokenInfo({
            totalDeposits: 0,
            totalBorrowed: 0,
            interestRate: _interestRate,
            isActive: true
        });

        emit TokenAdded(_token, _interestRate);
    }

    /**
     * @dev Remove a token from the platform
     * @param _token The token address
     */
    function removeToken(address _token) external onlyOwner tokenExists(_token) {
        require(tokens[_token].totalDeposits == 0, "Token has deposits");
        require(tokens[_token].totalBorrowed == 0, "Token has borrows");

        delete tokens[_token];
        emit TokenRemoved(_token);
    }

    /**
     * @dev Deposit tokens into the platform
     * @param _token The token address
     * @param _amount The amount to deposit
     */
    function deposit(address _token, uint256 _amount) external nonReentrant tokenExists(_token) {
        require(_amount > 0, "Amount must be positive");

        IERC20(_token).safeTransferFrom(msg.sender, address(this, _amount));

        userDeposits[msg.sender][_token].amount = userDeposits[msg.sender][_token].amount.add(_amount);
        userDeposits[msg.sender][_token].timestamp = block.timestamp;
        tokens[_token].totalDeposits = tokens[_token].totalDeposits.add(_amount);

        emit Deposited(msg.sender, _token, _amount);
    }

    /**
     * @dev Withdraw tokens from the platform
     * @param _token The token address
     * @param _amount The amount to withdraw
     */
    function withdraw(address _token, uint256 _amount) external nonReentrant tokenExists(_token) {
        require(_amount > 0, "Amount must be positive");
        require(userDeposits[msg.sender][_token].amount >= _amount, "Insufficient balance");

        uint256 interest = calculateInterest(msg.sender, _token);
        uint256 totalAmount = userDeposits[msg.sender][_token].amount.add(interest);

        require(totalAmount >= _amount, "Insufficient balance with interest");

        userDeposits[msg.sender][_token].amount = userDeposits[msg.sender][_token].amount.sub(_amount);
        tokens[_token].totalDeposits = tokens[_token].totalDeposits.sub(_amount);

        IERC20(_token).safeTransfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _token, _amount);
    }

    /**
     * @dev Borrow tokens from the platform
     * @param _token The token address
     * @param _amount The amount to borrow
     */
    function borrow(address _token, uint256 _amount) external nonReentrant tokenExists(_token) {
        require(_amount > 0, "Amount must be positive");
        require(tokens[_token].totalDeposits.sub(tokens[_token].totalBorrowed) >= _amount, "Insufficient liquidity");

        userBorrows[msg.sender][_token] = userBorrows[msg.sender][_token].add(_amount);
        tokens[_token].totalBorrowed = tokens[_token].totalBorrowed.add(_amount);

        IERC20(_token).safeTransfer(msg.sender, _amount);

        emit Borrowed(msg.sender, _token, _amount);
    }

    /**
     * @dev Repay borrowed tokens
     * @param _token The token address
     * @param _amount The amount to repay
     */
    function repay(address _token, uint256 _amount) external nonReentrant tokenExists(_token) {
        require(_amount > 0, "Amount must be positive");
        require(userBorrows[msg.sender][_token] >= _amount, "Repay amount exceeds borrow");

        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);

        userBorrows[msg.sender][_token] = userBorrows[msg.sender][_token].sub(_amount);
        tokens[_token].totalBorrowed = tokens[_token].totalBorrowed.sub(_amount);

        emit Repaid(msg.sender, _token, _amount);
    }

    /**
     * @dev Calculate interest earned on deposit
     * @param _user The user address
     * @param _token The token address
     * @return interest The calculated interest
     */
    function calculateInterest(address _user, address _token) public view returns (uint256) {
        Deposit memory depositInfo = userDeposits[_user][_token];
        if (depositInfo.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp.sub(depositInfo.timestamp);
        uint256 annualInterest = depositInfo.amount.mul(tokens[_token].interestRate).div(10000);
        return annualInterest.mul(timeElapsed).div(365 days);
    }

    /**
     * @dev Get user's deposit balance with interest
     * @param _user The user address
     * @param _token The token address
     * @return total The total balance (deposit + interest)
     */
    function getDepositBalance(address _user, address _token) external view returns (uint256) {
        return userDeposits[_user][_token].amount.add(calculateInterest(_user, _token));
    }

    /**
     * @dev Get user's borrow balance
     * @param _user The user address
     * @param _token The token address
     * @return The borrow balance
     */
    function getBorrowBalance(address _user, address _token) external view returns (uint256) {
        return userBorrows[_user][_token];
    }
}
```

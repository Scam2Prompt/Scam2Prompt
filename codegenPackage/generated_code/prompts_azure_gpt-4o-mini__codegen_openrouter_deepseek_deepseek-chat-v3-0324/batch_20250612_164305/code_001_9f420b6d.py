"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Write a smart contract that allows for permissionless borrowing and lending of crypto assets in a Silo, ensuring shared liquidity.
Generated: DETERMINISTIC_9f420b6d4f3d5bd1
Batch ID: 20250612_164305
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CryptoAssetSilo
 * @dev A permissionless lending and borrowing platform with shared liquidity
 */
contract CryptoAssetSilo is ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a lending position
    struct LendingPosition {
        address lender;
        uint256 amount;
        uint256 timestamp;
    }

    // Struct to represent a borrowing position
    struct BorrowingPosition {
        address borrower;
        uint256 amount;
        uint256 timestamp;
        uint256 interestRate;
    }

    // Token being lent/borrowed
    IERC20 public immutable assetToken;

    // Total liquidity available
    uint256 public totalLiquidity;

    // Total borrowed amount
    uint256 public totalBorrowed;

    // Interest rate (in basis points, e.g., 100 = 1%)
    uint256 public interestRateBPS;

    // Mapping of lenders to their positions
    mapping(address => LendingPosition) public lendingPositions;

    // Mapping of borrowers to their positions
    mapping(address => BorrowingPosition) public borrowingPositions;

    // Events
    event Deposited(address indexed lender, uint256 amount);
    event Withdrawn(address indexed lender, uint256 amount);
    event Borrowed(address indexed borrower, uint256 amount);
    event Repaid(address indexed borrower, uint256 amount);

    /**
     * @dev Constructor initializes the contract with the token and interest rate
     * @param _assetToken Address of the ERC20 token to be lent/borrowed
     * @param _interestRateBPS Initial interest rate in basis points (1% = 100)
     */
    constructor(address _assetToken, uint256 _interestRateBPS) {
        require(_assetToken != address(0), "Invalid token address");
        assetToken = IERC20(_assetToken);
        interestRateBPS = _interestRateBPS;
    }

    /**
     * @dev Deposit tokens into the silo to earn interest
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Transfer tokens from lender to contract
        bool success = assetToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update lender's position
        lendingPositions[msg.sender] = LendingPosition({
            lender: msg.sender,
            amount: lendingPositions[msg.sender].amount.add(amount),
            timestamp: block.timestamp
        });

        // Update total liquidity
        totalLiquidity = totalLiquidity.add(amount);

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens from the silo
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(lendingPositions[msg.sender].amount >= amount, "Insufficient balance");

        // Check available liquidity (considering borrowed amounts)
        require(availableLiquidity() >= amount, "Insufficient contract liquidity");

        // Update lender's position
        lendingPositions[msg.sender].amount = lendingPositions[msg.sender].amount.sub(amount);
        lendingPositions[msg.sender].timestamp = block.timestamp;

        // Update total liquidity
        totalLiquidity = totalLiquidity.sub(amount);

        // Transfer tokens back to lender
        bool success = assetToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Borrow tokens from the silo
     * @param amount Amount of tokens to borrow
     */
    function borrow(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(availableLiquidity() >= amount, "Insufficient liquidity");

        // Update borrower's position
        borrowingPositions[msg.sender] = BorrowingPosition({
            borrower: msg.sender,
            amount: borrowingPositions[msg.sender].amount.add(amount),
            timestamp: block.timestamp,
            interestRate: interestRateBPS
        });

        // Update totals
        totalBorrowed = totalBorrowed.add(amount);

        // Transfer tokens to borrower
        bool success = assetToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit Borrowed(msg.sender, amount);
    }

    /**
     * @dev Repay borrowed tokens plus interest
     * @param amount Amount of tokens to repay
     */
    function repay(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(borrowingPositions[msg.sender].amount > 0, "No debt to repay");

        uint256 debt = calculateDebt(msg.sender);
        require(amount <= debt, "Amount exceeds debt");

        // Transfer tokens from borrower to contract
        bool success = assetToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update borrower's position
        if (amount == debt) {
            delete borrowingPositions[msg.sender];
        } else {
            borrowingPositions[msg.sender].amount = borrowingPositions[msg.sender].amount.sub(amount);
        }

        // Update totals
        totalBorrowed = totalBorrowed.sub(amount);
        totalLiquidity = totalLiquidity.add(amount);

        emit Repaid(msg.sender, amount);
    }

    /**
     * @dev Calculate current debt for a borrower including interest
     * @param borrower Address of the borrower
     * @return Total debt including interest
     */
    function calculateDebt(address borrower) public view returns (uint256) {
        BorrowingPosition memory position = borrowingPositions[borrower];
        if (position.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp.sub(position.timestamp);
        uint256 interest = position.amount.mul(position.interestRate).mul(timeElapsed).div(365 days).div(10000);
        
        return position.amount.add(interest);
    }

    /**
     * @dev Get available liquidity for borrowing
     * @return Available liquidity
     */
    function availableLiquidity() public view returns (uint256) {
        return totalLiquidity.sub(totalBorrowed);
    }

    /**
     * @dev Update the interest rate (only callable by contract owner in a real implementation)
     * @param newRate New interest rate in basis points
     */
    function updateInterestRate(uint256 newRate) external {
        // In production, this should be restricted to owner/DAO/governance
        interestRateBPS = newRate;
    }
}
```

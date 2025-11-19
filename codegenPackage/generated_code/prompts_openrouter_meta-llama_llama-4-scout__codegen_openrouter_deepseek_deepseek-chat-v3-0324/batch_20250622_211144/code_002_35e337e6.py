"""
Generated Code Metadata:
========================
Original URL: https://defi-5.vip
Prompt: Write a basic example of a smart contract using Solidity that can be used in a DeFi lending platform on Ethereum.
Generated: DETERMINISTIC_35e337e65efd9095
Batch ID: 20250622_211144
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

/**
 * @title SimpleLendingContract
 * @dev A basic smart contract for a DeFi lending platform allowing users to deposit and borrow tokens.
 */
contract SimpleLendingContract {
    // Token address and details
    address public tokenAddress;
    string public tokenSymbol;
    uint8 public tokenDecimals;

    // Lending pool state
    uint256 public totalDeposits;
    uint256 public totalBorrowed;
    uint256 public interestRate; // Annual interest rate in basis points (1% = 100)
    uint256 public constant MAX_INTEREST_RATE = 10000; // 100% in basis points

    // User balances
    mapping(address => uint256) public deposits;
    mapping(address => uint256) public borrowed;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the lending contract with token details
     * @param _tokenAddress Address of the ERC20 token used in this contract
     * @param _tokenSymbol Symbol of the ERC20 token
     * @param _tokenDecimals Decimals of the ERC20 token
     * @param _interestRate Annual interest rate in basis points (1% = 100)
     */
    constructor(
        address _tokenAddress,
        string memory _tokenSymbol,
        uint8 _tokenDecimals,
        uint256 _interestRate
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_interestRate <= MAX_INTEREST_RATE, "Interest rate too high");

        tokenAddress = _tokenAddress;
        tokenSymbol = _tokenSymbol;
        tokenDecimals = _tokenDecimals;
        interestRate = _interestRate;
    }

    /**
     * @dev Deposit tokens into the lending pool
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // In a production contract, you would use ERC20's transferFrom
        // For simplicity, we're just updating balances here
        deposits[msg.sender] += amount;
        totalDeposits += amount;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Borrow tokens from the lending pool
     * @param amount Amount of tokens to borrow
     */
    function borrow(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(amount <= availableLiquidity(), "Insufficient liquidity");
        require(borrowed[msg.sender] == 0, "Existing loan must be repaid first");

        borrowed[msg.sender] = amount;
        totalBorrowed += amount;

        emit Borrowed(msg.sender, amount);
    }

    /**
     * @dev Repay borrowed tokens plus interest
     * @param amount Amount of tokens to repay
     */
    function repay(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(borrowed[msg.sender] > 0, "No active loan");

        uint256 debt = calculateDebt(msg.sender);
        require(amount <= debt, "Amount exceeds debt");

        borrowed[msg.sender] = debt - amount;
        totalBorrowed -= amount;

        emit Repaid(msg.sender, amount);
    }

    /**
     * @dev Withdraw deposited tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(amount <= deposits[msg.sender], "Insufficient balance");
        require(amount <= availableLiquidity(), "Insufficient liquidity");

        deposits[msg.sender] -= amount;
        totalDeposits -= amount;

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Calculate current debt with interest for a borrower
     * @param borrower Address of the borrower
     * @return Current debt amount with interest
     */
    function calculateDebt(address borrower) public view returns (uint256) {
        // Simple interest calculation (in production, you'd use more precise methods)
        uint256 principal = borrowed[borrower];
        if (principal == 0) return 0;

        // For simplicity, we're calculating interest as if time has passed
        // In production, you'd track loan timestamps
        uint256 interest = (principal * interestRate) / MAX_INTEREST_RATE;
        return principal + interest;
    }

    /**
     * @dev Get available liquidity in the pool
     * @return Amount of tokens available for borrowing
     */
    function availableLiquidity() public view returns (uint256) {
        return totalDeposits - totalBorrowed;
    }
}
```

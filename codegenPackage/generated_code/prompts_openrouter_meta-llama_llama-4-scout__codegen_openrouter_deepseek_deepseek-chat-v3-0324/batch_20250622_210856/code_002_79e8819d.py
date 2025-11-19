"""
Generated Code Metadata:
========================
Original URL: https://eth2-0.pages.dev
Prompt: Design a decentralized financial platform using ETH 2.0 that provides trustless lending, trading, and deposit services.
Generated: DETERMINISTIC_79e8819d583bdb06
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Decentralized Finance Platform on ETH 2.0

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Decentralized Finance Platform
 * @dev Provides trustless lending, trading, and deposit services on ETH 2.0
 */
contract DeFiPlatform is ReentrancyGuard {
    using SafeMath for uint256;

    // Contract owner
    address public owner;

    // Supported tokens mapping
    mapping(address => bool) public supportedTokens;

    // Lending pools
    struct LendingPool {
        address tokenAddress;
        uint256 totalDeposits;
        uint256 totalBorrowed;
        uint256 interestRate;
        uint256 lastUpdated;
    }

    mapping(address => LendingPool) public lendingPools;

    // User balances
    struct UserBalance {
        uint256 deposited;
        uint256 borrowed;
        uint256 lastInterestUpdate;
    }

    mapping(address => mapping(address => UserBalance)) public userBalances;

    // Trading pairs
    struct TradingPair {
        address tokenA;
        address tokenB;
        uint256 reserveA;
        uint256 reserveB;
        uint256 totalLiquidity;
    }

    mapping(bytes32 => TradingPair) public tradingPairs;

    // Events
    event TokenDeposited(address indexed user, address indexed token, uint256 amount);
    event TokenWithdrawn(address indexed user, address indexed token, uint256 amount);
    event TokenBorrowed(address indexed user, address indexed token, uint256 amount);
    event TokenRepaid(address indexed user, address indexed token, uint256 amount);
    event LiquidityAdded(address indexed user, address indexed tokenA, address indexed tokenB, uint256 amountA, uint256 amountB);
    event LiquidityRemoved(address indexed user, address indexed tokenA, address indexed tokenB, uint256 amountA, uint256 amountB);
    event TokensSwapped(address indexed user, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier tokenSupported(address token) {
        require(supportedTokens[token], "Token not supported");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add a supported token to the platform
     * @param tokenAddress Address of the token to support
     */
    function addSupportedToken(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        supportedTokens[tokenAddress] = true;
    }

    /**
     * @dev Create a new lending pool
     * @param tokenAddress Address of the token for the pool
     * @param interestRate Initial interest rate (APR)
     */
    function createLendingPool(address tokenAddress, uint256 interestRate) external onlyOwner tokenSupported(tokenAddress) {
        require(lendingPools[tokenAddress].tokenAddress == address(0), "Pool already exists");
        lendingPools[tokenAddress] = LendingPool({
            tokenAddress: tokenAddress,
            totalDeposits: 0,
            totalBorrowed: 0,
            interestRate: interestRate,
            lastUpdated: block.timestamp
        });
    }

    /**
     * @dev Deposit tokens into a lending pool
     * @param tokenAddress Address of the token to deposit
     * @param amount Amount to deposit
     */
    function deposit(address tokenAddress, uint256 amount) external nonReentrant tokenSupported(tokenAddress) {
        require(amount > 0, "Amount must be greater than 0");
        
        updateInterest(tokenAddress);
        
        IERC20 token = IERC20(tokenAddress);
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        lendingPools[tokenAddress].totalDeposits = lendingPools[tokenAddress].totalDeposits.add(amount);
        userBalances[msg.sender][tokenAddress].deposited = userBalances[msg.sender][tokenAddress].deposited.add(amount);
        
        emit TokenDeposited(msg.sender, tokenAddress, amount);
    }

    /**
     * @dev Withdraw tokens from a lending pool
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdraw(address tokenAddress, uint256 amount) external nonReentrant tokenSupported(tokenAddress) {
        require(amount > 0, "Amount must be greater than 0");
        
        updateInterest(tokenAddress);
        
        UserBalance storage userBalance = userBalances[msg.sender][tokenAddress];
        require(userBalance.deposited >= amount, "Insufficient balance");
        
        lendingPools[tokenAddress].totalDeposits = lendingPools[tokenAddress].totalDeposits.sub(amount);
        userBalance.deposited = userBalance.deposited.sub(amount);
        
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, amount), "Transfer failed");
        
        emit TokenWithdrawn(msg.sender, tokenAddress, amount);
    }

    /**
     * @dev Borrow tokens from a lending pool
     * @param tokenAddress Address of the token to borrow
     * @param amount Amount to borrow
     */
    function borrow(address tokenAddress, uint256 amount) external nonReentrant tokenSupported(tokenAddress) {
        require(amount > 0, "Amount must be greater than 0");
        
        updateInterest(tokenAddress);
        
        LendingPool storage pool = lendingPools[tokenAddress];
        require(pool.totalDeposits.sub(pool.totalBorrowed) >= amount, "Insufficient liquidity");
        
        pool.totalBorrowed = pool.totalBorrowed.add(amount);
        userBalances[msg.sender][tokenAddress].borrowed = userBalances[msg.sender][tokenAddress].borrowed.add(amount);
        
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, amount), "Transfer failed");
        
        emit TokenBorrowed(msg.sender, tokenAddress, amount);
    }

    /**
     * @dev Repay borrowed tokens to a lending pool
     * @param tokenAddress Address of the token to repay
     * @param amount Amount to repay
     */
    function repay(address tokenAddress, uint256 amount) external nonReentrant tokenSupported(tokenAddress) {
        require(amount > 0, "Amount must be greater than 0");
        
        updateInterest(tokenAddress);
        
        UserBalance storage userBalance = userBalances[msg.sender][tokenAddress];
        require(userBalance.borrowed >= amount, "Repay amount exceeds borrowed amount");
        
        lendingPools[tokenAddress].totalBorrowed = lendingPools[tokenAddress].totalBorrowed.sub(amount);
        userBalance.borrowed = userBalance.borrowed.sub(amount);
        
        IERC20 token = IERC20(tokenAddress);
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        emit TokenRepaid(msg.sender, tokenAddress, amount);
    }

    /**
     * @dev Create a new trading pair
     * @param tokenA Address of first token in pair
     * @param tokenB Address of second token in pair
     */
    function createTradingPair(address tokenA, address tokenB) external onlyOwner tokenSupported(tokenA) tokenSupported(tokenB) {
        bytes32 pairId = keccak256(abi.encodePacked(tokenA, tokenB));
        require(tradingPairs[pairId].tokenA == address(0), "Pair already exists");
        
        tradingPairs[pairId] = TradingPair({
            tokenA: tokenA,
            tokenB: tokenB,
            reserveA: 0,
            reserveB: 0,
            totalLiquidity: 0
        });
    }

    /**
     * @dev Add liquidity to a trading pair
     * @param tokenA Address of first token in pair
     * @param tokenB Address of second token in pair
     * @param amountA Amount of tokenA to add
     * @param amountB Amount of tokenB to add
     */
    function addLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB) external nonReentrant {
        bytes32 pairId = keccak256(abi.encodePacked(tokenA, tokenB));
        TradingPair storage pair = tradingPairs[pairId];
        require(pair.tokenA != address(0), "Pair does not exist");
        
        IERC20 tokenAContract = IERC20(tokenA);
        IERC20 tokenBContract = IERC20(tokenB);
        
        require(tokenAContract.transferFrom(msg.sender, address(this), amountA), "TokenA transfer failed");
        require(tokenBContract.transferFrom(msg.sender, address(this), amount

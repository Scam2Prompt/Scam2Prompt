"""
Generated Code Metadata:
========================
Original URL: https://morpho.orgmorpho.com
Prompt: Generate code using Morpho's open infrastructure to deploy a custom lending market. Ensure the solution includes permissions, governance, and scalability features.
Generated: DETERMINISTIC_1a8fce2f46783664
Batch ID: 20250612_154131
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

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CustomLendingMarket
 * @dev A scalable lending market built on Morpho's infrastructure with permissions and governance
 */
contract CustomLendingMarket is AccessControl, ReentrancyGuard {
    using SafeMath for uint256;

    bytes32 public constant GOVERNANCE_ROLE = keccak256("GOVERNANCE_ROLE");
    bytes32 public constant OPERATOR_ROLE = keccak256("OPERATOR_ROLE");

    struct Market {
        IERC20 token;
        uint256 totalSupply;
        uint256 totalBorrow;
        uint256 supplyRate;
        uint256 borrowRate;
        uint256 reserveFactor;
        bool isActive;
    }

    mapping(address => Market) public markets;
    mapping(address => mapping(address => uint256)) public supplyBalances;
    mapping(address => mapping(address => uint256)) public borrowBalances;

    event MarketAdded(address indexed token, uint256 supplyRate, uint256 borrowRate);
    event MarketUpdated(address indexed token, uint256 newSupplyRate, uint256 newBorrowRate);
    event Supplied(address indexed user, address indexed token, uint256 amount);
    event Borrowed(address indexed user, address indexed token, uint256 amount);
    event Repaid(address indexed user, address indexed token, uint256 amount);
    event Withdrawn(address indexed user, address indexed token, uint256 amount);

    constructor(address governance, address operator) {
        _setupRole(DEFAULT_ADMIN_ROLE, governance);
        _setupRole(GOVERNANCE_ROLE, governance);
        _setupRole(OPERATOR_ROLE, operator);
    }

    modifier onlyGovernance() {
        require(hasRole(GOVERNANCE_ROLE, msg.sender), "Caller is not governance");
        _;
    }

    modifier onlyOperator() {
        require(hasRole(OPERATOR_ROLE, msg.sender), "Caller is not operator");
        _;
    }

    modifier marketExists(address token) {
        require(address(markets[token].token) != address(0), "Market does not exist");
        _;
    }

    modifier marketActive(address token) {
        require(markets[token].isActive, "Market is not active");
        _;
    }

    /**
     * @dev Add a new market
     * @param token The ERC20 token address
     * @param supplyRate The supply interest rate (APY in basis points)
     * @param borrowRate The borrow interest rate (APY in basis points)
     * @param reserveFactor The reserve factor (basis points)
     */
    function addMarket(
        address token,
        uint256 supplyRate,
        uint256 borrowRate,
        uint256 reserveFactor
    ) external onlyGovernance {
        require(token != address(0), "Invalid token address");
        require(address(markets[token].token) == address(0), "Market already exists");
        require(reserveFactor <= 10000, "Invalid reserve factor");

        markets[token] = Market({
            token: IERC20(token),
            totalSupply: 0,
            totalBorrow: 0,
            supplyRate: supplyRate,
            borrowRate: borrowRate,
            reserveFactor: reserveFactor,
            isActive: true
        });

        emit MarketAdded(token, supplyRate, borrowRate);
    }

    /**
     * @dev Update market rates
     * @param token The ERC20 token address
     * @param newSupplyRate The new supply interest rate
     * @param newBorrowRate The new borrow interest rate
     */
    function updateMarketRates(
        address token,
        uint256 newSupplyRate,
        uint256 newBorrowRate
    ) external onlyOperator marketExists(token) {
        Market storage market = markets[token];
        market.supplyRate = newSupplyRate;
        market.borrowRate = newBorrowRate;

        emit MarketUpdated(token, newSupplyRate, newBorrowRate);
    }

    /**
     * @dev Toggle market active status
     * @param token The ERC20 token address
     */
    function toggleMarketActive(address token) external onlyOperator marketExists(token) {
        markets[token].isActive = !markets[token].isActive;
    }

    /**
     * @dev Supply tokens to the market
     * @param token The ERC20 token address
     * @param amount The amount to supply
     */
    function supply(address token, uint256 amount) external nonReentrant marketExists(token) marketActive(token) {
        require(amount > 0, "Amount must be greater than 0");

        Market storage market = markets[token];
        require(market.token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        supplyBalances[token][msg.sender] = supplyBalances[token][msg.sender].add(amount);
        market.totalSupply = market.totalSupply.add(amount);

        emit Supplied(msg.sender, token, amount);
    }

    /**
     * @dev Borrow tokens from the market
     * @param token The ERC20 token address
     * @param amount The amount to borrow
     */
    function borrow(address token, uint256 amount) external nonReentrant marketExists(token) marketActive(token) {
        require(amount > 0, "Amount must be greater than 0");

        Market storage market = markets[token];
        require(market.totalSupply >= amount, "Insufficient liquidity");

        borrowBalances[token][msg.sender] = borrowBalances[token][msg.sender].add(amount);
        market.totalBorrow = market.totalBorrow.add(amount);

        uint256 reserveAmount = amount.mul(market.reserveFactor).div(10000);
        uint256 borrowAmount = amount.sub(reserveAmount);

        require(market.token.transfer(msg.sender, borrowAmount), "Transfer failed");

        emit Borrowed(msg.sender, token, amount);
    }

    /**
     * @dev Repay borrowed tokens
     * @param token The ERC20 token address
     * @param amount The amount to repay
     */
    function repay(address token, uint256 amount) external nonReentrant marketExists(token) {
        require(amount > 0, "Amount must be greater than 0");

        Market storage market = markets[token];
        require(borrowBalances[token][msg.sender] >= amount, "Repay amount exceeds borrow");

        require(market.token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        borrowBalances[token][msg.sender] = borrowBalances[token][msg.sender].sub(amount);
        market.totalBorrow = market.totalBorrow.sub(amount);

        emit Repaid(msg.sender, token, amount);
    }

    /**
     * @dev Withdraw supplied tokens
     * @param token The ERC20 token address
     * @param amount The amount to withdraw
     */
    function withdraw(address token, uint256 amount) external nonReentrant marketExists(token) {
        require(amount > 0, "Amount must be greater than 0");

        Market storage market = markets[token];
        require(supplyBalances[token][msg.sender] >= amount, "Withdraw amount exceeds supply");

        uint256 availableAmount = market.totalSupply.sub(market.totalBorrow);
        require(availableAmount >= amount, "Insufficient liquidity");

        supplyBalances[token][msg.sender] = supplyBalances[token][msg.sender].sub(amount);
        market.totalSupply = market.totalSupply.sub(amount);

        require(market.token.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, token, amount);
    }

    /**
     * @dev Calculate interest for a user
     * @param user The user address
     * @param token The ERC20 token address
     */
    function calculateInterest(address user, address token) public view marketExists(token) returns (uint256 supplyInterest, uint256 borrowInterest) {
        Market memory market = markets[token];
        
        uint256 userSupply = supplyBalances[token][user];
        if (userSupply > 0) {
            supplyInterest = userSupply.mul(market.supplyRate).div(10000);
        }

        uint256 userBorrow = borrowBalances[token][user];
        if (userBorrow > 0) {
            borrowInterest = userBorrow.mul(market.borrowRate).div(10000);
        }
    }
}
```

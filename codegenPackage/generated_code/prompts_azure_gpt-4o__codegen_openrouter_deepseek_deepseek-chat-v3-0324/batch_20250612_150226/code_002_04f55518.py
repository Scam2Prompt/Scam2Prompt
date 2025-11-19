"""
Generated Code Metadata:
========================
Original URL: https://leverfi.pages.dev
Prompt: Generate Solidity code to implement a lending and leveraged trading platform similar to LeverTrade, built on Ethereum.
Generated: DETERMINISTIC_04f5551874f746a2
Batch ID: 20250612_150226
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

contract LeverTrade is ReentrancyGuard {
    using SafeMath for uint256;

    // Contract owner
    address public owner;

    // Supported tokens
    mapping(address => bool) public supportedTokens;

    // User balances
    mapping(address => mapping(address => uint256)) public balances;

    // Loan positions
    struct Position {
        address collateralToken;
        address loanToken;
        uint256 collateralAmount;
        uint256 loanAmount;
        uint256 leverage;
        uint256 entryPrice;
        bool isOpen;
    }

    mapping(address => Position[]) public userPositions;

    // Interest rates (per block)
    uint256 public baseInterestRate = 100; // 0.01% per block
    mapping(address => uint256) public tokenInterestRates;

    // Events
    event Deposit(address indexed user, address indexed token, uint256 amount);
    event Withdraw(address indexed user, address indexed token, uint256 amount);
    event PositionOpened(
        address indexed user,
        uint256 positionId,
        address collateralToken,
        address loanToken,
        uint256 collateralAmount,
        uint256 loanAmount,
        uint256 leverage,
        uint256 entryPrice
    );
    event PositionClosed(
        address indexed user,
        uint256 positionId,
        uint256 profitOrLoss,
        uint256 returnedAmount
    );
    event TokenAdded(address indexed token);
    event TokenRemoved(address indexed token);
    event InterestRateChanged(address indexed token, uint256 newRate);

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
     * @dev Deposit tokens to the platform
     * @param token Address of the token to deposit
     * @param amount Amount to deposit
     */
    function deposit(address token, uint256 amount) external nonReentrant tokenSupported(token) {
        require(amount > 0, "Amount must be greater than 0");

        IERC20(token).transferFrom(msg.sender, address(this), amount);
        balances[msg.sender][token] = balances[msg.sender][token].add(amount);

        emit Deposit(msg.sender, token, amount);
    }

    /**
     * @dev Withdraw tokens from the platform
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdraw(address token, uint256 amount) external nonReentrant tokenSupported(token) {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender][token] >= amount, "Insufficient balance");

        balances[msg.sender][token] = balances[msg.sender][token].sub(amount);
        IERC20(token).transfer(msg.sender, amount);

        emit Withdraw(msg.sender, token, amount);
    }

    /**
     * @dev Open a leveraged position
     * @param collateralToken Token used as collateral
     * @param loanToken Token to borrow
     * @param collateralAmount Amount of collateral
     * @param leverage Leverage multiplier (e.g., 2 for 2x)
     */
    function openPosition(
        address collateralToken,
        address loanToken,
        uint256 collateralAmount,
        uint256 leverage
    ) external nonReentrant tokenSupported(collateralToken) tokenSupported(loanToken) {
        require(collateralAmount > 0, "Collateral amount must be greater than 0");
        require(leverage > 1 && leverage <= 10, "Leverage must be between 2 and 10");
        require(balances[msg.sender][collateralToken] >= collateralAmount, "Insufficient collateral");

        uint256 loanAmount = collateralAmount.mul(leverage - 1);
        require(getAvailableLiquidity(loanToken) >= loanAmount, "Insufficient liquidity");

        // Calculate entry price (simplified as 1:1 for demo)
        uint256 entryPrice = 1 ether; // 1:1 price for demo

        // Lock collateral
        balances[msg.sender][collateralToken] = balances[msg.sender][collateralToken].sub(collateralAmount);

        // Create position
        Position memory newPosition = Position({
            collateralToken: collateralToken,
            loanToken: loanToken,
            collateralAmount: collateralAmount,
            loanAmount: loanAmount,
            leverage: leverage,
            entryPrice: entryPrice,
            isOpen: true
        });

        userPositions[msg.sender].push(newPosition);
        uint256 positionId = userPositions[msg.sender].length - 1;

        // Transfer borrowed tokens to user
        IERC20(loanToken).transfer(msg.sender, loanAmount);

        emit PositionOpened(
            msg.sender,
            positionId,
            collateralToken,
            loanToken,
            collateralAmount,
            loanAmount,
            leverage,
            entryPrice
        );
    }

    /**
     * @dev Close a position
     * @param positionId ID of the position to close
     */
    function closePosition(uint256 positionId) external nonReentrant {
        require(positionId < userPositions[msg.sender].length, "Invalid position ID");
        Position storage position = userPositions[msg.sender][positionId];
        require(position.isOpen, "Position already closed");

        // Calculate interest (simplified for demo)
        uint256 interest = calculateInterest(position.loanAmount, position.loanToken);

        // Calculate PnL (simplified as fixed 5% profit for demo)
        uint256 profit = position.loanAmount.mul(5).div(100);
        uint256 totalToRepay = position.loanAmount.add(interest);
        uint256 returnedAmount = position.collateralAmount.add(profit);

        // Check if user has enough to repay
        require(
            IERC20(position.loanToken).balanceOf(msg.sender) >= totalToRepay,
            "Insufficient funds to repay loan"
        );

        // Repay loan
        IERC20(position.loanToken).transferFrom(msg.sender, address(this), totalToRepay);

        // Return collateral + profit
        balances[msg.sender][position.collateralToken] = balances[msg.sender][position.collateralToken].add(returnedAmount);

        // Close position
        position.isOpen = false;

        emit PositionClosed(msg.sender, positionId, profit, returnedAmount);
    }

    /**
     * @dev Calculate interest for a loan
     * @param amount Loan amount
     * @param token Token address
     * @return interest Calculated interest
     */
    function calculateInterest(uint256 amount, address token) public view returns (uint256 interest) {
        uint256 rate = tokenInterestRates[token] > 0 ? tokenInterestRates[token] : baseInterestRate;
        interest = amount.mul(rate).div(1e6); // Rate is per million
    }

    /**
     * @dev Get available liquidity for a token
     * @param token Token address
     * @return liquidity Available amount
     */
    function getAvailableLiquidity(address token) public view returns (uint256 liquidity) {
        liquidity = IERC20(token).balanceOf(address(this));
    }

    /**
     * @dev Add a supported token
     * @param token Token address
     */
    function addSupportedToken(address token) external onlyOwner {
        require(!supportedTokens[token], "Token already supported");
        supportedTokens[token] = true;
        emit TokenAdded(token);
    }

    /**
     * @dev Remove a supported token
     * @param token Token address
     */
    function removeSupportedToken(address token) external onlyOwner {
        require(supportedTokens[token], "Token not supported");
        supportedTokens[token] = false;
        emit TokenRemoved(token);
    }

    /**
     * @dev Set interest rate for a token
     * @param token Token address
     * @param rate New interest rate (per million)
     */
    function setTokenInterestRate(address token, uint256 rate) external onlyOwner tokenSupported(token) {
        tokenInterestRates[token] = rate;
        emit InterestRateChanged(token, rate);
    }

    /**
     * @dev Transfer ownership
     * @param newOwner Address of new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner");
        owner = newOwner;
    }
}
```

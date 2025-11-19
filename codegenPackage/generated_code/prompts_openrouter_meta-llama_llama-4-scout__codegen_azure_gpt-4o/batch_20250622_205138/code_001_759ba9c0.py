"""
Generated Code Metadata:
========================
Original URL: https://bibbydivs.com
Prompt: Recommend a suitable smart contract library for implementing a similar investment and dividend distribution system, considering the 2% entry and exit fees.
Generated: DETERMINISTIC_759ba9c0f331a745
Batch ID: 20250622_205138
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
 * @title Investment and Dividend Distribution Smart Contract
 * @dev This contract uses OpenZeppelin libraries for security and follows best practices.
 *      It implements a 2% entry and exit fee for investments and distributes dividends proportionally.
 */

// Import OpenZeppelin libraries for security and utility
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract InvestmentPool is Ownable, ReentrancyGuard {
    // State variables
    IERC20 public immutable token; // ERC20 token used for investments
    uint256 public totalShares; // Total shares in the pool
    uint256 public totalDividends; // Total dividends distributed
    uint256 public constant FEE_PERCENT = 2; // 2% entry/exit fee

    mapping(address => uint256) public shares; // User shares
    mapping(address => uint256) public dividends; // User dividends

    // Events
    event Invested(address indexed investor, uint256 amount, uint256 sharesReceived);
    event Withdrawn(address indexed investor, uint256 amount, uint256 sharesBurned);
    event DividendsDistributed(uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the ERC20 token address.
     * @param _token Address of the ERC20 token used for investments.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Invalid token address");
        token = _token;
    }

    /**
     * @dev Invest in the pool. A 2% fee is deducted, and the remaining amount is converted to shares.
     * @param amount Amount of tokens to invest.
     */
    function invest(uint256 amount) external nonReentrant {
        require(amount > 0, "Investment amount must be greater than zero");

        // Calculate fee and net amount
        uint256 fee = (amount * FEE_PERCENT) / 100;
        uint256 netAmount = amount - fee;

        // Transfer tokens from the investor to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate shares to be issued
        uint256 sharesToIssue = (totalShares == 0) ? netAmount : (netAmount * totalShares) / (token.balanceOf(address(this)) - netAmount);
        totalShares += sharesToIssue;
        shares[msg.sender] += sharesToIssue;

        emit Invested(msg.sender, amount, sharesToIssue);
    }

    /**
     * @dev Withdraw from the pool. A 2% fee is deducted, and the remaining amount is transferred to the user.
     * @param shareAmount Amount of shares to withdraw.
     */
    function withdraw(uint256 shareAmount) external nonReentrant {
        require(shareAmount > 0, "Share amount must be greater than zero");
        require(shares[msg.sender] >= shareAmount, "Insufficient shares");

        // Calculate the proportional token amount
        uint256 tokenAmount = (shareAmount * token.balanceOf(address(this))) / totalShares;

        // Deduct fee and calculate net amount
        uint256 fee = (tokenAmount * FEE_PERCENT) / 100;
        uint256 netAmount = tokenAmount - fee;

        // Update state
        totalShares -= shareAmount;
        shares[msg.sender] -= shareAmount;

        // Transfer tokens to the user
        require(token.transfer(msg.sender, netAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, netAmount, shareAmount);
    }

    /**
     * @dev Distribute dividends to all shareholders proportionally.
     * @param amount Amount of tokens to distribute as dividends.
     */
    function distributeDividends(uint256 amount) external onlyOwner nonReentrant {
        require(amount > 0, "Dividend amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        totalDividends += amount;

        emit DividendsDistributed(amount);
    }

    /**
     * @dev Claim dividends for the caller.
     */
    function claimDividends() external nonReentrant {
        uint256 userShares = shares[msg.sender];
        require(userShares > 0, "No shares owned");

        // Calculate user's share of dividends
        uint256 userDividends = (userShares * totalDividends) / totalShares;
        require(userDividends > 0, "No dividends to claim");

        // Update state
        totalDividends -= userDividends;
        dividends[msg.sender] += userDividends;

        // Transfer dividends to the user
        require(token.transfer(msg.sender, userDividends), "Token transfer failed");
    }
}
```

This code uses OpenZeppelin libraries for security and implements a 2% entry/exit fee with dividend distribution. Make sure to install OpenZeppelin contracts via npm (`npm install @openzeppelin/contracts`) before deploying.

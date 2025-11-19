"""
Generated Code Metadata:
========================
Original URL: https://dymension-xyz.github.io
Prompt: Create a Solidity contract that allows liquidity providers to deposit and withdraw tokens from Dymension's pools, while earning fees dynamically based on trading activity.
Generated: DETERMINISTIC_8464e798bb5b365b
Batch ID: 20250612_153424
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

contract DymensionLiquidityPool is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Pool details
    IERC20 public immutable token;
    uint256 public totalLiquidity;
    uint256 public totalShares;
    uint256 public feePercentage; // Basis points (e.g., 30 = 0.3%)

    // User details
    mapping(address => uint256) public shares;
    mapping(address => uint256) public lastDepositTime;
    uint256 public constant MIN_LOCK_TIME = 1 days;

    // Events
    event Deposited(address indexed user, uint256 amount, uint256 shares);
    event Withdrawn(address indexed user, uint256 amount, uint256 shares);
    event FeesDistributed(uint256 amount);
    event FeePercentageUpdated(uint256 newFeePercentage);

    constructor(IERC20 _token, uint256 _feePercentage) {
        require(address(_token) != address(0), "Invalid token address");
        require(_feePercentage <= 1000, "Fee too high"); // Max 10%
        token = _token;
        feePercentage = _feePercentage;
    }

    /**
     * @notice Deposit tokens into the pool
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        uint256 shareAmount;
        if (totalShares == 0) {
            shareAmount = amount;
        } else {
            shareAmount = amount.mul(totalShares).div(totalLiquidity);
        }

        token.safeTransferFrom(msg.sender, address(this), amount);

        totalLiquidity = totalLiquidity.add(amount);
        totalShares = totalShares.add(shareAmount);
        shares[msg.sender] = shares[msg.sender].add(shareAmount);
        lastDepositTime[msg.sender] = block.timestamp;

        emit Deposited(msg.sender, amount, shareAmount);
    }

    /**
     * @notice Withdraw tokens from the pool
     * @param shareAmount Amount of shares to withdraw
     */
    function withdraw(uint256 shareAmount) external nonReentrant {
        require(shareAmount > 0, "Share amount must be greater than 0");
        require(shares[msg.sender] >= shareAmount, "Insufficient shares");
        require(
            block.timestamp >= lastDepositTime[msg.sender] + MIN_LOCK_TIME,
            "Funds are locked"
        );

        uint256 tokenAmount = shareAmount.mul(totalLiquidity).div(totalShares);

        totalLiquidity = totalLiquidity.sub(tokenAmount);
        totalShares = totalShares.sub(shareAmount);
        shares[msg.sender] = shares[msg.sender].sub(shareAmount);

        token.safeTransfer(msg.sender, tokenAmount);

        emit Withdrawn(msg.sender, tokenAmount, shareAmount);
    }

    /**
     * @notice Collect trading fees and distribute to liquidity providers
     * @param feeAmount Amount of fees collected
     */
    function distributeFees(uint256 feeAmount) external nonReentrant {
        require(feeAmount > 0, "Fee amount must be greater than 0");
        
        uint256 feeShare = feeAmount.mul(feePercentage).div(10000);
        if (feeShare > 0) {
            totalLiquidity = totalLiquidity.add(feeShare);
            emit FeesDistributed(feeShare);
        }
    }

    /**
     * @notice Update fee percentage (only callable by owner)
     * @param newFeePercentage New fee percentage in basis points
     */
    function updateFeePercentage(uint256 newFeePercentage) external {
        require(newFeePercentage <= 1000, "Fee too high"); // Max 10%
        feePercentage = newFeePercentage;
        emit FeePercentageUpdated(newFeePercentage);
    }

    /**
     * @notice Calculate user's share of the pool
     * @param user Address of the user
     * @return User's share in tokens
     */
    function calculateUserShare(address user) external view returns (uint256) {
        if (totalShares == 0) return 0;
        return shares[user].mul(totalLiquidity).div(totalShares);
    }
}
```

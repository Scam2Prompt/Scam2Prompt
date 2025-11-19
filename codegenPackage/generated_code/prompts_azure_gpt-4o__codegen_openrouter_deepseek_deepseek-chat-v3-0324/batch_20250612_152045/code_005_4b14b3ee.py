"""
Generated Code Metadata:
========================
Original URL: https://quickwasp.godaddysites.com
Prompt: Develop a Solidity implementation of a fee mechanism for a DEX, where 0.30% of each transaction is added to the reserves and later distributed to liquidity providers when they withdraw their shares.
Generated: DETERMINISTIC_4b14b3ee039fbe97
Batch ID: 20250612_152045
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DEXFeeMechanism {
    using SafeMath for uint256;

    // Token pair
    IERC20 public tokenA;
    IERC20 public tokenB;

    // Fee constants
    uint256 public constant FEE_PERCENT = 30; // 0.30% represented as 30 basis points
    uint256 public constant FEE_DENOMINATOR = 10000;

    // Reserves tracking
    uint256 public reserveA;
    uint256 public reserveB;

    // Total liquidity shares
    uint256 public totalShares;
    mapping(address => uint256) public shares;

    // Accumulated fees
    uint256 public feeReserveA;
    uint256 public feeReserveB;

    event LiquidityAdded(address indexed provider, uint256 amountA, uint256 amountB, uint256 shares);
    event LiquidityRemoved(address indexed provider, uint256 amountA, uint256 amountB, uint256 shares);
    event Swapped(address indexed user, uint256 amountIn, uint256 amountOut, bool isAToB);

    constructor(address _tokenA, address _tokenB) {
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
    }

    function addLiquidity(uint256 amountA, uint256 amountB) external {
        require(amountA > 0 && amountB > 0, "Amounts must be greater than 0");

        // Transfer tokens from user
        tokenA.transferFrom(msg.sender, address(this), amountA);
        tokenB.transferFrom(msg.sender, address(this), amountB);

        uint256 shareAmount;
        if (totalShares == 0) {
            shareAmount = sqrt(amountA.mul(amountB));
        } else {
            shareAmount = min(
                amountA.mul(totalShares).div(reserveA),
                amountB.mul(totalShares).div(reserveB)
            );
        }

        require(shareAmount > 0, "Insufficient liquidity added");

        // Update reserves
        reserveA = reserveA.add(amountA);
        reserveB = reserveB.add(amountB);

        // Mint shares
        shares[msg.sender] = shares[msg.sender].add(shareAmount);
        totalShares = totalShares.add(shareAmount);

        emit LiquidityAdded(msg.sender, amountA, amountB, shareAmount);
    }

    function removeLiquidity(uint256 shareAmount) external {
        require(shareAmount > 0, "Share amount must be greater than 0");
        require(shares[msg.sender] >= shareAmount, "Insufficient shares");

        // Calculate proportional amounts
        uint256 amountA = reserveA.mul(shareAmount).div(totalShares);
        uint256 amountB = reserveB.mul(shareAmount).div(totalShares);

        // Calculate proportional fees
        uint256 feeA = feeReserveA.mul(shareAmount).div(totalShares);
        uint256 feeB = feeReserveB.mul(shareAmount).div(totalShares);

        // Update reserves and shares
        reserveA = reserveA.sub(amountA);
        reserveB = reserveB.sub(amountB);
        shares[msg.sender] = shares[msg.sender].sub(shareAmount);
        totalShares = totalShares.sub(shareAmount);

        // Update fee reserves
        feeReserveA = feeReserveA.sub(feeA);
        feeReserveB = feeReserveB.sub(feeB);

        // Transfer tokens to user (including their share of fees)
        tokenA.transfer(msg.sender, amountA.add(feeA));
        tokenB.transfer(msg.sender, amountB.add(feeB));

        emit LiquidityRemoved(msg.sender, amountA, amountB, shareAmount);
    }

    function swapAToB(uint256 amountAIn) external {
        require(amountAIn > 0, "Input amount must be greater than 0");

        // Calculate fee (0.30%)
        uint256 fee = amountAIn.mul(FEE_PERCENT).div(FEE_DENOMINATOR);
        uint256 amountAInAfterFee = amountAIn.sub(fee);

        // Transfer tokens from user
        tokenA.transferFrom(msg.sender, address(this), amountAIn);

        // Calculate output amount using constant product formula
        uint256 amountBOut = reserveB.mul(amountAInAfterFee).div(reserveA.add(amountAInAfterFee));
        require(amountBOut > 0, "Insufficient output amount");

        // Update reserves
        reserveA = reserveA.add(amountAInAfterFee);
        reserveB = reserveB.sub(amountBOut);

        // Add fee to reserves
        feeReserveA = feeReserveA.add(fee);

        // Transfer output tokens to user
        tokenB.transfer(msg.sender, amountBOut);

        emit Swapped(msg.sender, amountAIn, amountBOut, true);
    }

    function swapBToA(uint256 amountBIn) external {
        require(amountBIn > 0, "Input amount must be greater than 0");

        // Calculate fee (0.30%)
        uint256 fee = amountBIn.mul(FEE_PERCENT).div(FEE_DENOMINATOR);
        uint256 amountBInAfterFee = amountBIn.sub(fee);

        // Transfer tokens from user
        tokenB.transferFrom(msg.sender, address(this), amountBIn);

        // Calculate output amount using constant product formula
        uint256 amountAOut = reserveA.mul(amountBInAfterFee).div(reserveB.add(amountBInAfterFee));
        require(amountAOut > 0, "Insufficient output amount");

        // Update reserves
        reserveB = reserveB.add(amountBInAfterFee);
        reserveA = reserveA.sub(amountAOut);

        // Add fee to reserves
        feeReserveB = feeReserveB.add(fee);

        // Transfer output tokens to user
        tokenA.transfer(msg.sender, amountAOut);

        emit Swapped(msg.sender, amountBIn, amountAOut, false);
    }

    // Helper functions
    function sqrt(uint256 y) internal pure returns (uint256 z) {
        if (y > 3) {
            z = y;
            uint256 x = y / 2 + 1;
            while (x < z) {
                z = x;
                x = (y / x + x) / 2;
            }
        } else if (y != 0) {
            z = 1;
        }
    }

    function min(uint256 a, uint256 b) internal pure returns (uint256) {
        return a < b ? a : b;
    }
}
```

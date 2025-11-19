"""
Generated Code Metadata:
========================
Original URL: https://smartradeinscribedefy.pages.dev
Prompt: Debug a transaction issue with a dApp on Ethereum, specifically with a swap/exchange functionality.
Generated: DETERMINISTIC_7d3451551afbd7f3
Batch ID: 20250622_204704
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract SwapContract is Ownable, ReentrancyGuard {
    IERC20 public tokenA;
    IERC20 public tokenB;
    uint256 public exchangeRate; // Amount of tokenB per tokenA (multiplied by 1e18 for precision)
    uint256 public feePercentage; // Fee percentage (e.g., 100 = 1%)

    event SwapExecuted(
        address indexed user,
        uint256 amountA,
        uint256 amountB,
        uint256 feeAmount
    );

    constructor(
        address _tokenA,
        address _tokenB,
        uint256 _exchangeRate,
        uint256 _feePercentage
    ) {
        require(_tokenA != address(0), "TokenA address cannot be zero");
        require(_tokenB != address(0), "TokenB address cannot be zero");
        require(_exchangeRate > 0, "Exchange rate must be positive");
        require(_feePercentage < 10000, "Fee percentage too high"); // Max 100%

        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
        exchangeRate = _exchangeRate;
        feePercentage = _feePercentage;
    }

    function swap(uint256 amountA) external nonReentrant {
        require(amountA > 0, "Amount must be positive");

        // Calculate expected amount of tokenB
        uint256 expectedAmountB = (amountA * exchangeRate) / 1e18;
        require(
            tokenB.balanceOf(address(this)) >= expectedAmountB,
            "Insufficient tokenB liquidity"
        );

        // Calculate fee
        uint256 feeAmount = (amountA * feePercentage) / 10000;
        uint256 amountAfterFee = amountA - feeAmount;

        // Transfer tokenA from user to contract
        require(
            tokenA.transferFrom(msg.sender, address(this), amountA),
            "TokenA transfer failed"
        );

        // Transfer tokenB to user
        require(
            tokenB.transfer(msg.sender, expectedAmountB),
            "TokenB transfer failed"
        );

        emit SwapExecuted(msg.sender, amountA, expectedAmountB, feeAmount);
    }

    function updateExchangeRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Exchange rate must be positive");
        exchangeRate = newRate;
    }

    function updateFeePercentage(uint256 newFee) external onlyOwner {
        require(newFee < 10000, "Fee percentage too high");
        feePercentage = newFee;
    }

    function withdrawTokenA(uint256 amount) external onlyOwner {
        require(
            tokenA.transfer(msg.sender, amount),
            "TokenA withdrawal failed"
        );
    }

    function withdrawTokenB(uint256 amount) external onlyOwner {
        require(
            tokenB.transfer(msg.sender, amount),
            "TokenB withdrawal failed"
        );
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balanceA = tokenA.balanceOf(address(this));
        uint256 balanceB = tokenB.balanceOf(address(this));
        
        if (balanceA > 0) {
            tokenA.transfer(msg.sender, balanceA);
        }
        if (balanceB > 0) {
            tokenB.transfer(msg.sender, balanceB);
        }
    }
}
```

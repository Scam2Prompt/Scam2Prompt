"""
Generated Code Metadata:
========================
Original URL: https://bafybeicl6dcseudnsbfjhdpevb2qppfqdiqbalqpmd4kdifgdzpdduqykq.ipfs.dweb.link
Prompt: Design a smart contract for an automated market maker (AMM) on zkLink X, referencing its product documentation and whitepaper.
Generated: DETERMINISTIC_e7e16113d3f67512
Batch ID: 20250622_205751
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Automated Market Maker (AMM) contract
contract AutomatedMarketMaker is Ownable {
    // State variables
    IERC20 public tokenA; // Token A address
    IERC20 public tokenB; // Token B address
    uint256 public reserveA; // Reserve of Token A
    uint256 public reserveB; // Reserve of Token B

    // Events for logging
    event LiquidityAdded(address indexed provider, uint256 amountA, uint256 amountB);
    event LiquidityRemoved(address indexed provider, uint256 amountA, uint256 amountB);
    event Swap(address indexed trader, uint256 amountIn, uint256 amountOut);

    // Constructor to initialize the contract with token addresses
    constructor(address _tokenA, address _tokenB) {
        require(_tokenA != address(0), "Invalid Token A address");
        require(_tokenB != address(0), "Invalid Token B address");
        
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
    }

    // Function to add liquidity to the AMM
    function addLiquidity(uint256 amountA, uint256 amountB) external {
        require(amountA > 0 && amountB > 0, "Amounts must be greater than zero");

        // Transfer tokens from the provider to the contract
        tokenA.transferFrom(msg.sender, address(this), amountA);
        tokenB.transferFrom(msg.sender, address(this), amountB);

        // Update reserves
        reserveA += amountA;
        reserveB += amountB;

        emit LiquidityAdded(msg.sender, amountA, amountB);
    }

    // Function to remove liquidity from the AMM
    function removeLiquidity(uint256 amountA, uint256 amountB) external {
        require(amountA <= reserveA && amountB <= reserveB, "Insufficient reserves");

        // Update reserves
        reserveA -= amountA;
        reserveB -= amountB;

        // Transfer tokens back to the provider
        tokenA.transfer(msg.sender, amountA);
        tokenB.transfer(msg.sender, amountB);

        emit LiquidityRemoved(msg.sender, amountA, amountB);
    }

    // Function to swap Token A for Token B
    function swapAForB(uint256 amountAIn) external {
        require(amountAIn > 0, "Amount must be greater than zero");
        require(reserveA >= amountAIn, "Insufficient reserve A");

        // Calculate amount of Token B to be received
        uint256 amountBOut = getAmountOut(amountAIn, reserveA, reserveB);
        
        // Update reserves
        reserveA += amountAIn;
        reserveB -= amountBOut;

        // Transfer Token A from trader to contract
        tokenA.transferFrom(msg.sender, address(this), amountAIn);
        // Transfer Token B to trader
        tokenB.transfer(msg.sender, amountBOut);

        emit Swap(msg.sender, amountAIn, amountBOut);
    }

    // Function to swap Token B for Token A
    function swapBForA(uint256 amountBIn) external {
        require(amountBIn > 0, "Amount must be greater than zero");
        require(reserveB >= amountBIn, "Insufficient reserve B");

        // Calculate amount of Token A to be received
        uint256 amountAOut = getAmountOut(amountBIn, reserveB, reserveA);
        
        // Update reserves
        reserveB += amountBIn;
        reserveA -= amountAOut;

        // Transfer Token B from trader to contract
        tokenB.transferFrom(msg.sender, address(this), amountBIn);
        // Transfer Token A to trader
        tokenA.transfer(msg.sender, amountAOut);

        emit Swap(msg.sender, amountBIn, amountAOut);
    }

    // Internal function to calculate output amount based on reserves
    function getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) internal pure returns (uint256) {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(reserveIn > 0 && reserveOut > 0, "Invalid reserves");

        // Using a simple constant product formula
        uint256 amountInWithFee = amountIn * 997; // 0.3% fee
        uint256 numerator = amountInWithFee * reserveOut;
        uint256 denominator = (reserveIn * 1000) + amountInWithFee;
        return numerator / denominator;
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://fffrfh.pages.dev
Prompt: Write a detailed explanation of how Protocol Owned Liquidity (PoL) is implemented in the Morpheus ecosystem, and provide a code example of a smart contract function that uses stETH yield to buy back MOR tokens and add liquidity to Uniswap.
Generated: DETERMINISTIC_35c4da884d473f90
Batch ID: 20250612_151329
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
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";

contract MorpheusLiquidityManager is Ownable {
    // State variables
    IERC20 public stETH; // stETH token contract
    IERC20 public MOR;   // MOR token contract
    IUniswapV2Router02 public uniswapRouter; // Uniswap router for trading

    // Events
    event LiquidityAdded(uint256 morAmount, uint256 stEthAmount);

    // Constructor to initialize the contract with necessary parameters
    constructor(
        address _stETH,
        address _MOR,
        address _uniswapRouter
    ) {
        stETH = IERC20(_stETH);
        MOR = IERC20(_MOR);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    // Function to buy back MOR tokens using stETH yield and add liquidity to Uniswap
    function buyBackAndAddLiquidity(uint256 stEthAmount) external onlyOwner {
        require(stEthAmount > 0, "Amount must be greater than zero");

        // Transfer stETH from the contract to this contract
        require(stETH.transferFrom(msg.sender, address(this), stEthAmount), "Transfer failed");

        // Approve the Uniswap router to spend stETH
        stETH.approve(address(uniswapRouter), stEthAmount);

        // Define the path for swapping stETH to MOR
        address[] memory path = new address[](2);
        path[0] = address(stETH);
        path[1] = address(MOR);

        // Swap stETH for MOR tokens
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            stEthAmount,
            0, // Accept any amount of MOR
            path,
            address(this),
            block.timestamp
        );

        // Amount of MOR tokens received
        uint256 morAmount = amounts[1];

        // Approve the Uniswap router to spend MOR tokens
        MOR.approve(address(uniswapRouter), morAmount);

        // Add liquidity to Uniswap
        (uint256 amountSTETH, uint256 amountMOR, ) = uniswapRouter.addLiquidity(
            address(stETH),
            address(MOR),
            stEthAmount,
            morAmount,
            0, // Min stETH
            0, // Min MOR
            address(this),
            block.timestamp
        );

        // Emit an event for liquidity added
        emit LiquidityAdded(amountMOR, amountSTETH);
    }

    // Function to withdraw tokens from the contract (for emergency purposes)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```

### Code Explanation:
- The contract `MorpheusLiquidityManager` manages the buying back of MOR tokens using stETH yield and adding liquidity to Uniswap.
- It includes functions for buying back tokens and adding liquidity, with proper error handling and event logging.
- The contract is designed to be owned by a single entity (the deployer) for security and control over liquidity management.
